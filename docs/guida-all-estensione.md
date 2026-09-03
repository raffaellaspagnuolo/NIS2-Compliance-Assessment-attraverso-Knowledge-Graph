# Guida all'estensione del sistema

Questo documento raccoglie i contratti tecnici da rispettare quando il sistema
viene esteso. Lo scopo è preservare separazione delle responsabilità,
riproducibilità e tracciabilità anche quando aumentano fonti, regole o modalità
di presentazione.

- Tipo asset: estendere `AssetType` e inserirlo nei controlli applicabili.
- Evaluator ACN: restituire `EvaluationOutput` con fatti strutturati e
  registrarlo in `CORE_EVALUATOR_REGISTRY`; le tuple legacy non sono ammesse.
- Regola: aggiungere condizioni, selector, decision policy, aggregazione,
  esiti ammessi, remediation, origine e policy per collezioni vuote.
- Copertura: aggiungere il record a `acn_coverage.example.yaml` e rigenerare la
  matrice con `make coverage-matrix`.
- Policy: aggiungere freshness, priorità delle fonti o soglie al catalogo
  appropriato; non introdurre valori decisionali nascosti nel codice.
- Relazione: usare un tipo Neo4j valido e documentarne dominio/codominio.
- Reporter: consumare il risultato strutturato senza ricalcolare gli esiti. Un
  eventuale LLM può riformulare o sintetizzare il contenuto, ma non deve
  modificare stati, evidenze o motivazioni e deve mantenere il collegamento con
  la fonte strutturata.
- Backend grafo: implementare il protocollo `GraphRepository` mantenendo il mapping fuori dal dominio.
- Framework: implementare `FrameworkRepository`; requisiti e regole mantengono
  identificativi del framework, quindi il motore non è vincolato alla NIS2.
