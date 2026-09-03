"""Orchestra l'intero assessment collegando validazione, grafo, motore e report.

È il caso d'uso principale richiamato sia dalla CLI sia dall'API. Mantiene le
singole componenti separate e stabilisce l'ordine in cui devono essere eseguite.
"""

from collections.abc import Callable
from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import ValidationError
from yaml import YAMLError

from nis2_assessor import __version__
from nis2_assessor.application.aggregation import aggregate
from nis2_assessor.application.engine import Evaluator, evaluate
from nis2_assessor.application.policies import (
    bundled_catalog_path,
    evidence_expiry,
    load_coverage_catalog,
    load_evidence_policies,
    load_operational_policy,
)
from nis2_assessor.application.ports import Clock, GraphRepository
from nis2_assessor.application.report_context import build_report_context
from nis2_assessor.application.runtime import SystemClock, random_assessment_id
from nis2_assessor.application.validation import load_environment, load_yaml_mapping
from nis2_assessor.domain.models import (
    Evidence,
    NormalizedEnvironment,
    Relationship,
    Requirement,
    Rule,
)
from nis2_assessor.domain.report_types import EvidenceRejection
from nis2_assessor.infrastructure.graph import Neo4jGraphRepository
from nis2_assessor.infrastructure.reporting import (
    general_markdown_path,
    knowledge_graph_markdown_path,
    technical_attachment_markdown_path,
    write_knowledge_graph_markdown,
    write_markdown,
    write_technical_attachment_markdown,
)


class CatalogValidationError(ValueError):
    """Errore uniforme per cataloghi YAML mancanti, malformati o incoerenti."""

    def __init__(self, catalog: str, details: str) -> None:
        super().__init__(f"catalogo {catalog} non valido: {details}")
        self.catalog = catalog
        self.details = details


def load_rules(path: Path) -> list[Rule]:
    """Carica in sicurezza le regole esterne e ne valida la versione."""
    try:
        raw = load_yaml_mapping(path)
        if raw.get("schema_version") != "2.0":
            raise ValueError("versione schema regole non supportata")
        if raw.get("catalog_version") not in (None, "2.1.0"):
            raise ValueError("versione catalogo regole non supportata")
        items = raw.get("rules")
        if not isinstance(items, list):
            raise ValueError("rules deve essere una lista")
        return [Rule.model_validate(item) for item in items]
    except (OSError, YAMLError, ValidationError, ValueError, TypeError) as exc:
        if isinstance(exc, CatalogValidationError):
            raise
        raise CatalogValidationError("regole", str(exc)) from exc


def load_requirements(path: Path) -> list[Requirement]:
    """Carica il catalogo separato dei requisiti e ne valida lo schema."""
    try:
        raw = load_yaml_mapping(path)
        if raw.get("schema_version") != "2.0":
            raise ValueError("versione schema requisiti non supportata")
        items = raw.get("requirements")
        if not isinstance(items, list):
            raise ValueError("requirements deve essere una lista")
        return [Requirement.model_validate(item) for item in items]
    except (OSError, YAMLError, ValidationError, ValueError, TypeError) as exc:
        if isinstance(exc, CatalogValidationError):
            raise
        raise CatalogValidationError("requisiti", str(exc)) from exc


