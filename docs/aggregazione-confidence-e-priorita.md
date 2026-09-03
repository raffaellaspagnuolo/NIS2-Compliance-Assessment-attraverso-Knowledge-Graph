# Aggregazione dei risultati, confidence e priorità operativa

Questo documento specifica i calcoli descrittivi eseguiti dopo che il motore ha
prodotto gli stati tecnici e di governance.

L'aggregazione non produce una percentuale di conformità. La copertura
informativa è il rapporto fra risultati tecnicamente determinati e controlli
applicabili, con numeratore e denominatore espliciti.

La confidence è categoriale (`HIGH`, `MEDIUM`, `LOW`, `INSUFFICIENT`) e descrive
quanto la decisione è sostenuta da informazioni complete, attuali e
tracciabili. Non esprime una probabilità di conformità e non modifica lo stato
del controllo.

La priorità operativa è additiva su scala 0–100:

```text
100 × (0,40 × stato + 0,25 × criticità + 0,20 × impatto + 0,15 × esposizione)
```

I punteggi di stato sono `NON_COMPLIANT=1`, `NOT_VERIFIABLE=0,65` e, per una
possibile estensione futura, `PARTIALLY_COMPLIANT=0,5`. I risultati conformi e
non applicabili sono esclusi. Un valore nullo di esposizione non annulla stato,
criticità e impatto.

Il punteggio serve a ordinare gli interventi e a rendere espliciti i criteri di
prioritizzazione. Non misura la gravità normativa, non trasforma gli esiti in
una percentuale di conformità e non sostituisce la scelta del responsabile.
