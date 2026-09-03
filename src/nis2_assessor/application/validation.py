"""Carica il dataset normalizzato e ne controlla coerenza e riferimenti.

La validazione avviene in due livelli: Pydantic verifica struttura e tipi;
validate_references controlla duplicati e collegamenti fra entità diverse.
"""

from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError
from yaml.constructor import ConstructorError

from nis2_assessor.domain.models import NormalizedEnvironment

ALLOWED_PREDICATES = {
    "EXPOSES",
    "PRESENTS",
    "AFFECTS",
    "PROCESSES",
    "MANAGED_BY",
    "SUPPORTS",
    "USES",
    "DEPENDS_ON",
    "PROTECTED_BY",
    "REFERS_TO",
    "ASSOCIATED_WITH",
    "APPLIES_TO",
}


class DatasetValidationError(ValueError):
    """Errore applicativo che conserva una lista di problemi leggibili."""

    def __init__(self, errors: list[dict[str, Any]]) -> None:
        super().__init__("dataset normalizzato non valido")
        self.errors = errors


class UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader che rifiuta chiavi duplicate invece di sovrascriverle."""


def _construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"chiave YAML duplicata: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Carica un documento YAML sicuro, a chiavi univoche e con radice mapping."""
    raw = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    if not isinstance(raw, dict):
        raise ValueError("il documento YAML deve contenere un oggetto alla radice")
    return raw


def load_environment(path: Path) -> NormalizedEnvironment:
    """Legge un ambiente già normalizzato senza completarne semanticamente i dati."""
    try:
        raw = load_yaml_mapping(path)
        if raw.get("schema_version") != "2.0":
            raise ValueError("il catalogo principale richiede schema_version 2.0")
        env = NormalizedEnvironment.model_validate(raw)
    except (OSError, yaml.YAMLError, ValidationError, ValueError) as exc:
        if isinstance(exc, ValidationError):
            details = []
            for item in exc.errors():
                detail = dict(item)
                location = detail.get("loc", ())
                detail["path"] = _format_validation_path(location)
                detail["message"] = str(detail.get("msg", "errore di validazione"))
                details.append(detail)
        else:
            details = [{"message": str(exc)}]
        raise DatasetValidationError(details) from exc
    errors = validate_references(env)
    if errors:
        raise DatasetValidationError(errors)
    return env


def _format_validation_path(location: Any) -> str:
    """Converte una locazione Pydantic nel path leggibile usato dagli errori."""
    if not isinstance(location, (list, tuple)):
        return str(location)
    result = ""
    for part in location:
        if isinstance(part, int):
            result += f"[{part}]"
        else:
            result += ("." if result else "") + str(part)
    return result


def migrate_legacy_environment_v2(raw: dict[str, Any]) -> dict[str, Any]:
    """Migra esplicitamente un input 2.0 legacy verso il contratto strict.

    La funzione conserva le precedenti scelte di compatibilità, ma opera su una
    copia e non viene mai richiamata automaticamente da ``load_environment``.
    """
    migrated = deepcopy(raw)
    candidate = migrated.get("dataset")
    dataset: dict[str, Any] = candidate if isinstance(candidate, dict) else {}
    generated_at = dataset.get("generated_at")

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if {"status", "value", "provenance_ids"} <= value.keys():
                status = value.get("status")
                if status == "known":
                    value.setdefault("observation_type", "declared")
                    if generated_at:
                        value.setdefault("observed_at", generated_at)
                elif status == "conflicting":
                    value.setdefault("unknown_cause", "conflicting_sources")
                elif status == "unknown":
                    value.setdefault("unknown_cause", "not_declared")
            for nested in value.values():
                visit(nested)
        elif isinstance(value, list):
            for nested in value:
                visit(nested)

    visit(migrated)
    migrated.setdefault("network_interfaces", [])
    migrated.setdefault("inventory_states", [])
    return migrated


