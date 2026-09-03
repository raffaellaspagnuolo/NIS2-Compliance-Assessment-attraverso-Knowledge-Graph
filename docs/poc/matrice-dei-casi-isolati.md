# Matrice dei casi asset-controllo isolati

Questa matrice dettaglia le varianti degli input della prova di concetto. La sua
funzione è rendere visibile la composizione della base sperimentale e mostrare
che ogni regola è esercitata almeno in condizioni positive, negative o
informativamente insufficienti. L'interpretazione complessiva degli esiti non
viene ricavata dalla matrice.

Il catalogo `data/poc/cases.yaml` espande 26 gruppi di regole in 93 casi. Le
varianti descrivono conoscenze di ingresso, non risultati calcolati dalla PoC.

| Regola | Casi | Copertura attesa |
|---|---:|---|
| `RULE-ID-AM-01` | 3 | conforme, violazione, senza evidenza |
| `RULE-ID-AM-02` | 3 | conforme, violazione, senza evidenza |
| `RULE-ID-AM-03-E` | 4 | base + profilo important |
| `RULE-ID-AM-04` | 3 | conforme, violazione, senza evidenza |
| `RULE-ID-RA-01` | 3 | scansione valida, scaduta, assente |
| `RULE-ID-RA-01-E` | 4 | base + profilo important |
| `RULE-ID-RA-08` | 4 | base + rischio accettato |
| `RULE-ID-RA-08-E` | 4 | base + profilo important |
| `RULE-PR-AA-01` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-AA-03` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-AA-05` | 4 | base + condizioni miste |
| `RULE-PR-AA-06` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-DS-01` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-DS-02` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-DS-11` | 4 | base + condizioni miste |
| `RULE-PR-DS-11-E` | 4 | base + profilo important |
| `RULE-PR-PS-01-E` | 5 | base + profilo important + deroga |
| `RULE-PR-PS-02` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-PS-02-E` | 4 | base + profilo important |
| `RULE-PR-PS-03-E` | 4 | base + profilo important |
| `RULE-PR-PS-04` | 4 | base + condizioni miste |
| `RULE-PR-IR-01` | 3 | conforme, violazione, senza evidenza |
| `RULE-PR-IR-03-E` | 4 | base + profilo important |
| `RULE-DE-CM-01` | 4 | base + condizioni miste |
| `RULE-DE-CM-01-E` | 4 | base + profilo important |
| `RULE-DE-CM-09` | 3 | conforme, violazione, senza evidenza |

## Significato delle varianti

- `positive`: tutte le conoscenze necessarie sono note, positive e sostenute da evidenza valida;
- `known_violation`: i fatti sono noti ma violano le condizioni tecniche;
- `without_evidence`: l'evidenza richiesta non viene associata alla coppia;
- `important_profile`: il contenitore usa il profilo `important` per una regola solo `essential`;
- `mixed_conditions`: una condizione obbligatoria fallisce mentre le altre sono
  soddisfatte e l'esito tecnico resta `NON_COMPLIANT`;
- `active_exception`: una deroga tecnica valida richiede decisione umana nello
  stato di governance;
- `accepted_risk`: il rischio accettato richiede revisione di governance senza
  cancellare l'esito tecnico.

Per aggiungere un caso occorre modificare il catalogo informativo e, in modo
separato, la ground truth. Requisiti, controlli, regole ed evaluator devono
continuare a provenire dai componenti generali.
