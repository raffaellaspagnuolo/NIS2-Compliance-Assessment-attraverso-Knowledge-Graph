# Validazione sperimentale

Questo documento descrive il disegno della validazione, la composizione dei
casi, gli esiti attesi e quelli prodotti. La sperimentazione non è presentata
soltanto come collaudo del software: serve a verificare se le scelte centrali
della metodologia producono decisioni coerenti, distinguibili e ricostruibili.

## 1. Disegno della validazione

La sperimentazione distingue due livelli complementari.

La **verifica dell'implementazione** controlla che il software rispetti i
contratti dichiarati: validazione degli input, riferimenti, funzioni degli
evaluator, applicabilità tri-state, semantica degli stati, serializzazione,
persistenza nel grafo, aggregazione, reporting, API/CLI, integrazione Neo4j,
determinismo e regressioni.

La **validazione dell'approccio** usa casi con oracle separati e scenari
end-to-end per verificare, entro il perimetro del prototipo, che le decisioni
siano coerenti con le circostanze costruite: profili diversi, asset inclusi ed
esclusi, valori veri, falsi, sconosciuti o contrastanti, collezioni multiple,
evidenze valide, mancanti, scadute o associate in modo errato, deroghe e rischi
accettati.

In particolare, la validazione cerca risposta a quattro domande. Verifica se
applicabilità e verificabilità restano separate; se una violazione certa non
viene attenuata dalla presenza di altre lacune; se evidenze e governance
influenzano l'esito soltanto secondo i criteri dichiarati; e se, a conclusione
dell'assessment, è possibile ricostruire il percorso dai fatti al risultato.

Questa seconda attività non è una validazione esterna. Organizzazioni, persone,
asset e prodotti sono inventati e non rappresentano organizzazioni reali, casi
aziendali reali o casi d'uso normativi. Gli eventuali CVE reali restano
associati a prodotti sintetici soltanto a fini dimostrativi.

## 2. Composizione della base sperimentale

La base combina granularità diverse per evitare che un solo tipo di verifica venga
assunto come prova dell'intero approccio. I casi normativi isolano le attese
minime di ciascuna regola; la PoC esercita varianti positive, negative,
incomplete e di governance; gli scenari end-to-end osservano le interazioni tra
profilo, asset, inventari, evidenze e aggregazione.

La base corrente comprende 52 casi normativi indipendenti, due per ciascuna
delle 26 regole. Il file `data/normative_cases.yaml` dichiara input, asset,
regola ed esito atteso senza leggere evaluator, parametri o selector. A questi
si aggiungono 93 coppie asset-controllo della Proof of Concept. Gli input sono
contenuti in `data/poc/cases.yaml`, mentre gli esiti attesi tecnici e di
governance sono conservati separatamente in `data/poc/ground_truth.yaml` e
vengono caricati dopo l'esecuzione.

Il livello end-to-end comprende tre organizzazioni sintetiche, ciascuna con due
asset e 26 regole. L'oracle dell'asset principale è registrato in
`data/validation/scenario_results.yaml`; gli esiti complessivi prodotti sono
conservati nei report degli scenari. La verifica effettuata prima della
consegna ha inoltre controllato contratti, semantica degli stati, regressioni,
integrazione e riproducibilità degli artefatti.

I 93 casi PoC coprono tutte le regole e includono 29 oracle `compliant`, 29
`non_compliant`, 26 `not_verifiable` e 9 `not_applicable`; quattro casi
esercitano combinazioni conservative e due casi separano esito tecnico e
revisione di governance. La PoC costruisce una micro-organizzazione sintetica
per ogni caso e invoca la pipeline generale una volta: non usa un secondo
motore.

I 52 casi normativi riutilizzano circostanze degli scenari ma fissano
esplicitamente due aspettative per ogni regola. La separazione tra dati di
validazione e codice del motore evita che gli oracle dipendano
dall'implementazione valutata.

## 3. Scenari end-to-end

Ogni file in `data/scenarios/` contiene un ambiente già normalizzato che emula
l'input richiesto al prototipo. La dicitura interna “output dei moduli 1 e 2”
descrive il confine del contratto, non moduli presenti nel repository: la
raccolta e la normalizzazione non sono implementate.

Ogni scenario contiene un asset principale NIS rilevante e un asset ausiliario
con rilevanza NIS nota e negativa. La pipeline valuta tutte le 52 coppie
asset-regola; le 26 coppie dell'asset ausiliario sono escluse con motivo
tracciato. In Tirrena altre nove coppie dell'asset principale sono escluse
perché le regole con suffisso `-E` non appartengono al profilo `important`.

