# Report di valutazione tecnica — Aurora Salute S.p.A.

## 1. Scenario

La valutazione dello scenario `scenario-aurora-essential-mature` riguarda Aurora Salute S.p.A., con profilo ACN **essenziale**, alla data del 15 agosto 2026. Sono stati osservati 2 asset; un asset è rilevante per il perimetro NIS.


## 2. Sintesi della valutazione

Sono applicabili 26 controlli: 25 risultano soddisfatti, nessuno risulta non soddisfatto e uno non è verificabile. 26 valutazioni non sono applicabili; nessun risultato richiede una revisione manuale di governance.

I controlli soddisfatti riguardano la gestione degli asset, la sicurezza tecnica dei fornitori, la gestione delle vulnerabilità, il controllo degli accessi, la sicurezza fisica, la crittografia, il backup e il ripristino, system security, la gestione degli aggiornamenti, il logging e il monitoraggio, la sicurezza di rete, emergency communications, il monitoraggio di sicurezza e la sicurezza degli endpoint. Gli scostamenti e le lacune informative interessano soprattutto la protezione dei dati.

Il problema complessivamente più urgente riguarda la protezione dei dati a riposo di Core Clinical Gateway, per cui occorre completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura.

| Esito | Numero |
| --- | ---: |
| Soddisfatti | 25 |
| Non soddisfatti | 0 |
| Non verificabili | 1 |
| Non applicabili | 26 |
| Revisione manuale | 0 |

I conteggi si riferiscono alle valutazioni asset-controllo e non rappresentano una percentuale complessiva di conformità NIS2.


## 3. Analisi per asset

### Core Clinical Gateway (`asset-aurora-core`)

Per Core Clinical Gateway sono applicabili 26 controlli: 25 sono soddisfatti, nessuno risulta non soddisfatto e uno non è verificabile. Nell'ordine operativo, i primi problemi riguardano la protezione dei dati a riposo.

### Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`)

L'asset è escluso dalla valutazione tecnica perché la sua rilevanza NIS è conosciuta e negativa.


## 4. Controlli non verificabili

### Protezione dei dati a riposo (`CTRL-PR-DS-01`) — Core Clinical Gateway

Il controllo verifica la cifratura dei supporti rimovibili censiti per l'asset. Non è nota la completezza dell'inventario dei dati e dei supporti rimovibili; senza questa informazione non è possibile stabilire se tutti gli elementi da proteggere siano stati considerati. Finché la lacuna permane, il controllo non è verificabile. Occorre completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura.


## 5. Controlli soddisfatti

### Inventario hardware (`CTRL-ID-AM-01`) — Core Clinical Gateway

L'inventario hardware dell'asset risulta completo sulla base dei dati acquisiti dalla CMDB; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Inventario software e servizi (`CTRL-ID-AM-02`) — Core Clinical Gateway

L'asset, i servizi e i componenti software richiesti risultano censiti e autorizzati sulla base dei dati acquisiti dalla CMDB; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) — Core Clinical Gateway

I flussi di rete pertinenti risultano censiti e autorizzati sulla base dei dati acquisiti dal gestore della rete; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Servizi dei fornitori (`CTRL-ID-AM-04`) — Core Clinical Gateway

I servizi erogati da fornitori risultano censiti nell'inventario tecnico sulla base dei dati acquisiti dal catalogo aziendale. Il controllo è soddisfatto limitatamente alla presenza dell'inventario strutturato dei servizi erogati da fornitori, mentre non valuta l'aggiornamento sostanziale e la completezza dei rapporti di fornitura.

### Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) — Core Clinical Gateway

Le fonti informative pertinenti alle vulnerabilità risultano monitorate sulla base dei dati acquisiti dal gestore delle vulnerabilità. Il controllo è soddisfatto limitatamente all'uso dichiarato dei canali monitorati per identificare vulnerabilità, mentre non valuta la completezza sostanziale dell'identificazione su ogni tecnologia.

### Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) — Core Clinical Gateway

Risultano svolte le attività aggiuntive di valutazione delle vulnerabilità sulla base dei dati acquisiti dallo scanner delle vulnerabilità. Il controllo è soddisfatto limitatamente alla presenza, alla freschezza e alla struttura della relazione di valutazione delle vulnerabilità, mentre non valuta la profondità tecnica e l'adeguatezza sostanziale delle valutazioni e dei test tecnici approfonditi.

### Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) — Core Clinical Gateway

Le vulnerabilità considerate risultano rimosse o mitigate e le fonti pertinenti monitorate sulla base dei dati acquisiti dal gestore delle vulnerabilità. Il controllo è soddisfatto limitatamente al monitoraggio e allo stato tecnico di rimozione o mitigazione, mentre non valuta il piano organizzativo, i ruoli e l'approvazione dell'organo direttivo.

### Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) — Core Clinical Gateway

Risultano monitorati i canali dei fornitori del software critico sulla base dei dati acquisiti dal gestore delle vulnerabilità. Il controllo è soddisfatto limitatamente al monitoraggio strutturato dei canali dei fornitori critici, mentre non valuta l'adeguatezza sostanziale della selezione dei fornitori e delle risposte.

### Identità e credenziali (`CTRL-PR-AA-01`) — Core Clinical Gateway

Le utenze considerate risultano individuali, autorizzate e soggette a gestione delle credenziali sulla base dei dati acquisiti dal sistema IAM; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Autenticazione a più fattori (MFA) (`CTRL-PR-AA-03`) — Core Clinical Gateway

