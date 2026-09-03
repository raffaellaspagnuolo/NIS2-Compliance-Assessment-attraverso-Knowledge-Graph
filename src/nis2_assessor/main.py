"""Espone tramite FastAPI le funzioni principali del checker.

Gli endpoint validano le richieste e delegano ai casi d'uso. I registri in
memoria sono adatti alla PoC; in produzione andrebbero sostituiti da repository.
"""

import secrets
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, cast

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field

from nis2_assessor import __version__
from nis2_assessor.application.pipeline import (
    CatalogValidationError,
    build_graph,
    load_rules,
    run_assessment,
)
from nis2_assessor.application.runtime import random_assessment_id
from nis2_assessor.application.validation import DatasetValidationError, load_environment
from nis2_assessor.config import load_settings
from nis2_assessor.domain.models import Rule
from nis2_assessor.infrastructure.graph import Neo4jGraphRepository
from nis2_assessor.infrastructure.reporting import (
    general_markdown_path,
    render_knowledge_graph_markdown,
    technical_attachment_markdown_path,
)
from nis2_assessor.infrastructure.state import SQLiteStateRepository


@asynccontextmanager
async def lifespan(application: FastAPI) -> Any:
    """Chiude il pool di connessioni Neo4j allo spegnimento dell'API."""
    yield
    close = getattr(application.state.graph, "close", None)
    if callable(close):
        close()


# Applicazione ASGI importata da Uvicorn e dagli altri processi compatibili ASGI.
app = FastAPI(title="NIS2 Asset Technical Checker", version=__version__, lifespan=lifespan)
SETTINGS = load_settings()
ROOT = SETTINGS.project_root
REPORTS = SETTINGS.report_dir
# Lo stato applicativo usa SQLite; il grafo viene invece persistito da Neo4j.
app.state.repository = SQLiteStateRepository(SETTINGS.state_database)
app.state.graph = Neo4jGraphRepository(
    uri=SETTINGS.neo4j_uri,
    username=SETTINGS.neo4j_username,
    password=SETTINGS.neo4j_password,
    database=SETTINGS.neo4j_database,
    graph_id=SETTINGS.neo4j_graph_id,
)


@app.middleware("http")
async def authenticate(request: Request, call_next: Any) -> Any:
    """Richiede una API key su ogni endpoint, eccetto il controllo di salute."""
    if request.url.path != "/health":
        supplied = request.headers.get("X-API-Key", "")
        if not secrets.compare_digest(supplied, SETTINGS.api_key):
            return JSONResponse(status_code=401, content={"detail": "API key non valida"})
    return await call_next(request)


def authorize_organization(request: Request, organization_id: str) -> None:
    """Impedisce a un chiamante di accedere ai dati di un'altra organizzazione."""
    if request.headers.get("X-Organization-ID") != organization_id:
        raise HTTPException(403, "organizzazione non autorizzata")


def require_graph_debug() -> None:
    """Protegge gli endpoint che potrebbero esporre la topologia completa."""
    if not SETTINGS.graph_debug_enabled:
        raise HTTPException(403, "endpoint del grafo disabilitato fuori dalla modalità debug")


def safe_path(
    value: str, allowed: tuple[Path, ...] = (ROOT / "data", ROOT / "reports", ROOT / "examples")
) -> Path:
    """Risolve un percorso e impedisce l'uscita dalle directory autorizzate."""
    candidate = (ROOT / value).resolve()
    if not any(
        candidate == root.resolve() or root.resolve() in candidate.parents for root in allowed
    ):
        raise HTTPException(400, "percorso fuori dalle directory autorizzate")
    if candidate.is_file() and candidate.stat().st_size > SETTINGS.max_import_bytes:
        raise HTTPException(413, "file oltre il limite massimo configurato")
    return candidate


class FileRequest(BaseModel):
    """Payload comune agli endpoint che ricevono un percorso locale."""

    path: str


class AssessmentRequest(BaseModel):
    """Parametri necessari per avviare una valutazione completa."""

    input_path: str = "data/normalized_environment.example.yaml"
    rules_path: str = "data/technical_rules.example.yaml"
    requirements_path: str = "data/nis2_requirements.example.yaml"
    evidence_policies_path: str | None = None
    operational_policy_path: str | None = None
    coverage_catalog_path: str | None = None
    assessment_id: str | None = Field(default=None, pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]{0,79}$")
    organization_id: str | None = None
    framework_id: str | None = None


