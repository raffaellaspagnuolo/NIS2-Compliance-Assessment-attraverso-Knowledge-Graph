# Modello del dominio

Questo documento definisce gli oggetti, gli stati e i vincoli del dominio
applicativo.

## Conoscenza e inventari

`KnowledgeValue` separa lo stato (`known`, `unknown`, `not_applicable`,
`conflicting`) dal valore. Registra `observation_type`, `observed_at`,
`unknown_cause` e provenienza. Un valore `false` noto non equivale mai a un dato
assente.

`InventoryState` descrive la completezza di `Asset`, `Account`,
`SoftwareComponent`, `Service`, `NetworkInterface`, `NetworkFlow`,
`BackupRecord`, `Vulnerability` e `SecurityCapability` entro uno scope dataset o
asset. Gli stati sono `complete`, `incomplete` e `unknown`.

## Regole e decisioni

`RuleCondition` dichiara percorso, obbligatorietà, origine
`REGULATORY/PROJECT_BASELINE`, selector e remediation. `DecisionPolicy`
supporta più strategie nel motore estendibile; le 26 regole correnti dichiarano
`ALL_REQUIRED` e aggregazione `ALL_MUST_PASS`. Il modello delle regole rifiuta
attualmente l'abilitazione degli esiti parziali.

`ApplicabilityResult` conserva stato tri-state, motivazioni, selector,
entità selezionate e indeterminate. `EvaluatedFact` conserva valore, confronto,
esito, origine, observation type, timestamp e provenienza.

## AssessmentResult

`technical_status` è canonico; `status` è un alias temporaneo in lettura e nel
report. Gli stati prodotti dalle 26 regole sono `COMPLIANT`, `NON_COMPLIANT`,
`NOT_VERIFIABLE` e `NOT_APPLICABLE`. `PARTIALLY_COMPLIANT` esiste nel dominio
per estensioni future ma richiede una policy esplicita e non è ammesso dal
catalogo corrente.

`governance_status` è indipendente e vale `NONE` oppure
`MANUAL_REVIEW_REQUIRED`. Il risultato contiene inoltre:

- `known_violations`, `missing_information`, `conflicting_information`;
- `selector_decisions`, `thresholds_used`, `decision_policy`;
- `decision_trace`, evidenze ammesse e timestamp;
- `confidence_level` (`HIGH`, `MEDIUM`, `LOW`, `INSUFFICIENT`);
- remediation tecniche e azioni informative separate.

La confidence non è numerica e non rappresenta una probabilità di conformità.

## Modalità di verifica

Le modalità canoniche sono `DIRECT_TECHNICAL`, `EVIDENCE_ASSISTED` e
`MANUAL_ONLY`. Il valore storico `automatic` è accettato come alias di input ma
viene serializzato come `direct_technical`.
