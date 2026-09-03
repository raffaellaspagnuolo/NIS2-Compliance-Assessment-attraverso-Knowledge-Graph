"""Configurazione minimale letta da variabili d'ambiente.

Non usa librerie esterne e mantiene valori sicuri per la demo locale. In una
distribuzione reale questo oggetto può essere sostituito tramite dependency
injection senza modificare dominio o casi d'uso.
"""

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Percorsi autorizzati e limite massimo dei file importabili."""

    project_root: Path
    report_dir: Path
    max_import_bytes: int
    state_database: Path
    api_key: str
    graph_debug_enabled: bool
    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str
    neo4j_database: str
    neo4j_graph_id: str


def load_settings() -> Settings:
    """Costruisce impostazioni validate a partire dall'ambiente del processo."""
    root = Path(os.getenv("NIS2_ALLOWED_ROOT", ".")).resolve()
    report_value = os.getenv("NIS2_REPORT_DIR", "reports")
    report_dir = (root / report_value).resolve()
    max_bytes = int(os.getenv("NIS2_MAX_IMPORT_BYTES", "5242880"))
    if max_bytes <= 0:
        raise ValueError("NIS2_MAX_IMPORT_BYTES deve essere positivo")
    database_value = os.getenv("NIS2_STATE_DATABASE", "reports/api-state.sqlite3")
    api_key = os.getenv("NIS2_API_KEY", "change-me-local-demo")
    graph_debug = os.getenv("NIS2_GRAPH_DEBUG", "false").lower() == "true"
    return Settings(
        project_root=root,
        report_dir=report_dir,
        max_import_bytes=max_bytes,
        state_database=(root / database_value).resolve(),
        api_key=api_key,
        graph_debug_enabled=graph_debug,
        neo4j_uri=os.getenv("NIS2_NEO4J_URI", "bolt://localhost:7687"),
        neo4j_username=os.getenv("NIS2_NEO4J_USERNAME", "neo4j"),
        neo4j_password=os.getenv("NIS2_NEO4J_PASSWORD", "nis2-local-password"),
        neo4j_database=os.getenv("NIS2_NEO4J_DATABASE", "neo4j"),
        neo4j_graph_id=os.getenv("NIS2_NEO4J_GRAPH_ID", "default"),
    )
