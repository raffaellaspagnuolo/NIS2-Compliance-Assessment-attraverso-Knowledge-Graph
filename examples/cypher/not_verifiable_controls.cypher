// Mostra gli esiti non verificabili usando il campo canonico technical_status.
MATCH (result:AssessmentResult {graph_id: $graph_id, technical_status: "not_verifiable"})
RETURN result.id AS result, result.control_id AS control
ORDER BY result