def validate_framework_alignment(
    env: NormalizedEnvironment, requirements: list[Requirement], rules: list[Rule]
) -> None:
    """Verifica in entrambe le direzioni i legami requisito-controllo-regola."""
    requirement_map = {item.id: item for item in requirements}
    control_map = {item.id: item for item in env.controls}
    rule_map = {item.id: item for item in rules}
    if len(requirement_map) != len(requirements) or len(rule_map) != len(rules):
        raise ValueError("requisiti o regole contengono identificativi duplicati")
    for requirement in requirements:
        if requirement.source_document == "Direttiva (UE) 2022/2555" and not requirement.acn_point:
            raise ValueError(
                f"requisito {requirement.id} collegato genericamente alla sola NIS2"
            )
        if requirement.verification_mode.value == "manual_only":
            if requirement.control_ids or not requirement.manual_only_reason:
                raise ValueError(
                    f"requisito manual_only {requirement.id} deve avere motivazione e nessun controllo"
                )
            continue
        if not requirement.control_ids:
            raise ValueError(f"requisito tecnico {requirement.id} privo di controllo")
        missing_controls = set(requirement.control_ids) - control_map.keys()
        if missing_controls:
            raise ValueError(
                f"controlli inesistenti nel requisito {requirement.id}: {missing_controls}"
            )
    for control in env.controls:
        linked_requirement = requirement_map.get(control.requirement_id)
        if linked_requirement is None or control.id not in linked_requirement.control_ids:
            raise ValueError(f"controllo {control.id} non collegato correttamente al requisito")
        if set(control.rule_ids) - rule_map.keys():
            raise ValueError(f"controllo {control.id} riferisce regole inesistenti")
        if not control.rule_ids:
            raise ValueError(f"controllo tecnico {control.id} privo di regola")
        if set(control.applicable_profiles) != set(linked_requirement.applicable_profiles):
            raise ValueError(f"profili incoerenti per il controllo {control.id}")
    for rule in rules:
        linked_control = control_map.get(rule.control_id)
        if linked_control is None:
            raise ValueError(f"regola {rule.id} collegata a un controllo inesistente")
        if (
            rule.requirement_id != linked_control.requirement_id
            or rule.id not in linked_control.rule_ids
        ):
            raise ValueError(f"regola {rule.id} incoerente con controllo e requisito")
        if set(rule.applicable_profiles) != set(linked_control.applicable_profiles):
            raise ValueError(f"profili incoerenti per la regola {rule.id}")
        if rule.verification_mode != linked_control.verification_mode:
            raise ValueError(f"modalità di verifica incoerente per la regola {rule.id}")
        if set(rule.required_properties) != set(linked_control.required_properties):
            raise ValueError(f"proprietà richieste incoerenti per la regola {rule.id}")
        if set(rule.required_evidence_types) != set(linked_control.required_evidence_types):
            raise ValueError(f"evidenze richieste incoerenti per la regola {rule.id}")
        if rule.relevant_system_required != linked_control.relevant_system_required:
            raise ValueError(f"rilevanza NIS incoerente per la regola {rule.id}")


def filter_current_evidence(
    env: NormalizedEnvironment,
    now: datetime,
    evidence_policies: dict[str, Any] | None = None,
) -> tuple[NormalizedEnvironment, list[EvidenceRejection]]:
    """Esclude evidenze scadute e registra il motivo per il report finale."""
    accepted, rejected = _classify_current_evidence(env, now, evidence_policies)
    return env.model_copy(update={"evidences": accepted}), rejected


def _classify_current_evidence(
    env: NormalizedEnvironment,
    now: datetime,
    evidence_policies: dict[str, Any] | None = None,
) -> tuple[list[Evidence], list[EvidenceRejection]]:
    """Classifica freshness senza copiare o modificare l'ambiente normalizzato."""
    active_policies = evidence_policies or load_evidence_policies(
        bundled_catalog_path("evidence_policies.example.yaml")
    )
    accepted: list[Evidence] = []
    rejected: list[EvidenceRejection] = []
    for evidence in env.evidences:
        policy = active_policies["policies"].get(evidence.evidence_type)
        if policy is None:
            rejected.append(
                {"evidence_id": evidence.id, "reason": "tipologia priva di policy di freschezza"}
            )
            continue
        expiry = evidence_expiry(evidence.model_dump(mode="python"), policy)
        if expiry is None:
            rejected.append(
                {"evidence_id": evidence.id, "reason": "validità non determinabile"}
            )
        elif expiry < now:
            rejected.append({"evidence_id": evidence.id, "reason": "evidenza scaduta"})
        else:
            accepted.append(evidence)
    return accepted, rejected


