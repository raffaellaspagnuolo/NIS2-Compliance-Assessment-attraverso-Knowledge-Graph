// Trova gli asset per cui l'esposizione Internet e esplicitamente vera.
MATCH (asset:Asset {graph_id: $graph_id, internet_exposed: true})
RETURN asset.id AS asset
ORDER BY asset
