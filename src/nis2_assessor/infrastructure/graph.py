"""Persistenza e interrogazione del Knowledge Graph tramite Neo4j.

Le entita Pydantic sono mappate su nodi del property graph e le relazioni del
dataset su archi Neo4j. Tutti gli accessi applicativi usano query Cypher
parametrizzate; le query fornite dall'utente sono limitate alla sola lettura.
"""

from __future__ import annotations

import json
import os
import re
from collections.abc import Mapping
from datetime import date, datetime, time
from typing import Any

from neo4j import GraphDatabase, RoutingControl
from neo4j.graph import Node, Path
from neo4j.graph import Relationship as Neo4jRelationship

from nis2_assessor.domain.models import Relationship

_IDENTIFIER = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
_WRITE_CLAUSES = re.compile(
    r"\b(ALTER|CALL|CREATE|DELETE|DENY|DETACH|DROP|FOREACH|GRANT|LOAD|MERGE|"
    r"REMOVE|RENAME|REVOKE|SET|START|STOP|TERMINATE)\b",
    re.IGNORECASE,
)
_READ_START = re.compile(
    r"^(EXPLAIN\s+|PROFILE\s+)?(MATCH|OPTIONAL\s+MATCH|RETURN|SHOW|UNWIND|WITH)\b",
    re.IGNORECASE,
)


