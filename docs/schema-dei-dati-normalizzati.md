# Schema dei dati normalizzati

Questo documento specifica il contratto tecnico dell'input richiesto dalla
pipeline.

## Principi

Il contratto mantiene la compatibilità con gli input supportati dal progetto.
Tutti i timestamp includono il fuso; gli ID sono univoci e ogni riferimento
deve risolversi. Le entità portano provenienza ed evidenze associate
esplicitamente.

## KnowledgeValue

```yaml
status: known                 # known, unknown, not_applicable, conflicting
value: true
provenance_ids: [prov-config]
observation_type: direct      # direct, derived, declared, evidence_based
observed_at: "2026-08-15T09:00:00+02:00"
unknown_cause: null
```

`known` richiede un valore e un `observation_type`; gli altri stati non possono
contenere un valore. `conflicting` richiede almeno due fonti e la causa
esplicita `conflicting_sources`. Gli unknown dichiarano una causa fra
`not_collected`, `collection_failed`,
`source_unavailable`, `conflicting_sources`, `not_declared` e
`stale_information`.

`load_environment()` non arricchisce gli input incompleti. La funzione di
migrazione mantiene la compatibilità con input precedenti, completando alcuni
metadati prima del caricamento strict. Nessuna migrazione inferisce `false`
dall'assenza di un dato.
Anche `source_category` di evidenze e record di provenance è obbligatorio.

## InventoryState

```yaml
- id: inventory-accounts-asset-web
  entity_type: Account
  scope: asset
  scope_id: asset-web
  status: complete            # complete, incomplete, unknown
  unknown_cause: null
  observed_at: "2026-08-15T09:00:00+02:00"
  provenance_ids: [prov-access]
```

Gli stati inventariali sono supportati per dataset/asset e per Asset, Account,
SoftwareComponent, Service, NetworkInterface, NetworkFlow, BackupRecord,
Vulnerability e SecurityCapability.

## Entità

Il contratto dell'ambiente comprende `DatasetInfo`, `Organization`,
`ResponsibleParty`, `Process`, `DataObject`, `Asset`, `Service`,
`SoftwareComponent`, `Account`, `NetworkInterface`, `NetworkFlow`,
`BackupRecord`, `Vulnerability`, `SecurityCapability`, `TechnicalException`,
`Evidence`, `ProvenanceRecord`, `Requirement`, `Control`, `Relationship` e
`InventoryState`. `Rule` appartiene al catalogo esterno e viene validata con gli
stessi modelli prima di essere aggiunta al grafo.

## Evidenze

Ogni evidenza dichiara tipologia, fonte, categoria, `collected_at`, eventuale
`valid_until`, reliability, contenuto, asset/servizi/vulnerabilità/controlli e
provenienza. La validità effettiva deriva dalla scadenza più vicina fra
`valid_until` e `maximum_age` della policy. Una tipologia senza policy non è
ammessa alla decisione.

## Output

`AssessmentResult` usa `technical_status`, `governance_status`, confidence
categoriale, violazioni, lacune, conflitti, selector, soglie, decision policy,
decision trace, remediation ed evidenze. `status` resta un alias di
compatibilità nel report strutturato.
