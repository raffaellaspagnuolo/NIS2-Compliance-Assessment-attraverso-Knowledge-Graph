# Copertura dei controlli ACN

> Documento generato dal catalogo di copertura; la tabella non deve essere modificata manualmente.

Fonte normativa: [Determinazione ACN 379907/2025 e Allegati 1–2](https://www.acn.gov.it/portale/nis/la-normativa).

`complete` e `partial` descrivono il rapporto tra la regola implementata e la
parte tecnica selezionata del controllo. Non sono esiti di conformità
dell'organizzazione. Una copertura parziale non rende inutile la verifica:
identifica con trasparenza la parte osservabile dal sistema e quella che
richiede informazioni o valutazioni ulteriori.

| Regola | Copertura | Parte verificata | Parte non verificata |
|---|---|---|---|
| `RULE-ID-AM-01` | `complete` | Inventario aggiornato e approvato dell'hardware nello scope dichiarato. | — |
| `RULE-ID-AM-02` | `complete` | Inventari di sistemi, servizi e componenti software, con identificazione e autorizzazione. | — |
| `RULE-ID-AM-03-E` | `complete` | Inventario e autorizzazione dei flussi di rete nello scope dichiarato. | — |
| `RULE-ID-AM-04` | `partial` | Presenza dell'inventario strutturato dei servizi erogati da fornitori. | Aggiornamento sostanziale e completezza dei rapporti di fornitura. |
| `RULE-ID-RA-01` | `partial` | Uso dichiarato dei canali monitorati per identificare vulnerabilità. | Completezza sostanziale dell'identificazione su ogni tecnologia. |
| `RULE-ID-RA-01-E` | `partial` | Presenza, freschezza e struttura della relazione di vulnerability assessment. | Profondità tecnica e adeguatezza sostanziale di VA e penetration test. |
| `RULE-ID-RA-08` | `partial` | Monitoraggio e stato tecnico di remediation o mitigazione. | Piano organizzativo, ruoli e approvazione dell'organo direttivo. |
| `RULE-ID-RA-08-E` | `partial` | Monitoraggio strutturato dei canali dei fornitori critici. | Adeguatezza sostanziale della selezione dei fornitori e delle risposte. |
| `RULE-PR-AA-01` | `complete` | Censimento, autorizzazione, individualità, credenziali e revisione delle utenze. | — |
| `RULE-PR-AA-03` | `partial` | MFA per utenze privilegiate o remote selezionate in modo tri-state. | Giudizio complessivo di adeguatezza dell'autenticazione rispetto al rischio. |
| `RULE-PR-AA-05` | `complete` | Minimo privilegio per tutte le utenze e separazione per quelle amministrative. | — |
| `RULE-PR-AA-06` | `partial` | Presenza e validità dell'evidenza di protezione fisica. | Adeguatezza sostanziale delle misure fisiche. |
| `RULE-PR-DS-01` | `partial` | Cifratura dei supporti rimovibili censiti. | Dispositivi portatili, auto-esecuzione e scansione antimalware. |
| `RULE-PR-DS-02` | `partial` | Configurazione crittografica dei servizi Internet censiti. | Tutti i flussi esterni vocali, video, testuali e non TLS. |
| `RULE-PR-DS-11` | `complete` | Periodicità prevista e copie offline dei backup. | — |
| `RULE-PR-DS-11-E` | `complete` | Protezione delle copie e test periodico di ripristino. | — |
| `RULE-PR-PS-01-E` | `complete` | Baseline hardened versionata, definita e documentata. | — |
| `RULE-PR-PS-02` | `complete` | Supporto e aggiornamento del software rispetto al piano di rischio. | — |
| `RULE-PR-PS-02-E` | `complete` | Test degli aggiornamenti del software critico. | — |
| `RULE-PR-PS-03-E` | `partial` | Evidenze strutturate di manutenzione e dismissione sicura. | Adeguatezza sostanziale delle procedure di trasferimento e dismissione. |
| `RULE-PR-PS-04` | `complete` | Logging remoto/amministrativo, protezione e retention; centralizzazione informativa. | — |
| `RULE-PR-IR-01` | `complete` | Registro accessi remoti, protezione dei canali e capacità firewall. | — |
| `RULE-PR-IR-03-E` | `complete` | Capacità protetta e mantenuta per comunicazioni di emergenza. | — |
| `RULE-DE-CM-01` | `complete` | Strumenti tecnici aggiornati, mantenuti e configurati per il rilevamento. | — |
| `RULE-DE-CM-01-E` | `complete` | Parametri quantitativi e qualitativi definiti, monitorati e documentati. | — |
| `RULE-DE-CM-09` | `complete` | Protezione endpoint presente, aggiornata, mantenuta e configurata. | — |

Totale: **16 complete**, **10 partial**, 26 regole.

La validazione automatica richiede `verified_scope` per ogni record e `unverified_scope` per ogni copertura parziale.
