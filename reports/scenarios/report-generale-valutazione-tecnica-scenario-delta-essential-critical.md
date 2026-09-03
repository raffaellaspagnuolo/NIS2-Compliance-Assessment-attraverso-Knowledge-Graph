# Report di valutazione tecnica — Manifattura Delta S.p.A.

## 1. Scenario

La valutazione dello scenario `scenario-delta-essential-critical` riguarda Manifattura Delta S.p.A., con profilo ACN **essenziale**, alla data del 15 agosto 2026. Sono stati osservati 2 asset; un asset è rilevante per il perimetro NIS.


## 2. Sintesi della valutazione

Sono applicabili 26 controlli: uno risulta soddisfatto, 20 non risultano soddisfatti e 5 non sono verificabili. 26 valutazioni non sono applicabili; 2 risultati richiedono una revisione manuale di governance.

I controlli soddisfatti riguardano la gestione degli asset. Gli scostamenti e le lacune informative interessano soprattutto la gestione delle vulnerabilità, il controllo degli accessi e la gestione degli asset.

Il problema complessivamente più urgente riguarda il monitoraggio di rete e degli accessi di Production Integration Server, per cui occorre abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.

| Esito | Numero |
| --- | ---: |
| Soddisfatti | 1 |
| Non soddisfatti | 20 |
| Non verificabili | 5 |
| Non applicabili | 26 |
| Revisione manuale | 2 |

I conteggi si riferiscono alle valutazioni asset-controllo e non rappresentano una percentuale complessiva di conformità NIS2.


## 3. Analisi per asset

### Production Integration Server (`asset-delta-core`)

Per Production Integration Server sono applicabili 26 controlli: uno è soddisfatto, 20 non sono soddisfatti e 5 non sono verificabili. Nell'ordine operativo, i primi problemi riguardano il monitoraggio di rete e degli accessi, le soglie di rilevamento delle anomalie e la protezione degli endpoint.

### Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`)

L'asset è escluso dalla valutazione tecnica perché la sua rilevanza NIS è conosciuta e negativa.


## 4. Controlli non soddisfatti

### Inventario hardware (`CTRL-ID-AM-01`) — Production Integration Server

Il controllo riguardante l'inventario hardware non è soddisfatto perché l'inventario hardware dell'asset è incompleto. La decisione si basa sui dati acquisiti dalla CMDB. Per correggere lo scostamento occorre completare e validare il record inventariale dell'asset.

### Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) — Production Integration Server

Il controllo riguardante il censimento dei flussi di rete non è soddisfatto perché il flusso di rete `flow-delta-https` non risulta autorizzato nel contesto valutato. La decisione si basa sui dati acquisiti dal gestore della rete. Per correggere lo scostamento occorre documentare l'origine, la destinazione, i protocolli e l'autorizzazione dei flussi.

### Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) — Production Integration Server

Il controllo riguardante la valutazione approfondita delle vulnerabilità non è soddisfatto perché non risulta eseguita la valutazione approfondita delle vulnerabilità richiesta. La decisione si basa sui dati acquisiti dallo scanner delle vulnerabilità. La verifica riguarda la presenza, la freschezza e la struttura della relazione di valutazione delle vulnerabilità, mentre non valuta la profondità tecnica e l'adeguatezza sostanziale delle valutazioni e dei test tecnici approfonditi. Per correggere lo scostamento occorre documentare l'approfondimento applicato alla valutazione delle vulnerabilità.

### Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) — Production Integration Server

Il controllo riguardante il trattamento delle vulnerabilità non è soddisfatto perché non è disponibile un dato conclusivo sul monitoraggio delle fonti pertinenti alle vulnerabilità e la vulnerabilità `vuln-delta-001` è ancora aperta o in corso di trattamento e non risulta rimossa o mitigata. Resta inoltre una lacuna informativa: il dato sul monitoraggio delle fonti pertinenti alle vulnerabilità non è stato raccolto. La decisione si basa sui dati acquisiti dal gestore delle vulnerabilità. La verifica riguarda il monitoraggio e lo stato tecnico di rimozione o mitigazione, mentre non valuta il piano organizzativo, i ruoli e l'approvazione dell'organo direttivo. Per correggere gli scostamenti occorre rimuovere o mitigare la vulnerabilità e registrare l'eventuale rischio residuo.

