"""Prepara il contenuto descrittivo del report senza rivalutare gli esiti.

Il modulo costruisce una vista di lettura usando esclusivamente entità recuperate
dal Knowledge Graph, risultati del motore e indicatori già prodotti
dall'aggregazione. Le classificazioni qui presenti sono proiezioni dirette dello
stato esistente e non modificano status, confidence, punteggi o raccomandazioni.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from nis2_assessor.domain.enums import ApplicabilityStatus
from nis2_assessor.domain.models import ApplicabilityResult, AssessmentResult
from nis2_assessor.domain.report_types import EvidenceRejection

STATUS_PRESENTATION = {
    "compliant": {
        "label": "Condizione tecnica soddisfatta",
        "meaning": "Le condizioni tecniche previste dalla regola risultano soddisfatte.",
    },
    "partially_compliant": {
        "label": "Condizione tecnica parzialmente soddisfatta",
        "meaning": "Solo una parte delle condizioni tecniche risulta soddisfatta.",
    },
    "non_compliant": {
        "label": "Scostamento tecnico rilevato",
        "meaning": "È stato osservato almeno un dato tecnico contrario alla regola.",
    },
    "not_verifiable": {
        "label": "Non verificabile con i dati disponibili",
        "meaning": "I dati o le evidenze disponibili non consentono una verifica conclusiva.",
    },
    "not_applicable": {
        "label": "Non applicabile",
        "meaning": "Il controllo è stato escluso dalle condizioni di applicabilità.",
    },
    "not_assessed": {
        "label": "Non valutato",
        "meaning": "Il controllo non è stato valutato.",
    },
    "manual_review_required": {
        "label": "Revisione manuale necessaria",
        "meaning": "L'esito richiede una verifica da parte di una persona competente.",
    },
    "insufficient_evidence": {
        "label": "Evidenze insufficienti",
        "meaning": "Le evidenze disponibili non sono sufficienti per concludere.",
    },
    "error": {
        "label": "Errore di valutazione",
        "meaning": "La valutazione non è stata completata a causa di un errore.",
    },
}

FINDING_CATEGORIES = {
    "non_compliant": "technical_deviation",
    "partially_compliant": "partial_result",
    "not_verifiable": "information_gap",
    "insufficient_evidence": "information_gap",
    "manual_review_required": "manual_review",
    "not_assessed": "not_assessed",
    "error": "evaluation_error",
}

ENTITY_TYPE_LABELS = {
    "DatasetInfo": "Dataset",
    "Organization": "Organizzazione",
    "ResponsibleParty": "Responsabili",
    "Process": "Processi",
    "DataObject": "Categorie di dati",
    "Asset": "Asset",
    "Service": "Servizi",
    "SoftwareComponent": "Componenti software",
    "Account": "Utenze",
    "NetworkInterface": "Interfacce di rete",
    "NetworkFlow": "Flussi di rete",
    "BackupRecord": "Backup",
    "SecurityCapability": "Capacità di sicurezza",
    "TechnicalException": "Deroghe tecniche",
    "Vulnerability": "Vulnerabilità",
    "Evidence": "Evidenze",
    "ProvenanceRecord": "Fonti e provenienza",
    "InventoryState": "Stato degli inventari",
    "Requirement": "Requisiti",
    "Control": "Controlli tecnici",
    "Rule": "Regole di valutazione",
    "AssessmentResult": "Esiti della valutazione",
}

RELATIONSHIP_LABELS = {
    "DESCRIBES": "descrive",
    "EXPOSES": "espone",
    "PRESENTS": "presenta",
    "AFFECTS": "interessa",
    "PROCESSES": "tratta",
    "MANAGED_BY": "è gestito da",
    "PROTECTED_BY": "è protetto da",
    "SUPPORTS": "supporta",
    "DEPENDS_ON": "dipende da",
    "REFERS_TO": "si riferisce a",
    "ASSOCIATED_WITH": "è associato a",
    "APPLIES_TO": "si applica a",
    "IMPLEMENTS": "implementa",
    "DERIVES_FROM": "deriva da",
    "EVALUATES": "valuta",
    "RESULT_OF": "è esito del controllo",
    "TRACES_TO": "è riconducibile al requisito",
    "APPLIES_RULE": "applica la regola",
}


def build_report_context(
    *,
    assessment_id: str,
    generated_at: str,
    requirements_source: str,
    evidence_input_source: str,
    graph_id: str,
    dataset: Mapping[str, Any],
    organization: Mapping[str, Any],
    assets: Sequence[Mapping[str, Any]],
    controls: Sequence[Mapping[str, Any]],
    requirements: Sequence[Mapping[str, Any]],
    rules: Sequence[Mapping[str, Any]],
    evidences: Sequence[Mapping[str, Any]],
    provenance_records: Sequence[Mapping[str, Any]],
    graph_entities: Mapping[str, Sequence[Mapping[str, Any]]],
    graph_relationships: Sequence[Mapping[str, Any]],
    results: Sequence[AssessmentResult],
    decisions: Mapping[str, ApplicabilityResult],
    summary: Mapping[str, Any],
    rejected_evidences: Sequence[EvidenceRejection],
    assessment_engine_version: str,
    rule_catalog_version: str,
    framework_version: str,
    evidence_policy_version: str,
    operational_policy_version: str,
    coverage_catalog: Mapping[str, Any],
) -> dict[str, Any]:
    """Costruisce il report strutturato preservando tutti i valori calcolati."""
    asset_map = _by_id(assets)
    control_map = _by_id(controls)
    requirement_map = _by_id(requirements)
    rule_map = _by_id(rules)
    evidence_map = _by_id(evidences)
    provenance_map = _by_id(provenance_records)
    technical_exception_map = _by_id(graph_entities.get("TechnicalException", []))
    vulnerabilities_by_asset: dict[str, list[Mapping[str, Any]]] = {}
    for vulnerability in graph_entities.get("Vulnerability", []):
        vulnerabilities_by_asset.setdefault(str(vulnerability.get("asset_id")), []).append(
            vulnerability
        )

    priorities = [dict(item) for item in summary["priorities"]]
    priority_by_result = {
        str(item["result_id"]): {**item, "rank": rank}
        for rank, item in enumerate(priorities, start=1)
    }
    detailed_results = [
        _result_view(
            result,
            asset_map,
            control_map,
            requirement_map,
            rule_map,
            evidence_map,
            provenance_map,
            priority_by_result,
            coverage_catalog["by_rule"],
            technical_exception_map,
            vulnerabilities_by_asset,
        )
        for result in results
    ]
    for item in detailed_results:
        decision = decisions.get(f"{item['asset_id']}:{item['control_id']}")
        item["applicability_details"] = (
            decision.model_dump(mode="json") if decision is not None else None
        )

    findings = [
        _finding_view(item)
        for item in detailed_results
        if item["status"] in FINDING_CATEGORIES
    ]
    technical_deviations = [item for item in detailed_results if item["status"] == "non_compliant"]
    partial_results = [item for item in detailed_results if item["status"] == "partially_compliant"]
    information_gaps = [
        item
        for item in detailed_results
        if item["status"] in {"not_verifiable", "insufficient_evidence"}
    ]
    manual_reviews = [
        item
        for item in detailed_results
        if item["governance_status"] == "manual_review_required"
    ]
    manual_requirements = [
        item for item in requirements if item.get("verification_mode") == "manual_only"
    ]
    action_plan = _action_plan(priorities, detailed_results)
    excluded_controls = _excluded_controls(decisions, asset_map, control_map)
    knowledge_graph_view = _knowledge_graph_view(graph_entities, graph_relationships)
    related_by_asset = _asset_related_entities(assets, graph_entities, graph_relationships)

    critical_asset_ids = {
        str(asset["id"]) for asset in assets if asset.get("criticality") == "critical"
    }
    by_asset = summary["results_by_asset"]
    all_asset_overviews = [
        {
            "asset": _asset_context(asset),
            "status_counts": dict(by_asset.get(str(asset["id"]), {})),
            "applicable_results": [
                item
                for item in detailed_results
                if item["asset_id"] == str(asset["id"])
                and item["status"] != "not_applicable"
            ],
            "priority_actions": [
                item for item in action_plan if item["asset_id"] == str(asset["id"])
            ],
            "excluded_controls": [
                item for item in excluded_controls if item["asset_id"] == str(asset["id"])
            ],
            "related_entities": related_by_asset.get(str(asset["id"]), []),
        }
        for asset in sorted(assets, key=lambda item: str(item["id"]))
    ]
    asset_overviews = all_asset_overviews

    return {
        "report_schema_version": "6.0",
        "assessment_id": assessment_id,
        "dataset_id": str(dataset["id"]),
        "organization_id": str(organization["id"]),
        "dataset": _select(dataset, "id", "name", "description", "generated_at", "source_systems"),
        "organization": _select(
            organization,
            "id",
            "name",
            "nis_profile",
            "risk_assessment_reference",
            "acn_specification",
        ),
        "requirements_source": requirements_source,
        "evidence_input_source": evidence_input_source,
        "knowledge_graph_used_for_decisions": True,
        "knowledge_graph_id": graph_id,
        "knowledge_graph_view": knowledge_graph_view,
        "generated_at": generated_at,
        "assessment_date": generated_at,
        "framework_metadata": {
            "acn_profile": organization.get("nis_profile"),
            "framework_version": framework_version,
            "rule_catalog_version": rule_catalog_version,
            "assessment_engine_version": assessment_engine_version,
            "evidence_priority_policy_version": evidence_policy_version,
            "operational_policy_version": operational_policy_version,
            "coverage_catalog_version": coverage_catalog.get("catalog_version"),
        },
        "coverage_catalog": {
            "catalog_version": coverage_catalog.get("catalog_version"),
            "records": list(coverage_catalog["records"]),
        },
        "rejected_evidences": list(rejected_evidences),
        "scope": {
            "description": (
                "Valutazione del sottoinsieme tecnico ACN selezionato, con condizioni "
                "osservabili a livello di asset."
            ),
            "limitations": [
                "Non costituisce certificazione o attestazione di conformità NIS2.",
                "Non rappresenta il catalogo completo delle misure ACN.",
                "I conteggi descrivono esclusivamente i controlli tecnici inclusi nel perimetro.",
                "La qualità della lettura dipende da completezza e affidabilità dei dati già estratti.",
            ],
        },
        "reading_guide": {
            "purpose": (
                "Rendere leggibili gli esiti tecnici già prodotti dal motore, senza modificarli "
                "o completarli con supposizioni."
            ),
            "score_note": (
                "Non viene calcolata alcuna percentuale di conformità. La copertura informa "
                "sulle determinazioni sostenute da fatti o evidenze ed è sempre accompagnata "
                "dalla propria frazione; la priorità operativa è non normativa."
            ),
            "confidence_note": (
                "La confidence esprime quanto il motore considera solida la base informativa "
                "dell'esito; non è una probabilità di conformità NIS2."
            ),
        },
        "status_legend": STATUS_PRESENTATION,
        "catalog_overview": {
            "nis_profile": organization.get("nis_profile"),
            "technical_requirements": len(requirements) - len(manual_requirements),
            "manual_only_requirements": len(manual_requirements),
            "source_documents": sorted(
                {str(item.get("source_document")) for item in requirements if item.get("source_document")}
            ),
        },
        "manual_requirements": [
            _select(
                item,
                "id",
                "title",
                "description",
                "source_reference",
                "source_document",
                "acn_measure",
                "acn_point",
                "manual_only_reason",
            )
            for item in manual_requirements
        ],
        "summary": {
            key: value
            for key, value in summary.items()
            if key not in {"results_by_asset", "results_by_area", "priorities"}
        },
        "results_by_area": summary["results_by_area"],
        "results_by_asset": by_asset,
        "assessment_results": detailed_results,
        "findings": findings,
        "technical_deviations": technical_deviations,
        "partial_results": partial_results,
        "information_gaps": information_gaps,
        "manual_reviews": manual_reviews,
        "critical_asset_findings": [
            item for item in findings if item["asset_id"] in critical_asset_ids
        ],
        "missing_information": sorted(
            {value for result in results for value in result.missing_information}
        ),
        "priorities": priorities,
        "action_plan": action_plan,
        "recommendations": sorted(
            {result.recommendation for result in results if result.recommendation}
        ),
        "traceability": {item["id"]: item["traceability"] for item in detailed_results},
        "applicability": {key: value.model_dump(mode="json") for key, value in decisions.items()},
        "excluded_controls": excluded_controls,
        "asset_overviews": asset_overviews,
        "evidence_catalog": [
            _select(
                item,
                "id",
                "title",
                "description",
                "evidence_type",
                "source",
                "source_category",
                "collected_at",
                "valid_until",
                "reliability",
                "file_reference",
                "provenance_ids",
            )
            for item in evidences
        ],
        "provenance_catalog": [
            _select(
                item,
                "id",
                "source",
                "source_type",
                "source_category",
                "collected_at",
                "method",
                "reliability",
                "original_reference",
                "notes",
            )
            for item in provenance_records
        ],
    }


def _result_view(
    result: AssessmentResult,
    assets: Mapping[str, Mapping[str, Any]],
    controls: Mapping[str, Mapping[str, Any]],
    requirements: Mapping[str, Mapping[str, Any]],
    rules: Mapping[str, Mapping[str, Any]],
    evidences: Mapping[str, Mapping[str, Any]],
    provenance_records: Mapping[str, Mapping[str, Any]],
    priorities: Mapping[str, Mapping[str, Any]],
    coverage_records: Mapping[str, Mapping[str, Any]],
    technical_exceptions: Mapping[str, Mapping[str, Any]],
    vulnerabilities_by_asset: Mapping[str, Sequence[Mapping[str, Any]]],
) -> dict[str, Any]:
    record = result.model_dump(mode="json")
    status = result.technical_status.value
    # Alias di sola compatibilità per i consumer del report v2/v5.
    record["status"] = status
    record["status_presentation"] = STATUS_PRESENTATION.get(
        status, {"label": status, "meaning": "Esito tecnico prodotto dal motore."}
    )
    record["category"] = FINDING_CATEGORIES.get(status, "satisfied_condition")
    asset = assets.get(result.asset_id, {"id": result.asset_id})
    control = controls.get(result.control_id, {"id": result.control_id})
    requirement = requirements.get(result.requirement_id, {"id": result.requirement_id})
    rule = rules.get(result.rule_id, {"id": result.rule_id})
    record["context"] = {
        "asset": _asset_context(asset),
        "control": _select(
            control,
            "id",
            "title",
            "description",
            "technical_area",
            "applicable_profiles",
            "verification_mode",
            "relevant_system_required",
        ),
        "requirement": _select(
            requirement,
            "id",
            "framework",
            "title",
            "description",
            "source_reference",
            "source_document",
            "source_version",
            "source_url",
            "acn_measure",
            "acn_point",
            "article_24_element",
            "applicable_profiles",
            "verification_mode",
            "risk_clause",
            "scope_note",
        ),
        "rule": {
            **_select(
                rule,
                "id",
                "version",
                "title",
                "description",
                "verification_mode",
                "decision_policy",
                "allowed_outcomes",
                "empty_collection_policy",
            ),
            "coverage": dict(coverage_records.get(result.rule_id, {})),
        },
    }
    record["evidence_details"] = [
        _select(
            evidences.get(evidence_id, {"id": evidence_id}),
            "id",
            "title",
            "description",
            "evidence_type",
            "source",
            "source_category",
            "collected_at",
            "valid_until",
            "reliability",
            "file_reference",
            "provenance_ids",
        )
        for evidence_id in result.evidence_ids
    ]
    provenance_ids = {
        str(provenance_id)
        for fact in result.evaluated_facts
        for provenance_id in fact.provenance_ids
    }
    for evidence_id in result.evidence_ids:
        provenance_ids.update(
            str(value) for value in evidences.get(evidence_id, {}).get("provenance_ids", [])
        )
    record["provenance_details"] = [
        _select(
            provenance_records.get(provenance_id, {"id": provenance_id}),
            "id",
            "source",
            "source_type",
            "source_category",
            "collected_at",
            "method",
            "reliability",
            "original_reference",
            "notes",
        )
        for provenance_id in sorted(provenance_ids)
    ]
    record["priority"] = dict(priorities[result.id]) if result.id in priorities else None
    exception = technical_exceptions.get(result.technical_exception_id or "")
    record["technical_exception_details"] = (
        _select(
            exception,
            "id",
            "rationale",
            "compensating_measure",
            "residual_risk",
            "approval_reference",
            "valid_until",
            "evidence_ids",
            "provenance_ids",
        )
        if exception
        else None
    )
    evaluated_entity_ids = {
        str(value) for value in result.decision_trace.get("evaluated_entity_ids", [])
    }
    accepted_risks = [
        _select(
            item,
            "id",
            "title",
            "component",
            "cve",
            "severity",
            "remediation_status",
            "remediation_due_date",
            "accepted_exception",
            "evidence_ids",
            "provenance_ids",
        )
        for item in vulnerabilities_by_asset.get(result.asset_id, [])
        if item.get("accepted_exception") is True
        and (not evaluated_entity_ids or str(item.get("id")) in evaluated_entity_ids)
    ]
    record["accepted_risk_details"] = accepted_risks
    record["traceability"] = {
        "requirement_id": result.requirement_id,
        "requirement_title": requirement.get("title"),
        "source_reference": requirement.get("source_reference"),
        "source_document": requirement.get("source_document"),
        "source_version": requirement.get("source_version"),
        "acn_measure": requirement.get("acn_measure"),
        "acn_point": requirement.get("acn_point"),
        "applicable_profiles": requirement.get("applicable_profiles"),
        "risk_clause": result.risk_clause,
        "technical_exception_id": result.technical_exception_id,
        "control_id": result.control_id,
        "control_title": control.get("title"),
        "asset_id": result.asset_id,
        "asset_name": asset.get("name"),
        "rule_id": result.rule_id,
        "rule_title": rule.get("title"),
        "rule_version": result.rule_version,
        "coverage": dict(coverage_records.get(result.rule_id, {})),
        "technical_status": result.technical_status.value,
        "governance_status": result.governance_status.value,
        "confidence_level": result.confidence_level.value,
        "evidence_ids": list(result.evidence_ids),
    }
    return record


def _finding_view(result: Mapping[str, Any]) -> dict[str, Any]:
    context = result["context"]
    return {
        "id": f"finding-{result['id']}",
        "assessment_result_id": result["id"],
        "category": result["category"],
        "status": result["status"],
        "status_label": result["status_presentation"]["label"],
        "asset_id": result["asset_id"],
        "asset_name": context["asset"].get("name"),
        "control_id": result["control_id"],
        "control_title": context["control"].get("title"),
        "title": f"{result['status_presentation']['label']}: {context['control'].get('title', result['control_id'])}",
        "description": result["reason"],
        "asset_criticality": context["asset"].get("criticality"),
        "confidence_level": result["confidence_level"],
        "evidence_ids": result["evidence_ids"],
        "missing_information": result["missing_information"],
        "recommendation": result["recommendation"],
        "priority": result["priority"],
    }


def _action_plan(
    priorities: Sequence[Mapping[str, Any]], results: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    result_map = {str(item["id"]): item for item in results}
    actions: list[dict[str, Any]] = []
    for rank, priority in enumerate(priorities, start=1):
        result = result_map[str(priority["result_id"])]
        context = result["context"]
        actions.append(
            {
                **priority,
                "rank": rank,
                "status": result["status"],
                "status_label": result["status_presentation"]["label"],
                "asset_criticality": context["asset"].get("criticality"),
                "confidence_level": result["confidence_level"],
                "asset_name": context["asset"].get("name"),
                "control_title": context["control"].get("title"),
                "reason": result["reason"],
                "recommendation": result["recommendation"],
            }
        )
    return actions


def _excluded_controls(
    decisions: Mapping[str, ApplicabilityResult],
    assets: Mapping[str, Mapping[str, Any]],
    controls: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    excluded: list[dict[str, Any]] = []
    for key, decision in sorted(decisions.items()):
        if decision.status != ApplicabilityStatus.NOT_APPLICABLE:
            continue
        asset_id, separator, control_id = key.partition(":")
        if not separator:
            asset_id, control_id = key, ""
        excluded.append(
            {
                "asset_id": asset_id,
                "asset_name": assets.get(asset_id, {}).get("name"),
                "control_id": control_id,
                "control_title": controls.get(control_id, {}).get("title"),
                "reason_code": decision.reason_code.value,
                "reasons": list(decision.reasons),
                "evaluated_conditions": list(decision.evaluated_conditions),
            }
        )
    return excluded


def _asset_context(asset: Mapping[str, Any]) -> dict[str, Any]:
    return _select(
        asset,
        "id",
        "name",
        "description",
        "asset_type",
        "hostname",
        "ip_addresses",
        "environment",
        "network_segment",
        "network_segment_status",
        "internet_exposed",
        "internet_exposed_status",
        "nis_relevant",
        "nis_relevant_status",
        "criticality",
        "impact_level",
        "exposure_level",
        "risk_assessment_reference",
        "lifecycle_status",
        "operating_system",
        "operating_system_version",
        "support_status",
        "owner_id",
    )


def _asset_related_entities(
    assets: Sequence[Mapping[str, Any]],
    entities: Mapping[str, Sequence[Mapping[str, Any]]],
    relationships: Sequence[Mapping[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    """Prepara il contesto direttamente associato a ogni asset senza interpretarlo."""
    context_types = {
        "ResponsibleParty",
        "Process",
        "DataObject",
        "Service",
        "SoftwareComponent",
        "Account",
        "NetworkInterface",
        "NetworkFlow",
        "BackupRecord",
        "SecurityCapability",
        "TechnicalException",
        "Vulnerability",
    }
    entity_index = {
        str(item["id"]): (entity_type, item)
        for entity_type, items in entities.items()
        if entity_type in context_types
        for item in items
    }
    relation_index: dict[str, list[tuple[str, str, str]]] = {}
    for relationship in relationships:
        subject_id = str(relationship.get("subject") or relationship.get("subject_id") or "")
        object_id = str(relationship.get("object") or relationship.get("object_id") or "")
        predicate = str(relationship.get("predicate") or "")
        relation_index.setdefault(subject_id, []).append((object_id, predicate, "outgoing"))
        relation_index.setdefault(object_id, []).append((subject_id, predicate, "incoming"))

    related: dict[str, list[dict[str, Any]]] = {}
    for asset in assets:
        asset_id = str(asset["id"])
        candidates: dict[str, tuple[str, Mapping[str, Any], str, str]] = {}
        for entity_id, predicate, direction in relation_index.get(asset_id, []):
            if entity_id in entity_index:
                entity_type, item = entity_index[entity_id]
                candidates[entity_id] = (entity_type, item, predicate, direction)
        for entity_id, (entity_type, item) in entity_index.items():
            item_asset_id = str(item.get("asset_id") or "")
            item_asset_ids = {str(value) for value in item.get("asset_ids", [])}
            is_owner = entity_id == str(asset.get("owner_id") or "")
            if item_asset_id == asset_id or asset_id in item_asset_ids or is_owner:
                candidates.setdefault(
                    entity_id, (entity_type, item, "ASSOCIATED_WITH", "derived")
                )
        related[asset_id] = [
            {
                "entity_type": entity_type,
                "entity_label": ENTITY_TYPE_LABELS.get(entity_type, entity_type),
                "id": entity_id,
                "display_name": _entity_display_name(item),
                "relationship": predicate,
                "relationship_label": RELATIONSHIP_LABELS.get(predicate, predicate.lower()),
                "direction": direction,
                "properties": {
                    key: value
                    for key, value in item.items()
                    if key not in {"labels", "graph_id"}
                },
            }
            for entity_id, (entity_type, item, predicate, direction) in sorted(
                candidates.items(), key=lambda value: (value[1][0], value[0])
            )
        ]
    return related


def _by_id(items: Sequence[Mapping[str, Any]]) -> dict[str, Mapping[str, Any]]:
    return {str(item["id"]): item for item in items}


def _select(item: Mapping[str, Any], *keys: str) -> dict[str, Any]:
    return {key: item[key] for key in keys if key in item and item[key] is not None}


def _knowledge_graph_view(
    entities: Mapping[str, Sequence[Mapping[str, Any]]],
    relationships: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Riassume nodi e archi esistenti e genera una vista Mermaid del loro schema."""
    entity_types = [
        {
            "entity_type": entity_type,
            "label": ENTITY_TYPE_LABELS.get(entity_type, entity_type),
            "count": len(items),
        }
        for entity_type, items in entities.items()
        if items
    ]
    id_to_type = {
        str(item["id"]): entity_type for entity_type, items in entities.items() for item in items
    }
    relationship_counts: dict[str, int] = {}
    schema_counts: dict[tuple[str, str, str], int] = {}
    for relationship in relationships:
        subject_id = str(relationship.get("subject") or relationship.get("subject_id") or "")
        object_id = str(relationship.get("object") or relationship.get("object_id") or "")
        predicate = str(relationship.get("predicate") or "")
        if not predicate:
            continue
        relationship_counts[predicate] = relationship_counts.get(predicate, 0) + 1
        subject_type = id_to_type.get(subject_id)
        object_type = id_to_type.get(object_id)
        if subject_type and object_type:
            key = (subject_type, predicate, object_type)
            schema_counts[key] = schema_counts.get(key, 0) + 1

    schema_relations = [
        {
            "subject_type": subject_type,
            "subject_label": ENTITY_TYPE_LABELS.get(subject_type, subject_type),
            "predicate": predicate,
            "predicate_label": RELATIONSHIP_LABELS.get(predicate, predicate.lower()),
            "object_type": object_type,
            "object_label": ENTITY_TYPE_LABELS.get(object_type, object_type),
            "count": count,
        }
        for (subject_type, predicate, object_type), count in sorted(schema_counts.items())
    ]
    nodes = [
        {
            "id": str(item["id"]),
            "entity_type": entity_type,
            "entity_label": ENTITY_TYPE_LABELS.get(entity_type, entity_type),
            "display_name": _entity_display_name(item),
            "properties": {
                key: value for key, value in item.items() if key not in {"labels", "graph_id"}
            },
        }
        for entity_type, items in entities.items()
        for item in items
    ]
    normalized_relationships = [
        {
            "id": relationship.get("id"),
            "subject_id": str(relationship.get("subject") or relationship.get("subject_id") or ""),
            "predicate": str(relationship.get("predicate") or ""),
            "predicate_label": RELATIONSHIP_LABELS.get(
                str(relationship.get("predicate") or ""),
                str(relationship.get("predicate") or "").lower(),
            ),
            "object_id": str(relationship.get("object") or relationship.get("object_id") or ""),
        }
        for relationship in relationships
    ]
    return {
        "node_count": sum(len(items) for items in entities.values()),
        "relationship_count": len(relationships),
        "nodes": nodes,
        "relationships": normalized_relationships,
        "entity_types": entity_types,
        "relationship_types": [
            {
                "predicate": predicate,
                "label": RELATIONSHIP_LABELS.get(predicate, predicate.lower()),
                "count": count,
            }
            for predicate, count in sorted(relationship_counts.items())
        ],
        "schema_relations": schema_relations,
        "reading_note": (
            "Ogni riquadro rappresenta un tipo di informazione presente nel grafo. "
            "Le frecce mostrano come le informazioni sono collegate; il numero tra "
            "parentesi indica quanti nodi o collegamenti di quel tipo sono presenti."
        ),
    }


def _entity_display_name(item: Mapping[str, Any]) -> str:
    for key in ("name", "title", "description"):
        if item.get(key):
            return str(item[key])
    return str(item["id"])
