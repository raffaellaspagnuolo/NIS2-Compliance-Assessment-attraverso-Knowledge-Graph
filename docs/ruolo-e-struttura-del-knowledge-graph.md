# Ruolo e struttura del Knowledge Graph

Questo documento descrive mapping, relazioni, uso operativo e confine
decisionale del grafo Neo4j. Nel progetto il Knowledge Graph non è un semplice
archivio: integra informazioni eterogenee in una rappresentazione comune e
mantiene i collegamenti necessari a spiegare ogni risultato.

Il mapping è isolato in `Neo4jGraphRepository`. Ogni modello Pydantic diventa
un nodo con le label `:Entity` e `:<NomeModello>`, per esempio `:Entity:Asset`.
Le proprietà comuni sono `id` e `graph_id`; quest'ultima separa più dataset o
assessment nello stesso database Neo4j.

Oltre ad `Asset`, `Service`, `Vulnerability`, `DataObject` ed `Evidence`, il
grafo rappresenta i record tipizzati `SoftwareComponent`, `Account`,
`NetworkInterface`, `NetworkFlow`, `BackupRecord`, `SecurityCapability`,
`InventoryState` e `TechnicalException`.
Servizi e oggetti dati conservano protocolli, cifratura e configurazioni
osservate; asset e risultati conservano profilo ACN e rilevanza NIS.

I `KnowledgeValue` sono appiattiti in proprietà interrogabili. Per esempio
`internet_exposed` produce valore, status, observation type, timestamp, causa
degli unknown e `internet_exposed_provenance_ids`. Le mappe arbitrarie sono conservate
come JSON per rispettare i tipi di proprietà supportati da Neo4j.

Le relazioni comprendono EXPOSES, PRESENTS, AFFECTS, PROCESSES, MANAGED_BY,
SUPPORTS, USES, DEPENDS_ON, PROTECTED_BY, REFERS_TO, ASSOCIATED_WITH e
APPLIES_TO. Gli esiti aggiungono EVALUATES, RESULT_OF, TRACES_TO e APPLIES_RULE.

## Confine nel processo decisionale

Il file normalizzato è usato per validare e popolare il repository. Dopo il
popolamento, `application/engine.py` non riceve più `NormalizedEnvironment`:
enumera dal grafo `Asset`, `Control`, `Rule` ed `Evidence`, mentre ogni evaluator
recupera tramite `GraphRepository` le collezioni tipizzate necessarie. Il grafo
rappresenta e rende disponibili i fatti; applicabilità, preflight, evaluator e
risolutore determinano gli esiti.

Le regole vengono persistite come nodi `:Rule` e collegate tramite `IMPLEMENTS`
e `DERIVES_FROM`. I risultati sono salvati come `:AssessmentResult` e collegati
con `EVALUATES`, `RESULT_OF`, `TRACES_TO` e `APPLIES_RULE`. Il dataset resta
quindi l'ingresso iniziale, mentre il repository del grafo è la fonte letta dal
motore durante l'assessment.

Le deroghe sono nodi informativi collegati al contesto tecnico e alimentano
`governance_status=manual_review_required` senza sostituire
`technical_status`. I nodi `Rule` possono selezionare soltanto gli evaluator
registrati nel catalogo applicativo.

## Query

Le query sono Cypher di sola lettura e ricevono automaticamente `$graph_id`.
Le query mutative, le procedure `CALL` e gli statement multipli sono rifiutati
prima di raggiungere il driver. Valori applicativi e parametri restano separati
dalla stringa Cypher.

```cypher
MATCH (asset:Asset {graph_id: $graph_id, criticality: "critical"})
RETURN asset.id AS asset, asset.name AS name
ORDER BY asset
```

Le query dimostrative sono conservate in `examples/cypher/`.

## Configurazione

La connessione è controllata da `NIS2_NEO4J_URI`, `NIS2_NEO4J_USERNAME`,
`NIS2_NEO4J_PASSWORD`, `NIS2_NEO4J_DATABASE` e `NIS2_NEO4J_GRAPH_ID`.
`docker compose up neo4j` avvia l'istanza locale della demo.