def validate_references(env: NormalizedEnvironment) -> list[dict[str, Any]]:
    """Restituisce tutti gli ID duplicati o riferimenti non risolvibili."""
    # Le collezioni contengono modelli differenti ma condividono id e model_dump.
    # Any descrive qui soltanto questo confine eterogeneo già validato da Pydantic.
    node_groups: list[list[Any]] = [
        [env.dataset],
        [env.organization],
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
    ]
    all_groups = [*node_groups, env.relationships]
    ids = [item.id for group in all_groups for item in group]
    errors: list[dict[str, Any]] = []
    for item_id, count in Counter(ids).items():
        if count > 1:
            errors.append(
                {
                    "path": "id",
                    "value": item_id,
                    "type": "duplicate_id",
                    "message": "identificativo duplicato",
                    "suggestion": "usare un ID univoco",
                }
            )
    node_ids = {item.id for group in node_groups for item in group}
    asset_ids = {item.id for item in env.assets}
    responsible_ids = {item.id for item in env.responsible_parties}
    process_ids = {item.id for item in env.processes}
    data_object_ids = {item.id for item in env.data_objects}
    service_ids = {item.id for item in env.services}
    vulnerability_ids = {item.id for item in env.vulnerabilities}
    evidence_ids = {item.id for item in env.evidences}
    control_ids = {item.id for item in env.controls}
    provenance_ids = {p.id for p in env.provenance_records}

    def require(path: str, value: str | None, expected: set[str]) -> None:
        """Aggiunge un errore contestualizzato quando un riferimento non esiste."""
        if value and value not in expected:
            errors.append(
                {
                    "path": path,
                    "value": value,
                    "type": "invalid_reference",
                    "message": "riferimento inesistente",
                    "suggestion": "definire o correggere l'ID",
                }
            )

    for asset in env.assets:
        require(f"assets.{asset.id}.owner_id", asset.owner_id, responsible_ids)
        for key, refs, expected in (
            ("process_ids", asset.process_ids, process_ids),
            ("data_object_ids", asset.data_object_ids, data_object_ids),
            ("service_ids", asset.service_ids, service_ids),
            ("evidence_ids", asset.evidence_ids, evidence_ids),
        ):
            for ref in refs:
                require(f"assets.{asset.id}.{key}", ref, expected)
    for process in env.processes:
        require(f"processes.{process.id}.owner_id", process.owner_id, responsible_ids)
        for ref in process.asset_ids:
            require(f"processes.{process.id}.asset_ids", ref, asset_ids)
        for ref in process.data_object_ids:
            require(f"processes.{process.id}.data_object_ids", ref, data_object_ids)
    for data_object in env.data_objects:
        for ref in data_object.asset_ids:
            require(f"data_objects.{data_object.id}.asset_ids", ref, asset_ids)
    for service in env.services:
        require(f"services.{service.id}.asset_id", service.asset_id, asset_ids)
        for ref in service.evidence_ids:
            require(f"services.{service.id}.evidence_ids", ref, evidence_ids)
    for group_name, group in (
        ("software_components", env.software_components),
        ("accounts", env.accounts),
        ("network_interfaces", env.network_interfaces),
        ("network_flows", env.network_flows),
        ("backups", env.backups),
        ("security_capabilities", env.security_capabilities),
    ):
        for item in group:
            require(f"{group_name}.{item.id}.asset_id", item.asset_id, asset_ids)
            for ref in item.evidence_ids:
                require(f"{group_name}.{item.id}.evidence_ids", ref, evidence_ids)
    valid_inventory_scopes = {env.dataset.id, *asset_ids}
    for state in env.inventory_states:
        require(f"inventory_states.{state.id}.scope_id", state.scope_id, valid_inventory_scopes)
    for exception in env.technical_exceptions:
        require(
            f"technical_exceptions.{exception.id}.asset_id", exception.asset_id, asset_ids
        )
        require(
            f"technical_exceptions.{exception.id}.control_id",
            exception.control_id,
            control_ids,
        )
        for ref in exception.evidence_ids:
            require(f"technical_exceptions.{exception.id}.evidence_ids", ref, evidence_ids)
    for vuln in env.vulnerabilities:
        require(f"vulnerabilities.{vuln.id}.asset_id", vuln.asset_id, asset_ids)
        require(f"vulnerabilities.{vuln.id}.service_id", vuln.service_id, service_ids)
        for ref in vuln.evidence_ids:
            require(f"vulnerabilities.{vuln.id}.evidence_ids", ref, evidence_ids)
    for evidence in env.evidences:
        for key, refs, expected in (
            ("asset_ids", evidence.asset_ids, asset_ids),
            ("service_ids", evidence.service_ids, service_ids),
            ("vulnerability_ids", evidence.vulnerability_ids, vulnerability_ids),
            ("control_ids", evidence.control_ids, control_ids),
        ):
            for ref in refs:
                require(f"evidences.{evidence.id}.{key}", ref, expected)
    for rel in env.relationships:
        require(f"relationships.{rel.id}.subject_id", rel.subject_id, node_ids)
        require(f"relationships.{rel.id}.object_id", rel.object_id, node_ids)
        if rel.predicate not in ALLOWED_PREDICATES:
            errors.append(
                {
                    "path": f"relationships.{rel.id}.predicate",
                    "value": rel.predicate,
                    "type": "invalid_predicate",
                    "message": "predicato non ammesso",
                }
            )
    for group in all_groups:
        for item in group:
            # I gruppi contengono modelli diversi ma tutti espongono model_dump;
            # l'annotazione rende esplicita la forma comune dopo la serializzazione.
            dumped: dict[str, Any] = item.model_dump()
            for key, value in dumped.items():
                if key == "provenance_ids" and isinstance(value, list):
                    for ref in value:
                        require(f"{item.id}.provenance_ids", ref, provenance_ids)
                if isinstance(value, dict) and "provenance_ids" in value:
                    nested_refs = value["provenance_ids"]
                    if not isinstance(nested_refs, list):
                        continue
                    for ref in nested_refs:
                        require(f"{item.id}.{key}.provenance_ids", ref, provenance_ids)
    return errors
