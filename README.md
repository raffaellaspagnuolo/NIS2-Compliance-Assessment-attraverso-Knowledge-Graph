# Valutatore tecnico asset-centrico per il supporto agli assessment NIS2

Il progetto propone un metodo riproducibile per valutare un sottoinsieme
tecnico delle Specifiche di base ACN. Ventisei regole asset-centriche collegano
requisiti, controlli, fatti osservati ed evidenze, producendo esiti che possono
essere ricostruiti anziché soltanto consultati. Il valore del prototipo non è
quindi limitato all'automazione del controllo: consiste soprattutto nella
tracciabilità del percorso che conduce alla decisione.

Il sistema parte da un `NormalizedEnvironment` già costruito. Acquisizione e
normalizzazione delle fonti operative delimitano un possibile sviluppo a
monte, ma non fanno parte dell'implementazione corrente.

L'ambiente contiene organizzazione e profilo ACN, asset, servizi, account,
software, vulnerabilità, capacità di sicurezza, evidenze, provenienze e
relazioni. La pipeline valida questi dati, li rappresenta nel Knowledge Graph,
determina l'applicabilità delle regole, valuta i fatti e produce un risultato
strutturato per ogni coppia asset-controllo.

Gli output di un assessment sono:

- report principale per la lettura immediata;
- allegato tecnico con la traccia decisionale completa;
- snapshot Markdown del Knowledge Graph valutato;
- contesto strutturato restituito dalla pipeline applicativa e dall'API per
  ulteriori elaborazioni.

Il checker valuta il perimetro tecnico codificato e offre una base strutturata
per il lavoro dell'esperto. Non sostituisce il giudizio complessivo di
conformità, che comprende anche aspetti organizzativi, giuridici e di rischio.

## Avvio minimo

Richiede Python 3.12 o successivo e un'istanza Neo4j configurata.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
docker compose up -d neo4j
nis2-assessor assess \
  --input data/normalized_environment.example.yaml \
  --rules data/technical_rules.example.yaml \
  --requirements data/nis2_requirements.example.yaml \
  --output-dir reports
```

Per conoscere comandi e opzioni disponibili:

```bash
nis2-assessor --help
```

## Scenari disponibili

I tre scenari end-to-end rappresentano organizzazioni interamente sintetiche e
servono a esercitare circostanze differenti, non casi aziendali o normativi
reali:

- **Aurora** (`essential`): condizioni prevalentemente soddisfatte;
- **Tirrena** (`important`): combinazione di esiti soddisfatti, non soddisfatti
  e non verificabili;
- **Delta** (`essential`): criticità tecniche, lacune informative e revisioni
  manuali di governance.

Gli eventuali CVE reali presenti nei file sono associati a prodotti e
organizzazioni inventati esclusivamente a fini dimostrativi.

## Percorso di lettura

1. [Metodologia di valutazione](docs/metodologia-di-valutazione.md) — processo
   decisionale, semantica degli esiti e tracciabilità.
2. [Validazione sperimentale](docs/validazione-sperimentale.md) — base
   sperimentale, scenari e confronto atteso-effettivo.
3. [Analisi critica e sviluppi futuri](docs/analisi-critica-e-sviluppi-futuri.md)
   — limiti, posizionamento del progetto e automazione potenziale.
4. [Indice della documentazione](docs/README.md) — responsabilità e ordine di
   consultazione dei documenti specialistici.
