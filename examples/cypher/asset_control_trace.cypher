// Ricostruisce la catena requisito -> controllo -> asset per la tracciabilita.
MATCH (control:Control {graph_id: $graph_id})-[:ASSOCIATED_WITH]->(requirement:Requirement)
MATCH (control)-[:APPLIES_TO]->(asset:Asset)
RETURN requirement.id AS requirement, control.id AS control, asset.id AS asset
ORDER BY requirement, control, asset
