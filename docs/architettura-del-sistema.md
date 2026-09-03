# Architettura del sistema

Questo documento descrive componenti, dipendenze, confini e collocazione del
codice implementato.

## Componenti

Il dominio definisce modelli Pydantic, enumerazioni e contratti dei risultati
senza dipendere da YAML, API o Neo4j. Le strutture principali si trovano in
`domain/models.py`, `domain/enums.py` e `domain/report_types.py`.

Il livello applicativo carica e valida gli input, i cataloghi e le policy. La
validazione controlla schema, unicità e integrità referenziale; la pipeline
coordina l'assessment e la scrittura degli artefatti. Il motore contenuto in
`application/engine.py` gestisce applicabilità, controlli preliminari, selezione
delle entità, valutazione, stato di governance e confidence. I calcoli
descrittivi successivi, come conteggi, copertura informativa e priorità
operativa, sono separati in `application/aggregation.py`.

L'accesso al grafo passa attraverso la porta definita in
`application/ports.py`. Le implementazioni Neo4j e in memoria, collocate in
`infrastructure/graph.py`, condividono lo stesso contratto e isolano i dati
mediante `graph_id`. La parte di reporting costruisce il contesto e produce il
report principale, l'allegato tecnico e lo snapshot del grafo tramite i moduli
in `application/report_context.py` e `infrastructure/`.

La CLI in `cli.py` e l'API FastAPI in `main.py` espongono le stesse funzioni
applicative. `infrastructure/state.py` gestisce infine la persistenza delle
organizzazioni, dei framework e degli assessment usati dall'API.

## Confini e dipendenze

Il dominio non importa infrastruttura. `GraphRepository` consente di usare
Neo4j in esercizio e il repository in memoria nelle esecuzioni riproducibili
senza modificare il motore. Dopo `populate_graph()`, gli evaluator ricevono soltanto il repository
e non il `NormalizedEnvironment`.

Il registro degli evaluator è chiuso: una regola YAML può selezionare soltanto
funzioni registrate. Quando viene caricato il catalogo completo, registro e
catalogo sono confrontati in entrambe le direzioni. Le soglie tecniche, la
freshness delle evidenze e i pesi della priorità sono esterni al codice
decisionale. Questa separazione rende le scelte esplicite e consente di
aggiornarle e collaudarle senza nasconderle negli evaluator.

La CLI e l'API richiamano le stesse funzioni applicative. La Proof of Concept
costruisce input sintetici minimi ma usa la medesima pipeline, lo stesso
registro e gli stessi renderer. I moduli di acquisizione e normalizzazione non
fanno parte dell'architettura implementata.

## Proprietà di audit

Le regole sono inserite nel grafo prima della valutazione. Ogni
`AssessmentResult` viene poi salvato nello stesso `graph_id` e collegato ad
asset, controllo, requisito e regola con `EVALUATES`, `RESULT_OF`, `TRACES_TO`
e `APPLIES_RULE`. Aggregazione e reporting consumano i risultati già calcolati:
non eseguono regole e non modificano gli stati.
