"""Motore deterministico e conservativo basato esclusivamente sul Knowledge Graph."""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import NAMESPACE_URL, uuid5

from nis2_assessor.application.policies import (
    bundled_catalog_path,
    evidence_expiry,
    load_evidence_policies,
    load_operational_policy,
)
from nis2_assessor.application.ports import GraphRepository
from nis2_assessor.domain.enums import (
    ApplicabilityReasonCode,
    ApplicabilityStatus,
    ComplianceStatus,
    ConfidenceLevel,
    DecisionPolicyType,
    EntityAggregationPolicy,
    GovernanceStatus,
    InventoryStatus,
    KnowledgeValueStatus,
    NisProfile,
    ObservationType,
    SelectorStatus,
    UnknownCause,
)
from nis2_assessor.domain.models import (
    ApplicabilityResult,
    AssessmentResult,
    ConflictRecord,
    EvaluatedFact,
    KnowledgeValue,
    Rule,
    SelectorDecision,
    ViolationRecord,
)

GraphEntity = dict[str, Any]


@dataclass(slots=True)
class EvaluationOutput:
    """Risultato strutturato di un evaluator, prima della decision policy comune."""

    facts: list[EvaluatedFact] = field(default_factory=list)
    evidence_ids: list[str] = field(default_factory=list)
    missing_information: list[str] = field(default_factory=list)
    conflicting_information: list[ConflictRecord] = field(default_factory=list)
    forced_status: ComplianceStatus | None = None
    thresholds_used: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class PreflightResult:
    facts: list[EvaluatedFact] = field(default_factory=list)
    evidence_ids: list[str] = field(default_factory=list)
    missing_information: list[str] = field(default_factory=list)
    conflicts: list[ConflictRecord] = field(default_factory=list)
    discarded_evidence: list[dict[str, str]] = field(default_factory=list)
    thresholds_used: dict[str, Any] = field(default_factory=dict)


Evaluator = Callable[
    [GraphRepository, GraphEntity, Rule, ApplicabilityResult], EvaluationOutput
]


def unknown(value: KnowledgeValue[Any]) -> bool:
    return value.status in {KnowledgeValueStatus.UNKNOWN, KnowledgeValueStatus.CONFLICTING}


def fact(
    path: str,
    value: KnowledgeValue[Any],
    comparison: str,
    result: bool | None,
    rule: Rule | None = None,
    *,
    mandatory: bool | None = None,
) -> EvaluatedFact:
    condition = _condition(rule, path) if rule else None
    return EvaluatedFact(
        path=path,
        observed_value=value.value,
        value_status=value.status.value,
        comparison=comparison,
        comparison_result=result,
        provenance_ids=value.provenance_ids,
        mandatory=condition.mandatory if condition and mandatory is None else mandatory is not False,
        condition_origin=condition.origin if condition else "regulatory",
        observation_type=value.observation_type,
        observed_at=value.observed_at,
    )


def applicability(
    asset: GraphEntity,
    control: GraphEntity,
    rule: Rule,
    graph: GraphRepository,
    profile: NisProfile,
) -> ApplicabilityResult:
    """Determina soltanto il perimetro; la sufficienza informativa resta distinta."""
    checks = ["knowledge_graph_entities", "acn_profile"]
    asset_id = str(asset["id"])
    control_id = str(control["id"])
    missing_entities = [item for item in (asset_id, control_id) if not graph.entity_exists(item)]
    if missing_entities:
        return _undetermined(
            ApplicabilityReasonCode.MISSING_GRAPH_ENTITY,
            ["entità mancanti nel Knowledge Graph: " + ", ".join(missing_entities)],
            checks,
            [f"knowledge_graph.entity.{item}" for item in missing_entities],
        )
    if profile not in rule.applicable_profiles:
        return _not_applicable(
            ApplicabilityReasonCode.PROFILE_EXCLUDED,
            [f"regola esclusa dal profilo ACN {profile.value}"],
            checks,
        )
    if rule.relevant_system_required:
        checks.append("nis_relevant_system")
        relevance = _knowledge(asset, "nis_relevant")
        if relevance.status == KnowledgeValueStatus.KNOWN and relevance.value is False:
            return _not_applicable(
                ApplicabilityReasonCode.NIS_RELEVANCE_EXCLUDED,
                ["asset con rilevanza NIS nota e negativa"],
                checks,
            )
        if unknown(relevance) or relevance.value is not True:
            return _undetermined(
                ApplicabilityReasonCode.NIS_RELEVANCE_UNDETERMINED,
                ["rilevanza NIS dell'asset non determinabile"],
                checks,
                ["asset.nis_relevant"],
            )
    applicable_types = {str(item) for item in control.get("applicable_asset_types", [])}
    if str(asset.get("asset_type", "")) not in applicable_types:
        return _not_applicable(
            ApplicabilityReasonCode.ASSET_TYPE_EXCLUDED,
            ["tipo di asset escluso"],
            checks + ["asset_type"],
        )

    services = graph.find_entities("Service", {"asset_id": asset_id})
    if rule.applicability.get("has_internet_exposed_services"):
        if not services:
            return _absence_decision(
                graph,
                asset_id,
                "Service",
                checks + ["has_internet_exposed_services"],
                ApplicabilityReasonCode.SERVICES_ABSENT,
                ApplicabilityReasonCode.SERVICE_EXPOSURE_UNDETERMINED,
                "inventario Service completo e privo di record",
            )
        exposures = [(item, _knowledge(item, "internet_exposed")) for item in services]
        if not any(value.value is True for _, value in exposures):
            if any(unknown(value) for _, value in exposures):
                return _undetermined(
                    ApplicabilityReasonCode.SERVICE_EXPOSURE_UNDETERMINED,
                    ["esposizione Internet dei servizi non determinabile"],
                    checks + ["has_internet_exposed_services"],
                    [f"Service.{item['id']}.internet_exposed" for item, value in exposures if unknown(value)],
                )
            return _absence_decision(
                graph,
                asset_id,
                "Service",
                checks + ["has_internet_exposed_services"],
                ApplicabilityReasonCode.SERVICE_EXPOSURE_EXCLUDED,
                ApplicabilityReasonCode.SERVICE_EXPOSURE_UNDETERMINED,
                "inventario Service completo e nessun servizio esposto a Internet",
            )
    if rule.applicability.get("has_removable_media"):
        data_objects = [
            item
            for item in graph.find_entities("DataObject")
            if asset_id in {str(value) for value in item.get("asset_ids", [])}
        ]
        if not data_objects:
            return _absence_decision(
                graph,
                asset_id,
                "DataObject",
                checks + ["has_removable_media"],
                ApplicabilityReasonCode.REMOVABLE_MEDIA_EXCLUDED,
                ApplicabilityReasonCode.REMOVABLE_MEDIA_UNDETERMINED,
                "inventario DataObject completo e privo di record",
            )
        removable = [(item, _knowledge(item, "removable_media")) for item in data_objects]
        if not any(value.value is True for _, value in removable):
            if any(unknown(value) for _, value in removable):
                return _undetermined(
                    ApplicabilityReasonCode.REMOVABLE_MEDIA_UNDETERMINED,
                    ["presenza di supporti rimovibili non determinabile"],
                    checks + ["has_removable_media"],
                    [f"DataObject.{item['id']}.removable_media" for item, value in removable if unknown(value)],
                )
            return _absence_decision(
                graph,
                asset_id,
                "DataObject",
                checks + ["has_removable_media"],
                ApplicabilityReasonCode.REMOVABLE_MEDIA_EXCLUDED,
                ApplicabilityReasonCode.REMOVABLE_MEDIA_UNDETERMINED,
                "inventario DataObject completo e nessun supporto rimovibile presente",
            )

    selector_decisions, selected, undetermined = _select_entities(graph, asset, rule)
    if selector_decisions and rule.id != "RULE-PR-AA-05" and not selected:
        entity_type = str(rule.parameters.get("entity_type", "Entity"))
        if undetermined:
            return ApplicabilityResult(
                status=ApplicabilityStatus.UNDETERMINED,
                reason_code=ApplicabilityReasonCode.CONDITIONS_SATISFIED,
                reasons=["appartenenza delle entità al perimetro non determinabile"],
                evaluated_conditions=checks + ["selectors"],
                missing_information=[
                    value
                    for decision in selector_decisions
                    for value in decision.missing_information
                ],
                selector_decisions=selector_decisions,
                undetermined_entity_ids=undetermined,
            )
        if _inventory_status(graph, asset_id, entity_type) == InventoryStatus.COMPLETE:
            return ApplicabilityResult(
                status=ApplicabilityStatus.NOT_APPLICABLE,
                reason_code=ApplicabilityReasonCode.CONDITIONS_SATISFIED,
                reasons=["nessuna entità rientra certamente nel selector"],
                evaluated_conditions=checks + ["selectors"],
                selector_decisions=selector_decisions,
            )

    collection_entity_type = _rule_entity_type(rule)
    if collection_entity_type and not graph.find_entities(
        collection_entity_type, {"asset_id": asset_id}
    ):
        if (
            _inventory_status(graph, asset_id, collection_entity_type)
            == InventoryStatus.COMPLETE
            and rule.empty_collection_policy.value == "not_applicable"
        ):
            return ApplicabilityResult(
                status=ApplicabilityStatus.NOT_APPLICABLE,
                reason_code=ApplicabilityReasonCode.CONDITIONS_SATISFIED,
                reasons=[
                    f"inventario {collection_entity_type} completo e perimetro assente"
                ],
                evaluated_conditions=checks + ["empty_collection_policy"],
                selector_decisions=selector_decisions,
            )

    return ApplicabilityResult(
        status=ApplicabilityStatus.APPLICABLE,
        reason_code=ApplicabilityReasonCode.CONDITIONS_SATISFIED,
        reasons=["condizioni di applicabilità soddisfatte"],
        evaluated_conditions=checks,
        missing_information=[
            value
            for decision in selector_decisions
            if decision.status == SelectorStatus.UNDETERMINED
            for value in decision.missing_information
        ],
        selector_decisions=selector_decisions,
        selected_entity_ids=(
            [str(item["id"]) for item in graph.find_entities("Account", {"asset_id": asset_id})]
            if rule.id == "RULE-PR-AA-05"
            else selected
        ),
        undetermined_entity_ids=undetermined,
    )


