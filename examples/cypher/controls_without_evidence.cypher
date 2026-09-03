// Individua controlli per i quali il grafo non contiene evidenze di supporto.
MATCH (control:Control {graph_id: $graph_id})
WHERE NOT EXISTS {
  MATCH (:Evidence {graph_id: $graph_id})-[:SUPPORTS]->(control)
}
RETURN control.id AS control
ORDER BY control
