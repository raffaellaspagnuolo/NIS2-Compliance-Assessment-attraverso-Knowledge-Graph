"""Adatta casi asset-controllo isolati alla pipeline applicativa generale.

La PoC costruisce soltanto ingressi normalizzati minimi, invoca
``execute_assessment`` una volta per caso e confronta gli esiti reali con una
ground truth caricata dopo le valutazioni. Non contiene evaluator, preflight o
logica di classificazione degli stati.
"""

from __future__ import annotations

import asyncio
import csv
import tempfile
from collections.abc import Iterable
from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

from nis2_assessor.application.pipeline import (
    execute_assessment,
    load_requirements,
    load_rules,
)
from nis2_assessor.application.ports import GraphRepository
from nis2_assessor.application.runtime import FixedClock
from nis2_assessor.application.validation import load_environment
from nis2_assessor.domain.enums import ComplianceStatus, GovernanceStatus, NisProfile
from nis2_assessor.domain.models import NormalizedEnvironment, Requirement, Rule

_ROOT = Path(__file__).parents[3]
_POC_INSTANT = datetime(2026, 8, 14, 10, 0, tzinfo=UTC)
_VALIDATION_CSV = "confronto-ground-truth-casi-uso-poc.csv"
_SOURCE_ASSET_ID = "asset-web"

CaseKind = Literal[
    "positive",
    "known_violation",
    "without_evidence",
    "important_profile",
    "mixed_conditions",
    "active_exception",
    "accepted_risk",
]

_CASE_SUFFIX: dict[str, str] = {
    "positive": "COMPLIANT",
    "known_violation": "VIOLATION",
    "without_evidence": "NO-EVIDENCE",
    "important_profile": "PROFILE-NA",
    "mixed_conditions": "PARTIAL",
    "active_exception": "MANUAL-EXCEPTION",
    "accepted_risk": "MANUAL-ACCEPTED-RISK",
}
_PURPOSES: dict[str, str] = {
    "positive": "Positive path: all observable rule conditions and required evidence are satisfied.",
    "known_violation": "Known values deliberately violate the technical conditions exercised by this rule.",
    "without_evidence": "A required evidence item is detached; the rule cannot be verified conclusively.",
    "important_profile": "The organization wrapper uses the important profile for an essential-only rule.",
    "mixed_conditions": "Only one of several technical conditions is violated while the others remain satisfied.",
    "active_exception": "An active technical exception is attached and requires human review.",
    "accepted_risk": "A vulnerability has an explicitly accepted exception and requires human review.",
}


class PoCRuleCases(BaseModel):
    """Varianti di conoscenza da applicare a una regola reale."""

    model_config = ConfigDict(extra="forbid")

    rule_id: str
    cases: list[CaseKind]
    partial_false: list[str] = Field(default_factory=list)


class PoCCaseCatalog(BaseModel):
    """Catalogo compatto espanso dal runner nei 93 casi autonomi."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str
    rules: list[PoCRuleCases]


class PoCCase(BaseModel):
    """Caso asset-controllo privo dell'esito atteso."""

    model_config = ConfigDict(extra="forbid")

    test_id: str
    rule_id: str
    kind: CaseKind
    purpose: str
    partial_false: list[str] = Field(default_factory=list)


class PoCGroundTruthRule(BaseModel):
    """Oracle separati per le varianti di una regola."""

    model_config = ConfigDict(extra="forbid")

    rule_id: str
    control_id: str
    requirement_id: str
    expected: dict[str, ComplianceStatus]
    expected_governance: dict[str, GovernanceStatus] = Field(default_factory=dict)