def populate_graph(
    env: NormalizedEnvironment, graph: GraphRepository | None = None
) -> GraphRepository:
    """Inserisce nel repository tutte le entità e relazioni dell'ambiente."""
    repository = graph or Neo4jGraphRepository(graph_id=env.dataset.id)
    repository.clear()
    repository.add_entity(env.dataset)
    repository.add_entity(env.organization)
    for group in (
        env.responsible_parties,
        env.processes,
        env.data_objects,
        env.assets,
        env.services,
        env.software_components,
        env.accounts,
        env.network_interfaces,
        env.network_flows,
        env.backups,
        env.security_capabilities,
        env.technical_exceptions,
        env.vulnerabilities,
        env.evidences,
        env.requirements,
        env.controls,
        env.provenance_records,
        env.inventory_states,
    ):
        for entity in group:
            repository.add_entity(entity)
    for relationship in env.relationships:
        repository.add_relationship(relationship)
    repository.add_relationship(
        Relationship(
            id=f"{env.dataset.id}:DESCRIBES",
            subject_id=env.dataset.id,
            predicate="DESCRIBES",
            object_id=env.organization.id,
        )
    )
    return repository


def populate_rules(graph: GraphRepository, rules: list[Rule]) -> None:
    """Persiste le regole e i loro collegamenti prima della valutazione."""
    for rule in rules:
        graph.add_entity(rule)
        for predicate, object_id in (
            ("IMPLEMENTS", rule.control_id),
            ("DERIVES_FROM", rule.requirement_id),
        ):
            graph.add_relationship(
                Relationship(
                    id=f"{rule.id}:{predicate}",
                    subject_id=rule.id,
                    predicate=predicate,
                    object_id=object_id,
                )
            )


def build_graph(
    input_path: Path, graph: GraphRepository | None = None
) -> tuple[Any, GraphRepository]:
    """Valida il dataset e popola il Knowledge Graph Neo4j selezionato."""
    env = load_environment(input_path)
    return env, populate_graph(env, graph)


