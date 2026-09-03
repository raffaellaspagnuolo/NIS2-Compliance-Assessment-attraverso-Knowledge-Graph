"""Vista Markdown completa del Knowledge Graph già costruito dalla pipeline."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from typing import Any


def render_knowledge_graph_markdown(report: Mapping[str, Any]) -> str:
    graph = report["knowledge_graph_view"]
    nodes = graph["nodes"]
    relationships = graph["relationships"]
    lines = [
        f"# Knowledge Graph completo — assessment `{_text(report['assessment_id'])}`",
        "",
        "> Questa vista rappresenta lo stesso grafo Neo4j usato dalla pipeline per "
        "valutare il sottoinsieme tecnico ACN selezionato. Non rappresenta il catalogo "
        "completo delle misure ACN e non aggiunge dati, ipotesi o nuovi calcoli.",
        "",
        "## Come leggere il grafo",
        "",
        "- I nodi azzurri descrivono il contesto e gli asset osservati.",
        "- I nodi verdi descrivono evidenze e provenienza delle informazioni.",
        "- I nodi arancioni descrivono requisiti, controlli e regole di confronto.",
        "- I nodi viola sono gli esiti prodotti e persistiti dopo la valutazione.",
        "",
        f"Il grafo contiene **{graph['node_count']} nodi** e "
        f"**{graph['relationship_count']} relazioni**.",
        "",
        "## Vista complessiva",
        "",
        "```mermaid",
        _knowledge_graph_mermaid(nodes, relationships),
        "```",
        "",
        "## Inventario completo dei nodi e delle proprietà",
        "",
        "Ogni riga seguente riporta una proprietà già presente in Neo4j. I valori "
        "sconosciuti restano esplicitamente indicati come tali.",
        "",
        "| Tipo | Nodo | Proprietà | Valore |",
        "|---|---|---|---|",
    ]
    for node in nodes:
        for key, value in sorted(node["properties"].items()):
            lines.append(
                f"| {_cell(node['entity_label'])} "
                f"| {_cell(node['display_name'])} (`{_cell(node['id'])}`) "
                f"| `{_cell(key)}` | {_cell(value)} |"
            )
    lines += [
        "",
        "## Inventario completo delle relazioni",
        "",
        "| Nodo di partenza | Relazione | Nodo di arrivo |",
        "|---|---|---|",
        *[
            f"| `{_cell(item['subject_id'])}` "
            f"| {_cell(item['predicate_label'])} (`{_cell(item['predicate'])}`) "
            f"| `{_cell(item['object_id'])}` |"
            for item in relationships
        ],
    ]
    return "\n".join(lines) + "\n"


def _knowledge_graph_mermaid(
    nodes: Sequence[Mapping[str, Any]], relationships: Sequence[Mapping[str, Any]]
) -> str:
    lines = [
        "flowchart TB",
        "    classDef context fill:#e3f2fd,stroke:#1565c0,color:#0d47a1",
        "    classDef evidence fill:#e0f2f1,stroke:#00796b,color:#004d40",
        "    classDef logic fill:#fff3e0,stroke:#ef6c00,color:#5d4037",
        "    classDef result fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c",
    ]
    node_ids: dict[str, str] = {}
    for index, node in enumerate(nodes, start=1):
        node_id = f"nodo{index}"
        node_ids[str(node["id"])] = node_id
        lines.append(f'    {node_id}["{_mermaid_node_label(node)}"]')
        lines.append(f"    class {node_id} {_mermaid_node_class(node)}")
    for relationship in relationships:
        subject = node_ids.get(str(relationship["subject_id"]))
        object_ = node_ids.get(str(relationship["object_id"]))
        if subject and object_:
            label = _mermaid_text(str(relationship["predicate_label"]))
            lines.append(f'    {subject} -->|"{label}"| {object_}')
    return "\n".join(lines)


def _mermaid_node_label(node: Mapping[str, Any]) -> str:
    properties = node["properties"]
    selected_keys = {
        "Asset": _asset_observed_property_keys(properties),
        "Evidence": ["evidence_type", "source", "collected_at", "reliability", "content_json"],
        "ProvenanceRecord": ["source", "method", "collected_at", "reliability"],
        "Requirement": ["source_reference"],
        "Control": ["technical_area", "verification_mode", "applicable_profiles"],
        "Rule": ["evaluator", "parameters_json", "verification_mode", "risk_clause"],
        "AssessmentResult": [
            "technical_status",
            "governance_status",
            "reason",
            "confidence_level",
            "evaluated_facts_json",
        ],
    }.get(str(node["entity_type"]), [])
    label_lines = [str(node["entity_label"]), str(node["display_name"])]
    for key in selected_keys:
        if key in properties:
            label_lines.append(f"{key}: {_short_value(properties[key])}")
    return "<br/>".join(_mermaid_text(value) for value in label_lines)


def _asset_observed_property_keys(properties: Mapping[str, Any]) -> list[str]:
    standard = {
        "id",
        "name",
        "asset_type",
        "description",
        "hostname",
        "ip_addresses",
        "mac_addresses",
        "environment",
        "network_segment",
        "network_segment_status",
        "network_segment_provenance_ids",
        "internet_exposed",
        "internet_exposed_status",
        "internet_exposed_provenance_ids",
        "criticality",
        "lifecycle_status",
        "owner_id",
        "process_ids",
        "data_object_ids",
        "service_ids",
        "evidence_ids",
        "provenance_ids",
    }
    return [
        key
        for key in sorted(properties)
        if key not in standard and not key.endswith("_provenance_ids")
    ]


def _mermaid_node_class(node: Mapping[str, Any]) -> str:
    return {
        "Evidence": "evidence",
        "ProvenanceRecord": "evidence",
        "Requirement": "logic",
        "Control": "logic",
        "Rule": "logic",
        "AssessmentResult": "result",
    }.get(str(node["entity_type"]), "context")


def _short_value(value: Any, limit: int = 100) -> str:
    rendered = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str) if isinstance(value, (dict, list)) else str(value)
    return rendered if len(rendered) <= limit else rendered[: limit - 1] + "…"


def _mermaid_text(value: str) -> str:
    return value.replace('"', "'").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;")


def _cell(value: Any) -> str:
    return _text(value).replace("|", "\\|").replace("\n", " ")


def _text(value: Any) -> str:
    if value is None or value == "":
        return "non disponibile"
    if isinstance(value, Mapping):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return ", ".join(_text(item) for item in value) or "nessuna"
    return str(value)
