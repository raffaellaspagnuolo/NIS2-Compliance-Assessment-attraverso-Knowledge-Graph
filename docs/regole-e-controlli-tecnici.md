# Regole e controlli tecnici

Questo documento è il catalogo leggibile delle 26 regole tecniche selezionate e
implementate. Non è un catalogo ACN completo. Le fonti eseguibili sono
`data/technical_rules.example.yaml` e `data/nis2_requirements.example.yaml`.
La fonte è la [Determinazione ACN 379907/2025 con Allegati 1 e
2](https://www.acn.gov.it/portale/nis/la-normativa).

Ogni regola si applica soltanto a sistemi marcati come NIS rilevanti e ai profili
indicati. L'applicabilità è tri-state: un contesto certamente assente è
`not_applicable`, mentre un contesto non conoscibile è `undetermined` e produce
`not_verifiable`. `direct_technical` significa che l'esito deriva interamente da dati tecnici
normalizzati; `evidence_assisted` richiede anche evidenze documentali qualificate.
Nessuna delle due modalità equivale a una certificazione della conformità
organizzativa.

## Preflight comune

Prima di ogni evaluator il motore verifica centralmente:

- presenza e stato `known`, `unknown` o `conflicting` delle proprietà richieste;
- tipo dell'evidenza e associazione corretta ad asset e controllo;
- validità temporale, fonte e riferimenti di provenienza;
- presenza di deroghe tecniche, misure compensative o rischio accettato.

Un dato mancante, confliggente o riferito all'asset sbagliato non può sostenere
`compliant`. Una deroga non sostituisce l'esito tecnico: produce separatamente
`governance_status=manual_review_required` e resta tracciata anche se scaduta o
priva di supporto.

Profilo, rilevanza NIS, tipo di asset e condizioni contestuali sono risolti prima
del preflight. In particolare `RULE-PR-DS-01` richiede supporti rimovibili noti e
presenti, mentre `RULE-PR-DS-02` richiede almeno un servizio con esposizione
Internet nota e positiva. Gli evaluator non possono produrre autonomamente
`not_applicable`.

## Le 26 regole tecniche selezionate

| Regola | Punto ACN | Profili | Verifica | Evaluator | Evidenze richieste | Clausola di rischio o baseline |
|---|---|---|---|---|---|---|
| `RULE-ID-AM-01` | `ID.AM-01` | importante, essenziale | `direct_technical` | `asset_properties` | `asset_inventory` | Completezza e granularità sono definite dal perimetro di rischio. |
| `RULE-ID-AM-02` | `ID.AM-02` | importante, essenziale | `direct_technical` | `collection_inventory` | `software_inventory` | Il dettaglio dipende dal rischio e dall'architettura. |
| `RULE-ID-AM-03-E` | `ID.AM-03` | essenziale | `direct_technical` | `collection_inventory` | `network_flow_inventory` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| `RULE-ID-AM-04` | `ID.AM-04` | importante, essenziale | `evidence_assisted` | `asset_properties` | `provider_service_inventory` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| `RULE-ID-RA-01` | `ID.RA-01` | importante, essenziale | `direct_technical` | `asset_properties` | `vulnerability_management` | Le fonti sono selezionate rispetto alle tecnologie inventariate. |
| `RULE-ID-RA-01-E` | `ID.RA-01` | essenziale | `evidence_assisted` | `vulnerability_assessment` | `vulnerability_scan` | Tecniche e profondità dipendono dal rischio e dallo stato dell'arte. |
| `RULE-ID-RA-08` | `ID.RA-08` | importante, essenziale | `direct_technical` | `vulnerability_treatment` | `vulnerability_management`, `vulnerability_treatment` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| `RULE-ID-RA-08-E` | `ID.RA-08` | essenziale | `evidence_assisted` | `asset_properties` | `vulnerability_management` | Sono osservati i canali dei fornitori del software critico. |
| `RULE-PR-AA-01` | `PR.AA-01` | importante, essenziale | `direct_technical` | `collection_inventory` | `access_review` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| `RULE-PR-AA-03` | `PR.AA-03` | importante, essenziale | `direct_technical` | `collection_booleans` | `access_configuration` | L'MFA è valutata rispetto a rilevanza del sistema e rischio degli accessi. |
| `RULE-PR-AA-05` | `PR.AA-05` | importante, essenziale | `direct_technical` | `collection_booleans` | `access_configuration` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| `RULE-PR-AA-06` | `PR.AA-06` | importante, essenziale | `evidence_assisted` | `asset_properties` | `physical_security` | Le misure fisiche dipendono da ubicazione, minacce e impatto. |
| `RULE-PR-DS-01` | `PR.DS-01` | importante, essenziale | `direct_technical` | `data_object_protection` | `encryption_configuration` | Tecniche e perimetro derivano da classificazione e rischio. |
| `RULE-PR-DS-02` | `PR.DS-02` | importante, essenziale | `direct_technical` | `cryptographic_configuration` | `encryption_configuration` | Algoritmi e protocolli ammessi provengono dalla baseline crittografica di progetto, non direttamente dalla NIS2. |
| `RULE-PR-DS-11` | `PR.DS-11` | importante, essenziale | `direct_technical` | `collection_booleans` | `backup_record` | Frequenza e copie offline provengono dai piani di continuità e ripristino. |
| `RULE-PR-DS-11-E` | `PR.DS-11` | essenziale | `direct_technical` | `collection_booleans` | `backup_record`, `restore_test` | Protezione e test dipendono dagli scenari di perdita e compromissione. |
| `RULE-PR-PS-01-E` | `PR.PS-01` | essenziale | `direct_technical` | `asset_properties` | `system_configuration` | La baseline di hardening dipende dalla tecnologia e dallo stato dell'arte. |
| `RULE-PR-PS-02` | `PR.PS-02` | importante, essenziale | `direct_technical` | `supported_and_updated_software` | `software_inventory`, `patch_record` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| `RULE-PR-PS-02-E` | `PR.PS-02` | essenziale | `direct_technical` | `supported_and_updated_software` | `patch_record` | Modalità e ambiente di test dipendono da rischio e compatibilità. |
| `RULE-PR-PS-03-E` | `PR.PS-03` | essenziale | `evidence_assisted` | `asset_properties` | `maintenance_record` | Le tecniche dipendono da supporto, dati e rischio residuo. |
| `RULE-PR-PS-04` | `PR.PS-04` | importante, essenziale | `direct_technical` | `asset_properties` | `log_configuration` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| `RULE-PR-IR-01` | `PR.IR-01` | importante, essenziale | `direct_technical` | `asset_properties` | `network_security` | Regole firewall e canali remoti sono commisurati a esposizione e rischio. |
| `RULE-PR-IR-03-E` | `PR.IR-03` | essenziale | `evidence_assisted` | `collection_booleans` | `emergency_communications` | Canali e protezioni dipendono dagli scenari di crisi. |
| `RULE-DE-CM-01` | `DE.CM-01` | importante, essenziale | `direct_technical` | `collection_booleans` | `monitoring_configuration` | Osserva gli strumenti tecnici di rilevamento del punto 1. |
| `RULE-DE-CM-01-E` | `DE.CM-01` | essenziale | `direct_technical` | `asset_properties` | `monitoring_configuration` | Le soglie del punto 6 sono calibrate sul comportamento atteso. |
| `RULE-DE-CM-09` | `DE.CM-09` | importante, essenziale | `direct_technical` | `collection_booleans` | `endpoint_protection` | La capacità è selezionata in base al tipo di endpoint e al rischio. |

Le regole del profilo essenziale sono aggiuntive rispetto alla base comune. Il
suffisso `-E` rende visibile questa differenza negli identificativi senza
duplicare i controlli comuni.

## Requisiti organizzativi non valutati

Il catalogo dei requisiti conserva cinque voci `manual_only`, prive di regola ed
evaluator e quindi escluse dai conteggi tecnici:

| Requisito | Punto | Ambito |
|---|---|---|
| `REQ-MANUAL-POLICIES` | `GV.PO-01` | Politiche di sicurezza |
| `REQ-MANUAL-TRAINING` | `PR.AT-01` | Formazione e sensibilizzazione |
| `REQ-MANUAL-SUPPLY` | `GV.SC-01` | Gestione contrattuale della supply chain |
| `REQ-MANUAL-INCIDENT` | `RS.MA-01` | Piano di risposta agli incidenti |
| `REQ-MANUAL-BCP` | `RC.RP-01` | Continuità operativa e gestione della crisi |

## Proprietà decisionali del catalogo

Tutte le 26 regole usano `ALL_REQUIRED` e `ALL_MUST_PASS` e nessuna ammette
`PARTIALLY_COMPLIANT`. Severità e pesi appartengono alla policy operativa, non
al catalogo normativo.
