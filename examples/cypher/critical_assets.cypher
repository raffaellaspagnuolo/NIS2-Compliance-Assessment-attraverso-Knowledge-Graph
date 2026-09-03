// Elenca identificativo e nome degli asset classificati come critici.
MATCH (asset:Asset {graph_id: $graph_id, criticality: "critical"})
RETURN asset.id AS asset, asset.name AS name
ORDER BY asset
