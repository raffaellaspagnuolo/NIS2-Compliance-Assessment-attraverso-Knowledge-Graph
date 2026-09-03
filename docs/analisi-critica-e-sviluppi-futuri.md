# Analisi critica e sviluppi futuri

## 1. Criterio e finalità dell'analisi

Il prototipo copre una parte delimitata del processo di compliance tecnica: usa
un ambiente già normalizzato, applica 26 regole codificate e conserva gli
elementi necessari a ricostruire ogni decisione. L'analisi distingue pertanto
quattro piani che non devono essere sovrapposti: ciò che il software automatizza
oggi, ciò che richiederebbe nuova implementazione, ciò che rimane una decisione
umana e ciò che la base sperimentale consente effettivamente di sostenere.

L'analisi critica non ridimensiona il contributo realizzato: serve a indicare
con precisione dove il prototipo è già solido e dove il metodo può essere
esteso. Questa distinzione evita due conclusioni improprie. La
prima consiste nell'equiparare l'esecuzione corretta di una regola tecnica a un
giudizio complessivo di conformità. La seconda consiste nel considerare ogni
attività oggi manuale come automaticamente delegabile a un algoritmo. Una parte
del lavoro è manuale per mancanza di integrazioni; un'altra lo è perché contiene
scelte normative, organizzative o discrezionali non riducibili ai fatti tecnici
codificati.

## 2. Automazione implementata

Nel progetto il termine *automazione* indica anzitutto l'esecuzione
riproducibile di attività prima svolte manualmente: validazione dei dati,
selezione del perimetro, applicazione delle regole, trattamento delle evidenze,
aggregazione e reporting. Non significa semplicemente che il software “fa da
solo” un'operazione, ma che criteri, input e passaggi sono resi espliciti,
controllabili e ripetibili.

Il punto di ingresso è un `NormalizedEnvironment` già costruito. Acquisizione
da fonti operative e normalizzazione non sono implementate: la pipeline non
interroga scanner, CMDB, IAM, sistemi di ticketing o piattaforme di
monitoraggio e non estrae informazioni da documenti non strutturati.

Entro questo confine, il prototipo automatizza realmente:

- la validazione formale e semantica dell'ambiente normalizzato, compresi
  schema strict, timestamp, unicità, riferimenti e allineamento tra requisito,
  controllo e regola;
- il popolamento del Knowledge Graph con entità, relazioni, regole e, dopo la
  valutazione, risultati;
- la selezione delle regole rispetto al profilo e agli asset rappresentati;
- la determinazione tri-state dell'applicabilità sulle sole condizioni
  codificate;
- la selezione delle entità e la valutazione dei fatti tecnici presenti nel
  grafo;
- l'ammissione formale delle evidenze in base a tipo, associazione, validità,
  fonte e provenienza;
- l'aggregazione deterministica delle condizioni e degli esiti per entità;
- la conservazione della traccia decisionale, comprese violazioni, lacune,
  conflitti ed evidenze scartate;
- il calcolo di confidence categoriale, copertura informativa e priorità
  operativa non normativa;
- la generazione deterministica del report principale, dell'allegato tecnico e
  dello snapshot del grafo.

Il Knowledge Graph è una rappresentazione interrogabile del contesto e un
supporto alla tracciabilità. Non attribuisce autonomamente applicabilità o
stati: tali decisioni appartengono al motore delle regole. Analogamente, i
renderer presentano risultati già determinati e non possono correggerli,
completarli o rivalutarli.

Questa impostazione offre riproducibilità e separazione delle responsabilità,
ma trasferisce a monte una dipendenza rilevante: il sistema può valutare solo
ciò che l'ambiente normalizzato rappresenta in modo sufficientemente completo,
attuale e correttamente associato.

Il risultato più significativo è la combinazione di tre proprietà. La prima è
la distinzione tra non applicabilità, informazione insufficiente e violazione
certa. La seconda è la separazione tra stato tecnico e decisione di governance.
La terza è la possibilità di risalire dall'esito alla regola, ai fatti, alle
evidenze e alla loro provenienza. Considerate insieme, queste proprietà rendono
il prototipo più utile di un semplice insieme di controlli booleani: il sistema
produce una base argomentata per la revisione dell'esperto.

## 3. Automazione potenziale, anche mediante intelligenza artificiale