async def execute_assessment(
    input_path: Path,
    rules_path: Path,
    assessment_id: str | None = None,
    requirements_path: Path | None = None,
    rules_override: list[Rule] | None = None,
    expected_organization_id: str | None = None,
    clock: Clock | None = None,
    id_factory: Callable[[], str] = random_assessment_id,
    graph: GraphRepository | None = None,
    evaluator_registry: dict[str, Evaluator] | None = None,
    evidence_policies_path: Path | None = None,
    operational_policy_path: Path | None = None,
    coverage_catalog_path: Path | None = None,
) -> dict[str, Any]:
    """Esegue la pipeline comune e restituisce il contesto senza creare artefatti."""
    env = load_environment(input_path)
    if expected_organization_id and env.organization.id != expected_organization_id:
        raise ValueError("il dataset non appartiene all'organizzazione selezionata")

    active_clock = clock or SystemClock()
    now = active_clock.now()

    # Se non viene indicato un file, cerchiamo il catalogo accanto al dataset.
    candidate = requirements_path or input_path.parent / "nis2_requirements.example.yaml"
    requirements = load_requirements(candidate) if candidate.exists() else env.requirements
    # Le evidenze appartengono già al NormalizedEnvironment validato. La copia
    # superficiale serve soltanto ad associare l'eventuale catalogo requisiti e
    # preserva la medesima collezione di evidenze prodotta dai Moduli 1-2.
    env = env.model_copy(update={"requirements": requirements})
    rules = rules_override if rules_override is not None else load_rules(rules_path)
    raw_rule_catalog = load_yaml_mapping(rules_path)
    rule_catalog_version = str(
        raw_rule_catalog.get("catalog_version") or max(rule.version for rule in rules)
    )
    evidence_candidate = _resolve_catalog_path(
        evidence_policies_path, rules_path.parent, "evidence_policies.example.yaml"
    )
    operational_candidate = _resolve_catalog_path(
        operational_policy_path, rules_path.parent, "operational_policy.example.yaml"
    )
    coverage_candidate = _resolve_catalog_path(
        coverage_catalog_path, rules_path.parent, "acn_coverage.example.yaml"
    )
    evidence_policies = load_evidence_policies(evidence_candidate)
    operational_policy = load_operational_policy(operational_candidate)
    coverage_catalog = load_coverage_catalog(coverage_candidate)
    rule_ids = {rule.id for rule in rules}
    coverage_ids = set(coverage_catalog["by_rule"])
    if rule_ids - coverage_ids or (len(rule_ids) == 26 and rule_ids != coverage_ids):
        raise CatalogValidationError(
            "copertura ACN",
            f"regole mancanti={sorted(rule_ids - coverage_ids)}, "
            f"record orfani={sorted(coverage_ids - rule_ids)}",
        )
    validate_framework_alignment(env, requirements, rules)
    # Le evidenze scadute restano nel Knowledge Graph con i relativi metadati:
    # il preflight generale deve poter distinguere una fonte assente da una
    # fonte presente ma non piu valida. La classificazione alimenta comunque
    # il report delle evidenze rifiutate.
    _, rejected_evidences = _classify_current_evidence(env, now, evidence_policies)

    assessment_id = assessment_id or id_factory()
    active_graph = graph or Neo4jGraphRepository(graph_id=assessment_id)
    active_graph = populate_graph(env, active_graph)
    populate_rules(active_graph, rules)
    # Da questo punto il motore legge esclusivamente il grafo: l'ambiente
    # normalizzato non viene passato agli evaluator.
    results, decisions = evaluate(
        active_graph,
        assessment_id,
        now,
        evaluator_registry=evaluator_registry,
        evidence_policies=evidence_policies,
        operational_policy=operational_policy,
    )
    # Gli esiti diventano parte dello stesso grafo e sono quindi interrogabili
    # in Cypher insieme ad asset, controlli e requisiti.
    for result in results:
        active_graph.add_entity(result)
        for predicate, object_id in (
            ("EVALUATES", result.asset_id),
            ("RESULT_OF", result.control_id),
            ("TRACES_TO", result.requirement_id),
            ("APPLIES_RULE", result.rule_id),
        ):
            active_graph.add_relationship(
                Relationship(
                    id=f"{result.id}:{predicate}",
                    subject_id=result.id,
                    predicate=predicate,
                    object_id=object_id,
                )
            )
    graph_assets = active_graph.find_entities("Asset")
    graph_controls = active_graph.find_entities("Control")
    graph_datasets = active_graph.find_entities("DatasetInfo")
    graph_organizations = active_graph.find_entities("Organization")
    graph_requirements = active_graph.find_entities("Requirement")
    graph_rules = active_graph.find_entities("Rule")
    graph_evidences = active_graph.find_entities("Evidence")
    graph_provenance_records = active_graph.find_entities("ProvenanceRecord")
    graph_entity_groups = {
        "DatasetInfo": graph_datasets,
        "Organization": graph_organizations,
        "ResponsibleParty": active_graph.find_entities("ResponsibleParty"),
        "Process": active_graph.find_entities("Process"),
        "DataObject": active_graph.find_entities("DataObject"),
        "Asset": graph_assets,
        "Service": active_graph.find_entities("Service"),
        "SoftwareComponent": active_graph.find_entities("SoftwareComponent"),
        "Account": active_graph.find_entities("Account"),
        "NetworkInterface": active_graph.find_entities("NetworkInterface"),
        "NetworkFlow": active_graph.find_entities("NetworkFlow"),
        "BackupRecord": active_graph.find_entities("BackupRecord"),
        "SecurityCapability": active_graph.find_entities("SecurityCapability"),
        "TechnicalException": active_graph.find_entities("TechnicalException"),
        "Vulnerability": active_graph.find_entities("Vulnerability"),
        "Evidence": graph_evidences,
        "ProvenanceRecord": graph_provenance_records,
        "InventoryState": active_graph.find_entities("InventoryState"),
        "Requirement": graph_requirements,
        "Control": graph_controls,
        "Rule": graph_rules,
        "AssessmentResult": active_graph.find_entities("AssessmentResult"),
    }
    graph_relationships = active_graph.list_relationships()
    if len(graph_datasets) != 1 or len(graph_organizations) != 1:
        raise ValueError("dataset o organizzazione mancanti nel Knowledge Graph")
    graph_dataset = graph_datasets[0]
    graph_organization = graph_organizations[0]
    summary = aggregate(results, graph_assets, graph_controls, operational_policy)
    return build_report_context(
        assessment_id=assessment_id,
        generated_at=now.isoformat(),
        requirements_source=(str(candidate) if candidate.exists() else "embedded_dataset"),
        evidence_input_source="normalized_environment",
        graph_id=str(getattr(active_graph, "graph_id", assessment_id)),
        dataset=graph_dataset,
        organization=graph_organization,
        assets=graph_assets,
        controls=graph_controls,
        requirements=graph_requirements,
        rules=graph_rules,
        evidences=graph_evidences,
        provenance_records=graph_provenance_records,
        graph_entities=graph_entity_groups,
        graph_relationships=graph_relationships,
        results=results,
        decisions=decisions,
        summary=summary,
        rejected_evidences=rejected_evidences,
        assessment_engine_version=__version__,
        rule_catalog_version=rule_catalog_version,
        framework_version=str(graph_organization.get("acn_specification", "")),
        evidence_policy_version=str(evidence_policies["policy_version"]),
        operational_policy_version=str(operational_policy["policy_version"]),
        coverage_catalog=coverage_catalog,
    )


