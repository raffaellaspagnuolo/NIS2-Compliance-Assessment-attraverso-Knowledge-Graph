# Perimetro normativo

Questo documento delimita fonte, profili e copertura normativa del catalogo.

## Fonte e identificazione

Il riferimento del catalogo è la Determinazione ACN n. 379907/2025 e i relativi
Allegati 1 e 2, pubblicati nella [pagina normativa ufficiale
ACN](https://www.acn.gov.it/portale/nis/la-normativa). Ogni requisito conserva
punto ACN, profili applicabili, documento di origine, URL e clausola di rischio.

Il perimetro è intenzionalmente circoscritto a 26 regole tecniche osservabili su
un ambiente normalizzato. Le regole comuni si applicano ai profili `important`
ed `essential`; quelle con suffisso `-E` soltanto al profilo `essential`. Il
prototipo non amplia questo insieme durante l'esecuzione.

## Copertura

`data/acn_coverage.example.yaml` è il catalogo machine-readable della copertura:
16 regole sono `complete` e 10 `partial`. `complete` significa che la parte
tecnica selezionata è interamente rappresentata; `partial` distingue
obbligatoriamente `verified_scope` e `unverified_scope`.

La copertura descrive che cosa il checker prova a valutare, non la conformità di
un'organizzazione. Le soglie TLS, la freshness e la priorità operativa sono
scelte tecniche del progetto, rese esplicite e separate dal testo normativo.
Non costituiscono prescrizioni NIS2 autonome.

## Parti affidate alla valutazione umana

Cinque requisiti organizzativi sono presenti in
`data/nis2_requirements.example.yaml` con modalità `manual_only`: politiche di
sicurezza, formazione e sensibilizzazione, gestione contrattuale della supply
chain, risposta agli incidenti e continuità operativa. Non hanno controlli o
regole e non partecipano ai conteggi tecnici.

Anche nei controlli `evidence_assisted`, il prototipo tratta soltanto presenza,
validità, provenienza, associazione e coerenza formale dell'evidenza. Il giudizio
sostanziale e l'interpretazione normativa complessiva restano umani. Di
conseguenza il report tecnico non costituisce certificazione o attestazione di
conformità alla NIS2.