### Identità e credenziali (`CTRL-PR-AA-01`) — Production Integration Server

Il controllo riguardante la gestione delle identità e delle credenziali non è soddisfatto perché le credenziali dell'utenza `account-delta-admin` non risultano gestite secondo le condizioni previste. Resta inoltre da acquisire l'evidenza richiesta per sostenere la verifica con dati ammissibili e aggiornati. Per correggere lo scostamento occorre censire e revisionare le utenze e il ciclo di vita delle credenziali.

### Autenticazione a più fattori (MFA) (`CTRL-PR-AA-03`) — Production Integration Server

Il controllo riguardante l'autenticazione a più fattori (MFA) non è soddisfatto perché `account-delta-admin` non dispone dell'autenticazione a più fattori. La decisione si basa sui dati acquisiti dal sistema IAM. La verifica riguarda l'autenticazione a più fattori per le utenze privilegiate o remote selezionate distinguendo stati noti, sconosciuti e contrastanti, mentre non valuta il giudizio complessivo di adeguatezza dell'autenticazione rispetto al rischio. Per correggere lo scostamento occorre applicare MFA agli accessi privilegiati o remoti individuati dal rischio.

### Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) — Production Integration Server

Il controllo riguardante il minimo privilegio e gli account amministrativi non è soddisfatto perché all'utenza `account-delta-admin` non è applicato il minimo privilegio e l'utenza amministrativa `account-delta-admin` non dispone di un account separato per le sole attività privilegiate. La decisione si basa sui dati acquisiti dal sistema IAM. Per correggere gli scostamenti occorre ridurre i privilegi e separare le credenziali amministrative.

### Protezione dei dati in transito (`CTRL-PR-DS-02`) — Production Integration Server

Il controllo riguardante la protezione dei dati in transito non è soddisfatto perché il servizio `svc-delta-https` trasmette dati senza la cifratura richiesta e il servizio `svc-delta-https` utilizza una versione del protocollo di cifratura non ammessa dalla baseline tecnica. La decisione si basa sui dati acquisiti dal gestore delle configurazioni. La verifica riguarda la configurazione crittografica dei servizi Internet censiti, mentre non valuta tutti i flussi esterni vocali, video, testuali e non TLS. Per correggere gli scostamenti occorre allineare i protocolli alla baseline crittografica approvata.

### Backup e ripristino (`CTRL-PR-DS-11`) — Production Integration Server

Il controllo riguardante il backup e il ripristino non è soddisfatto perché il backup `backup-delta-core` non rispetta la frequenza stabilita dal piano e per il backup `backup-delta-core` non risulta disponibile la copia offline richiesta. La decisione si basa sui dati acquisiti dal gestore dei backup. Per correggere gli scostamenti occorre adeguare la frequenza e le copie offline al piano approvato.

### Separazione delle copie di backup (`CTRL-PR-DS-11-E`) — Production Integration Server

Il controllo riguardante la protezione e il collaudo dei backup non è soddisfatto perché la copia di backup `backup-delta-core` non risulta protetta e la prova di ripristino del backup `backup-delta-core` non ha avuto esito positivo. La decisione si basa sui dati acquisiti dal gestore dei backup. Per correggere gli scostamenti occorre proteggere le copie e completare con successo le prove di ripristino pianificate.

### Baseline di hardening (`CTRL-PR-PS-01-E`) — Production Integration Server

Il controllo riguardante l'hardening dei sistemi non è soddisfatto perché la baseline tecnica di hardening non risulta applicata all'asset. La decisione si basa sui dati acquisiti dal gestore delle configurazioni. Per correggere lo scostamento occorre applicare e versionare una baseline di hardening appropriata.

### Software supportato e aggiornato (`CTRL-PR-PS-02`) — Production Integration Server

Il controllo riguardante il supporto e l'aggiornamento del software non è soddisfatto perché il componente software `software-delta-core` non è più supportato e il componente software `software-delta-core` ha superato il termine di aggiornamento previsto dal piano di rischio. La decisione si basa sui dati acquisiti dal gestore degli aggiornamenti e dalla CMDB. Per correggere gli scostamenti occorre aggiornare il componente software e ricondurne la gestione entro i termini previsti dal piano di rischio. Occorre inoltre sostituire o migrare il componente software fuori supporto.

### Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) — Production Integration Server

Il controllo riguardante il collaudo degli aggiornamenti critici non è soddisfatto perché il componente software `software-delta-core` non è più supportato, il componente software `software-delta-core` ha superato il termine di aggiornamento previsto dal piano di rischio e gli aggiornamenti critici del componente `software-delta-core` non risultano testati. La decisione si basa sui dati acquisiti dal gestore degli aggiornamenti. Per correggere gli scostamenti occorre testare e tracciare gli aggiornamenti critici prima della distribuzione prevista.

### Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) — Production Integration Server

Il controllo riguardante la manutenzione e la dismissione sicura non è soddisfatto perché le attività di manutenzione dell'asset non risultano registrate e la dismissione sicura dell'asset non risulta documentata. La decisione si basa sui dati acquisiti dal gestore delle configurazioni. La verifica riguarda le evidenze strutturate di manutenzione e dismissione sicura, mentre non valuta l'adeguatezza sostanziale delle procedure di trasferimento e dismissione. Per correggere gli scostamenti occorre registrare le attività di manutenzione e le procedure di dismissione sicura.

### Logging di sicurezza (`CTRL-PR-PS-04`) — Production Integration Server

Il controllo riguardante il logging di sicurezza non è soddisfatto perché gli accessi amministrativi e remoti non risultano registrati, i log di sicurezza non risultano protetti e la conservazione dei log non rispetta il piano definito. La decisione si basa sui dati acquisiti dalla piattaforma di logging. Per correggere gli scostamenti occorre registrare gli accessi amministrativi e remoti e proteggere i log per il periodo pianificato.

### Accesso remoto e firewall (`CTRL-PR-IR-01`) — Production Integration Server

Il controllo riguardante gli accessi remoti e il firewall non è soddisfatto perché il registro degli accessi remoti è incompleto, gli accessi remoti non risultano adeguatamente protetti e il firewall richiesto non risulta attivo. La decisione si basa sui dati acquisiti dal gestore della rete. Per correggere gli scostamenti occorre governare gli accessi remoti e applicare regole firewall approvate.

### Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) — Production Integration Server

Il controllo riguardante le comunicazioni di emergenza non è soddisfatto perché la capacità di sicurezza `cap-delta-emergency` non risulta configurata e la capacità di sicurezza `cap-delta-emergency` non risulta mantenuta. La decisione si basa sui dati acquisiti dalla piattaforma di gestione delle emergenze. Per correggere gli scostamenti occorre predisporre, testare e mantenere comunicazioni di emergenza protette.

### Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) — Production Integration Server

Il controllo riguardante il monitoraggio di rete e degli accessi non è soddisfatto perché la capacità di sicurezza `cap-delta-ids` non risulta attiva, la capacità di sicurezza `cap-delta-ids` non risulta configurata e la capacità di sicurezza `cap-delta-ids` non risulta monitorata. La decisione si basa sui dati acquisiti dalla piattaforma di monitoraggio. Per correggere gli scostamenti occorre abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.

### Monitoraggio avanzato (`CTRL-DE-CM-01-E`) — Production Integration Server

Il controllo riguardante le soglie di rilevamento delle anomalie non è soddisfatto perché le soglie per il rilevamento delle anomalie non risultano configurate. La decisione si basa sui dati acquisiti dalla piattaforma di monitoraggio. Per correggere lo scostamento occorre calibrare e riesaminare le soglie e le regole di anomalia.

### Protezione endpoint (`CTRL-DE-CM-09`) — Production Integration Server

Il controllo riguardante la protezione degli endpoint non è soddisfatto perché la capacità di sicurezza `cap-delta-endpoint` non risulta attiva, la capacità di sicurezza `cap-delta-endpoint` non risulta configurata, la capacità di sicurezza `cap-delta-endpoint` non risulta mantenuta e la capacità di sicurezza `cap-delta-endpoint` non risulta monitorata. La decisione si basa sui dati acquisiti dalla piattaforma di protezione degli endpoint. Per correggere gli scostamenti occorre installare, configurare, mantenere e monitorare la protezione degli endpoint appropriata.


