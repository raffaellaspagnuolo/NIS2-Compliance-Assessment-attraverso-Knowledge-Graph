# Documentazione del progetto

Questo indice è l'unico punto nel quale i contenuti della documentazione sono
messi in relazione tra loro. Ogni documento specialistico sviluppa un tema
autonomo, evitando rimandi ripetitivi. I report in `reports/` sono artefatti
generati; i cataloghi YAML in `data/` e il codice in `src/` restano le fonti
autoritative per il comportamento eseguibile.

## Percorso principale

1. [Metodologia di valutazione](metodologia-di-valutazione.md): dall'ambiente
   normalizzato al risultato, con applicabilità, verificabilità, evidenze,
   stati e ricostruzione della decisione. È il riferimento per comprendere il
   processo decisionale implementato.
2. [Validazione sperimentale](validazione-sperimentale.md): verifica
   dell'implementazione, validazione dell'approccio, scenari sintetici, oracle
   e confronto tra risultati attesi ed effettivi. Serve a interpretare portata e significato dei
   risultati sperimentali.
3. [Analisi critica e sviluppi futuri](analisi-critica-e-sviluppi-futuri.md):
   automazione implementata e potenziale, decisioni umane, limiti, uso
   controllato di un LLM e possibilità di sviluppo. Conclude il
   percorso principale e delimita le estensioni non ancora realizzate.

## Documenti specialistici

4. [Perimetro normativo](perimetro-normativo.md): delimita la fonte ACN, le 26
   regole selezionate, i profili e le parti escluse dalla valutazione.
5. [Architettura del sistema](architettura-del-sistema.md): descrive componenti,
   dipendenze, confini e collocazione delle responsabilità nel codice.
6. [Modello del dominio](modello-del-dominio.md): precisa oggetti, stati e
   contratti del dominio applicativo.
7. [Schema dei dati normalizzati](schema-dei-dati-normalizzati.md): definisce il
   contratto di input, i vincoli, le entità e le evidenze richieste.
8. [Regole e controlli tecnici](regole-e-controlli-tecnici.md): presenta il
   catalogo eseguibile e le modalità di verifica del sottoinsieme tecnico.
9. [Copertura dei controlli ACN](copertura-dei-controlli-acn.md): distingue, per
   ogni regola, la parte verificata da quella che resta fuori dal prototipo.
10. [Ruolo e struttura del Knowledge Graph](ruolo-e-struttura-del-knowledge-graph.md):
    descrive nodi, relazioni, query e confine decisionale del grafo.
11. [Aggregazione, confidence e priorità](aggregazione-confidence-e-priorita.md):
    spiega i calcoli descrittivi effettuati dopo la decisione tecnica.
12. [Generazione dei report](generazione-dei-report.md): descrive contenuto e
    funzione dei tre artefatti prodotti.
13. [Prova di concetto con casi isolati](poc/prova-di-concetto-casi-isolati.md):
    documenta l'esecuzione delle 93 coppie asset-controllo.
14. [Matrice dei casi isolati](poc/matrice-dei-casi-isolati.md): riporta le
    varianti di ingresso esercitate per ogni regola.
15. [Guida all'estensione](guida-all-estensione.md): definisce i contratti da
    rispettare quando si aggiungono tipi, regole, policy o backend.
16. [Query di esempio](../examples/README.md): raccoglie comandi e parametri per
    interrogazioni Cypher di sola lettura.
