"""Caricamento e validazione dei cataloghi metodologici non normativi."""

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from nis2_assessor.application.validation import load_yaml_mapping


def bundled_catalog_path(filename: str) -> Path:
    """Restituisce il catalogo distribuito con il pacchetto o con il repository."""
    packaged = Path(__file__).resolve().parents[1] / "data" / filename
    if packaged.exists():
        return packaged
    return Path(__file__).resolve().parents[3] / "data" / filename


def load_evidence_policies(path: Path) -> dict[str, Any]:
    raw = load_yaml_mapping(path)
    if raw.get("schema_version") != "1.0" or not isinstance(raw.get("policies"), dict):
        raise ValueError("catalogo policy evidenze non valido")
    for evidence_type, policy in raw["policies"].items():
        if not isinstance(policy, dict) or not policy.get("source_priority"):
            raise ValueError(f"policy evidenza incompleta: {evidence_type}")
        if not policy.get("explicit_validity_only") and not isinstance(
            policy.get("maximum_age_days"), int
        ):
            raise ValueError(f"freschezza non definita: {evidence_type}")
    return raw


def load_operational_policy(path: Path) -> dict[str, Any]:
    raw = load_yaml_mapping(path)
    priority = raw.get("priority")
    if raw.get("schema_version") != "1.0" or not isinstance(priority, dict):
        raise ValueError("catalogo policy operativa non valido")
    if not raw.get("policy_version") or not isinstance(raw.get("technical_thresholds"), dict):
        raise ValueError("versione o soglie della policy operativa mancanti")
    weights = priority.get("weights", {})
    if abs(sum(float(value) for value in weights.values()) - 1.0) > 0.0001:
        raise ValueError("i pesi di priorità devono sommare a 1")
    return raw


def load_coverage_catalog(path: Path) -> dict[str, Any]:
    raw = load_yaml_mapping(path)
    records = raw.get("records")
    if raw.get("schema_version") != "1.0" or not isinstance(records, list):
        raise ValueError("catalogo copertura ACN non valido")
    if len(records) != 26:
        raise ValueError("il catalogo di copertura ACN deve contenere esattamente 26 record")
    by_rule: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict) or record.get("level") not in {"complete", "partial"}:
            raise ValueError("record di copertura non valido")
        rule_id = str(record.get("rule_id", ""))
        if not rule_id or rule_id in by_rule:
            raise ValueError("rule_id di copertura mancante o duplicato")
        if record["level"] == "partial" and not record.get("unverified_scope"):
            raise ValueError(f"copertura parziale senza limite: {rule_id}")
        by_rule[rule_id] = record
    return {**raw, "by_rule": by_rule}


def evidence_expiry(
    evidence: dict[str, Any], policy: dict[str, Any]
) -> datetime | None:
    """Calcola la scadenza effettiva scegliendo la finestra più restrittiva."""
    collected_at = _datetime(evidence.get("collected_at"))
    valid_until = _datetime(evidence.get("valid_until"))
    maximum_age = policy.get("maximum_age_days")
    age_expiry = (
        collected_at + timedelta(days=int(maximum_age))
        if collected_at is not None and maximum_age is not None
        else None
    )
    candidates = [value for value in (valid_until, age_expiry) if value is not None]
    return min(candidates) if candidates else None


def _datetime(value: Any) -> datetime | None:
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
