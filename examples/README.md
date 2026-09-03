# Esempi di interrogazione del Knowledge Graph

Questa guida riguarda esclusivamente l'esecuzione delle query di esempio sul
grafo già popolato. Non descrive la metodologia di assessment e non modifica
gli esiti prodotti dal motore.

I file in `examples/cypher/` sono query di sola lettura da usare con il comando
`nis2-assessor query`. Ogni query richiede il parametro `graph_id`, così i dati
di assessment diversi restano separati.

Esempio:

```bash
printf '{"graph_id":"scenario-delta-essential-critical"}' > /tmp/nis2-query-params.json
nis2-assessor query \
  --query examples/cypher/non_compliant_results.cypher \
  --graph-id scenario-delta-essential-critical \
  --parameters /tmp/nis2-query-params.json
```

Gli esempi sugli esiti usano `AssessmentResult.technical_status`, che è il campo
canonico. Il campo `status` presente nel report strutturato è soltanto un alias
di compatibilità e non deve essere usato nelle query sul grafo.
