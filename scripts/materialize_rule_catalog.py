"""Materializza nel catalogo ogni default strutturato validato dal dominio."""

from __future__ import annotations

from pathlib import Path

import yaml

from nis2_assessor.application.pipeline import load_rules
from nis2_assessor.application.validation import load_yaml_mapping

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "technical_rules.example.yaml"


def main() -> None:
    raw = load_yaml_mapping(CATALOG)
    rules = load_rules(CATALOG)
    materialized = {
        "schema_version": raw["schema_version"],
        "catalog_id": raw["catalog_id"],
        "catalog_version": raw["catalog_version"],
        "rules": [rule.model_dump(mode="json") for rule in rules],
    }
    CATALOG.write_text(
        yaml.safe_dump(materialized, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