def asset_properties(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del graph, decision
    output = EvaluationOutput(evidence_ids=_asset_evidence(asset))
    for key in [str(item) for item in rule.parameters.get("properties", [])]:
        value = _knowledge(asset, key)
        output.facts.append(fact(f"asset.{key}", value, "true", value.value is True, rule))
        _record_unknown(output, f"asset.{key}", value)
    return output


def collection_inventory(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del decision
    if rule.id == "RULE-ID-AM-02":
        return _software_services_system_inventory(graph, asset, rule)
    entity_type = str(rule.parameters["entity_type"])
    fields = [str(item) for item in rule.parameters.get("fields", [])]
    items = graph.find_entities(entity_type, {"asset_id": str(asset["id"])})
    output = EvaluationOutput()
    if not items:
        if _inventory_status(graph, str(asset["id"]), entity_type) == InventoryStatus.COMPLETE:
            output.forced_status = ComplianceStatus.NON_COMPLIANT
            output.facts.append(_synthetic_failure(f"{entity_type}.records", "almeno un record"))
        else:
            output.missing_information.append(f"{entity_type}.inventory_status")
        return output
    for item in items:
        _evaluate_inventory_fields(output, item, entity_type, fields, rule)
    output.evidence_ids = _entity_evidence(items)
    return output


def collection_booleans(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    entity_type = str(rule.parameters["entity_type"])
    fields = [str(item) for item in rule.parameters.get("properties", [])]
    all_items = graph.find_entities(entity_type, {"asset_id": str(asset["id"])})
    by_id = {str(item["id"]): item for item in all_items}
    items = [by_id[item_id] for item_id in decision.selected_entity_ids if item_id in by_id]
    if not rule.parameters.get("selectors_any") and not rule.parameters.get("selectors_all"):
        items = all_items
    required_types = {str(item) for item in rule.parameters.get("capability_types", [])}
    if required_types:
        items = [item for item in items if str(item.get("capability_type")) in required_types]
    output = EvaluationOutput()
    if not items:
        inventory_status = _inventory_status(graph, str(asset["id"]), entity_type)
        if inventory_status == InventoryStatus.COMPLETE and rule.empty_collection_policy.value == "non_compliant":
            output.forced_status = ComplianceStatus.NON_COMPLIANT
            output.facts.append(_synthetic_failure(f"{entity_type}.records", "capacità obbligatoria"))
        elif inventory_status == InventoryStatus.COMPLETE and rule.empty_collection_policy.value == "not_applicable":
            output.forced_status = ComplianceStatus.NOT_APPLICABLE
        elif inventory_status != InventoryStatus.COMPLETE:
            output.missing_information.append(f"{entity_type}.inventory_status")
        return output
    if rule.id == "RULE-PR-AA-05":
        for item in all_items:
            value = _knowledge(item, "least_privilege")
            output.facts.append(
                fact(f"Account.{item['id']}.least_privilege", value, "true", value.value is True, rule)
            )
            _record_unknown(output, f"Account.{item['id']}.least_privilege", value)
        privileged_ids = {
            decision_item.entity_id
            for decision_item in decision.selector_decisions
            if decision_item.status == SelectorStatus.SELECTED
        }
        for item in all_items:
            if str(item["id"]) not in privileged_ids:
                continue
            value = _knowledge(item, "separate_admin_account")
            output.facts.append(
                fact(
                    f"Account.{item['id']}.separate_admin_account",
                    value,
                    "true",
                    value.value is True,
                    rule,
                )
            )
            _record_unknown(output, f"Account.{item['id']}.separate_admin_account", value)
    else:
        for item in items:
            for key in fields:
                value = _knowledge(item, key)
                path = f"{entity_type}.{item['id']}.{key}"
                output.facts.append(fact(path, value, "true", value.value is True, rule))
                _record_unknown(output, path, value)
    output.evidence_ids = _entity_evidence(items)
    return output


def vulnerability_assessment(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del decision
    output = EvaluationOutput()
    performed = _knowledge(asset, "extended_vulnerability_assessment_performed")
    path = "asset.extended_vulnerability_assessment_performed"
    output.facts.append(fact(path, performed, "true", performed.value is True, rule))
    _record_unknown(output, path, performed)
    scans = [
        item
        for item in graph.find_entities("Evidence")
        if item.get("evidence_type") == "vulnerability_scan"
        and str(asset["id"]) in {str(value) for value in item.get("asset_ids", [])}
        and rule.control_id in {str(value) for value in item.get("control_ids", [])}
    ]
    output.evidence_ids = [str(item["id"]) for item in scans]
    for scan in scans:
        content = _json_mapping(scan.get("content_json"))
        for key in ("activity_description", "outcomes", "vulnerabilities", "impact_levels"):
            if key not in content:
                output.missing_information.append(f"Evidence.{scan['id']}.content.{key}")
    return output


def vulnerability_treatment(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del decision
    output = EvaluationOutput()
    monitored = _knowledge(asset, "vulnerability_advisories_monitored")
    monitored_path = "asset.vulnerability_advisories_monitored"
    output.facts.append(fact(monitored_path, monitored, "true", monitored.value is True, rule))
    _record_unknown(output, monitored_path, monitored)
    items = graph.find_entities("Vulnerability", {"asset_id": str(asset["id"])})
    if not items and _inventory_status(graph, str(asset["id"]), "Vulnerability") != InventoryStatus.COMPLETE:
        output.missing_information.append("Vulnerability.inventory_status")
    for item in items:
        value = _knowledge(item, "remediation_status")
        path = f"Vulnerability.{item['id']}.remediation_status"
        output.facts.append(
            fact(path, value, "remediated o mitigated", value.value in {"remediated", "mitigated"}, rule)
        )
        _record_unknown(output, path, value)
    output.evidence_ids = _entity_evidence(items)
    return output


def supported_and_updated_software(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del decision
    items = graph.find_entities("SoftwareComponent", {"asset_id": str(asset["id"])})
    output = EvaluationOutput()
    if not items:
        inventory_status = _inventory_status(graph, str(asset["id"]), "SoftwareComponent")
        if inventory_status == InventoryStatus.COMPLETE and rule.empty_collection_policy.value == "not_applicable":
            output.forced_status = ComplianceStatus.NOT_APPLICABLE
        elif inventory_status != InventoryStatus.COMPLETE:
            output.missing_information.append("SoftwareComponent.inventory_status")
        return output
    for item in items:
        for key, accepted in (
            ("support_status", {"supported"}),
            ("security_update_status", {"within_risk_plan", "current"}),
        ):
            value = _knowledge(item, key)
            path = f"SoftwareComponent.{item['id']}.{key}"
            output.facts.append(
                fact(path, value, "{" + ", ".join(sorted(accepted)) + "}", value.value in accepted, rule)
            )
            _record_unknown(output, path, value)
        if rule.parameters.get("critical_patch_test_required"):
            value = _knowledge(item, "critical_update_tested")
            path = f"SoftwareComponent.{item['id']}.critical_update_tested"
            output.facts.append(fact(path, value, "true", value.value is True, rule))
            _record_unknown(output, path, value)
    output.evidence_ids = _entity_evidence(items)
    return output


def cryptographic_configuration(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del decision
    services = [
        item
        for item in graph.find_entities("Service", {"asset_id": str(asset["id"])})
        if _knowledge(item, "internet_exposed").value is True
    ]
    output = EvaluationOutput(
        thresholds_used={
            "baseline_id": rule.parameters.get("baseline_id"),
            "allowed_tls_versions": rule.parameters.get("allowed_tls_versions", []),
            "origin": "project_baseline",
        }
    )
    allowed = {str(item) for item in rule.parameters.get("allowed_tls_versions", [])}
    for service in services:
        encrypted = _knowledge(service, "encrypted")
        path = f"Service.{service['id']}.encrypted"
        output.facts.append(fact(path, encrypted, "true", encrypted.value is True, rule))
        _record_unknown(output, path, encrypted)
        tls_enabled = _knowledge(service, "tls_enabled")
        versions = _knowledge(service, "tls_versions")
        if rule.parameters.get("requires_tls"):
            path = f"Service.{service['id']}.tls_enabled"
            output.facts.append(
                fact(path, tls_enabled, "true", tls_enabled.value is True, rule)
            )
            _record_unknown(output, path, tls_enabled)
        if tls_enabled.value is True and rule.parameters.get("requires_tls"):
            path = f"Service.{service['id']}.tls_versions"
            ok = isinstance(versions.value, list) and bool(versions.value) and set(versions.value) <= allowed
            output.facts.append(fact(path, versions, "baseline crittografica", ok, rule))
            _record_unknown(output, path, versions)
    output.evidence_ids = _entity_evidence(services)
    return output


def data_object_protection(
    graph: GraphRepository, asset: GraphEntity, rule: Rule, decision: ApplicabilityResult
) -> EvaluationOutput:
    del decision
    items = [
        item
        for item in graph.find_entities("DataObject")
        if str(asset["id"]) in {str(value) for value in item.get("asset_ids", [])}
        and _knowledge(item, "removable_media").value is True
    ]
    output = EvaluationOutput(evidence_ids=_asset_evidence(asset))
    for item in items:
        value = _knowledge(item, "removable_media_encrypted")
        path = f"DataObject.{item['id']}.removable_media_encrypted"
        output.facts.append(fact(path, value, "true", value.value is True, rule))
        _record_unknown(output, path, value)
    return output


CORE_EVALUATOR_REGISTRY: dict[str, Evaluator] = {
    "asset_properties": asset_properties,
    "collection_inventory": collection_inventory,
    "collection_booleans": collection_booleans,
    "vulnerability_assessment": vulnerability_assessment,
    "vulnerability_treatment": vulnerability_treatment,
    "supported_and_updated_software": supported_and_updated_software,
    "cryptographic_configuration": cryptographic_configuration,
    "data_object_protection": data_object_protection,
}
EVALUATOR_REGISTRY = CORE_EVALUATOR_REGISTRY


def evaluate(
    graph: GraphRepository,
    assessment_id: str,
    evaluated_at: datetime | None = None,
    evaluator_registry: dict[str, Evaluator] | None = None,
    evidence_policies: dict[str, Any] | None = None,
    operational_policy: dict[str, Any] | None = None,
) -> tuple[list[AssessmentResult], dict[str, ApplicabilityResult]]:
    """Valuta tutte le coppie asset-regola conservando ogni causa decisionale."""
    assets = graph.find_entities("Asset")
    controls = {str(item["id"]): item for item in graph.find_entities("Control")}
    requirements = {str(item["id"]): item for item in graph.find_entities("Requirement")}
    organizations = graph.find_entities("Organization")
    if len(organizations) != 1:
        raise ValueError("il Knowledge Graph deve contenere una sola organizzazione")
    profile = NisProfile(str(organizations[0]["nis_profile"]))
    rules = [_rule_from_graph(item) for item in graph.find_entities("Rule")]
    active_operational_policy = operational_policy or load_operational_policy(
        bundled_catalog_path("operational_policy.example.yaml")
    )
    rules = [_apply_technical_threshold(rule, active_operational_policy) for rule in rules]
    active_registry = evaluator_registry or CORE_EVALUATOR_REGISTRY
    missing_evaluators = {rule.evaluator for rule in rules} - active_registry.keys()
    unused_evaluators = active_registry.keys() - {rule.evaluator for rule in rules}
    if missing_evaluators:
        raise ValueError("evaluator non consentiti: " + ", ".join(sorted(missing_evaluators)))
    if evaluator_registry is None and len(rules) == 26 and unused_evaluators:
        raise ValueError("evaluator core non referenziati: " + ", ".join(sorted(unused_evaluators)))
    now = evaluated_at or datetime.now(UTC)
    active_evidence_policies = evidence_policies or load_evidence_policies(
        bundled_catalog_path("evidence_policies.example.yaml")
    )
    policy_records = active_evidence_policies["policies"]
    results: list[AssessmentResult] = []
    decisions: dict[str, ApplicabilityResult] = {}
    for asset in assets:
        asset_id = str(asset["id"])
        for rule in rules:
            control = controls.get(rule.control_id)
            requirement = requirements.get(rule.requirement_id)
            if control is None or requirement is None:
                raise ValueError(f"catalogo incompleto per {rule.id}")
            decision = applicability(asset, control, rule, graph, profile)
            decisions[f"{asset_id}:{rule.control_id}"] = decision
            if decision.status == ApplicabilityStatus.NOT_APPLICABLE:
                technical_status = ComplianceStatus.NOT_APPLICABLE
                output = EvaluationOutput()
                known_violations: list[ViolationRecord] = []
                conflicts: list[ConflictRecord] = []
                missing: list[str] = []
                evidence_ids: list[str] = []
                discarded_evidence: list[dict[str, str]] = []
            elif decision.status == ApplicabilityStatus.UNDETERMINED:
                technical_status = ComplianceStatus.NOT_VERIFIABLE
                output = EvaluationOutput()
                known_violations = []
                conflicts = [
                    conflict
                    for selector in decision.selector_decisions
                    for conflict in selector.conflicting_information
                ]
                missing = list(decision.missing_information)
                evidence_ids = []
                discarded_evidence = []
            else:
                preflight = _preflight(
                    graph,
                    asset,
                    rule,
                    now,
                    policy_records,
                    str(active_evidence_policies["policy_version"]),
                )
                discarded_evidence = preflight.discarded_evidence
                candidate_output = active_registry[rule.evaluator](graph, asset, rule, decision)
                if not isinstance(candidate_output, EvaluationOutput):
                    if (
                        isinstance(candidate_output, tuple)
                        and candidate_output
                        and candidate_output[0] == ComplianceStatus.NOT_APPLICABLE
                    ):
                        raise ValueError(
                            "NOT_APPLICABLE deve essere decisa dall'applicabilità"
                        )
                    raise TypeError("un evaluator deve restituire EvaluationOutput")
                output = candidate_output
                output.conflicting_information.extend(
                    conflict
                    for selector in decision.selector_decisions
                    for conflict in selector.conflicting_information
                )
                output.thresholds_used = {
                    **preflight.thresholds_used,
                    **output.thresholds_used,
                }
                output.facts = [*preflight.facts, *output.facts]
                # Solo le evidenze ammesse dal preflight entrano nella decisione.
                output.evidence_ids = sorted(set(preflight.evidence_ids))
                output.missing_information = sorted(
                    set(decision.missing_information + preflight.missing_information + output.missing_information)
                )
                output.conflicting_information = [*preflight.conflicts, *output.conflicting_information]
                technical_status, known_violations, missing, conflicts = _resolve(rule, output)
                evidence_ids = output.evidence_ids
            governance_status, exception_id = _governance_overlay(
                graph, asset_id, rule.control_id, now, policy_records
            )
            if rule.evaluator == "vulnerability_treatment" and any(
                _knowledge(item, "accepted_exception").value is True
                for item in graph.find_entities("Vulnerability", {"asset_id": asset_id})
            ):
                governance_status = GovernanceStatus.MANUAL_REVIEW_REQUIRED
            if conflicts:
                governance_status = GovernanceStatus.MANUAL_REVIEW_REQUIRED
            confidence = _confidence_level(technical_status, output.facts, missing, evidence_ids, graph)
            reason = (
                "; ".join(decision.reasons)
                if technical_status == ComplianceStatus.NOT_APPLICABLE
                or decision.status == ApplicabilityStatus.UNDETERMINED
                else rule.messages.get(technical_status.value, "Esito tecnico determinato dalla policy.")
            )
            technical_remediations = sorted(
                {
                    str(item.remediation or rule.recommendation)
                    for item in known_violations
                    if item.remediation or rule.recommendation
                }
            )
            information_actions = _information_actions(rule, missing, conflicts)
            result_id = str(
                uuid5(NAMESPACE_URL, f"{assessment_id}:{asset_id}:{rule.control_id}:{rule.version}")
            )
            results.append(
                AssessmentResult(
                    id=result_id,
                    assessment_id=assessment_id,
                    asset_id=asset_id,
                    control_id=rule.control_id,
                    requirement_id=rule.requirement_id,
                    rule_id=rule.id,
                    rule_version=rule.version,
                    technical_status=technical_status,
                    governance_status=governance_status,
                    reason=reason,
                    evaluated_facts=output.facts,
                    evidence_ids=evidence_ids,
                    missing_information=missing,
                    recommendation=(
                        rule.recommendation
                        if technical_status
                        in {ComplianceStatus.NON_COMPLIANT, ComplianceStatus.NOT_VERIFIABLE}
                        or governance_status == GovernanceStatus.MANUAL_REVIEW_REQUIRED
                        else None
                    ),
                    nis_profile=profile,
                    acn_point=str(requirement["acn_point"]),
                    verification_mode=rule.verification_mode,
                    risk_clause=rule.risk_clause,
                    technical_exception_id=exception_id,
                    evaluated_at=now,
                    confidence_level=confidence,
                    known_violations=known_violations,
                    conflicting_information=conflicts,
                    selector_decisions=decision.selector_decisions,
                    thresholds_used={**_thresholds(rule), **output.thresholds_used},
                    decision_policy=rule.decision_policy.type.value,
                    decision_trace={
                        "rule_id": rule.id,
                        "rule_version": rule.version,
                        "asset_id": asset_id,
                        "nis_profile": profile.value,
                        "evaluated_entity_ids": decision.selected_entity_ids,
                        "undetermined_entity_ids": decision.undetermined_entity_ids,
                        "selector_decisions": [
                            item.model_dump(mode="json") for item in decision.selector_decisions
                        ],
                        "conditions": [
                            item.model_dump(mode="json") for item in output.facts
                        ],
                        "admitted_evidence_ids": evidence_ids,
                        "discarded_evidence": discarded_evidence,
                        "thresholds": {**_thresholds(rule), **output.thresholds_used},
                        "decision_policy": rule.decision_policy.model_dump(mode="json"),
                        "technical_status": technical_status.value,
                        "governance_status": governance_status.value,
                        "evaluated_at": now.isoformat(),
                    },
                    technical_remediations=technical_remediations,
                    information_actions=information_actions,
                    errors=[],
                )
            )
    return results, decisions


def _preflight(
    graph: GraphRepository,
    asset: GraphEntity,
    rule: Rule,
    evaluated_at: datetime,
    policies: dict[str, Any],
    policy_version: str,
) -> PreflightResult:
    result = PreflightResult()
    asset_id = str(asset["id"])
    all_evidence = graph.find_entities("Evidence")
    candidate_evidence = [
        item
        for item in all_evidence
        if str(item.get("evidence_type")) in set(rule.required_evidence_types)
    ]
    matched = [
        item
        for item in candidate_evidence
        if asset_id in {str(value) for value in item.get("asset_ids", [])}
        and rule.control_id in {str(value) for value in item.get("control_ids", [])}
    ]
    matched_ids = {str(item["id"]) for item in matched}
    result.discarded_evidence.extend(
        {"evidence_id": str(item["id"]), "reason": "associazione asset/controllo non valida"}
        for item in candidate_evidence
        if str(item["id"]) not in matched_ids
    )
    valid: list[GraphEntity] = []
    for item in matched:
        evidence_type = str(item.get("evidence_type"))
        policy = policies.get(evidence_type)
        if not isinstance(policy, dict):
            result.missing_information.append(f"evidence_policy.{evidence_type}")
            result.discarded_evidence.append(
                {"evidence_id": str(item["id"]), "reason": "policy assente"}
            )
            continue
        collected_at = _datetime(item.get("collected_at"))
        expiry = evidence_expiry(item, policy)
        result.thresholds_used[f"evidence.{item['id']}.freshness"] = {
            "value": expiry.isoformat() if expiry else None,
            "maximum_age_days": policy.get("maximum_age_days"),
            "valid_until": item.get("valid_until"),
            "policy": "evidence_freshness",
            "policy_version": policy_version,
            "origin": "project_baseline",
        }
        current = collected_at is not None and collected_at <= evaluated_at and expiry is not None and expiry >= evaluated_at
        if not current:
            result.missing_information.append(f"Evidence.{item['id']}.stale_information")
            result.discarded_evidence.append(
                {"evidence_id": str(item["id"]), "reason": "evidenza non corrente"}
            )
            continue
        if not item.get("source") or not item.get("source_category") or not item.get("provenance_ids"):
            result.missing_information.append(f"Evidence.{item['id']}.provenance")
            result.discarded_evidence.append(
                {"evidence_id": str(item["id"]), "reason": "provenienza insufficiente"}
            )
            continue
        valid.append(item)
    observed_types = {str(item.get("evidence_type")) for item in valid}
    result.missing_information.extend(
        f"evidence.{item}" for item in sorted(set(rule.required_evidence_types) - observed_types)
    )
    result.evidence_ids = [str(item["id"]) for item in valid]
    result.conflicts.extend(_evidence_conflicts(valid, policies))
    result.missing_information.extend(_missing_required_properties(graph, asset, rule))
    return result


def _resolve(
    rule: Rule, output: EvaluationOutput
) -> tuple[ComplianceStatus, list[ViolationRecord], list[str], list[ConflictRecord]]:
    conflicts = [
        item
        for item in output.conflicting_information
        if _path_is_mandatory(rule, item.path)
    ]
    for item in output.facts:
        if item.mandatory and item.value_status == KnowledgeValueStatus.CONFLICTING.value:
            conflicts.append(
                ConflictRecord(path=item.path, provenance_ids=item.provenance_ids)
            )
    missing = sorted(
        set(
            [
                path
                for path in output.missing_information
                if _path_is_mandatory(rule, path)
            ]
            + [
                item.path
                for item in output.facts
                if item.mandatory
                and item.value_status in {
                    KnowledgeValueStatus.UNKNOWN.value,
                    KnowledgeValueStatus.CONFLICTING.value,
                }
            ]
        )
    )
    mandatory_facts = [item for item in output.facts if item.mandatory]
    by_entity: dict[str, list[EvaluatedFact]] = {}
    for item in mandatory_facts:
        by_entity.setdefault(_fact_entity_key(item), []).append(item)
    condition_policy = (
        DecisionPolicyType.ALL_REQUIRED
        if rule.decision_policy.type == DecisionPolicyType.PER_ENTITY
        else rule.decision_policy.type
    )
    entity_statuses = [
        _condition_set_status(items, condition_policy, rule.decision_policy.threshold)
        for items in by_entity.values()
    ]
    status = _aggregate_entity_statuses(
        entity_statuses,
        rule.decision_policy.entity_aggregation,
        rule.decision_policy.threshold,
    )
    fact_paths = {item.path.lower() for item in mandatory_facts}
    external_missing = [
        path for path in missing if _path_without_cause(path).lower() not in fact_paths
    ]
    external_conflicts = [
        item for item in conflicts if item.path.lower() not in fact_paths
    ]
    if output.forced_status is not None:
        status = output.forced_status
    elif status == ComplianceStatus.COMPLIANT and (
        external_missing or external_conflicts
    ):
        status = ComplianceStatus.NOT_VERIFIABLE

    violations: list[ViolationRecord] = []
    if status == ComplianceStatus.NON_COMPLIANT:
        violations = [
            ViolationRecord(
                path=item.path,
                observed_value=item.observed_value,
                comparison=item.comparison,
                remediation=(
                    _condition(rule, item.path).remediation
                    if _condition(rule, item.path)
                    else rule.recommendation
                ),
            )
            for item in mandatory_facts
            if item.value_status == KnowledgeValueStatus.KNOWN.value
            and item.comparison_result is False
        ]
    if status == ComplianceStatus.NON_COMPLIANT and not violations:
        violations.append(
            ViolationRecord(
                path="collection.records",
                observed_value=[],
                comparison="collezione obbligatoria non vuota",
                remediation=rule.recommendation,
            )
        )
    if status == ComplianceStatus.PARTIALLY_COMPLIANT or (
        status not in rule.allowed_outcomes and status != ComplianceStatus.NOT_APPLICABLE
    ):
        raise ValueError(f"esito {status.value} non ammesso da {rule.id}")
    return status, violations, missing, _unique_conflicts(conflicts)


def _condition_set_status(
    facts: list[EvaluatedFact],
    policy: DecisionPolicyType,
    threshold: float | None,
) -> ComplianceStatus:
    if not facts:
        return ComplianceStatus.COMPLIANT
    satisfied = sum(
        item.value_status == KnowledgeValueStatus.KNOWN.value
        and item.comparison_result is True
        for item in facts
    )
    failed = sum(
        item.value_status == KnowledgeValueStatus.KNOWN.value
        and item.comparison_result is False
        for item in facts
    )
    uncertain = len(facts) - satisfied - failed
    if policy in {
        DecisionPolicyType.ALL_REQUIRED,
        DecisionPolicyType.MANDATORY_PLUS_OPTIONAL,
    }:
        if failed:
            return ComplianceStatus.NON_COMPLIANT
        return (
            ComplianceStatus.NOT_VERIFIABLE
            if uncertain
            else ComplianceStatus.COMPLIANT
        )
    if policy == DecisionPolicyType.AT_LEAST_ONE:
        if satisfied:
            return ComplianceStatus.COMPLIANT
        return (
            ComplianceStatus.NOT_VERIFIABLE
            if uncertain
            else ComplianceStatus.NON_COMPLIANT
        )
    if policy == DecisionPolicyType.THRESHOLD:
        if threshold is None:
            raise ValueError("threshold mancante nella decision policy")
        if satisfied / len(facts) >= threshold:
            return ComplianceStatus.COMPLIANT
        if (satisfied + uncertain) / len(facts) < threshold:
            return ComplianceStatus.NON_COMPLIANT
        return ComplianceStatus.NOT_VERIFIABLE
    raise ValueError(f"decision policy non supportata: {policy.value}")


def _aggregate_entity_statuses(
    statuses: list[ComplianceStatus],
    policy: EntityAggregationPolicy,
    threshold: float | None,
) -> ComplianceStatus:
    if not statuses:
        return ComplianceStatus.COMPLIANT
    failures = statuses.count(ComplianceStatus.NON_COMPLIANT)
    satisfied = statuses.count(ComplianceStatus.COMPLIANT)
    uncertain = statuses.count(ComplianceStatus.NOT_VERIFIABLE)
    if policy in {
        EntityAggregationPolicy.ALL_MUST_PASS,
        EntityAggregationPolicy.ANY_FAILURE_FAILS,
    }:
        if failures:
            return ComplianceStatus.NON_COMPLIANT
        return (
            ComplianceStatus.NOT_VERIFIABLE
            if uncertain
            else ComplianceStatus.COMPLIANT
        )
    if policy == EntityAggregationPolicy.BEST_EFFORT:
        if failures:
            return ComplianceStatus.NON_COMPLIANT
        if satisfied:
            return ComplianceStatus.COMPLIANT
        return ComplianceStatus.NOT_VERIFIABLE
    if policy == EntityAggregationPolicy.THRESHOLD:
        if threshold is None:
            raise ValueError("threshold mancante nell'entity aggregation")
        if satisfied / len(statuses) >= threshold:
            return ComplianceStatus.COMPLIANT
        if (satisfied + uncertain) / len(statuses) < threshold:
            return ComplianceStatus.NON_COMPLIANT
        return ComplianceStatus.NOT_VERIFIABLE
    raise ValueError(f"entity aggregation non supportata: {policy.value}")


def _fact_entity_key(item: EvaluatedFact) -> str:
    parts = item.path.split(".")
    if len(parts) >= 3 and parts[0].lower() not in {"asset", "evidence"}:
        return ".".join(parts[:2])
    return "__rule__"


def _select_entities(
    graph: GraphRepository, asset: GraphEntity, rule: Rule
) -> tuple[list[SelectorDecision], list[str], list[str]]:
    selectors_any = rule.parameters.get("selectors_any", {})
    selectors_all = rule.parameters.get("selectors_all", {})
    if not selectors_any and not selectors_all:
        return [], [], []
    entity_type = str(rule.parameters.get("entity_type", ""))
    items = graph.find_entities(entity_type, {"asset_id": str(asset["id"])})
    decisions: list[SelectorDecision] = []
    selected: list[str] = []
    undetermined: list[str] = []
    for item in items:
        decision = _selector_decision(item, selectors_any, selectors_all)
        decisions.append(decision)
        if decision.status == SelectorStatus.SELECTED:
            selected.append(str(item["id"]))
        elif decision.status == SelectorStatus.UNDETERMINED:
            undetermined.append(str(item["id"]))
    return decisions, selected, undetermined


def _selector_decision(
    item: GraphEntity, selectors_any: dict[str, Any], selectors_all: dict[str, Any]
) -> SelectorDecision:
    selector_type = "any" if selectors_any else "all"
    selectors = selectors_any or selectors_all
    evaluations: list[bool | None] = []
    missing: list[str] = []
    conflicts: list[ConflictRecord] = []
    for key, expected in selectors.items():
        value = _knowledge(item, str(key))
        if unknown(value):
            evaluations.append(None)
            missing.append(f"{item['id']}.{key}")
            if value.status == KnowledgeValueStatus.CONFLICTING:
                conflicts.append(
                    ConflictRecord(
                        path=f"{item['id']}.{key}",
                        provenance_ids=value.provenance_ids,
                    )
                )
        else:
            evaluations.append(value.value == expected)
    if selector_type == "any":
        status = (
            SelectorStatus.SELECTED
            if any(value is True for value in evaluations)
            else SelectorStatus.NOT_SELECTED
            if all(value is False for value in evaluations)
            else SelectorStatus.UNDETERMINED
        )
    else:
        status = (
            SelectorStatus.NOT_SELECTED
            if any(value is False for value in evaluations)
            else SelectorStatus.SELECTED
            if all(value is True for value in evaluations)
            else SelectorStatus.UNDETERMINED
        )
    return SelectorDecision(
        entity_id=str(item["id"]),
        status=status,
        selector_type=selector_type,
        evaluated_fields=[str(key) for key in selectors],
        missing_information=missing,
        conflicting_information=conflicts,
    )


def _software_services_system_inventory(
    graph: GraphRepository, asset: GraphEntity, rule: Rule
) -> EvaluationOutput:
    output = EvaluationOutput()
    output.facts.append(
        EvaluatedFact(
            path=f"Asset.{asset['id']}.name",
            observed_value=asset.get("name"),
            value_status="known" if asset.get("name") else "unknown",
            comparison="identificato",
            comparison_result=bool(asset.get("name")),
        )
    )
    collections = [
        ("Service", ["name", "authorized"]),
        ("SoftwareComponent", ["name", "version", "authorized"]),
    ]
    all_items: list[GraphEntity] = []
    for entity_type, fields in collections:
        items = graph.find_entities(entity_type, {"asset_id": str(asset["id"])})
        if not items:
            inventory_status = _inventory_status(graph, str(asset["id"]), entity_type)
            if inventory_status != InventoryStatus.COMPLETE:
                output.missing_information.append(f"{entity_type}.inventory_status")
            elif entity_type == "SoftwareComponent":
                output.facts.append(
                    _synthetic_failure("SoftwareComponent.records", "inventario software non vuoto")
                )
        for item in items:
            _evaluate_inventory_fields(output, item, entity_type, fields, rule)
        all_items.extend(items)
    output.evidence_ids = _entity_evidence(all_items)
    return output


def _evaluate_inventory_fields(
    output: EvaluationOutput,
    item: GraphEntity,
    entity_type: str,
    fields: list[str],
    rule: Rule,
) -> None:
    for key in fields:
        path = f"{entity_type}.{item['id']}.{key}"
        configured_condition = _condition(rule, path)
        mandatory = configured_condition.mandatory if configured_condition else False
        if f"{key}_status" in item:
            value = _knowledge(item, key)
            present = value.value not in (None, "", [])
            if isinstance(value.value, bool):
                present = value.value is True
            output.facts.append(
                fact(
                    path,
                    value,
                    "presente e autorizzato",
                    present,
                    rule,
                    mandatory=mandatory,
                )
            )
            if mandatory:
                _record_unknown(output, path, value)
        else:
            raw = item.get(key)
            output.facts.append(
                EvaluatedFact(
                    path=path,
                    observed_value=raw,
                    value_status="known" if raw not in (None, "", []) else "unknown",
                    comparison="presente",
                    comparison_result=raw not in (None, "", []),
                    mandatory=mandatory,
                )
            )
            if mandatory and raw in (None, "", []):
                output.missing_information.append(path)


def _inventory_status(
    graph: GraphRepository, asset_id: str, entity_type: str
) -> InventoryStatus:
    records = [
        item
        for item in graph.find_entities("InventoryState")
        if str(item.get("scope_id")) == asset_id and str(item.get("entity_type")) == entity_type
    ]
    if not records:
        return InventoryStatus.UNKNOWN
    try:
        return InventoryStatus(str(records[0].get("status", "unknown")))
    except ValueError:
        return InventoryStatus.UNKNOWN


def _rule_entity_type(rule: Rule) -> str | None:
    configured = rule.parameters.get("entity_type")
    if configured:
        return str(configured)
    return {
        "supported_and_updated_software": "SoftwareComponent",
        "vulnerability_treatment": "Vulnerability",
        "cryptographic_configuration": "Service",
    }.get(rule.evaluator)


def _absence_decision(
    graph: GraphRepository,
    asset_id: str,
    entity_type: str,
    checks: list[str],
    absent_reason: ApplicabilityReasonCode,
    undetermined_reason: ApplicabilityReasonCode,
    absent_message: str,
) -> ApplicabilityResult:
    inventory_status = _inventory_status(graph, asset_id, entity_type)
    if inventory_status == InventoryStatus.COMPLETE:
        return _not_applicable(
            absent_reason,
            [absent_message],
            checks,
        )
    completeness = (
        f"inventario {entity_type} dichiarato incompleto"
        if inventory_status == InventoryStatus.INCOMPLETE
        else f"completezza dell'inventario {entity_type} non nota"
    )
    return _undetermined(
        undetermined_reason,
        [completeness],
        checks,
        [f"{entity_type}.inventory_status"],
    )


def _not_applicable(
    reason: ApplicabilityReasonCode, messages: list[str], checks: list[str]
) -> ApplicabilityResult:
    return ApplicabilityResult(
        status=ApplicabilityStatus.NOT_APPLICABLE,
        reason_code=reason,
        reasons=messages,
        evaluated_conditions=checks,
    )


def _undetermined(
    reason: ApplicabilityReasonCode,
    messages: list[str],
    checks: list[str],
    missing: list[str],
) -> ApplicabilityResult:
    return ApplicabilityResult(
        status=ApplicabilityStatus.UNDETERMINED,
        reason_code=reason,
        reasons=messages,
        evaluated_conditions=checks,
        missing_information=missing,
    )


def _governance_overlay(
    graph: GraphRepository,
    asset_id: str,
    control_id: str,
    evaluated_at: datetime,
    policies: dict[str, Any],
) -> tuple[GovernanceStatus, str | None]:
    exceptions = graph.find_entities(
        "TechnicalException", {"asset_id": asset_id, "control_id": control_id}
    )
    if not exceptions:
        return GovernanceStatus.NONE, None
    exception = exceptions[0]
    valid_until = _datetime(exception.get("valid_until"))
    evidence_map = {str(item["id"]): item for item in graph.find_entities("Evidence")}
    supported = False
    for evidence_id in exception.get("evidence_ids", []):
        evidence = evidence_map.get(str(evidence_id))
        if not evidence:
            continue
        policy = policies.get(str(evidence.get("evidence_type")))
        expiry = evidence_expiry(evidence, policy) if isinstance(policy, dict) else None
        if expiry and expiry >= evaluated_at:
            supported = True
    active = valid_until is None or valid_until >= evaluated_at
    return (
        GovernanceStatus.MANUAL_REVIEW_REQUIRED
        if active or not supported
        else GovernanceStatus.NONE,
        str(exception["id"]),
    )


def _confidence_level(
    status: ComplianceStatus,
    facts: list[EvaluatedFact],
    missing: list[str],
    evidence_ids: list[str],
    graph: GraphRepository,
) -> ConfidenceLevel:
    if status == ComplianceStatus.NOT_APPLICABLE:
        return ConfidenceLevel.INSUFFICIENT
    if missing or any(item.value_status == "conflicting" for item in facts):
        return ConfidenceLevel.INSUFFICIENT
    observation_types = {item.observation_type for item in facts if item.observation_type}
    evidence_map = {str(item["id"]): item for item in graph.find_entities("Evidence")}
    reliabilities = {
        str(evidence_map[item].get("reliability", "")).lower()
        for item in evidence_ids
        if item in evidence_map
    }
    if ObservationType.DECLARED in observation_types or "low" in reliabilities:
        return ConfidenceLevel.LOW
    if ObservationType.EVIDENCE_BASED in observation_types or "medium" in reliabilities:
        return ConfidenceLevel.MEDIUM
    provenance_ids = {value for item in facts for value in item.provenance_ids}
    if (facts and evidence_ids) or len(provenance_ids) >= 2:
        return ConfidenceLevel.HIGH
    if facts or evidence_ids:
        return ConfidenceLevel.MEDIUM
    return ConfidenceLevel.LOW


def _evidence_conflicts(
    evidence: list[GraphEntity], policies: dict[str, Any]
) -> list[ConflictRecord]:
    conflicts: list[ConflictRecord] = []
    by_type: dict[str, list[GraphEntity]] = {}
    for item in evidence:
        by_type.setdefault(str(item.get("evidence_type")), []).append(item)
    for evidence_type, items in by_type.items():
        if len(items) < 2:
            continue
        policy = policies.get(evidence_type, {})
        priorities = [str(value) for value in policy.get("source_priority", [])]
        ranks = {
            str(item.get("id")): priorities.index(str(item.get("source_category")))
            if str(item.get("source_category")) in priorities
            else len(priorities)
            for item in items
        }
        best_rank = min(ranks.values())
        candidates = [item for item in items if ranks[str(item.get("id"))] == best_rank]
        if policy.get("prefer_latest_same_source"):
            sources = {str(item.get("source")) for item in candidates}
            if len(sources) == 1:
                timestamps = [
                    timestamp
                    for item in candidates
                    if (timestamp := _datetime(item.get("collected_at"))) is not None
                ]
                latest = max(timestamps, default=None)
                candidates = [
                    item for item in candidates if _datetime(item.get("collected_at")) == latest
                ]
        contents = {_canonical_content(item) for item in candidates}
        if len(contents) > 1:
            conflicts.append(
                ConflictRecord(
                    path=f"Evidence.{evidence_type}.content",
                    provenance_ids=sorted(
                        {
                            str(value)
                            for item in candidates
                            for value in item.get("provenance_ids", [])
                        }
                    ),
                )
            )
    return conflicts


def _missing_required_properties(
    graph: GraphRepository, asset: GraphEntity, rule: Rule
) -> list[str]:
    entity_types = {
        "service": "Service",
        "vulnerability": "Vulnerability",
        "software_component": "SoftwareComponent",
        "account": "Account",
        "network_interface": "NetworkInterface",
        "network_flow": "NetworkFlow",
        "backup": "BackupRecord",
        "security_capability": "SecurityCapability",
    }
    missing: list[str] = []
    for path in rule.required_properties:
        configured_condition = _condition(rule, path)
        if configured_condition is not None and not configured_condition.mandatory:
            continue
        prefix, _, key = path.partition(".")
        if prefix == "asset":
            value = _knowledge(asset, key)
            if unknown(value):
                missing.append(path)
            continue
        entity_type = entity_types.get(prefix)
        if not entity_type:
            continue
        items = graph.find_entities(entity_type, {"asset_id": str(asset["id"])})
        if not items:
            if _inventory_status(graph, str(asset["id"]), entity_type) != InventoryStatus.COMPLETE:
                missing.append(f"{prefix}.inventory_status")
            continue
        if all(unknown(_knowledge(item, key)) for item in items):
            missing.append(path)
    return sorted(set(missing))


def _record_unknown(output: EvaluationOutput, path: str, value: KnowledgeValue[Any]) -> None:
    if value.status == KnowledgeValueStatus.CONFLICTING:
        output.conflicting_information.append(
            ConflictRecord(path=path, provenance_ids=value.provenance_ids)
        )
    elif value.status == KnowledgeValueStatus.UNKNOWN:
        suffix = value.unknown_cause.value if value.unknown_cause else UnknownCause.NOT_DECLARED.value
        output.missing_information.append(f"{path}:{suffix}")


def _condition(rule: Rule | None, path: str) -> Any:
    if rule is None:
        return None
    normalized = _normalized_rule_path(path)
    parts = normalized.split(".")
    without_entity_id = ".".join((parts[0], parts[-1])) if len(parts) >= 3 else normalized
    return next(
        (
            item
            for item in rule.conditions
            if _normalized_rule_path(item.path) in {normalized, without_entity_id}
            or normalized.endswith(_normalized_rule_path(item.path))
            or _normalized_rule_path(item.path).endswith(normalized)
        ),
        None,
    )


def _normalized_rule_path(path: str) -> str:
    parts = _path_without_cause(path).split(".")
    if parts:
        parts[0] = re.sub(r"(?<!^)(?=[A-Z])", "_", parts[0]).lower()
    return ".".join(parts).lower()


def _path_without_cause(path: str) -> str:
    return path.rpartition(":")[0] if ":" in path else path


def _path_is_mandatory(rule: Rule, path: str) -> bool:
    configured_condition = _condition(rule, _path_without_cause(path))
    return configured_condition.mandatory if configured_condition else True


def _information_actions(
    rule: Rule, missing: list[str], conflicts: list[ConflictRecord]
) -> list[str]:
    actions: set[str] = set()
    for item in missing:
        candidate = item.rpartition(":")[2] if ":" in item else item.rpartition(".")[2]
        cause = (
            candidate
            if candidate
            in {
                "stale_information",
                "collection_failed",
                "source_unavailable",
                "not_declared",
                "not_collected",
                "conflicting_sources",
            }
            else "not_collected"
        )
        actions.add(
            rule.information_actions.get(
                cause,
                {
                    "stale_information": "Aggiornare l'evidenza o il dato scaduto.",
                    "collection_failed": "Correggere il collector e ripetere l'acquisizione.",
                    "source_unavailable": "Ripristinare o sostituire la fonte informativa.",
                    "not_declared": "Acquisire e dichiarare il dato mancante.",
                }.get(cause, "Acquisire l'informazione mancante indicata nel risultato."),
            )
        )
    if conflicts:
        actions.add("Risolvare il conflitto tra fonti e documentare la fonte autoritativa.")
    return sorted(actions)


def _thresholds(rule: Rule) -> dict[str, Any]:
    threshold_ref = rule.parameters.get("threshold_ref")
    if threshold_ref:
        return {
            "reference": threshold_ref,
            "policy_version": rule.parameters.get("threshold_policy_version"),
            "origin": rule.parameters.get("threshold_origin", "project_baseline"),
            "value": {
                key: value
                for key, value in rule.parameters.items()
                if key in {"baseline_id", "allowed_tls_versions", "requires_tls"}
            },
        }
    return {}


def _apply_technical_threshold(rule: Rule, policy: dict[str, Any]) -> Rule:
    reference = rule.parameters.get("threshold_ref")
    if not reference:
        return rule
    configured = policy.get("technical_thresholds", {}).get(str(reference))
    if not isinstance(configured, dict):
        raise ValueError(f"soglia tecnica non definita: {reference}")
    parameters = {
        **rule.parameters,
        **{key: value for key, value in configured.items() if key != "rationale"},
        "threshold_policy_version": policy["policy_version"],
        "threshold_origin": configured.get("origin", "project_baseline"),
    }
    return rule.model_copy(update={"parameters": parameters}, deep=True)


def _asset_evidence(asset: GraphEntity) -> list[str]:
    return [str(item) for item in asset.get("evidence_ids", [])]


def _entity_evidence(items: list[GraphEntity]) -> list[str]:
    return sorted({str(value) for item in items for value in item.get("evidence_ids", [])})


def _synthetic_failure(path: str, comparison: str) -> EvaluatedFact:
    return EvaluatedFact(
        path=path,
        observed_value=[],
        value_status="known",
        comparison=comparison,
        comparison_result=False,
    )


def _knowledge(entity: GraphEntity, key: str) -> KnowledgeValue[Any]:
    raw_status = str(entity.get(f"{key}_status", "unknown"))
    try:
        status = KnowledgeValueStatus(raw_status)
    except ValueError:
        status = KnowledgeValueStatus.UNKNOWN
    value = entity.get(key) if status == KnowledgeValueStatus.KNOWN else None
    if status == KnowledgeValueStatus.KNOWN and value is None:
        status = KnowledgeValueStatus.UNKNOWN
    observation_type = entity.get(f"{key}_observation_type")
    observed_at = entity.get(f"{key}_observed_at")
    unknown_cause = entity.get(f"{key}_unknown_cause")
    return KnowledgeValue[Any](
        status=status,
        value=value,
        provenance_ids=[str(item) for item in entity.get(f"{key}_provenance_ids", [])],
        observation_type=observation_type,
        observed_at=_datetime(observed_at),
        unknown_cause=unknown_cause,
    )


def _rule_from_graph(entity: GraphEntity) -> Rule:
    values: dict[str, Any] = {}
    json_fields = {
        "applicability",
        "parameters",
        "messages",
        "conditions",
        "decision_policy",
        "information_actions",
    }
    for field_name in Rule.model_fields:
        if field_name in json_fields:
            values[field_name] = json.loads(str(entity.get(f"{field_name}_json", "{}" if field_name not in {"conditions"} else "[]")))
        elif field_name in entity:
            values[field_name] = entity[field_name]
    return Rule.model_validate(values)


def _datetime(value: Any) -> datetime | None:
    if value in (None, ""):
        return None
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def _json_mapping(value: Any) -> dict[str, Any]:
    if not value:
        return {}
    if isinstance(value, dict):
        return value
    try:
        parsed = json.loads(str(value))
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _canonical_content(item: GraphEntity) -> str:
    return json.dumps(_json_mapping(item.get("content_json")), ensure_ascii=False, sort_keys=True)


def _unique_conflicts(items: list[ConflictRecord]) -> list[ConflictRecord]:
    by_path: dict[str, ConflictRecord] = {}
    for item in items:
        by_path.setdefault(item.path, item)
    return [by_path[key] for key in sorted(by_path)]