class PoCGroundTruthCatalog(BaseModel):
    """Documento delle aspettative, mai usato per costruire gli input."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str
    rules: list[PoCGroundTruthRule]


class PoCGroundTruth(BaseModel):
    """Aspettativa espansa per un singolo caso."""

    model_config = ConfigDict(extra="forbid")

    test_id: str
    rule_id: str
    control_id: str
    requirement_id: str
    expected_status: ComplianceStatus
    expected_governance_status: GovernanceStatus = GovernanceStatus.NONE


def load_cases(path: Path) -> list[PoCCase]:
    """Carica i casi senza accedere alla ground truth."""
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    catalog = PoCCaseCatalog.model_validate(raw)
    if catalog.schema_version != "1.0":
        raise ValueError("versione del catalogo PoC non supportata")
    cases = [
        PoCCase(
            test_id=f"TC-{group.rule_id}-{_CASE_SUFFIX[kind]}",
            rule_id=group.rule_id,
            kind=kind,
            purpose=_PURPOSES[kind],
            partial_false=group.partial_false if kind == "mixed_conditions" else [],
        )
        for group in catalog.rules
        for kind in group.cases
    ]
    _require_unique((item.test_id for item in cases), "test_id")
    return cases


def load_ground_truth(path: Path) -> list[PoCGroundTruth]:
    """Espande gli oracle mantenuti separati dagli input decisionali."""
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    catalog = PoCGroundTruthCatalog.model_validate(raw)
    if catalog.schema_version != "1.0":
        raise ValueError("versione della ground truth PoC non supportata")
    truths = [
        PoCGroundTruth(
            test_id=f"TC-{group.rule_id}-{_CASE_SUFFIX[kind]}",
            rule_id=group.rule_id,
            control_id=group.control_id,
            requirement_id=group.requirement_id,
            expected_status=status,
            expected_governance_status=group.expected_governance.get(
                kind, GovernanceStatus.NONE
            ),
        )
        for group in catalog.rules
        for kind, status in group.expected.items()
    ]
    _require_unique((item.test_id for item in truths), "test_id ground truth")
    return truths


def run_poc(
    cases_path: Path,
    ground_truth_path: Path,
    output_dir: Path,
    graph: GraphRepository | None = None,
    *,
    environment_template_path: Path = _ROOT / "data" / "normalized_environment.example.yaml",
    rules_path: Path = _ROOT / "data" / "technical_rules.example.yaml",
    requirements_path: Path = _ROOT / "data" / "nis2_requirements.example.yaml",
) -> dict[str, Any]:
    """Esegue la pipeline generale una volta per coppia e scrive un solo CSV."""
    cases = load_cases(cases_path)
    template = load_environment(environment_template_path)
    rules = {item.id: item for item in load_rules(rules_path)}
    requirements = {item.id: item for item in load_requirements(requirements_path)}
    controls = {item.id: item for item in template.controls}
    _validate_case_targets(cases, rules, requirements, controls)

    actual_rows = asyncio.run(
        _execute_cases(cases, template, rules, requirements, controls, graph)
    )

    # Gli oracle entrano in memoria soltanto dopo che ogni AssessmentResult e
    # stato prodotto dalla pipeline e persistito nel Knowledge Graph.
    truths = {item.test_id: item for item in load_ground_truth(ground_truth_path)}
    if set(truths) != {item.test_id for item in cases}:
        raise ValueError("casi e ground truth non hanno gli stessi identificativi")

    comparisons: list[dict[str, object]] = []
    for actual in actual_rows:
        truth = truths[str(actual["test_id"])]
        passed = (
            actual["asset_id"] == actual["expected_asset_id"]
            and actual["control_id"] == truth.control_id
            and actual["rule_id"] == truth.rule_id
            and actual["requirement_id"] == truth.requirement_id
            and actual["actual_status"] == truth.expected_status.value
            and actual["actual_governance_status"]
            == truth.expected_governance_status.value
        )
        comparisons.append(
            {
                "test_id": actual["test_id"],
                "asset_id": actual["asset_id"],
                "control_id": actual["control_id"],
                "rule_id": actual["rule_id"],
                "requirement_id": actual["requirement_id"],
                "expected_status": truth.expected_status.value.upper(),
                "actual_status": str(actual["actual_status"]).upper(),
                "expected_governance_status": truth.expected_governance_status.value.upper(),
                "actual_governance_status": str(
                    actual["actual_governance_status"]
                ).upper(),
                "passed": passed,
                "purpose": actual["purpose"],
                "details": actual["details"],
            }
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    validation_csv = output_dir / _VALIDATION_CSV
    _write_comparison_csv(comparisons, validation_csv)
    passed_count = sum(item["passed"] is True for item in comparisons)
    return {
        "case_count": len(cases),
        "passed_count": passed_count,
        "suite_type": "implementation_conformance_tests",
        "rule_conformance_rate": passed_count / len(cases),
        "pipeline": "execute_assessment",
        "pipeline_invocations": len(cases),
        "knowledge_graph_used_for_decisions": True,
        "results": actual_rows,
        "comparisons": comparisons,
        "report_files": {"validation_csv": str(validation_csv)},
    }


async def _execute_cases(
    cases: list[PoCCase],
    template: NormalizedEnvironment,
    rules: dict[str, Rule],
    requirements: dict[str, Requirement],
    controls: dict[str, Any],
    graph: GraphRepository | None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for case in cases:
        rule = rules[case.rule_id]
        requirement = requirements[rule.requirement_id]
        control = controls[rule.control_id]
        environment = _build_case_environment(case, template, rule, requirement, control)
        with tempfile.TemporaryDirectory(prefix="nis2-poc-") as temporary:
            directory = Path(temporary)
            input_path = directory / "normalized-environment.yaml"
            rule_path = directory / "technical-rules.yaml"
            requirement_path = directory / "requirements.yaml"
            _write_yaml(input_path, environment.model_dump(mode="json"))
            _write_yaml(
                rule_path,
                {"schema_version": "2.0", "rules": [rule.model_dump(mode="json")]},
            )
            _write_yaml(
                requirement_path,
                {
                    "schema_version": "2.0",
                    "requirements": [requirement.model_dump(mode="json")],
                },
            )
            report = await execute_assessment(
                input_path,
                rule_path,
                assessment_id=f"poc-{case.test_id.lower()}",
                requirements_path=requirement_path,
                clock=FixedClock(_POC_INSTANT),
                graph=graph,
                evidence_policies_path=_ROOT / "data" / "evidence_policies.example.yaml",
                operational_policy_path=_ROOT / "data" / "operational_policy.example.yaml",
                coverage_catalog_path=_ROOT / "data" / "acn_coverage.example.yaml",
            )
        results = report["assessment_results"]
        if len(results) != 1:
            raise ValueError(
                f"{case.test_id} deve produrre un solo AssessmentResult, trovati {len(results)}"
            )
        result = results[0]
        rows.append(
            {
                "test_id": case.test_id,
                "expected_asset_id": environment.assets[0].id,
                "asset_id": result["asset_id"],
                "control_id": result["control_id"],
                "rule_id": result["rule_id"],
                "requirement_id": result["requirement_id"],
                "actual_status": result["status"],
                "actual_governance_status": result["governance_status"],
                "purpose": case.purpose,
                "details": _result_details(result),
            }
        )
    return rows


def _build_case_environment(
    case: PoCCase,
    template: NormalizedEnvironment,
    rule: Rule,
    requirement: Requirement,
    control: Any,
) -> NormalizedEnvironment:
    """Crea l'involucro minimo senza anticipare la decisione dell'evaluator."""
    source = template.model_dump(mode="json")
    source_asset = next(item for item in source["assets"] if item["id"] == _SOURCE_ASSET_ID)
    asset_id = f"asset-{case.test_id.lower()}"
    asset = deepcopy(source_asset)
    asset.update(
        {
            "id": asset_id,
            "name": f"Asset sintetico {case.test_id}",
            "hostname": f"{case.test_id.lower()}.poc.invalid",
            "ip_addresses": ["192.0.2.10"],
            "process_ids": [],
            "service_ids": [],
            "data_object_ids": [],
            "evidence_ids": [],
            "properties": {},
        }
    )
    asset["nis_relevant"] = _known(True, "prov-inventory")
    asset["network_segment"] = _known("poc-segment", "prov-inventory")
    asset["internet_exposed"] = _known(False, "prov-inventory")

    groups = _select_supporting_entities(source, rule, asset_id)
    _prepare_compliant_knowledge(asset, groups, rule)

    evidence = [
        deepcopy(item)
        for item in source["evidences"]
        if item["evidence_type"] in set(rule.required_evidence_types)
    ]
    for item in evidence:
        item["asset_ids"] = [asset_id]
        item["control_ids"] = [rule.control_id]
        item["service_ids"] = [
            value for value in item.get("service_ids", []) if _entity_exists(groups, value)
        ]
        item["vulnerability_ids"] = [
            value
            for value in item.get("vulnerability_ids", [])
            if _entity_exists(groups, value)
        ]
        item["valid_until"] = "2026-12-31T23:59:59Z"

    _attach_evidence(groups, evidence)
    technical_exceptions: list[dict[str, Any]] = []
    profile = NisProfile.ESSENTIAL
    if case.kind == "known_violation":
        _apply_known_violation(asset, groups, rule)
    elif case.kind == "without_evidence":
        evidence = []
        _attach_evidence(groups, evidence)
    elif case.kind == "important_profile":
        profile = NisProfile.IMPORTANT
    elif case.kind == "mixed_conditions":
        _apply_partial_violation(asset, groups, case.partial_false)
    elif case.kind == "active_exception":
        technical_exceptions.append(
            {
                "id": f"exception-{case.test_id.lower()}",
                "asset_id": asset_id,
                "control_id": rule.control_id,
                "rationale": "Deroga tecnica sintetica della PoC",
                "compensating_measure": "Monitoraggio rafforzato sintetico",
                "residual_risk": "medium",
                "approval_reference": "POC-APPROVAL-001",
                "valid_until": "2026-12-31T23:59:59Z",
                "evidence_ids": [item["id"] for item in evidence],
                "provenance_ids": ["prov-governance"],
            }
        )
    elif case.kind == "accepted_risk":
        vulnerability = groups["vulnerabilities"][0]
        vulnerability["accepted_exception"] = _known(True, "prov-governance")

    asset["service_ids"] = [item["id"] for item in groups["services"]]
    asset["data_object_ids"] = [item["id"] for item in groups["data_objects"]]
    asset["evidence_ids"] = [item["id"] for item in evidence]

    responsible = deepcopy(source["responsible_parties"][0])
    responsible["id"] = "owner-poc"
    asset["owner_id"] = responsible["id"]
    relationships = [
        {
            "id": f"rel-{case.test_id.lower()}-control-requirement",
            "subject_id": rule.control_id,
            "predicate": "ASSOCIATED_WITH",
            "object_id": requirement.id,
            "provenance_ids": ["prov-governance"],
        },
        {
            "id": f"rel-{case.test_id.lower()}-control-asset",
            "subject_id": rule.control_id,
            "predicate": "APPLIES_TO",
            "object_id": asset_id,
            "provenance_ids": ["prov-inventory"],
        },
    ]
    relationships.extend(
        {
            "id": f"rel-{case.test_id.lower()}-evidence-{index}",
            "subject_id": item["id"],
            "predicate": "REFERS_TO",
            "object_id": asset_id,
            "provenance_ids": ["prov-inventory"],
        }
        for index, item in enumerate(evidence, start=1)
    )

    environment = {
        "schema_version": "2.0",
        "dataset": {
            "id": f"dataset-{case.test_id.lower()}",
            "name": f"Micro-organizzazione sintetica {case.test_id}",
            "generated_at": "2026-08-14T09:00:00Z",
            "description": "Fixture isolata asset-controllo della Proof of Concept",
            "source_systems": ["poc-case-adapter"],
        },
        "organization": {
            "id": f"org-{case.test_id.lower()}",
            "name": f"Organizzazione sintetica {case.test_id}",
            "nis_profile": profile.value,
            "risk_assessment_reference": "POC-RISK-ASSESSMENT",
            "acn_specification": "ACN specifiche di base 2.0",
        },
        "responsible_parties": [responsible],
        "processes": [],
        "data_objects": groups["data_objects"],
        "assets": [asset],
        "services": groups["services"],
        "software_components": groups["software_components"],
        "accounts": groups["accounts"],
        "network_flows": groups["network_flows"],
        "backups": groups["backups"],
        "security_capabilities": groups["security_capabilities"],
        "technical_exceptions": technical_exceptions,
        "vulnerabilities": groups["vulnerabilities"],
        "evidences": evidence,
        "requirements": [requirement.model_dump(mode="json")],
        "controls": [control.model_dump(mode="json")],
        "relationships": relationships,
        "provenance_records": _select_provenance(source, asset, groups, evidence),
    }
    return NormalizedEnvironment.model_validate(environment)


def _select_supporting_entities(
    source: dict[str, Any], rule: Rule, asset_id: str
) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {
        "data_objects": [],
        "services": [],
        "software_components": [],
        "accounts": [],
        "network_flows": [],
        "backups": [],
        "security_capabilities": [],
        "vulnerabilities": [],
    }
    mapping = {
        "DataObject": "data_objects",
        "Service": "services",
        "SoftwareComponent": "software_components",
        "Account": "accounts",
        "NetworkFlow": "network_flows",
        "BackupRecord": "backups",
        "SecurityCapability": "security_capabilities",
        "Vulnerability": "vulnerabilities",
    }
    entity_type = str(rule.parameters.get("entity_type", ""))
    if rule.evaluator in {"vulnerability_assessment", "vulnerability_treatment"}:
        entity_type = "Vulnerability"
    elif rule.evaluator == "supported_and_updated_software":
        entity_type = "SoftwareComponent"
    elif rule.evaluator == "cryptographic_configuration":
        entity_type = "Service"
    elif rule.evaluator == "data_object_protection":
        entity_type = "DataObject"
    group_name = mapping.get(entity_type)
    if group_name:
        candidates = source[group_name]
        capability_types = set(rule.parameters.get("capability_types", []))
        for candidate in candidates:
            if capability_types and candidate.get("capability_type") not in capability_types:
                continue
            item = deepcopy(candidate)
            if "asset_id" in item:
                item["asset_id"] = asset_id
            if "asset_ids" in item:
                item["asset_ids"] = [asset_id]
            if group_name == "vulnerabilities":
                item["service_id"] = None
            groups[group_name].append(item)
    if rule.id == "RULE-ID-AM-02":
        for source_group in ("services", "software_components"):
            if groups[source_group]:
                continue
            item = deepcopy(source[source_group][0])
            item["asset_id"] = asset_id
            groups[source_group].append(item)
    return groups


def _prepare_compliant_knowledge(
    asset: dict[str, Any], groups: dict[str, list[dict[str, Any]]], rule: Rule
) -> None:
    evaluator = rule.evaluator
    if evaluator == "vulnerability_assessment":
        asset["properties"]["extended_vulnerability_assessment_performed"] = _known(
            True, "prov-scan"
        )
        return
    if evaluator == "asset_properties":
        keys = [str(item) for item in rule.parameters.get("properties", [])]
        asset["properties"] = {key: _known(True, "prov-config") for key in keys}
        return

    entity_fields = {str(item) for item in rule.parameters.get("fields", [])}
    entity_fields.update(str(item) for item in rule.parameters.get("properties", []))
    selectors = {str(key): value for key, value in rule.parameters.get("selectors_any", {}).items()}
    entity_fields.update(selectors)
    if evaluator == "vulnerability_treatment":
        entity_fields.update({"remediation_status", "accepted_exception"})
    elif evaluator == "supported_and_updated_software":
        entity_fields.update({"support_status", "security_update_status"})
        if rule.parameters.get("critical_patch_test_required"):
            entity_fields.add("critical_update_tested")
    elif evaluator == "cryptographic_configuration":
        entity_fields.update({"encrypted", "tls_enabled", "tls_versions"})
    elif evaluator == "data_object_protection":
        entity_fields.add("removable_media")

    for item in _all_entities(groups):
        for key, value in list(item.items()):
            if _is_knowledge_value(value) and key not in entity_fields:
                item[key] = _unknown()
        for key in entity_fields:
            if key not in item:
                continue
            current = item[key]
            if _is_knowledge_value(current):
                item[key] = _positive_value(key, current)
            elif current in (None, "", []):
                item[key] = _positive_raw_value(key)
        for key, expected in selectors.items():
            if key in item:
                item[key] = _known(expected, "prov-config")
        if "evidence_ids" in item:
            item["evidence_ids"] = []

    if evaluator == "vulnerability_treatment":
        asset["properties"]["vulnerability_advisories_monitored"] = _known(
            True, "prov-config"
        )
        for item in groups["vulnerabilities"]:
            item["remediation_status"] = _known("remediated", "prov-patch")
            item["accepted_exception"] = _known(False, "prov-governance")
    elif evaluator == "supported_and_updated_software":
        for item in groups["software_components"]:
            item["support_status"] = _known("supported", "prov-patch")
            item["security_update_status"] = _known("within_risk_plan", "prov-patch")
            if rule.parameters.get("critical_patch_test_required"):
                item["critical_update_tested"] = _known(True, "prov-patch")
    elif evaluator == "cryptographic_configuration":
        for item in groups["services"]:
            item["internet_exposed"] = _known(True, "prov-config")
            item["encrypted"] = _known(True, "prov-config")
            item["tls_enabled"] = _known(True, "prov-config")
            item["tls_versions"] = _known(["TLSv1.3"], "prov-config")
            item["cryptographic_baseline_id"] = rule.parameters.get("baseline_id")
    elif evaluator == "data_object_protection":
        for item in groups["data_objects"]:
            for key in rule.parameters.get("properties", []):
                item[str(key)] = _known(True, "prov-config")
            item["removable_media"] = _known(True, "prov-config")
            item["removable_media_encrypted"] = _known(True, "prov-config")


def _apply_known_violation(
    asset: dict[str, Any],
    groups: dict[str, list[dict[str, Any]]],
    rule: Rule,
) -> None:
    evaluator = rule.evaluator
    if evaluator == "asset_properties":
        for key in asset["properties"]:
            asset["properties"][key] = _known(False, "prov-config")
    elif evaluator == "collection_inventory":
        fields = [str(item) for item in rule.parameters.get("fields", [])]
        for item in _all_entities(groups):
            for key in fields:
                if key not in item:
                    continue
                if _is_knowledge_value(item[key]):
                    current = item[key].get("value")
                    if key.endswith("_at"):
                        item[key] = _unknown()
                    else:
                        item[key] = _known(
                            False if isinstance(current, bool) else "", "prov-config"
                        )
                else:
                    item[key] = ""
    elif evaluator == "collection_booleans":
        fields = [str(item) for item in rule.parameters.get("properties", [])]
        for item in _all_entities(groups):
            for key in fields:
                if key in item:
                    item[key] = _known(False, "prov-config")
    elif evaluator == "vulnerability_assessment":
        asset["properties"]["extended_vulnerability_assessment_performed"] = _known(
            False, "prov-scan"
        )
    elif evaluator == "vulnerability_treatment":
        for item in groups["vulnerabilities"]:
            item["remediation_status"] = _known("in_progress", "prov-patch")
    elif evaluator == "supported_and_updated_software":
        for item in groups["software_components"]:
            item["support_status"] = _known("unsupported", "prov-patch")
            item["security_update_status"] = _known(
                "overdue_against_risk_plan", "prov-patch"
            )
            if rule.parameters.get("critical_patch_test_required"):
                item["critical_update_tested"] = _known(False, "prov-patch")
    elif evaluator == "cryptographic_configuration":
        for item in groups["services"]:
            item["encrypted"] = _known(False, "prov-config")
            item["tls_versions"] = _known(["TLSv1.0"], "prov-config")
            item["cryptographic_baseline_id"] = "WRONG-BASELINE"
    elif evaluator == "data_object_protection":
        for item in groups["data_objects"]:
            for key in rule.parameters.get("properties", []):
                item[str(key)] = _known(False, "prov-config")
            item["removable_media"] = _known(True, "prov-config")
            item["removable_media_encrypted"] = _known(False, "prov-config")


def _apply_partial_violation(
    asset: dict[str, Any],
    groups: dict[str, list[dict[str, Any]]],
    paths: list[str],
) -> None:
    if not paths:
        raise ValueError("un caso mixed_conditions richiede partial_false")
    for path in paths:
        entity_id, separator, field = path.partition(".")
        if not separator:
            if field := path:
                if field not in asset["properties"]:
                    raise ValueError(f"proprieta parziale inesistente: {field}")
                asset["properties"][field] = _known(False, "prov-config")
            continue
        entity = next(
            (item for item in _all_entities(groups) if item.get("id") == entity_id), None
        )
        if entity is None or field not in entity:
            raise ValueError(f"percorso parziale inesistente: {path}")
        entity[field] = _known(False, "prov-config")


def _attach_evidence(
    groups: dict[str, list[dict[str, Any]]], evidence: list[dict[str, Any]]
) -> None:
    evidence_ids = [item["id"] for item in evidence]
    for item in _all_entities(groups):
        if "evidence_ids" in item:
            item["evidence_ids"] = evidence_ids


def _select_provenance(
    source: dict[str, Any],
    asset: dict[str, Any],
    groups: dict[str, list[dict[str, Any]]],
    evidence: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    required = {"prov-inventory", "prov-governance"}
    for item in [asset, *_all_entities(groups), *evidence]:
        required.update(_collect_provenance_ids(item))
    return [
        deepcopy(item) for item in source["provenance_records"] if item["id"] in required
    ]


def _collect_provenance_ids(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        found.update(str(item) for item in value.get("provenance_ids", []))
        for nested in value.values():
            found.update(_collect_provenance_ids(nested))
        return found
    if isinstance(value, list):
        for nested in value:
            found.update(_collect_provenance_ids(nested))
        return found
    return set()


def _positive_value(key: str, current: dict[str, Any]) -> dict[str, Any]:
    value = current.get("value")
    if isinstance(value, bool):
        return _known(True, "prov-config")
    if key == "version":
        return _known("1.0.0", "prov-inventory")
    if key == "last_reviewed_at":
        return _known("2026-08-01T00:00:00Z", "prov-governance")
    if value in (None, "", []):
        return _known("synthetic-value", "prov-config")
    return _known(value, "prov-config")


def _positive_raw_value(key: str) -> str:
    return {
        "name": "Synthetic component",
        "source": "synthetic-source",
        "destination": "synthetic-destination",
        "transport_protocol": "tcp",
        "application_protocol": "https",
        "account_type": "individual",
    }.get(key, "synthetic-value")


def _known(value: Any, provenance_id: str) -> dict[str, Any]:
    return {
        "status": "known",
        "value": value,
        "provenance_ids": [provenance_id],
        "observation_type": "declared",
    }


def _unknown() -> dict[str, Any]:
    return {
        "status": "unknown",
        "value": None,
        "provenance_ids": [],
        "unknown_cause": "not_collected",
    }


def _is_knowledge_value(value: Any) -> bool:
    return isinstance(value, dict) and {"status", "value", "provenance_ids"} <= value.keys()


def _all_entities(groups: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    return [item for values in groups.values() for item in values]


def _entity_exists(groups: dict[str, list[dict[str, Any]]], entity_id: str) -> bool:
    return any(item.get("id") == entity_id for item in _all_entities(groups))


def _validate_case_targets(
    cases: list[PoCCase],
    rules: dict[str, Rule],
    requirements: dict[str, Requirement],
    controls: dict[str, Any],
) -> None:
    for case in cases:
        rule = rules.get(case.rule_id)
        if rule is None:
            raise ValueError(f"regola inesistente nel caso {case.test_id}: {case.rule_id}")
        if rule.requirement_id not in requirements or rule.control_id not in controls:
            raise ValueError(f"cataloghi generali incompleti per {case.test_id}")


def _result_details(result: dict[str, Any]) -> str:
    parts = [
        f"{item['path']}={item.get('observed_value')!r}:"
        + ("pass" if item.get("comparison_result") is True else "fail")
        for item in result.get("evaluated_facts", [])
    ]
    parts.extend(f"Missing {item}" for item in result.get("missing_information", []))
    if result.get("technical_exception_id"):
        parts.append(f"Active technical exception: {result['technical_exception_id']}")
    return " | ".join(parts) or str(result.get("reason", ""))


def _write_yaml(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )


def _write_comparison_csv(rows: list[dict[str, object]], path: Path) -> None:
    fieldnames = [
        "test_id",
        "asset_id",
        "control_id",
        "rule_id",
        "requirement_id",
        "expected_status",
        "actual_status",
        "expected_governance_status",
        "actual_governance_status",
        "passed",
        "purpose",
        "details",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _require_unique(values: Iterable[str], label: str) -> None:
    items = list(values)
    if len(items) != len(set(items)):
        raise ValueError(f"{label} duplicato nel catalogo PoC")