## 5. Controlli non verificabili

### Servizi dei fornitori (`CTRL-ID-AM-04`) — Production Integration Server

Il controllo verifica il censimento delle dipendenze tecniche dai fornitori. Non è stato dichiarato se l'inventario dei servizi erogati dai fornitori sia completo. Manca inoltre l'evidenza richiesta per sostenere la verifica con dati ammissibili e aggiornati. Finché la lacuna permane, il controllo non è verificabile. Occorre confermare la completezza dell'inventario dei servizi dei fornitori e acquisire l'evidenza richiesta.

### Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) — Production Integration Server

Il controllo verifica il monitoraggio delle fonti informative pertinenti per identificare le vulnerabilità. Il dato sul monitoraggio delle fonti pertinenti alle vulnerabilità non è stato raccolto. Manca inoltre l'evidenza richiesta per sostenere la verifica con dati ammissibili e aggiornati. Finché la lacuna permane, il controllo non è verificabile. Occorre acquisire lo stato del monitoraggio delle fonti pertinenti e la relativa evidenza.

### Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) — Production Integration Server

Il controllo verifica il monitoraggio dei canali dei fornitori del software ritenuto critico. Non è stato raccolto lo stato del monitoraggio dei canali dei fornitori del software critico. Manca inoltre l'evidenza richiesta per sostenere la verifica con dati ammissibili e aggiornati. Finché la lacuna permane, il controllo non è verificabile. Occorre acquisire lo stato del monitoraggio dei canali dei fornitori critici e la relativa evidenza.

### Protezione fisica (`CTRL-PR-AA-06`) — Production Integration Server

Il controllo verifica la documentazione delle misure di protezione fisica. Non è stato dichiarato se le misure di protezione fisica dell'asset siano documentate. Manca inoltre l'evidenza richiesta per sostenere la verifica con dati ammissibili e aggiornati. Finché la lacuna permane, il controllo non è verificabile. Occorre acquisire documentazione aggiornata sulle misure di protezione fisica dell'asset.

### Protezione dei dati a riposo (`CTRL-PR-DS-01`) — Production Integration Server

Il controllo verifica la cifratura dei supporti rimovibili censiti per l'asset. Non è nota la completezza dell'inventario dei dati e dei supporti rimovibili; senza questa informazione non è possibile stabilire se tutti gli elementi da proteggere siano stati considerati. Finché la lacuna permane, il controllo non è verificabile. Occorre completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura.


## 6. Revisioni manuali di governance

### Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) — Production Integration Server

L'esito tecnico del controllo resta **non soddisfatto** e non viene modificato dalla revisione di governance. È registrato un rischio accettato per `vuln-delta-001`, che richiede una verifica manuale di ambito, approvazione, durata e stato del trattamento.

### Baseline di hardening (`CTRL-PR-PS-01-E`) — Production Integration Server

L'esito tecnico del controllo resta **non soddisfatto** e non viene modificato dalla revisione di governance. È presente la deroga `exception-delta-hardening`. La motivazione registrata è: Il componente legacy non supporta la baseline di hardening corrente senza impatto sul processo produttivo. La misura compensativa registrata è segmentazione temporanea e controllo manuale degli accessi in attesa di sostituzione. Devono essere riesaminati l'approvazione RISK-ACCEPTANCE-DELTA-2026-03, il rischio residuo di livello alto e la validità fino al 31 ottobre 2026.


## 7. Controlli soddisfatti

### Inventario software e servizi (`CTRL-ID-AM-02`) — Production Integration Server

L'asset, i servizi e i componenti software richiesti risultano censiti e autorizzati sulla base dei dati acquisiti dalla CMDB; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola.


## 8. Controlli non applicabili

Per l'asset Sistema ausiliario fuori perimetro NIS non sono applicabili 26 controlli, poiché è dichiarato esterno al perimetro NIS.


## 9. Priorità di intervento