### 3.1 Aurora: condizioni prevalentemente soddisfatte

- **Obiettivo:** osservare un profilo `essential` con elevata maturità tecnica e
  una lacuna di perimetro che non deve essere scambiata per assenza certa.
- **Organizzazione sintetica:** Aurora Salute S.p.A.; asset principale `Core
  Clinical Gateway` e asset ausiliario fuori perimetro NIS.
- **Configurazione:** proprietà tecniche prevalentemente positive, evidenze
  correnti e una vulnerabilità dimostrativa associata a `CVE-2023-44487` nello
  stack sintetico AuroraGateway.
- **Circostanza discriminante:** la completezza dell'inventario `DataObject`
  non è nota; `CTRL-PR-DS-01` non può stabilire il perimetro dei supporti
  rimovibili.
- **Atteso:** 25 `compliant`, 1 `not_verifiable`, 26 `not_applicable`, nessuna
  revisione manuale.
- **Prodotto:** coincide con l'atteso; copertura informativa 25/26 (`0.9615`).
- **Interpretazione:** un ambiente quasi interamente positivo non viene
  dichiarato completamente verificato quando manca la conoscenza del
  perimetro di un controllo.

### 3.2 Tirrena: esiti misti e differenza di profilo

- **Obiettivo:** esercitare nello stesso ambiente fatti soddisfatti, violazioni
  certe, una lacuna informativa e l'esclusione delle regole del profilo
  `essential`.
- **Organizzazione sintetica:** Logistica Tirrena S.r.l., profilo `important`;
  asset principale `Logistics Application Server` e asset ausiliario fuori
  perimetro NIS.
- **Configurazione:** inventari di base presenti, controlli tecnici eterogenei,
  vulnerabilità dimostrativa `CVE-2021-41773` associata al prodotto sintetico
  TirrenaPortal.
- **Circostanze:** nove regole `-E` non sono applicabili all'asset principale;
  sette controlli presentano violazioni certe e l'inventario `DataObject` resta
  non determinato per `CTRL-PR-DS-01`.
- **Atteso:** 9 `compliant`, 7 `non_compliant`, 1 `not_verifiable` tra i 17
  controlli applicabili e 35 `not_applicable` complessivi; nessuna revisione.
- **Prodotto:** coincide con l'atteso; copertura informativa 16/17 (`0.9412`).
- **Interpretazione:** il profilo delimita l'applicabilità prima della
  verificabilità e falsità note e lacune non sono aggregate nello stesso stato.

### 3.3 Delta: criticità, lacune e governance

- **Obiettivo:** verificare la conservazione delle violazioni in presenza di
  lacune e la separazione tra decisione tecnica e revisione umana.
- **Organizzazione sintetica:** Manifattura Delta S.p.A., profilo `essential`;
  asset principale `Production Integration Server` e asset ausiliario fuori
  perimetro NIS.
- **Configurazione:** proprietà tecniche negative, dati non raccolti o non
  dichiarati, vulnerabilità dimostrativa `CVE-2021-44228` associata al prodotto
  sintetico DeltaIntegrator, rischio accettato e deroga di hardening.
- **Circostanze:** 20 regole hanno almeno una violazione certa; cinque non hanno
  informazioni sufficienti; `RULE-ID-RA-08` conserva una violazione insieme a
  una lacuna e a un rischio accettato; `RULE-PR-PS-01-E` ha una deroga attiva.
- **Atteso:** 1 `compliant`, 20 `non_compliant`, 5 `not_verifiable`, 26
  `not_applicable` e 2 revisioni manuali.
- **Prodotto:** coincide con l'atteso; copertura informativa 21/26 (`0.8077`).
- **Interpretazione:** lacune e governance non attenuano una violazione tecnica
  certa, ma restano disponibili nella traccia per l'analisi umana.

## 4. Confronto tra esiti attesi ed effettivi

Gli attesi tecnici per l'asset principale provengono da
`data/validation/scenario_results.yaml`; profilo, rilevanza NIS ed esclusione dei
26 risultati dell'asset ausiliario sono vincoli espliciti degli input in
`data/scenarios/` e dell'oracle. Gli effettivi sono le sintesi prodotte dalla
pipeline e preservate nei tre report principali in `reports/scenarios/`. L'oracle
tecnico non viene ricavato a posteriori dal report e non è contenuto negli
input degli scenari.