class QueryRequest(BaseModel):
    """Query Cypher di lettura e relativi parametri."""

    query: str = Field(max_length=10_000)
    parameters: dict[str, object] = Field(default_factory=dict)


class FrameworkImportRequest(BaseModel):
    """Percorso di un file di regole appartenente a un framework tecnico."""

    path: str
    framework_id: str = "nis2-technical-subset"


@app.get("/health")
def health() -> dict[str, str]:
    """Conferma che il processo API è attivo e raggiungibile."""
    return {"status": "ok"}


@app.post("/datasets/validate")
def validate_dataset(request: FileRequest) -> dict[str, Any]:
    """Valida il contratto normalizzato e restituisce l'ID del dataset."""
    try:
        env = load_environment(safe_path(request.path))
    except DatasetValidationError as exc:
        raise HTTPException(422, detail=exc.errors) from exc
    return {"valid": True, "dataset_id": env.dataset.id}


@app.post("/organizations/import", status_code=201)
def import_organization(request: FileRequest, http_request: Request) -> dict[str, Any]:
    """Importa la vista organizzativa minima contenuta nel dataset canonico."""
    try:
        env = load_environment(safe_path(request.path))
    except DatasetValidationError as exc:
        raise HTTPException(422, detail=exc.errors) from exc
    payload = env.organization.model_dump(mode="json")
    authorize_organization(http_request, env.organization.id)
    http_request.app.state.repository.save_organization(env.organization.id, payload, request.path)
    return payload


@app.get("/organizations/{organization_id}")
def get_organization(organization_id: str, request: Request) -> dict[str, Any]:
    """Recupera un'organizzazione precedentemente importata."""
    authorize_organization(request, organization_id)
    stored = request.app.state.repository.get_organization(organization_id)
    if stored is None:
        raise HTTPException(404, "organizzazione non trovata")
    return cast(dict[str, Any], stored[0])


@app.post("/frameworks/import", status_code=201)
def import_framework(request: FrameworkImportRequest, http_request: Request) -> dict[str, Any]:
    """Valida e registra un set di regole senza vincolare l'API alla NIS2."""
    try:
        rules = load_rules(safe_path(request.path))
    except CatalogValidationError as exc:
        raise HTTPException(422, str(exc)) from exc
    payload = {"framework_id": request.framework_id, "rule_ids": [rule.id for rule in rules]}
    http_request.app.state.repository.save_framework(request.framework_id, rules, request.path)
    return payload


@app.post("/graphs/build")
def graph_build(request: FileRequest, http_request: Request) -> dict[str, int | str]:
    """Ricostruisce il grafo logico Neo4j a partire dal dataset indicato."""
    _, graph = build_graph(safe_path(request.path), http_request.app.state.graph)
    return {
        "graph_id": getattr(graph, "graph_id", SETTINGS.neo4j_graph_id),
        "nodes": graph.count_entities(),
        "relationships": graph.count_relationships(),
    }


@app.get("/graphs/entities")
def graph_entities(request: Request) -> list[str]:
    """Elenca gli identificativi dei nodi presenti nel grafo corrente."""
    require_graph_debug()
    return cast(list[str], request.app.state.graph.list_entity_ids())


@app.get("/graphs/relationships")
def graph_relationships(request: Request) -> list[dict[str, str]]:
    """Espone le relazioni Neo4j come record JSON semplici."""
    require_graph_debug()
    return cast(list[dict[str, str]], request.app.state.graph.list_relationships())


