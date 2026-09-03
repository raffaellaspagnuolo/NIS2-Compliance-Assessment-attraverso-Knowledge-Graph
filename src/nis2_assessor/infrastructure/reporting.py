"""Facade dei renderer Markdown e convenzioni dei nomi di file."""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from nis2_assessor.infrastructure.knowledge_graph_reporting import (
    render_knowledge_graph_markdown as render_knowledge_graph_markdown,
)
from nis2_assessor.infrastructure.narrative_reporting import (
    render_main_report,
    render_technical_attachment,
)


def general_markdown_path(output_dir: Path, assessment_id: str) -> Path:
    identifier = _filename_component(assessment_id)
    return output_dir / f"report-generale-valutazione-tecnica-{identifier}.md"


def technical_attachment_markdown_path(output_dir: Path, assessment_id: str) -> Path:
    identifier = _filename_component(assessment_id)
    return output_dir / f"allegato-tecnico-valutazione-{identifier}.md"


def knowledge_graph_markdown_path(output_dir: Path, assessment_id: str) -> Path:
    """Nome del Knowledge Graph completo prodotto dall'assessment."""
    identifier = _filename_component(assessment_id)
    return output_dir / f"knowledge-graph-completo-valutazione-tecnica-{identifier}.md"


def write_markdown(report: dict[str, Any], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_main_report(report), encoding="utf-8")


def write_technical_attachment_markdown(
    report: Mapping[str, Any], destination: Path
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_technical_attachment(report), encoding="utf-8")


def write_knowledge_graph_markdown(
    report: Mapping[str, Any], destination: Path
) -> None:
    """Scrive lo snapshot completo del grafo consultato dall'assessment."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_knowledge_graph_markdown(report), encoding="utf-8")


def _filename_component(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    component = re.sub(r"[^A-Za-z0-9]+", "-", normalized).strip("-").lower()
    return component or "senza-identificativo"