L'automazione futura comprende due famiglie complementari. La prima estende le
integrazioni e le regole deterministiche, per esempio con connettori verso CMDB,
scanner, IAM e sistemi di ticketing. La seconda introduce tecniche di
intelligenza artificiale per attività nelle quali il linguaggio o l'eterogeneità
dei dati rendono insufficienti trasformazioni rigide: estrazione da documenti,
classificazione assistita delle evidenze, interrogazione in linguaggio naturale
e generazione del report. L'IA è quindi una forma effettiva di automazione, ma
non autorizza a rendere opache o non verificabili le decisioni.

Le estensioni seguenti sono possibilità progettuali, non funzionalità presenti.
Una prima direzione riguarda l'acquisizione. Connettori verso scanner, CMDB,
sistemi IAM, piattaforme di monitoraggio e sistemi di ticketing potrebbero
raccogliere inventari, configurazioni, identità, vulnerabilità e interventi
senza richiedere la preparazione manuale dell'intero input. Resterebbe
necessario confermare il perimetro, controllare la copertura delle sorgenti e
verificare che i record siano associati all'asset corretto. Per non perdere
tracciabilità, ogni dato dovrebbe conservare la sorgente, il momento della
raccolta, il connettore utilizzato e il valore originale.

La normalizzazione potrebbe essere in parte automatizzata mediante mapping e
trasformazioni verso il contratto del `NormalizedEnvironment`. I casi ambigui
richiederebbero comunque approvazione, perché campi simili provenienti da
sistemi diversi possono avere significati differenti. La traccia dovrebbe
quindi riportare il campo sorgente, la trasformazione applicata, il valore
normalizzato e gli eventuali errori.

L'intelligenza artificiale potrebbe intervenire soprattutto quando le
informazioni non sono già strutturate. Tecniche di estrazione del testo
potrebbero individuare entità, date, responsabilità e misure all'interno di
politiche, procedure o contratti. Modelli di classificazione potrebbero
proporre il tipo di evidenza e il collegamento con asset e controlli. Queste
funzioni ridurrebbero il lavoro preparatorio, ma non dimostrerebbero da sole la
qualità sostanziale del documento o la correttezza del collegamento. Ogni
informazione estratta dovrebbe rimanere associata al passaggio del documento
da cui proviene e alla successiva conferma del revisore.

Un ulteriore livello di assistenza potrebbe individuare lacune e conflitti tra
fonti oppure suggerire azioni correttive a partire da violazioni, dipendenze e
criticità. In questi casi il sistema dovrebbe formulare una proposta, non
eseguire modifiche implicite. La scelta dell'intervento, la valutazione degli
effetti collaterali e l'accettazione del rischio rimarrebbero responsabilità
umane registrate nella traccia.

L'IA potrebbe anche sostenere la manutenzione del catalogo, segnalando
variazioni nei riferimenti normativi o proponendo corrispondenze e bozze di
regole. L'interpretazione del requisito, il test della regola e la sua
approvazione non possono però essere dedotti dalla sola proposta. Lo stesso
principio vale per l'interrogazione del Knowledge Graph in linguaggio naturale:
la traduzione della domanda in una query di sola lettura faciliterebbe
l'esplorazione, ma domanda, query generata e risultati dovrebbero essere
conservati e verificati quando sostengono una decisione.

Il confronto tra assessment successivi potrebbe infine rendere visibili
variazioni di asset, evidenze ed esiti. La comparazione avrebbe significato
soltanto a parità, o previa esplicita riconciliazione, di perimetro, regole,
policy e qualità delle fonti. Un cambiamento del risultato non dovrebbe essere
attribuito automaticamente a un miglioramento o a un peggioramento tecnico.

L'automazione a monte aumenterebbe la tempestività, ma allargherebbe anche la
superficie di errore. Il dato non sarebbe più soltanto validato: verrebbe
selezionato, trasformato e associato da nuovi componenti. Per questo motivo la
provenienza dovrebbe coprire l'intera catena di acquisizione e non limitarsi
alla fonte finale registrata nell'ambiente normalizzato.

## 4. Uso controllato di un LLM nella generazione del report

### 4.1 Scelta attuale

Il sistema attuale genera i report mediante template deterministici. Questa
scelta consente di ottenere lo stesso testo a parità di input, mantenere stabile
la struttura, controllare quali contenuti possono comparire e collegare ogni
frase a campi già presenti nel risultato. Riduce inoltre il rischio che la
narrazione introduca informazioni non osservate o attenui condizioni
sfavorevoli. La rigidità espressiva è quindi il costo di una proprietà utile per
audit, test di regressione e riproducibilità.