class Neo4jGraphRepository:
    """Repository Neo4j isolato logicamente mediante la proprieta ``graph_id``."""

    def __init__(
        self,
        uri: str | None = None,
        username: str | None = None,
        password: str | None = None,
        database: str | None = None,
        graph_id: str = "default",
        driver: Any | None = None,
    ) -> None:
        """Configura il driver senza aprire una connessione fino alla prima query."""
        self.database = database or os.getenv("NIS2_NEO4J_DATABASE", "neo4j")
        self.graph_id = graph_id
        self._owns_driver = driver is None
        resolved_uri = uri or os.getenv("NIS2_NEO4J_URI") or "bolt://localhost:7687"
        resolved_username = username or os.getenv("NIS2_NEO4J_USERNAME") or "neo4j"
        resolved_password = password or os.getenv("NIS2_NEO4J_PASSWORD") or "nis2-local-password"
        self._driver = driver or GraphDatabase.driver(
            resolved_uri,
            auth=(resolved_username, resolved_password),
        )

    def close(self) -> None:
        """Rilascia le risorse di rete quando il repository possiede il driver."""
        if self._owns_driver:
            self._driver.close()

    def __enter__(self) -> Neo4jGraphRepository:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def scoped(self, graph_id: str) -> Neo4jGraphRepository:
        """Crea una vista su un altro grafo logico riutilizzando lo stesso driver."""
        return Neo4jGraphRepository(
            database=self.database,
            graph_id=graph_id,
            driver=self._driver,
        )

    def verify_connectivity(self) -> None:
        """Verifica esplicitamente credenziali e raggiungibilita del DBMS."""
        self._driver.verify_connectivity(database=self.database)

    def clear(self) -> None:
        """Elimina soltanto i nodi appartenenti al grafo logico corrente."""
        self._write(
            "MATCH (n:Entity {graph_id: $graph_id}) DETACH DELETE n",
            graph_id=self.graph_id,
        )

    def add_entity(self, entity: Any) -> None:
        """Inserisce o aggiorna un'entita come nodo ``:Entity:<Tipo>``."""
        label = _safe_identifier(type(entity).__name__, "label")
        properties = _entity_properties(entity)
        self._write(
            f"MERGE (n:Entity:{label} {{graph_id: $graph_id, id: $id}}) SET n += $properties",
            graph_id=self.graph_id,
            id=entity.id,
            properties=properties,
        )

    def add_relationship(self, relationship: Relationship) -> None:
        """Inserisce un arco tipizzato fra due entita del medesimo grafo logico."""
        relationship_type = _safe_identifier(relationship.predicate, "tipo di relazione")
        self._write(
            "MATCH (subject:Entity {graph_id: $graph_id, id: $subject_id}) "
            "MATCH (object:Entity {graph_id: $graph_id, id: $object_id}) "
            f"MERGE (subject)-[r:{relationship_type} {{id: $relationship_id}}]->(object) "
            "SET r.graph_id = $graph_id, r.provenance_ids = $provenance_ids",
            graph_id=self.graph_id,
            subject_id=relationship.subject_id,
            object_id=relationship.object_id,
            relationship_id=relationship.id,
            provenance_ids=relationship.provenance_ids,
        )

    def entity_exists(self, entity_id: str) -> bool:
        """Indica se esiste un nodo con l'identificativo richiesto."""
        rows = self._read(
            "MATCH (n:Entity {graph_id: $graph_id, id: $entity_id}) RETURN count(n) > 0 AS exists",
            graph_id=self.graph_id,
            entity_id=entity_id,
        )
        return bool(rows and rows[0]["exists"])

    def get_entity(self, entity_id: str) -> dict[str, Any] | None:
        """Restituisce label e proprieta semplici di un nodo."""
        rows = self._read(
            "MATCH (n:Entity {graph_id: $graph_id, id: $entity_id}) "
            "RETURN labels(n) AS labels, properties(n) AS properties LIMIT 1",
            graph_id=self.graph_id,
            entity_id=entity_id,
        )
        if not rows:
            return None
        properties = dict(rows[0]["properties"])
        properties["labels"] = rows[0]["labels"]
        return properties

    def get_property(self, entity_id: str, property_name: str) -> object | None:
        """Legge una proprieta usando l'accesso dinamico sicuro di Cypher."""
        rows = self._read(
            "MATCH (n:Entity {graph_id: $graph_id, id: $entity_id}) "
            "RETURN n[$property_name] AS value LIMIT 1",
            graph_id=self.graph_id,
            entity_id=entity_id,
            property_name=property_name,
        )
        return rows[0]["value"] if rows else None

    def find_entities(
        self, entity_type: str, filters: dict[str, object] | None = None
    ) -> list[dict[str, Any]]:
        """Restituisce entita di un tipo filtrandole su proprieta parametrizzate."""
        label = _safe_identifier(entity_type, "label")
        rows = self._read(
            f"MATCH (n:Entity:{label} {{graph_id: $graph_id}}) "
            "WHERE all(key IN keys($filters) WHERE n[key] = $filters[key]) "
            "RETURN properties(n) AS properties ORDER BY n.id",
            graph_id=self.graph_id,
            filters=filters or {},
        )
        return [dict(row["properties"]) for row in rows]

    def count_entities(self) -> int:
        """Conta i nodi nel grafo logico corrente."""
        rows = self._read(
            "MATCH (n:Entity {graph_id: $graph_id}) RETURN count(n) AS count",
            graph_id=self.graph_id,
        )
        return int(rows[0]["count"])

    def count_relationships(self) -> int:
        """Conta gli archi interni al grafo logico corrente."""
        rows = self._read(
            "MATCH (:Entity {graph_id: $graph_id})-[r]->(:Entity {graph_id: $graph_id}) "
            "RETURN count(r) AS count",
            graph_id=self.graph_id,
        )
        return int(rows[0]["count"])

    def list_entity_ids(self) -> list[str]:
        """Elenca gli identificativi dei nodi del grafo corrente."""
        return [
            str(row["id"])
            for row in self._read(
                "MATCH (n:Entity {graph_id: $graph_id}) RETURN n.id AS id ORDER BY id",
                graph_id=self.graph_id,
            )
        ]

    def list_relationships(self) -> list[dict[str, Any]]:
        """Espone gli archi come record JSON adatti all'endpoint di debug."""
        return self._read(
            "MATCH (subject:Entity {graph_id: $graph_id})-[r]->"
            "(object:Entity {graph_id: $graph_id}) "
            "RETURN subject.id AS subject, type(r) AS predicate, object.id AS object, "
            "r.id AS id ORDER BY id",
            graph_id=self.graph_id,
        )

    def execute_read(
        self, query: str, parameters: Mapping[str, object] | None = None
    ) -> list[dict[str, Any]]:
        """Esegue una query Cypher di sola lettura con parametri separati."""
        validate_read_query(query)
        values = dict(parameters or {})
        # Lo scope appartiene al repository: un chiamante non puo sostituirlo
        # tramite il payload dei parametri e leggere un altro grafo logico.
        values["graph_id"] = self.graph_id
        return self._read(query, **values)

    def _read(self, query: str, **parameters: object) -> list[dict[str, Any]]:
        records, _, _ = self._driver.execute_query(
            query,
            parameters_=parameters,
            database_=self.database,
            routing_=RoutingControl.READ,
        )
        return [
            {str(key): _neo4j_value(value) for key, value in record.items()} for record in records
        ]

    def _write(self, query: str, **parameters: object) -> None:
        self._driver.execute_query(
            query,
            parameters_=parameters,
            database_=self.database,
            routing_=RoutingControl.WRITE,
        )


