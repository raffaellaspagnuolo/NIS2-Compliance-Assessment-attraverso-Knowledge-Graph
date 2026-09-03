# Prova di concetto con casi asset-controllo isolati

Questo documento descrive esclusivamente l'adattatore e la riproduzione dei 93
casi isolati.

I 93 elementi misurano la coerenza dell'implementazione con oracle definiti
separatamente. La metrica pubblica è `rule_conformance_rate`, non una misura di
conformità normativa. La loro funzione sperimentale è isolare le condizioni
che distinguono un esito dall'altro e verificare che la metodologia le tratti
in modo stabile, senza l'interferenza di un ambiente complesso.

La PoC verifica le 26 regole del sottoinsieme tecnico ACN selezionato attraverso 93 coppie isolate
asset–controllo. Non implementa un secondo checker: costruisce gli ingressi
minimi mancanti, richiama la pipeline generale e confronta gli
`AssessmentResult` con oracle separati.

## Confine dell'adattatore

I soli compiti specifici della PoC sono:

- leggere `data/poc/cases.yaml` senza conoscere gli esiti attesi;
- selezionare requisito, controllo e regola dai cataloghi generali;
- creare una micro-organizzazione sintetica valida per una sola coppia;
- invocare `execute_assessment` una volta per caso;
- caricare dopo le valutazioni `data/poc/ground_truth.yaml`;
- scrivere l'unico CSV complessivo.

Validazione, preflight, applicabilità, evaluator, Knowledge Graph, persistenza,
aggregazione e contesto sono quelli della pipeline ordinaria. Le evidenze sono
già incluse nelle micro-organizzazioni normalizzate. La PoC non contiene
registry di evaluator e non modifica mai un esito reale.

## Micro-organizzazioni

La pipeline richiede un `NormalizedEnvironment` completo. Per ogni caso
l'adattatore materializza temporaneamente un dataset e un'organizzazione
sintetici, un responsabile, un asset NIS rilevante, un requisito, un controllo,
una regola e soltanto le entità ed evidenze necessarie.

Il contenitore organizzativo soddisfa il contratto dati ma non rappresenta una
valutazione aziendale. Le collezioni non pertinenti sono vuote; i fatti estranei
al controllo non vengono introdotti. Hostname e indirizzi usano rispettivamente
il dominio riservato `.invalid` e la rete documentale `192.0.2.0/24`.

Gli input temporanei sono rimossi dopo ogni esecuzione. Ogni grafo viene pulito
prima della coppia successiva e deve produrre esattamente un risultato.

## Esecuzione

```bash
nis2-assessor test-poc \
  --cases data/poc/cases.yaml \
  --ground-truth data/poc/ground_truth.yaml \
  --output-dir reports/poc
```

`--scenarios` resta un alias compatibile di `--cases`. Il comando esegue 93
invocazioni della pipeline generale e mostra casi superati, rule conformance rate e
percorso del CSV.

## Artefatto unico

L'unico file persistente prodotto è:

`reports/poc/confronto-ground-truth-casi-uso-poc.csv`

Le colonne sono:

| Colonna | Significato |
|---|---|
| `test_id` | Identificativo stabile del caso. |
| `asset_id` | Asset sintetico effettivamente valutato. |
| `control_id` | Controllo generale effettivamente applicato. |
| `rule_id` | Regola generale eseguita. |
| `requirement_id` | Requisito generale collegato. |
| `expected_status` | Oracle letto dopo la valutazione. |
| `actual_status` | Stato dell'`AssessmentResult`. |
| `expected_governance_status` | Oracle separato per la governance. |
| `actual_governance_status` | Stato governance effettivamente prodotto. |
| `passed` | Corrispondenza di tracciabilità ed esito. |
| `purpose` | Condizione informativa rappresentata. |
| `details` | Fatti, evidenze o informazioni mancanti restituiti dalla pipeline. |

Non vengono generati report narrativi, report del grafo, JSON o copie
permanenti degli ambienti normalizzati.

## Invarianti

- 93 casi, 93 invocazioni e 93 risultati singoli;
- 26 regole del catalogo generale, senza copie modificate;
- ground truth assente dagli input, dai grafi e dagli evaluator;
- clock fisso e identificativi deterministici;
- nessuna conoscenza condivisa fra casi;
- un mismatch produce `passed=False` senza correggere `actual_status`.

La riproduzione completa avviene con il comando `nis2-assessor test-poc`
mostrato sopra.