### 4.2 Estensione possibile

Un LLM potrebbe essere aggiunto soltanto come livello di presentazione posto
dopo il motore decisionale. Riceverebbe risultati, fatti, evidenze e
identificativi della traccia già determinati e potrebbe produrre una spiegazione
più naturale, una sintesi di assessment estesi o testi differenziati per un
destinatario tecnico e uno direzionale.

Il modello non dovrebbe stabilire l'applicabilità, modificare lo stato tecnico
o di governance, interpretare autonomamente la norma, creare evidenze, proporre
come certe azioni non presenti nell'output o nascondere lacune e conflitti. Il
testo dovrebbe mantenere riferimenti espliciti a risultati, controlli, fatti ed
evidenze, così da poter essere verificato rispetto alla fonte strutturata.

I vantaggi attesi sarebbero maggiore naturalezza, adattamento al destinatario,
sintesi di insiemi ampi di risultati e minore rigidità dei template. Non ne
discende automaticamente un miglioramento del sistema: la qualità narrativa
dovrebbe essere validata separatamente dalla correttezza del motore.

### 4.3 Rischi e misure di controllo

I rischi principali sono allucinazioni, omissione di condizioni sfavorevoli,
variazioni tra esecuzioni, perdita del collegamento con la decisione, esposizione
di dati sensibili, difficoltà di audit e introduzione di interpretazioni
normative non autorizzate.

Un impiego sperimentale richiederebbe almeno:

- generazione vincolata ai soli campi strutturati ammessi;
- configurazione stabile, con temperatura nulla quando disponibile;
- citazione obbligatoria degli identificativi della traccia;
- validazione automatica tra affermazioni generate e risultato strutturato;
- confronto con il renderer deterministico per rilevare omissioni o divergenze;
- revisione umana prima dell'uso esterno;
- conservazione di prompt, configurazione, output e risultato sorgente;
- permanenza dell'output strutturato come fonte autoritativa.

Anche con questi controlli, il testo generato non dovrebbe diventare l'unico
artefatto disponibile né essere riutilizzato dal motore come evidenza della
decisione che sta narrando.

## 5. Posizionamento del progetto e possibilità di sviluppo

Le soluzioni che trattano la conformità con ontologie, Knowledge Graph e regole
automatiche tendono a concentrarsi su parti diverse del processo. Alcune
rappresentano requisiti e controlli in forma strutturata; altre collegano le
prescrizioni a strumenti tecnici; altre ancora integrano inventari,
vulnerabilità, dipendenze ed evidenze provenienti dall'ambiente operativo.
Esistono inoltre approcci che usano tecniche di intelligenza artificiale per
estrarre informazioni dai testi, suggerire corrispondenze tra requisiti o
rendere più semplice l'interrogazione dei dati. Nessuna di queste attività,
presa isolatamente, copre l'intero assessment.

Il prototipo si colloca nella parte che collega un insieme delimitato di
requisiti e controlli a fatti osservabili nell'ambiente tecnico. I requisiti e
le 26 regole sono già codificati; l'ambiente è ricevuto in forma normalizzata;
il Knowledge Graph organizza asset, componenti, relazioni ed evidenze; il motore
applica condizioni deterministiche e conserva la spiegazione dell'esito. Il
progetto non estrae autonomamente le regole dalla norma e non acquisisce
direttamente i dati dagli strumenti operativi.

Il contributo consiste nell'aver riunito questi elementi in una pipeline
coerente. La valutazione non si ferma alla presenza di una configurazione, ma
mantiene il legame tra organizzazione, asset, controllo, requisito, regola,
fatti, evidenze e provenienza. Conserva inoltre le informazioni mancanti, le
fonti contrastanti e le decisioni di governance senza confonderle con lo stato
tecnico. Il risultato può quindi essere controllato e discusso da un revisore,
anziché essere presentato come una classificazione priva di spiegazione.

Questa scelta lascia aperte alcune parti del processo. L'acquisizione continua
da sorgenti aziendali permetterebbe di aggiornare il grafo al variare
dell'ambiente. L'estrazione assistita potrebbe ridurre il lavoro necessario per
trattare documenti ed evidenze non strutturate. Strumenti di supporto potrebbero
proporre collegamenti tra requisiti, regole e fonti tecniche oppure segnalare
quando un aggiornamento normativo richiede una revisione del catalogo. Formati
strutturati condivisi faciliterebbero lo scambio dei risultati con altri
strumenti di assessment.

