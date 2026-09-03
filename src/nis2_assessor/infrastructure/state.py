"""Repository SQLite per lo stato persistente dell'interfaccia API.

Il repository sostituisce dizionari globali e conserva organizzazioni, framework
e assessment anche dopo il riavvio del processo. I payload JSON restano semplici
da ispezionare, mentre SQLite gestisce concorrenza e transazioni locali.
"""

import json
import sqlite3
from pathlib import Path
from typing import Any

from nis2_assessor.domain.models import Rule


class SQLiteStateRepository:
    """Archivio persistente minimale adatto alla PoC e alle esecuzioni locali."""

    def __init__(self, path: Path) -> None:
        """Crea la directory e inizializza le tabelle se non esistono."""
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS organizations (
                    id TEXT PRIMARY KEY, payload TEXT NOT NULL, dataset_path TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS frameworks (
                    id TEXT PRIMARY KEY, rules TEXT NOT NULL, rules_path TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS assessments (
                    id TEXT PRIMARY KEY, organization_id TEXT NOT NULL, report TEXT NOT NULL
                );
                """
            )

    def _connect(self) -> sqlite3.Connection:
        """Apre una connessione breve; ogni metodo chiude tramite context manager."""
        return sqlite3.connect(self.path, timeout=10)

    def save_organization(self, identifier: str, payload: dict[str, Any], path: str) -> None:
        """Inserisce o aggiorna organizzazione e dataset associato."""
        with self._connect() as connection:
            connection.execute(
                "INSERT OR REPLACE INTO organizations VALUES (?, ?, ?)",
                (identifier, json.dumps(payload), path),
            )

    def get_organization(self, identifier: str) -> tuple[dict[str, Any], str] | None:
        """Recupera payload e percorso del dataset dell'organizzazione."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT payload, dataset_path FROM organizations WHERE id = ?", (identifier,)
            ).fetchone()
        return (json.loads(row[0]), row[1]) if row else None

    def save_framework(self, identifier: str, rules: list[Rule], path: str) -> None:
        """Conserva regole validate e percorso originale del framework."""
        serialized = json.dumps([rule.model_dump(mode="json") for rule in rules])
        with self._connect() as connection:
            connection.execute(
                "INSERT OR REPLACE INTO frameworks VALUES (?, ?, ?)",
                (identifier, serialized, path),
            )

    def get_framework(self, identifier: str) -> tuple[list[Rule], str] | None:
        """Ricostruisce i modelli Rule precedentemente validati."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT rules, rules_path FROM frameworks WHERE id = ?", (identifier,)
            ).fetchone()
        if row is None:
            return None
        return [Rule.model_validate(item) for item in json.loads(row[0])], row[1]

    def save_assessment(
        self, identifier: str, organization_id: str, report: dict[str, Any]
    ) -> None:
        """Salva il report e impedisce sovrascritture silenziose dello stesso ID."""
        try:
            with self._connect() as connection:
                connection.execute(
                    "INSERT INTO assessments VALUES (?, ?, ?)",
                    (identifier, organization_id, json.dumps(report, default=str)),
                )
        except sqlite3.IntegrityError as exc:
            raise ValueError("assessment_id già esistente") from exc

    def get_assessment(self, identifier: str) -> tuple[str, dict[str, Any]] | None:
        """Restituisce organizzazione proprietaria e contenuto del report."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT organization_id, report FROM assessments WHERE id = ?", (identifier,)
            ).fetchone()
        return (row[0], json.loads(row[1])) if row else None