Le utenze privilegiate o remote considerate dispongono dell'autenticazione a più fattori sulla base dei dati acquisiti dal sistema IAM. Il controllo è soddisfatto limitatamente all'autenticazione a più fattori per le utenze privilegiate o remote selezionate distinguendo stati noti, sconosciuti e contrastanti, mentre non valuta il giudizio complessivo di adeguatezza dell'autenticazione rispetto al rischio.

### Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) — Core Clinical Gateway

Le utenze rispettano il minimo privilegio e quelle amministrative sono separate dagli account ordinari sulla base dei dati acquisiti dal sistema IAM; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Protezione fisica (`CTRL-PR-AA-06`) — Core Clinical Gateway

La protezione fisica dell'asset risulta documentata sulla base dei dati acquisiti dalla funzione Facilities. Il controllo è soddisfatto limitatamente alla presenza e alla validità dell'evidenza di protezione fisica, mentre non valuta l'adeguatezza sostanziale delle misure fisiche.

### Protezione dei dati in transito (`CTRL-PR-DS-02`) — Core Clinical Gateway

Le comunicazioni considerate risultano cifrate secondo la configurazione ammessa sulla base dei dati acquisiti dal gestore delle configurazioni. Il controllo è soddisfatto limitatamente alla configurazione crittografica dei servizi Internet censiti, mentre non valuta tutti i flussi esterni vocali, video, testuali e non TLS.

### Backup e ripristino (`CTRL-PR-DS-11`) — Core Clinical Gateway

I backup rispettano il piano e comprendono copie offline sulla base dei dati acquisiti dal gestore dei backup; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Separazione delle copie di backup (`CTRL-PR-DS-11-E`) — Core Clinical Gateway

Le copie di backup risultano protette e le prove di ripristino hanno avuto esito positivo sulla base dei dati acquisiti dal gestore dei backup; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Baseline di hardening (`CTRL-PR-PS-01-E`) — Core Clinical Gateway

La baseline tecnica di hardening risulta applicata sulla base dei dati acquisiti dal gestore delle configurazioni; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Software supportato e aggiornato (`CTRL-PR-PS-02`) — Core Clinical Gateway

I componenti software risultano supportati e aggiornati nei termini del piano di rischio sulla base dei dati acquisiti dal gestore degli aggiornamenti e dalla CMDB; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) — Core Clinical Gateway

Gli aggiornamenti critici risultano testati secondo il processo previsto sulla base dei dati acquisiti dal gestore degli aggiornamenti; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) — Core Clinical Gateway

Le attività di manutenzione e dismissione sicura risultano documentate sulla base dei dati acquisiti dal gestore delle configurazioni. Il controllo è soddisfatto limitatamente alle evidenze strutturate di manutenzione e dismissione sicura, mentre non valuta l'adeguatezza sostanziale delle procedure di trasferimento e dismissione.

### Logging di sicurezza (`CTRL-PR-PS-04`) — Core Clinical Gateway

Gli accessi amministrativi e remoti sono registrati e i log richiesti risultano protetti e conservati secondo il piano sulla base dei dati acquisiti dalla piattaforma di logging; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Accesso remoto e firewall (`CTRL-PR-IR-01`) — Core Clinical Gateway

Gli accessi remoti risultano censiti e protetti e il firewall è attivo sulla base dei dati acquisiti dal gestore della rete; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) — Core Clinical Gateway

La capacità di comunicazione di emergenza risulta configurata e mantenuta sulla base dei dati acquisiti dalla piattaforma di gestione delle emergenze; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) — Core Clinical Gateway

Le capacità di rilevamento considerate risultano abilitate, configurate e monitorate sulla base dei dati acquisiti dalla piattaforma di monitoraggio; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Monitoraggio avanzato (`CTRL-DE-CM-01-E`) — Core Clinical Gateway

Le soglie per il rilevamento delle anomalie risultano configurate sulla base dei dati acquisiti dalla piattaforma di monitoraggio; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Protezione endpoint (`CTRL-DE-CM-09`) — Core Clinical Gateway

La protezione degli endpoint risulta abilitata, configurata, mantenuta e monitorata sulla base dei dati acquisiti dalla piattaforma di protezione degli endpoint; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.


## 6. Controlli non applicabili

Per l'asset Sistema ausiliario fuori perimetro NIS non sono applicabili 26 controlli, poiché è dichiarato esterno al perimetro NIS.


## 7. Priorità di intervento

Gli interventi prioritari riguardano la protezione dei dati a riposo. L'ordine deriva dallo score operativo già calcolato, usato soltanto per ordinare gli interventi: non misura la conformità NIS2 né la gravità normativa.

| Ordine | Asset | Controllo | Intervento |
| ---: | --- | --- | --- |
| 1 | Core Clinical Gateway | Protezione dei dati a riposo | Completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura. |


## 8. Perimetro e limiti

La valutazione riguarda esclusivamente il sottoinsieme di controlli tecnici modellato nel progetto per il profilo ACN **essenziale** e dipende dai dati acquisiti nel `NormalizedEnvironment` `dataset-aurora-normalized-2026`. Una copertura parziale limita l'esito alla parte tecnicamente osservabile indicata dalla regola e non lo estende agli aspetti organizzativi o sostanziali non modellati. Il report non costituisce una certificazione né un'attestazione complessiva di conformità alla NIS2.
