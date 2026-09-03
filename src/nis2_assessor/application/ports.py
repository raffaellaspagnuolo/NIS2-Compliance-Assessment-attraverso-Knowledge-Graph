"""Definisce i contratti astratti fra applicazione e infrastruttura.

I Protocol descrivono le operazioni necessarie senza imporre Neo4j o filesystem.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Protocol

from nis2_assessor.domain.models import (
    NormalizedEnvironment,
    Relationship,
    Requirement,
    Rule,
)


class GraphRepository(Protocol):
    """Contratto sostituibile per salvare e interrogare il grafo."""

    def clear(self) -> None: ...
    def add_entity(self, entity: Any) -> None: ...
    def add_relationship(self, relationship: Relationship) -> None: ...
    def entity_exists(self, entity_id: str) -> bool: ...
    def get_entity(self, entity_id: str) -> dict[str, Any] | None: ...
    def find_entities(
        self, entity_type: str, filters: dict[str, object] | None = None
    ) -> list[dict[str, Any]]: ...
    def get_property(self, entity_id: str, property_name: str) -> object | None: ...
    def count_entities(self) -> int: ...
    def count_relationships(self) -> int: ...
    def list_entity_ids(self) -> list[str]: ...
    def list_relationships(self) -> list[dict[str, Any]]: ...
    def execute_read(
        self, query: str, parameters: dict[str, object] | None = None
    ) -> list[dict[str, Any]]: ...


class NormalizedDataRepository(Protocol):
    """Contratto per caricare un ambiente già normalizzato."""

    def load(self, path: Path) -> NormalizedEnvironment: ...


class Clock(Protocol):
    """Fonte del tempo iniettabile per rendere validazioni e report deterministici."""

    def now(self) -> datetime: ...


class ControlEvaluator(Protocol):
    """Strategia sostituibile che valuta una regola su un ambiente."""

    evaluator_id: str

    def supports(self, evaluator_name: str) -> bool: ...


class FrameworkRepository(Protocol):
    """Porta generica per framework NIS2, ISO 27001, NIST o personalizzati."""

    def load_requirements(self, path: Path) -> list[Requirement]: ...

    def load_rules(self, path: Path) -> list[Rule]: ...
