# Report di valutazione tecnica — Logistica Tirrena S.r.l.

## 1. Scenario

La valutazione dello scenario `scenario-tirrena-important-mixed` riguarda Logistica Tirrena S.r.l., con profilo ACN **importante**, alla data del 15 agosto 2026. Sono stati osservati 2 asset; un asset è rilevante per il perimetro NIS.


## 2. Sintesi della valutazione

Sono applicabili 17 controlli: 9 risultano soddisfatti, 7 non risultano soddisfatti e uno non è verificabile. 35 valutazioni non sono applicabili; nessun risultato richiede una revisione manuale di governance.

I controlli soddisfatti riguardano la gestione degli asset, il controllo degli accessi, la sicurezza fisica, la crittografia, il backup e il ripristino, il logging e il monitoraggio, la sicurezza di rete e la sicurezza degli endpoint. Gli scostamenti e le lacune informative interessano soprattutto il controllo degli accessi, la gestione delle vulnerabilità e la protezione dei dati.

Il problema complessivamente più urgente riguarda il monitoraggio di rete e degli accessi di Logistics Application Server, per cui occorre abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.

| Esito | Numero |
| --- | ---: |
| Soddisfatti | 9 |
| Non soddisfatti | 7 |
| Non verificabili | 1 |
| Non applicabili | 35 |
| Revisione manuale | 0 |

I conteggi si riferiscono alle valutazioni asset-controllo e non rappresentano una percentuale complessiva di conformità NIS2.


## 3. Analisi per asset

### Logistics Application Server (`asset-tirrena-core`)

Per Logistics Application Server sono applicabili 17 controlli: 9 sono soddisfatti, 7 non sono soddisfatti e uno non è verificabile. Nell'ordine operativo, i primi problemi riguardano il monitoraggio di rete e degli accessi, il censimento dei servizi dei fornitori e la valutazione delle vulnerabilità.

### Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`)

L'asset è escluso dalla valutazione tecnica perché la sua rilevanza NIS è conosciuta e negativa.


## 4. Controlli non soddisfatti

### Servizi dei fornitori (`CTRL-ID-AM-04`) — Logistics Application Server

Il controllo riguardante il censimento dei servizi dei fornitori non è soddisfatto perché l'inventario dei servizi erogati dai fornitori è incompleto. La decisione si basa sui dati acquisiti dal catalogo aziendale. La verifica riguarda la presenza dell'inventario strutturato dei servizi erogati da fornitori, mentre non valuta l'aggiornamento sostanziale e la completezza dei rapporti di fornitura. Per correggere lo scostamento occorre completare l'elenco dei servizi dei fornitori che supportano l'asset.

### Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) — Logistics Application Server

Il controllo riguardante la valutazione delle vulnerabilità non è soddisfatto perché il monitoraggio delle fonti pertinenti alle vulnerabilità non è attivo. La decisione si basa sui dati acquisiti dal gestore delle vulnerabilità. La verifica riguarda l'uso dichiarato dei canali monitorati per identificare vulnerabilità, mentre non valuta la completezza sostanziale dell'identificazione su ogni tecnologia. Per correggere lo scostamento occorre monitorare le fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate.

### Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) — Logistics Application Server

Il controllo riguardante il trattamento delle vulnerabilità non è soddisfatto perché il monitoraggio delle fonti pertinenti alle vulnerabilità non è attivo e la vulnerabilità `vuln-tirrena-001` è ancora aperta o in corso di trattamento e non risulta rimossa o mitigata. La decisione si basa sui dati acquisiti dal gestore delle vulnerabilità. La verifica riguarda il monitoraggio e lo stato tecnico di rimozione o mitigazione, mentre non valuta il piano organizzativo, i ruoli e l'approvazione dell'organo direttivo. Per correggere gli scostamenti occorre rimuovere o mitigare la vulnerabilità e registrare l'eventuale rischio residuo.

### Autenticazione a più fattori (MFA) (`CTRL-PR-AA-03`) — Logistics Application Server

Il controllo riguardante l'autenticazione a più fattori (MFA) non è soddisfatto perché `account-tirrena-admin` non dispone dell'autenticazione a più fattori. La decisione si basa sui dati acquisiti dal sistema IAM. La verifica riguarda l'autenticazione a più fattori per le utenze privilegiate o remote selezionate distinguendo stati noti, sconosciuti e contrastanti, mentre non valuta il giudizio complessivo di adeguatezza dell'autenticazione rispetto al rischio. Per correggere lo scostamento occorre applicare MFA agli accessi privilegiati o remoti individuati dal rischio.

### Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) — Logistics Application Server

Il controllo riguardante il minimo privilegio e gli account amministrativi non è soddisfatto perché l'utenza amministrativa `account-tirrena-admin` non dispone di un account separato per le sole attività privilegiate. La decisione si basa sui dati acquisiti dal sistema IAM. Per correggere lo scostamento occorre ridurre i privilegi e separare le credenziali amministrative.

### Software supportato e aggiornato (`CTRL-PR-PS-02`) — Logistics Application Server

Il controllo riguardante il supporto e l'aggiornamento del software non è soddisfatto perché il componente software `software-tirrena-core` ha superato il termine di aggiornamento previsto dal piano di rischio. La decisione si basa sui dati acquisiti dal gestore degli aggiornamenti e dalla CMDB. Per correggere lo scostamento occorre aggiornare il componente software e ricondurne la gestione entro i termini previsti dal piano di rischio.

### Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) — Logistics Application Server

Il controllo riguardante il monitoraggio di rete e degli accessi non è soddisfatto perché la capacità di sicurezza `cap-tirrena-ids` non risulta monitorata. La decisione si basa sui dati acquisiti dalla piattaforma di monitoraggio. Per correggere lo scostamento occorre abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.


## 5. Controlli non verificabili

### Protezione dei dati a riposo (`CTRL-PR-DS-01`) — Logistics Application Server

Il controllo verifica la cifratura dei supporti rimovibili censiti per l'asset. Non è nota la completezza dell'inventario dei dati e dei supporti rimovibili; senza questa informazione non è possibile stabilire se tutti gli elementi da proteggere siano stati considerati. Finché la lacuna permane, il controllo non è verificabile. Occorre completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura.


## 6. Controlli soddisfatti

### Inventario hardware (`CTRL-ID-AM-01`) — Logistics Application Server

L'inventario hardware dell'asset risulta completo sulla base dei dati acquisiti dalla CMDB; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Inventario software e servizi (`CTRL-ID-AM-02`) — Logistics Application Server

L'asset, i servizi e i componenti software richiesti risultano censiti e autorizzati sulla base dei dati acquisiti dalla CMDB; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Identità e credenziali (`CTRL-PR-AA-01`) — Logistics Application Server

Le utenze considerate risultano individuali, autorizzate e soggette a gestione delle credenziali sulla base dei dati acquisiti dal sistema IAM; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Protezione fisica (`CTRL-PR-AA-06`) — Logistics Application Server

La protezione fisica dell'asset risulta documentata sulla base dei dati acquisiti dalla funzione Facilities. Il controllo è soddisfatto limitatamente alla presenza e alla validità dell'evidenza di protezione fisica, mentre non valuta l'adeguatezza sostanziale delle misure fisiche.

### Protezione dei dati in transito (`CTRL-PR-DS-02`) — Logistics Application Server

Le comunicazioni considerate risultano cifrate secondo la configurazione ammessa sulla base dei dati acquisiti dal gestore delle configurazioni. Il controllo è soddisfatto limitatamente alla configurazione crittografica dei servizi Internet censiti, mentre non valuta tutti i flussi esterni vocali, video, testuali e non TLS.

### Backup e ripristino (`CTRL-PR-DS-11`) — Logistics Application Server

I backup rispettano il piano e comprendono copie offline sulla base dei dati acquisiti dal gestore dei backup; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Logging di sicurezza (`CTRL-PR-PS-04`) — Logistics Application Server

Gli accessi amministrativi e remoti sono registrati e i log richiesti risultano protetti e conservati secondo il piano sulla base dei dati acquisiti dalla piattaforma di logging; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Accesso remoto e firewall (`CTRL-PR-IR-01`) — Logistics Application Server

Gli accessi remoti risultano censiti e protetti e il firewall è attivo sulla base dei dati acquisiti dal gestore della rete; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.

### Protezione endpoint (`CTRL-DE-CM-09`) — Logistics Application Server

La protezione degli endpoint risulta abilitata, configurata, mantenuta e monitorata sulla base dei dati acquisiti dalla piattaforma di protezione degli endpoint; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.


## 7. Controlli non applicabili

Per l'asset Sistema ausiliario fuori perimetro NIS non sono applicabili 17 controlli, poiché è dichiarato esterno al perimetro NIS.

Altre 18 valutazioni non sono applicabili perché riguardano 9 controlli esclusi dal profilo ACN importante per entrambi gli asset.


## 8. Priorità di intervento

Gli interventi prioritari riguardano il monitoraggio di rete e degli accessi, il censimento dei servizi dei fornitori e la valutazione delle vulnerabilità. L'ordine deriva dallo score operativo già calcolato, usato soltanto per ordinare gli interventi: non misura la conformità NIS2 né la gravità normativa.

| Ordine | Asset | Controllo | Intervento |
| ---: | --- | --- | --- |
| 1 | Logistics Application Server | Monitoraggio di rete e accessi | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| 2 | Logistics Application Server | Servizi dei fornitori | Completare l'elenco dei servizi dei fornitori che supportano l'asset. |
| 3 | Logistics Application Server | Valutazione delle vulnerabilità | Monitorare le fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate. |
| 4 | Logistics Application Server | Trattamento delle vulnerabilità | Rimuovere o mitigare la vulnerabilità e registrare l'eventuale rischio residuo. |
| 5 | Logistics Application Server | Autenticazione e MFA | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| 6 | Logistics Application Server | Minimo privilegio e account amministrativi | Ridurre i privilegi e separare le credenziali amministrative. |
| 7 | Logistics Application Server | Software supportato e aggiornato | Aggiornare il componente software e ricondurne la gestione entro i termini previsti dal piano di rischio. |
| 8 | Logistics Application Server | Protezione dei dati a riposo | Completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura. |


## 9. Perimetro e limiti

La valutazione riguarda esclusivamente il sottoinsieme di controlli tecnici modellato nel progetto per il profilo ACN **importante** e dipende dai dati acquisiti nel `NormalizedEnvironment` `dataset-tirrena-normalized-2026`. Una copertura parziale limita l'esito alla parte tecnicamente osservabile indicata dalla regola e non lo estende agli aspetti organizzativi o sostanziali non modellati. Il report non costituisce una certificazione né un'attestazione complessiva di conformità alla NIS2.