def validate_read_query(query: str) -> None:
    """Rifiuta Cypher mutativo, multi-statement o non riconducibile a lettura."""
    if len(query) > 10_000:
        raise ValueError("query troppo lunga")
    compact = _strip_cypher_literals_and_comments(query).strip()
    if not compact or ";" in compact or not _READ_START.match(compact):
        raise ValueError("sono ammesse esclusivamente query Cypher di sola lettura")
    if _WRITE_CLAUSES.search(compact):
        raise ValueError("sono ammesse esclusivamente query Cypher di sola lettura")


def _entity_properties(entity: Any) -> dict[str, object]:
    """Converte il modello in proprieta primitive supportate da Neo4j."""
    raw = entity.model_dump(mode="json")
    properties: dict[str, object] = {"id": entity.id}
    for key, value in raw.items():
        if key == "id" or value is None:
            continue
        _flatten_property(properties, key, value)
    return properties


def _flatten_property(target: dict[str, object], key: str, value: Any) -> None:
    if isinstance(value, dict) and "status" in value and "value" in value:
        if value["value"] is not None:
            target[key] = _property_value(value["value"])
        target[f"{key}_status"] = str(value["status"])
        if value.get("provenance_ids"):
            target[f"{key}_provenance_ids"] = list(value["provenance_ids"])
        for metadata_key in ("observation_type", "observed_at", "unknown_cause"):
            if value.get(metadata_key) is not None:
                target[f"{key}_{metadata_key}"] = _property_value(value[metadata_key])
        return
    if isinstance(value, dict):
        # Le proprieta estensibili degli asset mantengono nomi interrogabili;
        # gli altri oggetti arbitrari (per esempio Evidence.content) restano JSON.
        if value and all(isinstance(item, dict) and "status" in item for item in value.values()):
            for nested_key, nested_value in value.items():
                _flatten_property(target, str(nested_key), nested_value)
        else:
            target[f"{key}_json"] = json.dumps(value, ensure_ascii=False, sort_keys=True)
        return
    if isinstance(value, list) and any(isinstance(item, (dict, list)) for item in value):
        target[f"{key}_json"] = json.dumps(
            value, ensure_ascii=False, sort_keys=True, default=str
        )
        return
    target[key] = _property_value(value)


def _property_value(value: Any) -> object:
    if isinstance(value, (datetime, date, time)):
        return value.isoformat()
    if isinstance(value, list):
        return [_property_scalar(item) for item in value]
    return _property_scalar(value)


def _property_scalar(value: Any) -> str | int | float | bool:
    if isinstance(value, (str, int, float, bool)):
        return value
    if value is None:
        return ""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)


def _safe_identifier(value: str, description: str) -> str:
    if not _IDENTIFIER.fullmatch(value):
        raise ValueError(f"{description} Neo4j non valido: {value!r}")
    return value


def _strip_cypher_literals_and_comments(query: str) -> str:
    """Rimuove commenti e stringhe prima del controllo delle clausole."""
    without_block_comments = re.sub(r"/\*.*?\*/", " ", query, flags=re.DOTALL)
    without_line_comments = re.sub(r"//[^\n]*", " ", without_block_comments)
    without_strings = re.sub(
        r"'(?:\\.|''|[^'])*'|\"(?:\\.|\"\"|[^\"])*\"", "''", without_line_comments
    )
    return " ".join(without_strings.split())


def _neo4j_value(value: Any) -> Any:
    """Rende serializzabili i tipi grafo e temporali restituiti dal driver."""
    if isinstance(value, Node):
        return {
            "element_id": value.element_id,
            "labels": sorted(value.labels),
            "properties": {key: _neo4j_value(item) for key, item in value.items()},
        }
    if isinstance(value, Neo4jRelationship):
        return {
            "element_id": value.element_id,
            "type": value.type,
            "properties": {key: _neo4j_value(item) for key, item in value.items()},
        }
    if isinstance(value, Path):
        return {
            "nodes": [_neo4j_value(node) for node in value.nodes],
            "relationships": [_neo4j_value(item) for item in value.relationships],
        }
    if isinstance(value, Mapping):
        return {str(key): _neo4j_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_neo4j_value(item) for item in value]
    isoformat = getattr(value, "iso_format", None) or getattr(value, "isoformat", None)
    if callable(isoformat):
        return isoformat()
    return value