L'introduzione di queste funzioni non cambia il criterio di fondo del progetto:
ogni trasformazione o proposta dovrebbe restare verificabile e distinguibile
dalla decisione approvata. L'intelligenza artificiale può assistere
l'acquisizione, la classificazione, il collegamento e la presentazione delle
informazioni, ma non dovrebbe rendere implicito il passaggio dal testo
normativo alla regola eseguibile o dal dato raccolto al giudizio di conformità.

## 6. Attività che richiedono valutazione umana

Nel sistema corrente la scelta e la conferma del perimetro organizzativo
richiedono conoscenza di processi, responsabilità e confini che non deriva dai
soli attributi tecnici. L'interpretazione complessiva della norma e la
valutazione sostanziale di politiche, procedure e contratti richiedono inoltre
lettura giuridica e organizzativa: presenza, data e provenienza di un documento
non ne dimostrano adeguatezza o applicazione effettiva.

Anche il giudizio di adeguatezza delle misure rispetto al rischio, l'approvazione
delle deroghe, la valutazione delle misure compensative e l'accettazione del
rischio residuo contengono bilanciamenti tra impatto, obiettivi, risorse e
responsabilità. Il prototipo può presentare fatti e segnalare la necessità di
revisione, ma non possiede l'autorità né il contesto per assumere tali decisioni.

Devono rimanere umane anche la risoluzione dei conflitti che le policy non
determinano, la validazione di regole generate o aggiornate automaticamente e la
formulazione di un giudizio complessivo di conformità. In questi casi
l'operatore non compensa soltanto una mancanza tecnica: esercita una funzione
normativa, organizzativa o discrezionale che deve essere motivata e attribuita a
un responsabile identificabile.

L'obiettivo dell'automazione è quindi preparare una base informativa più
coerente e verificabile per il giudizio umano, non eliminare la responsabilità
dell'esperto.

## 7. Limiti

### 7.1 Limiti metodologici

La metodologia assume disponibile un ambiente normalizzato e dipende dalla sua
qualità. Una rappresentazione incompleta, non aggiornata o semanticamente errata
limita la valutazione anche se la pipeline opera correttamente. Le regole devono
essere mantenute al variare delle fonti normative e delle baseline; il loro
carattere deterministico rende l'esito riproducibile, ma non garantisce che la
formalizzazione sia completa o sostanzialmente adeguata.

Il perimetro è limitato a 26 regole, prevalentemente riferite a condizioni
tecnicamente osservabili. Dieci regole hanno copertura parziale e alcuni
controlli sulle evidenze riguardano forma, validità e associazione, non la
qualità sostanziale della misura. I requisiti organizzativi, l'interpretazione
complessiva e il giudizio rispetto al rischio restano fuori dalla decisione
automatica. Gli esiti non possono quindi essere interpretati come
certificazione NIS2.

### 7.2 Limiti della base sperimentale

La sperimentazione utilizza scenari sintetici e casi isolati costruiti per il
perimetro selezionato. Non comprende deployment presso organizzazioni reali,
una validazione esterna o dati operativi indipendenti. Gli oracle verificano le
circostanze definite e la corrispondenza atteso-effettivo, ma non dimostrano
efficacia generale in contesti differenti.

La prevalenza di condizioni tecnicamente osservabili e la copertura parziale di
alcune misure limitano inoltre la varietà delle decisioni esercitate. Prima di
generalizzare i risultati sarebbero necessari dati reali controllati, revisori
indipendenti, confronto con processi di assessment esistenti, analisi degli
errori di acquisizione e normalizzazione e valutazioni longitudinali. Anche una
futura generazione del report mediante LLM richiederebbe un protocollo separato
per misurare fedeltà, omissioni, stabilità e auditabilità del testo.

## 8. Valutazione complessiva e direzione di sviluppo

Lo sviluppo più coerente non consiste nell'aumentare indiscriminatamente il
numero di decisioni automatiche, ma nell'estendere in modo controllato la catena
informativa. Acquisizione, normalizzazione, integrazione delle sorgenti,
revisione delle evidenze e presentazione possono essere assistite, purché ogni
passaggio lasci una traccia verificabile e non trasformi un'incertezza in una
conclusione implicita.

Il nucleo deterministico può quindi restare la fonte autoritativa degli esiti
tecnici, mentre nuovi componenti migliorano tempestività, copertura e
leggibilità. La valutazione umana rimane necessaria dove il problema riguarda
interpretazione normativa, adeguatezza sostanziale, deroghe e rischio residuo.
