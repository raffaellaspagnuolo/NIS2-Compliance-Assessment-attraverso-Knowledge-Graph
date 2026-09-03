// Trova vulnerabilita critiche il cui stato di remediation e ancora aperto.
MATCH (vulnerability:Vulnerability {
  graph_id: $graph_id,
  severity: "critical",
  remediation_status: "open"
})
RETURN vulnerability.id AS vulnerability
ORDER BY vulnerability
