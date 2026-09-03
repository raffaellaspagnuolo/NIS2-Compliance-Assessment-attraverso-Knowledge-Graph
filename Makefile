# Scorciatoie per installazione, qualità, pipeline dimostrativa e API locale.
.PHONY: install lint typecheck assess api neo4j coverage-matrix materialize-rules
# Installa il progetto in modalità modificabile insieme agli strumenti di sviluppo.
install:
	python3 -m pip install -e '.[dev]'
# Verifica errori comuni, import e stile senza modificare i file.
lint:
	ruff check .
# Controlla staticamente la coerenza delle annotazioni di tipo Python.
typecheck:
	mypy src
assess:
	nis2-assessor assess --input data/normalized_environment.example.yaml --rules data/technical_rules.example.yaml --output-dir reports
api:
	uvicorn nis2_assessor.main:app --host 0.0.0.0 --port 8000
neo4j:
	docker compose up neo4j
coverage-matrix:
	.venv/bin/python scripts/generate_coverage_matrix.py
materialize-rules:
	.venv/bin/python scripts/materialize_rule_catalog.py
