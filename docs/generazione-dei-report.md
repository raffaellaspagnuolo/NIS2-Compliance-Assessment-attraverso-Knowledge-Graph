# Generazione e funzione dei report

Il report è l'ultimo passaggio della pipeline e traduce risultati strutturati in
una forma leggibile da destinatari diversi. Il renderer non valuta i controlli,
non ricalcola confidence, priorità o copertura e non modifica le decisioni del
motore. Questa separazione è essenziale: consente di migliorare il linguaggio
senza alterare il significato tecnico dell'assessment.

## Metadati

Il contesto strutturato espone profilo ACN, catalogo delle regole, criteri di
gestione delle evidenze e della priorità, identificativi dell'assessment e data
di esecuzione. Tali metadati permettono di ricondurre il testo all'elaborazione
che lo ha prodotto.

## Corpo principale

Il documento principale apre con l'identificazione dello scenario e con una
sintesi che chiarisce immediatamente quanti controlli risultano soddisfatti,
non soddisfatti, non verificabili e non applicabili. La lettura prosegue per
asset e per esito. I controlli problematici sono presentati per primi,
indicando che cosa è stato osservato, perché la condizione non è soddisfatta o
non può essere verificata e quale informazione o azione è necessaria. Seguono i
controlli soddisfatti e quelli non applicabili, raggruppati in modo da evitare
ripetizioni. Le eventuali revisioni di governance restano visivamente separate
dall'esito tecnico. Il documento si chiude con le priorità operative e con il
perimetro entro il quale i risultati devono essere interpretati.

Ogni controllo è descritto con un paragrafo autonomo e discorsivo. Le condizioni
e i valori interni sono tradotti in espressioni comprensibili, mentre gli
identificativi necessari alla verifica restano disponibili nell'allegato. Le
sezioni prive di contenuto non vengono mostrate: il report racconta lo scenario
effettivamente valutato e non presenta casi ipotetici.

Le tabelle sono limitate alla sintesi numerica e alla priorità degli interventi.
Le sezioni dedicate ai controlli non contengono JSON o decision trace, perché
questi elementi interromperebbero il flusso della spiegazione.

## Allegato tecnico

- tracciabilità tra risultati, controlli, regole e requisiti;
- condizioni, valori richiesti e osservati e policy decisionali;
- cataloghi completi delle evidenze e della provenienza;
- evidenze scartate e ragioni di non applicabilità;
- decision trace e fatti valutati in forma raw.

Le strutture interne non sono eliminate: vengono separate dal flusso narrativo
per conciliare leggibilità e auditabilità. Il lettore può quindi partire dalla
sintesi e approfondire ogni affermazione fino ai fatti e alle fonti che la
sostengono.

Il terzo artefatto è lo snapshot completo del medesimo Knowledge Graph
consultato dal motore, acquisito dopo l'inserimento dei risultati e delle
relazioni di tracciabilità. La vista comprende anche asset fuori perimetro,
evidenze, provenienze, requisiti, controlli e regole. Il contesto strutturato
resta la fonte autoritativa per elaborazioni successive.

## Possibile uso dell'intelligenza artificiale

L'automazione del reporting può evolvere oltre i template deterministici. Un
LLM potrebbe produrre sintesi più naturali, adattare il livello di dettaglio al
destinatario e ridurre le ripetizioni nei report estesi. Il modello dovrebbe
però operare soltanto sui risultati strutturati già determinati, senza creare
evidenze, cambiare stati o formulare autonomamente un giudizio normativo.

Per preservare la tracciabilità, ogni testo generato dovrebbe essere verificato
rispetto all'output sorgente, mantenere i riferimenti ai risultati descritti ed
essere affiancato dal renderer deterministico. Prompt, configurazione, output e
revisione umana dovrebbero inoltre essere conservati. In questa configurazione
l'intelligenza artificiale amplia l'automazione della presentazione, mentre il
motore a regole rimane responsabile della decisione tecnica riproducibile.
