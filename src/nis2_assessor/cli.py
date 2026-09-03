"""Interfaccia a riga di comando per usare il checker senza avviare l'API.

Ogni comando raccoglie percorsi e opzioni, poi delega la logica ai moduli
application. In questo file non vengono duplicate regole decisionali.
"""

import asyncio
import json
from pathlib import Path

import typer

from nis2_assessor.application.engine import evaluate as evaluate_controls
from nis2_assessor.application.pipeline import build_graph as construct_graph
from nis2_assessor.application.pipeline import (
    load_requirements,
    load_rules,
    populate_graph,
    populate_rules,
    run_assessment,
    validate_framework_alignment,
)
from nis2_assessor.application.poc import run_poc
from nis2_assessor.application.validation import load_environment
from nis2_assessor.config import load_settings
from nis2_assessor.infrastructure.graph import Neo4jGraphRepository

# Oggetto principale a cui Typer registra i sottocomandi definiti più sotto.
app = typer.Typer(help="NIS2 Technical Control Assessment System")


def _neo4j_repository(graph_id: str) -> Neo4jGraphRepository:
    """Costruisce il repository CLI dalle impostazioni centralizzate."""
    settings = load_settings()
    return Neo4jGraphRepository(
        uri=settings.neo4j_uri,
        username=settings.neo4j_username,
        password=settings.neo4j_password,
        database=settings.neo4j_database,
        graph_id=graph_id,
    )


@app.command()
def validate(input: Path = typer.Option(..., exists=True, dir_okay=False)) -> None:
    """Valida schema, tipi e riferimenti di un dataset normalizzato."""
    env = load_environment(input)
    typer.echo(f"Dataset valido: {env.dataset.id}")


@app.command("validate-data")
def validate_data(organization: Path = typer.Option(..., exists=True, dir_okay=False)) -> None:
    """Alias descrittivo che valida il file canonico dell'organizzazione."""
    validate(organization)


@app.command("build-graph")
def build_graph(
    input: Path = typer.Option(..., exists=True),
    graph_id: str = typer.Option("default", help="Identificativo logico del grafo Neo4j"),
) -> None:
    """Costruisce il Knowledge Graph nel database Neo4j configurato."""
    with _neo4j_repository(graph_id) as graph:
        construct_graph(input, graph)
        typer.echo(
            json.dumps(
                {
                    "graph_id": graph_id,
                    "nodes": graph.count_entities(),
                    "relationships": graph.count_relationships(),
                },
                indent=2,
            )
        )


@app.command()
def evaluate(
    input: Path = typer.Option(..., exists=True),
    rules: Path = typer.Option(..., exists=True),
    requirements: Path = typer.Option(
        Path("data/nis2_requirements.example.yaml"), exists=True
    ),
) -> None:
    """Mostra gli esiti puntuali senza generare il report completo."""
    environment = load_environment(input)
    loaded_rules = load_rules(rules)
    loaded_requirements = load_requirements(requirements)
    environment = environment.model_copy(update={"requirements": loaded_requirements})
    validate_framework_alignment(environment, loaded_requirements, loaded_rules)
    with _neo4j_repository("cli-evaluation") as graph:
        populate_graph(environment, graph)
        populate_rules(graph, loaded_rules)
        results, _ = evaluate_controls(graph, "cli-evaluation")
    typer.echo(json.dumps([r.model_dump(mode="json") for r in results], indent=2))


@app.command()
def assess(
    input: Path = typer.Option(..., exists=True),
    rules: Path = typer.Option(..., exists=True),
    requirements: Path = typer.Option(Path("data/nis2_requirements.example.yaml"), exists=True),
    output_dir: Path = typer.Option(Path("reports")),
    evidence_policies: Path | None = typer.Option(None, exists=True, dir_okay=False),
    operational_policy: Path | None = typer.Option(None, exists=True, dir_okay=False),
    coverage_catalog: Path | None = typer.Option(None, exists=True, dir_okay=False),
) -> None:
    """Esegue l'intera pipeline e genera tutti gli artefatti di output."""
    report = asyncio.run(
        run_assessment(
            input,
            rules,
            output_dir,
            requirements_path=requirements,
            evidence_policies_path=evidence_policies,
            operational_policy_path=operational_policy,
            coverage_catalog_path=coverage_catalog,
        )
    )
    typer.echo(f"Assessment completato: {report['assessment_id']}")


@app.command()
def query(
    query: Path = typer.Option(..., exists=True, dir_okay=False),
    graph_id: str = typer.Option("default", help="Identificativo logico del grafo Neo4j"),
    parameters: Path | None = typer.Option(
        None, exists=True, dir_okay=False, help="File JSON con i parametri Cypher"
    ),
) -> None:
    """Esegue una query Cypher di sola lettura sul grafo Neo4j indicato."""
    values = json.loads(parameters.read_text()) if parameters else {}
    if not isinstance(values, dict):
        raise typer.BadParameter("il file dei parametri deve contenere un oggetto JSON")
    with _neo4j_repository(graph_id) as repository:
        rows = repository.execute_read(query.read_text(encoding="utf-8"), values)
    typer.echo(json.dumps(rows, indent=2, default=str))


@app.command("query-graph")
def query_graph(
    query_file: Path = typer.Option(..., "--query", exists=True),
    graph_id: str = typer.Option("default"),
    parameters: Path | None = typer.Option(None, exists=True, dir_okay=False),
) -> None:
    """Alias del comando query coerente con la terminologia della nuova demo."""
    query(query_file, graph_id, parameters)


@app.command("test-poc")
def test_poc(
    cases: Path = typer.Option(
        Path("data/poc/cases.yaml"), "--cases", "--scenarios", exists=True
    ),
    ground_truth: Path = typer.Option(Path("data/poc/ground_truth.yaml"), exists=True),
    output_dir: Path = typer.Option(Path("reports/poc")),
) -> None:
    """Esegue 93 coppie asset-controllo tramite la pipeline generale."""
    with _neo4j_repository("poc") as graph:
        report = run_poc(cases, ground_truth, output_dir, graph=graph)
    csv_path = report["report_files"]["validation_csv"]
    typer.echo(
        f"PoC completata: {report['passed_count']}/{report['case_count']} casi, "
        f"rule conformance rate {report['rule_conformance_rate']:.1%}. CSV: {csv_path}"
    )


if __name__ == "__main__":
    app()
