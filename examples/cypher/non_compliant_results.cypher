// Estrae gli scostamenti usando il campo canonico technical_status.
MATCH (result:AssessmentResult {graph_id: $graph_id, technical_status: "non_compliant"})
RETURN result.id AS result, result.asset_id AS asset, result.control_id AS control
ORDER BY result