async def run_assessment(
    input_path: Path,
    rules_path: Path,
    output_dir: Path,
    assessment_id: str | None = None,
    requirements_path: Path | None = None,
    rules_override: list[Rule] | None = None,
    expected_organization_id: str | None = None,
    clock: Clock | None = None,
    id_factory: Callable[[], str] = random_assessment_id,
    graph: GraphRepository | None = None,
    evaluator_registry: dict[str, Evaluator] | None = None,
    evidence_policies_path: Path | None = None,
    operational_policy_path: Path | None = None,
    coverage_catalog_path: Path | None = None,
) -> dict[str, Any]:
    """Esegue la pipeline comune e genera i tre artefatti dell'assessment."""
    report = await execute_assessment(
        input_path,
        rules_path,
        assessment_id=assessment_id,
        requirements_path=requirements_path,
        rules_override=rules_override,
        expected_organization_id=expected_organization_id,
        clock=clock,
        id_factory=id_factory,
        graph=graph,
        evaluator_registry=evaluator_registry,
        evidence_policies_path=evidence_policies_path,
        operational_policy_path=operational_policy_path,
        coverage_catalog_path=coverage_catalog_path,
    )
    active_assessment_id = str(report["assessment_id"])
    markdown_path = general_markdown_path(output_dir, active_assessment_id)
    attachment_path = technical_attachment_markdown_path(output_dir, active_assessment_id)
    graph_path = knowledge_graph_markdown_path(output_dir, active_assessment_id)
    report["report_files"] = {
        "general_markdown": str(markdown_path),
        "technical_attachment_markdown": str(attachment_path),
        "knowledge_graph_markdown": str(graph_path),
    }
    write_markdown(report, markdown_path)
    write_technical_attachment_markdown(report, attachment_path)
    write_knowledge_graph_markdown(report, graph_path)
    return report


def _resolve_catalog_path(explicit: Path | None, adjacent: Path, filename: str) -> Path:
    if explicit is not None:
        return explicit
    candidate = adjacent / filename
    return candidate if candidate.exists() else bundled_catalog_path(filename)