@app.post("/graphs/query")
def graph_query(request: QueryRequest, http_request: Request) -> list[dict[str, object]]:
    """Endpoint di sviluppo per query Cypher di sola lettura."""
    require_graph_debug()
    try:
        return cast(
            list[dict[str, object]],
            http_request.app.state.graph.execute_read(request.query, request.parameters),
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/assessments")
async def create_assessment(request: AssessmentRequest, http_request: Request) -> dict[str, Any]:
    """Esegue la pipeline e conserva il report nell'indice in memoria."""
    # Il controllo anticipato evita di sovrascrivere i file prima che SQLite
    # possa segnalare il conflitto sull'identificativo già esistente.
    assessment_id = request.assessment_id or random_assessment_id()
    if http_request.app.state.repository.get_assessment(assessment_id) is not None:
        raise HTTPException(409, "assessment_id già esistente")
    # Quando vengono indicati gli ID importati, l'assessment usa realmente il
    # dataset dell'organizzazione e le regole del framework registrato.
    input_path = request.input_path
    if request.organization_id:
        authorize_organization(http_request, request.organization_id)
        stored_organization = http_request.app.state.repository.get_organization(
            request.organization_id
        )
        if stored_organization is None:
            raise HTTPException(404, "organizzazione non importata")
        input_path = stored_organization[1]

    # Autorizziamo prima di creare file: anche usando direttamente input_path,
    # l'organizzazione proprietaria viene ricavata dal dataset validato.
    try:
        dataset_organization_id = load_environment(safe_path(input_path)).organization.id
    except DatasetValidationError as exc:
        raise HTTPException(422, detail=exc.errors) from exc
    authorize_organization(http_request, dataset_organization_id)

    rules_override: list[Rule] | None = None
    rules_path = request.rules_path
    if request.framework_id:
        stored_framework = http_request.app.state.repository.get_framework(request.framework_id)
        if stored_framework is None:
            raise HTTPException(404, "framework non importato")
        rules_override, rules_path = stored_framework

    try:
        base_graph = http_request.app.state.graph
        assessment_graph = (
            base_graph.scoped(assessment_id) if hasattr(base_graph, "scoped") else base_graph
        )
        report = await run_assessment(
            safe_path(input_path),
            safe_path(rules_path),
            REPORTS,
            assessment_id,
            requirements_path=safe_path(request.requirements_path),
            rules_override=rules_override,
            expected_organization_id=dataset_organization_id,
            graph=assessment_graph,
            evidence_policies_path=(
                safe_path(request.evidence_policies_path)
                if request.evidence_policies_path
                else None
            ),
            operational_policy_path=(
                safe_path(request.operational_policy_path)
                if request.operational_policy_path
                else None
            ),
            coverage_catalog_path=(
                safe_path(request.coverage_catalog_path)
                if request.coverage_catalog_path
                else None
            ),
        )
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    # Anche quando organization_id non è stato dichiarato nel payload, il
    # proprietario ricavato dal dataset deve coincidere con l'header autorizzato.
    authorize_organization(http_request, report["organization_id"])
    try:
        http_request.app.state.repository.save_assessment(
            report["assessment_id"], report["organization_id"], report
        )
    except ValueError as exc:
        raise HTTPException(409, str(exc)) from exc
    return report


def get_assessment(assessment_id: str, request: Request) -> dict[str, Any]:
    """Recupera un assessment dalla memoria o dal corrispondente JSON."""
    stored = request.app.state.repository.get_assessment(assessment_id)
    if stored is None:
        raise HTTPException(404, "assessment non trovato")
    organization_id, report = stored
    authorize_organization(request, organization_id)
    return cast(dict[str, Any], report)


@app.get("/assessments/{assessment_id}")
def assessment(assessment_id: str, request: Request) -> dict[str, Any]:
    """Restituisce l'intero report di un assessment esistente."""
    return get_assessment(assessment_id, request)


@app.get("/assessments/{assessment_id}/results")
def results(assessment_id: str, request: Request) -> list[dict[str, Any]]:
    """Restituisce soltanto gli esiti puntuali asset-controllo."""
    return cast(list[dict[str, Any]], get_assessment(assessment_id, request)["assessment_results"])


@app.get("/assessments/{assessment_id}/summary")
def summary(assessment_id: str, request: Request) -> dict[str, Any]:
    """Restituisce conteggi tecnici, copertura e priorità non normativa."""
    return cast(dict[str, Any], get_assessment(assessment_id, request)["summary"])


@app.get("/reports/{assessment_id}/markdown", response_class=PlainTextResponse)
def markdown_report(assessment_id: str, request: Request) -> str:
    """Restituisce il report testuale senza modificarne il contenuto."""
    get_assessment(assessment_id, request)
    return general_markdown_path(REPORTS, assessment_id).read_text()


@app.get("/reports/{assessment_id}/graph", response_class=PlainTextResponse)
def graph_report(assessment_id: str, request: Request) -> str:
    """Rende tramite API la stessa vista completa persistita dalla pipeline."""
    report = get_assessment(assessment_id, request)
    return render_knowledge_graph_markdown(report)


@app.get("/reports/{assessment_id}/technical", response_class=PlainTextResponse)
def technical_attachment_report(assessment_id: str, request: Request) -> str:
    """Restituisce l'allegato tecnico separato dal report decisionale."""
    get_assessment(assessment_id, request)
    return technical_attachment_markdown_path(REPORTS, assessment_id).read_text()
