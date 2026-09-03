"""Genera la matrice Markdown dal catalogo machine-readable di copertura ACN."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "acn_coverage.example.yaml"
DESTINATION = ROOT / "docs" / "copertura-dei-controlli-acn.md"


def escaped(value: object) -> str:
    return str(value or "—").replace("|", "\\|").replace("\n", " ")


def main() -> None:
    catalog = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    records = catalog["records"]
    if len(records) != 26 or len({item["rule_id"] for item in records}) != 26:
        raise ValueError("il catalogo di copertura deve contenere 26 regole univoche")
    lines = [
        "# Copertura dei controlli ACN",
        "",
        "> Documento generato da `data/acn_coverage.example.yaml`; non modificare "
        "manualmente la tabella.",
        "",
        f"Versione catalogo: `{catalog['catalog_version']}`. Fonte normativa: "
        "[Determinazione ACN 379907/2025 e Allegati 1–2]"
        "(https://www.acn.gov.it/portale/nis/la-normativa).",
        "",
        "`complete` e `partial` descrivono la copertura del checker, non un esito "
        "di conformità dell'organizzazione.",
        "",
        "| Regola | Copertura | Parte verificata | Parte non verificata |",
        "|---|---|---|---|",
    ]
    lines.extend(
        f"| `{escaped(item['rule_id'])}` | `{escaped(item['level'])}` | "
        f"{escaped(item['verified_scope'])} | {escaped(item['unverified_scope'])} |"
        for item in records
    )
    complete = sum(item["level"] == "complete" for item in records)
    partial = sum(item["level"] == "partial" for item in records)
    lines += [
        "",
        f"Totale: **{complete} complete**, **{partial} partial**, 26 regole.",
        "",
        "La validazione automatica richiede `verified_scope` per ogni record e "
        "`unverified_scope` per ogni copertura parziale.",
    ]
    DESTINATION.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