Per la governance degli scenari non esiste invece un campo oracle separato nel
file degli oracle: l'atteso di Delta deriva dalle due circostanze dichiarate nello
scenario — rischio accettato su `RULE-ID-RA-08` e deroga attiva su
`RULE-PR-PS-01-E` — mentre il report prodotto contiene due revisioni. Questa è
una copertura sperimentale meno indipendente dell'oracle tecnico ed è trattata
come limite della matrice, non come risultato dedotto retroattivamente dal
motore.

Per Aurora erano attesi 26 controlli applicabili: 25 soddisfatti e uno non
verificabile. Gli altri 26 risultati, riferiti all'asset ausiliario, dovevano
essere non applicabili. Il sistema ha prodotto esattamente questi conteggi e
non ha richiesto revisioni manuali.

Per Tirrena erano attesi 17 controlli applicabili, dei quali nove soddisfatti,
sette non soddisfatti e uno non verificabile. I 35 risultati restanti dovevano
essere non applicabili per effetto del profilo e dell'esclusione dell'asset
ausiliario. Anche in questo scenario gli esiti prodotti coincidono con quelli
attesi e non risultano revisioni manuali.

Per Delta erano attesi 26 controlli applicabili: uno soddisfatto, 20 non
soddisfatti e cinque non verificabili. Gli altri 26 risultati dovevano essere
non applicabili. Le due circostanze di governance dovevano inoltre generare due
revisioni manuali. Il sistema ha riprodotto tutti i conteggi previsti.

“Applicabili” esclude i risultati `not_applicable`; i conteggi delle altre
colonne riguardano tutte le coppie asset-controllo prodotte. Ogni scenario
genera 52 risultati e tre artefatti. Nessuno emette `partially_compliant`.

## 5. Riproduzione

PoC isolata:

```bash
nis2-assessor test-poc \
  --cases data/poc/cases.yaml \
  --ground-truth data/poc/ground_truth.yaml \
  --output-dir reports/poc
```

Esecuzione interattiva degli scenari con la normale CLI:

```bash
nis2-assessor assess --input data/scenarios/normalized_environment_01_aurora_essential_mature.yaml --rules data/technical_rules.example.yaml --requirements data/nis2_requirements.example.yaml --output-dir reports/scenarios
nis2-assessor assess --input data/scenarios/normalized_environment_02_tirrena_important_mixed.yaml --rules data/technical_rules.example.yaml --requirements data/nis2_requirements.example.yaml --output-dir reports/scenarios
nis2-assessor assess --input data/scenarios/normalized_environment_03_delta_essential_critical.yaml --rules data/technical_rules.example.yaml --requirements data/nis2_requirements.example.yaml --output-dir reports/scenarios
```

La CLI genera un nuovo ID. Gli artefatti di riferimento conservati in
`reports/scenarios/` sono stati prodotti con clock fisso
`2026-08-15T10:00:00Z`, repository in memoria e ID stabili, quindi possono
essere confrontati byte per byte.

## 6. Discussione dei risultati

Nel perimetro considerato, la sperimentazione verifica la separazione tra
applicabilità e verificabilità, il trattamento distinto di valori falsi e
sconosciuti, la conservazione delle violazioni in presenza di lacune, la
gestione di più entità, il filtro delle evidenze, la separazione tra stato
tecnico e governance, la ricostruibilità della decisione e la stabilità dei
risultati sugli scenari definiti.

La corrispondenza osservata mostra che l'implementazione riproduce gli oracle
della base sperimentale e che le circostanze selezionate sono trattate secondo
la metodologia codificata. I tre scenari forniscono inoltre evidenza
complementare: Aurora mostra che un quadro quasi positivo non nasconde una
lacuna; Tirrena dimostra che profilo, violazione e informazione mancante restano
distinti; Delta mostra che una decisione tecnica sfavorevole può convivere con
informazioni incomplete e con una revisione di governance senza essere
riscritta.

Entro il perimetro dichiarato, i risultati sostengono quindi la validità
interna dell'approccio: non soltanto il codice funziona rispetto ai propri
contratti, ma le principali scelte metodologiche sono osservabili negli esiti e
nella traccia. Questo risultato è positivo, pur non costituendo ancora una
prova di efficacia generale in contesti reali. La base è sintetica, il
perimetro normativo è ristretto e manca una validazione esterna su dati
operativi indipendenti. Un passo successivo potrà confrontare le valutazioni
del sistema con quelle di esperti su casi reali anonimizzati e misurare anche
tempi, accordo tra valutatori e utilità della traccia decisionale.
