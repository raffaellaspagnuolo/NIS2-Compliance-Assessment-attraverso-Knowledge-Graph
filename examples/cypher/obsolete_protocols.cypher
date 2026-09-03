// Seleziona i servizi su cui e stato osservato un protocollo obsoleto.
MATCH (service:Service {graph_id: $graph_id, obsolete_protocol: true})
RETURN service.id AS service
ORDER BY service