Gli interventi prioritari riguardano il monitoraggio di rete e degli accessi, le soglie di rilevamento delle anomalie e la protezione degli endpoint. L'ordine deriva dallo score operativo già calcolato, usato soltanto per ordinare gli interventi: non misura la conformità NIS2 né la gravità normativa.

| Ordine | Asset | Controllo | Intervento |
| ---: | --- | --- | --- |
| 1 | Production Integration Server | Monitoraggio di rete e accessi | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| 2 | Production Integration Server | Monitoraggio avanzato | Calibrare e riesaminare le soglie e le regole di anomalia. |
| 3 | Production Integration Server | Protezione endpoint | Installare, configurare, mantenere e monitorare la protezione degli endpoint appropriata. |
| 4 | Production Integration Server | Inventario hardware | Completare e validare il record inventariale dell'asset. |
| 5 | Production Integration Server | Inventario dei flussi di rete | Documentare l'origine, la destinazione, i protocolli e l'autorizzazione dei flussi. |
| 6 | Production Integration Server | Assessment approfondito delle vulnerabilità | Documentare l'approfondimento applicato alla valutazione delle vulnerabilità. |
| 7 | Production Integration Server | Trattamento delle vulnerabilità | Rimuovere o mitigare la vulnerabilità e registrare l'eventuale rischio residuo. |
| 8 | Production Integration Server | Identità e credenziali | Censire e revisionare le utenze e il ciclo di vita delle credenziali. |
| 9 | Production Integration Server | Autenticazione e MFA | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| 10 | Production Integration Server | Minimo privilegio e account amministrativi | Ridurre i privilegi e separare le credenziali amministrative. |
| 11 | Production Integration Server | Protezione dei dati in transito | Allineare i protocolli alla baseline crittografica approvata. |
| 12 | Production Integration Server | Backup e ripristino | Adeguare la frequenza e le copie offline al piano approvato. |
| 13 | Production Integration Server | Separazione delle copie di backup | Proteggere le copie e completare con successo le prove di ripristino pianificate. |
| 14 | Production Integration Server | Accesso remoto e firewall | Governare gli accessi remoti e applicare regole firewall approvate. |
| 15 | Production Integration Server | Comunicazioni di emergenza protette | Predisporre, testare e mantenere comunicazioni di emergenza protette. |
| 16 | Production Integration Server | Baseline di hardening | Applicare e versionare una baseline di hardening appropriata. |
| 17 | Production Integration Server | Software supportato e aggiornato | Aggiornare il componente software e ricondurne la gestione entro i termini previsti dal piano di rischio. Occorre inoltre sostituire o migrare il componente software fuori supporto. |
| 18 | Production Integration Server | Test degli aggiornamenti critici | Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista. |
| 19 | Production Integration Server | Manutenzione e dismissione sicura | Registrare le attività di manutenzione e le procedure di dismissione sicura. |
| 20 | Production Integration Server | Logging di sicurezza | Registrare gli accessi amministrativi e remoti e proteggere i log per il periodo pianificato. |
| 21 | Production Integration Server | Servizi dei fornitori | Confermare la completezza dell'inventario dei servizi dei fornitori e acquisire l'evidenza richiesta. |
| 22 | Production Integration Server | Valutazione delle vulnerabilità | Acquisire lo stato del monitoraggio delle fonti pertinenti e la relativa evidenza. |
| 23 | Production Integration Server | Monitoraggio avanzato delle vulnerabilità | Acquisire lo stato del monitoraggio dei canali dei fornitori critici e la relativa evidenza. |
| 24 | Production Integration Server | Protezione fisica | Acquisire documentazione aggiornata sulle misure di protezione fisica dell'asset. |
| 25 | Production Integration Server | Protezione dei dati a riposo | Completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura. |


## 10. Perimetro e limiti

La valutazione riguarda esclusivamente il sottoinsieme di controlli tecnici modellato nel progetto per il profilo ACN **essenziale** e dipende dai dati acquisiti nel `NormalizedEnvironment` `dataset-delta-normalized-2026`. Una copertura parziale limita l'esito alla parte tecnicamente osservabile indicata dalla regola e non lo estende agli aspetti organizzativi o sostanziali non modellati. Il report non costituisce una certificazione né un'attestazione complessiva di conformità alla NIS2.
