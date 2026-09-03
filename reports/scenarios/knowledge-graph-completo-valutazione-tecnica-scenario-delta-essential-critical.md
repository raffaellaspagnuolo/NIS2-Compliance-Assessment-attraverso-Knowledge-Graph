# Knowledge Graph completo — assessment `scenario-delta-essential-critical`

> Questa vista rappresenta lo stesso grafo Neo4j usato dalla pipeline per valutare il sottoinsieme tecnico ACN selezionato. Non rappresenta il catalogo completo delle misure ACN e non aggiunge dati, ipotesi o nuovi calcoli.

## Come leggere il grafo

- I nodi azzurri descrivono il contesto e gli asset osservati.
- I nodi verdi descrivono evidenze e provenienza delle informazioni.
- I nodi arancioni descrivono requisiti, controlli e regole di confronto.
- I nodi viola sono gli esiti prodotti e persistiti dopo la valutazione.

Il grafo contiene **179 nodi** e **267 relazioni**.

## Vista complessiva

```mermaid
flowchart TB
    classDef context fill:#e3f2fd,stroke:#1565c0,color:#0d47a1
    classDef evidence fill:#e0f2f1,stroke:#00796b,color:#004d40
    classDef logic fill:#fff3e0,stroke:#ef6c00,color:#5d4037
    classDef result fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c
    nodo1["Dataset<br/>Ambiente normalizzato - Manifattura Delta"]
    class nodo1 context
    nodo2["Organizzazione<br/>Manifattura Delta S.p.A."]
    class nodo2 context
    nodo3["Responsabili<br/>Responsabile Operations IT/OT"]
    class nodo3 context
    nodo4["Processi<br/>Controllo produzione"]
    class nodo4 context
    nodo5["Categorie di dati<br/>Dati di produzione sintetici"]
    class nodo5 context
    nodo6["Asset<br/>Production Integration Server<br/>admin_remote_access_logging: False<br/>admin_remote_access_logging_observation_type: direct<br/>admin_remote_access_logging_observed_at: 2026-08-14T07:00:00Z<br/>admin_remote_access_logging_status: known<br/>anomaly_thresholds_configured: False<br/>anomaly_thresholds_configured_observation_type: direct<br/>anomaly_thresholds_configured_observed_at: 2026-08-14T07:00:00Z<br/>anomaly_thresholds_configured_status: known<br/>critical_software_supplier_channels_monitored_status: unknown<br/>critical_software_supplier_channels_monitored_unknown_cause: not_collected<br/>exposure_level: critical<br/>extended_vulnerability_assessment_performed: False<br/>extended_vulnerability_assessment_performed_observation_type: direct<br/>extended_vulnerability_assessment_performed_observed_at: 2026-08-14T05:00:00Z<br/>extended_vulnerability_assessment_performed_status: known<br/>firewall_enabled: False<br/>firewall_enabled_observation_type: direct<br/>firewall_enabled_observed_at: 2026-08-14T07:00:00Z<br/>firewall_enabled_status: known<br/>hardening_baseline_applied: False<br/>hardening_baseline_applied_observation_type: direct<br/>hardening_baseline_applied_observed_at: 2026-08-14T07:00:00Z<br/>hardening_baseline_applied_status: known<br/>hardware_inventory_complete: False<br/>hardware_inventory_complete_observation_type: evidence_based<br/>hardware_inventory_complete_observed_at: 2026-08-14T06:00:00Z<br/>hardware_inventory_complete_status: known<br/>impact_level: critical<br/>internet_exposed_observation_type: evidence_based<br/>internet_exposed_observed_at: 2026-08-14T06:00:00Z<br/>log_retention_within_plan: False<br/>log_retention_within_plan_observation_type: declared<br/>log_retention_within_plan_observed_at: 2026-08-10T09:00:00Z<br/>log_retention_within_plan_status: known<br/>logs_centralized: False<br/>logs_centralized_observation_type: direct<br/>logs_centralized_observed_at: 2026-08-14T07:00:00Z<br/>logs_centralized_status: known<br/>logs_protected: False<br/>logs_protected_observation_type: direct<br/>logs_protected_observed_at: 2026-08-14T07:00:00Z<br/>logs_protected_status: known<br/>maintenance_logged: False<br/>maintenance_logged_observation_type: direct<br/>maintenance_logged_observed_at: 2026-08-14T07:00:00Z<br/>maintenance_logged_status: known<br/>network_segment_observation_type: evidence_based<br/>network_segment_observed_at: 2026-08-14T06:00:00Z<br/>nis_relevant: True<br/>nis_relevant_observation_type: declared<br/>nis_relevant_observed_at: 2026-08-10T09:00:00Z<br/>nis_relevant_status: known<br/>operating_system: LegacyExampleOS<br/>operating_system_version: 7.4<br/>physical_protection_documented_status: unknown<br/>physical_protection_documented_unknown_cause: not_declared<br/>provider_services_inventory_complete_status: unknown<br/>provider_services_inventory_complete_unknown_cause: not_declared<br/>remote_access_protected: False<br/>remote_access_protected_observation_type: direct<br/>remote_access_protected_observed_at: 2026-08-14T07:00:00Z<br/>remote_access_protected_status: known<br/>remote_access_registry_complete: False<br/>remote_access_registry_complete_observation_type: declared<br/>remote_access_registry_complete_observed_at: 2026-08-10T09:00:00Z<br/>remote_access_registry_complete_status: known<br/>risk_assessment_reference: RISK-DELTA-2026-07<br/>secure_disposal_documented: False<br/>secure_disposal_documented_observation_type: declared<br/>secure_disposal_documented_observed_at: 2026-08-10T09:00:00Z<br/>secure_disposal_documented_status: known<br/>support_status: unsupported<br/>vulnerability_advisories_monitored_status: unknown<br/>vulnerability_advisories_monitored_unknown_cause: not_collected"]
    class nodo6 context
    nodo7["Asset<br/>Sistema ausiliario fuori perimetro NIS<br/>exposure_level: low<br/>impact_level: medium<br/>internet_exposed_observation_type: evidence_based<br/>internet_exposed_observed_at: 2026-08-14T06:00:00Z<br/>network_segment_observation_type: evidence_based<br/>network_segment_observed_at: 2026-08-14T06:00:00Z<br/>nis_relevant: False<br/>nis_relevant_observation_type: declared<br/>nis_relevant_observed_at: 2026-08-10T09:00:00Z<br/>nis_relevant_status: known<br/>properties_json: {}<br/>risk_assessment_reference: RISK-DELTA-2026-07<br/>support_status: supported"]
    class nodo7 context
    nodo8["Servizi<br/>HTTPS"]
    class nodo8 context
    nodo9["Componenti software<br/>DeltaIntegrator"]
    class nodo9 context
    nodo10["Utenze<br/>account-delta-admin"]
    class nodo10 context
    nodo11["Flussi di rete<br/>flow-delta-https"]
    class nodo11 context
    nodo12["Backup<br/>backup-delta-core"]
    class nodo12 context
    nodo13["Capacità di sicurezza<br/>cap-delta-emergency"]
    class nodo13 context
    nodo14["Capacità di sicurezza<br/>cap-delta-ids"]
    class nodo14 context
    nodo15["Capacità di sicurezza<br/>cap-delta-filter"]
    class nodo15 context
    nodo16["Capacità di sicurezza<br/>cap-delta-access-monitor"]
    class nodo16 context
    nodo17["Capacità di sicurezza<br/>cap-delta-endpoint"]
    class nodo17 context
    nodo18["Deroghe tecniche<br/>exception-delta-hardening"]
    class nodo18 context
    nodo19["Vulnerabilità<br/>Vulnerabilità critica su dipendenza Log4j legacy"]
    class nodo19 context
    nodo20["Evidenze<br/>Inventario asset<br/>evidence_type: asset_inventory<br/>source: CMDB<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo20 evidence
    nodo21["Evidenze<br/>Inventario software<br/>evidence_type: software_inventory<br/>source: CMDB<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo21 evidence
    nodo22["Evidenze<br/>Inventario flussi di rete<br/>evidence_type: network_flow_inventory<br/>source: network-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo22 evidence
    nodo23["Evidenze<br/>Scansione vulnerabilità<br/>evidence_type: vulnerability_scan<br/>source: vulnerability-scanner<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'activity_description': 'Vulnerability assessment autenticato.', 'cve': 'CVE-2021-44228', 'impact_…"]
    class nodo23 evidence
    nodo24["Evidenze<br/>Registro trattamento vulnerabilità<br/>evidence_type: vulnerability_treatment<br/>source: vulnerability-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo24 evidence
    nodo25["Evidenze<br/>Configurazione MFA e privilegi<br/>evidence_type: access_configuration<br/>source: IAM<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo25 evidence
    nodo26["Evidenze<br/>Configurazione cifratura<br/>evidence_type: encryption_configuration<br/>source: configuration-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'baseline_id': 'CRYPTO-BASELINE-2026.1'}"]
    class nodo26 evidence
    nodo27["Evidenze<br/>Registro backup<br/>evidence_type: backup_record<br/>source: backup-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'plan_reference': 'BACKUP-DELTA-2026'}"]
    class nodo27 evidence
    nodo28["Evidenze<br/>Test di ripristino<br/>evidence_type: restore_test<br/>source: backup-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo28 evidence
    nodo29["Evidenze<br/>Configurazione e hardening<br/>evidence_type: system_configuration<br/>source: configuration-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo29 evidence
    nodo30["Evidenze<br/>Registro patching<br/>evidence_type: patch_record<br/>source: patch-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo30 evidence
    nodo31["Evidenze<br/>Registro manutenzione<br/>evidence_type: maintenance_record<br/>source: configuration-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo31 evidence
    nodo32["Evidenze<br/>Configurazione logging<br/>evidence_type: log_configuration<br/>source: logging-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo32 evidence
    nodo33["Evidenze<br/>Configurazione accessi remoti e firewall<br/>evidence_type: network_security<br/>source: network-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo33 evidence
    nodo34["Evidenze<br/>Comunicazioni di emergenza<br/>evidence_type: emergency_communications<br/>source: crisis-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo34 evidence
    nodo35["Evidenze<br/>Configurazione monitoraggio<br/>evidence_type: monitoring_configuration<br/>source: monitoring-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo35 evidence
    nodo36["Evidenze<br/>Protezione endpoint<br/>evidence_type: endpoint_protection<br/>source: endpoint-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo36 evidence
    nodo37["Fonti e provenienza<br/>prov-inventory<br/>source: CMDB<br/>method: export autenticato<br/>collected_at: 2026-08-14T06:00:00Z<br/>reliability: high"]
    class nodo37 evidence
    nodo38["Fonti e provenienza<br/>prov-config<br/>source: configuration-manager<br/>method: raccolta automatizzata<br/>collected_at: 2026-08-14T07:00:00Z<br/>reliability: high"]
    class nodo38 evidence
    nodo39["Fonti e provenienza<br/>prov-governance<br/>source: registro governance<br/>method: dichiarazione approvata<br/>collected_at: 2026-08-10T09:00:00Z<br/>reliability: medium"]
    class nodo39 evidence
    nodo40["Fonti e provenienza<br/>prov-scan<br/>source: vulnerability-scanner<br/>method: scansione autenticata<br/>collected_at: 2026-08-14T05:00:00Z<br/>reliability: high"]
    class nodo40 evidence
    nodo41["Fonti e provenienza<br/>prov-patch<br/>source: patch-manager<br/>method: export stato<br/>collected_at: 2026-08-14T07:30:00Z<br/>reliability: high"]
    class nodo41 evidence
    nodo42["Fonti e provenienza<br/>prov-access<br/>source: IAM<br/>method: export utenze<br/>collected_at: 2026-08-14T07:45:00Z<br/>reliability: high"]
    class nodo42 evidence
    nodo43["Fonti e provenienza<br/>prov-network<br/>source: network-manager<br/>method: export configurazione<br/>collected_at: 2026-08-14T06:30:00Z<br/>reliability: high"]
    class nodo43 evidence
    nodo44["Fonti e provenienza<br/>prov-backup<br/>source: backup-manager<br/>method: export job e test<br/>collected_at: 2026-08-14T03:30:00Z<br/>reliability: high"]
    class nodo44 evidence
    nodo45["Requisiti<br/>Inventario hardware<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-01 punto 1"]
    class nodo45 logic
    nodo46["Requisiti<br/>Inventario software e servizi<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-02 punto 1"]
    class nodo46 logic
    nodo47["Requisiti<br/>Inventario dei flussi di rete<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-03 punto 1"]
    class nodo47 logic
    nodo48["Requisiti<br/>Servizi dei fornitori<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-04 punto 1"]
    class nodo48 logic
    nodo49["Requisiti<br/>Identificazione delle vulnerabilità<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-01 punto 1"]
    class nodo49 logic
    nodo50["Requisiti<br/>Approfondimenti di vulnerability assessment<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-01 punti 2 e 3"]
    class nodo50 logic
    nodo51["Requisiti<br/>Trattamento delle vulnerabilità<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-08 punti 1 e 2"]
    class nodo51 logic
    nodo52["Requisiti<br/>Canali dei fornitori del software critico<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-08 punto 5"]
    class nodo52 logic
    nodo53["Requisiti<br/>Identità e credenziali<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-01 punti 1, 2 e 3"]
    class nodo53 logic
    nodo54["Requisiti<br/>Autenticazione e MFA<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-03 punti 1 e 2"]
    class nodo54 logic
    nodo55["Requisiti<br/>Minimo privilegio e utenze amministrative<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-05 punti 1 e 2"]
    class nodo55 logic
    nodo56["Requisiti<br/>Protezione fisica<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-06 punto 1"]
    class nodo56 logic
    nodo57["Requisiti<br/>Cifratura dei supporti rimovibili<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-01 punto 1"]
    class nodo57 logic
    nodo58["Requisiti<br/>Protezione dei dati in transito<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-02 punto 1"]
    class nodo58 logic
    nodo59["Requisiti<br/>Backup periodici e copie offline<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-11 punto 1"]
    class nodo59 logic
    nodo60["Requisiti<br/>Protezione e test dei backup<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-11 punti 3 e 4"]
    class nodo60 logic
    nodo61["Requisiti<br/>Hardening<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-01 punto 1"]
    class nodo61 logic
    nodo62["Requisiti<br/>Software supportato e aggiornato<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-02 punti 1 e 2"]
    class nodo62 logic
    nodo63["Requisiti<br/>Test degli aggiornamenti critici<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-02 punto 4"]
    class nodo63 logic
    nodo64["Requisiti<br/>Manutenzione e dismissione sicura<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-03 punti 1 e 2"]
    class nodo64 logic
    nodo65["Requisiti<br/>Logging di sicurezza<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-04 punti 1, 2 e 3"]
    class nodo65 logic
    nodo66["Requisiti<br/>Accesso remoto e firewall<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.IR-01 punti 1, 2 e 3"]
    class nodo66 logic
    nodo67["Requisiti<br/>Comunicazioni di emergenza protette<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.IR-03 punto 1"]
    class nodo67 logic
    nodo68["Requisiti<br/>Strumenti per il rilevamento degli incidenti<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN DE.CM-01 punto 1"]
    class nodo68 logic
    nodo69["Requisiti<br/>Monitoraggio avanzato<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN DE.CM-01 punto 6"]
    class nodo69 logic
    nodo70["Requisiti<br/>Protezione endpoint<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN DE.CM-09 punto 1"]
    class nodo70 logic
    nodo71["Requisiti<br/>Politiche di sicurezza<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN GV.PO-01 punti 1, 2 e 3"]
    class nodo71 logic
    nodo72["Requisiti<br/>Formazione e sensibilizzazione<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AT-01 punti 1, 2 e 3"]
    class nodo72 logic
    nodo73["Requisiti<br/>Gestione contrattuale della supply chain<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN GV.SC-01 punto 1 (punto 2 per il solo profilo essenziale)"]
    class nodo73 logic
    nodo74["Requisiti<br/>Piano di risposta agli incidenti<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN RS.MA-01 punti 1, 2 e 3"]
    class nodo74 logic
    nodo75["Requisiti<br/>Continuità operativa e crisi<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN RC.RP-01 punto 1"]
    class nodo75 logic
    nodo76["Controlli tecnici<br/>Inventario hardware<br/>technical_area: asset_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo76 logic
    nodo77["Controlli tecnici<br/>Inventario software e servizi<br/>technical_area: asset_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo77 logic
    nodo78["Controlli tecnici<br/>Inventario dei flussi di rete<br/>technical_area: asset_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo78 logic
    nodo79["Controlli tecnici<br/>Servizi dei fornitori<br/>technical_area: supply_chain_technical<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['important', 'essential']"]
    class nodo79 logic
    nodo80["Controlli tecnici<br/>Valutazione delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo80 logic
    nodo81["Controlli tecnici<br/>Assessment approfondito delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo81 logic
    nodo82["Controlli tecnici<br/>Trattamento delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo82 logic
    nodo83["Controlli tecnici<br/>Monitoraggio avanzato delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo83 logic
    nodo84["Controlli tecnici<br/>Identità e credenziali<br/>technical_area: access_control<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo84 logic
    nodo85["Controlli tecnici<br/>Autenticazione e MFA<br/>technical_area: access_control<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo85 logic
    nodo86["Controlli tecnici<br/>Minimo privilegio e account amministrativi<br/>technical_area: access_control<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo86 logic
    nodo87["Controlli tecnici<br/>Protezione fisica<br/>technical_area: physical_security<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['important', 'essential']"]
    class nodo87 logic
    nodo88["Controlli tecnici<br/>Protezione dei dati a riposo<br/>technical_area: data_protection<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo88 logic
    nodo89["Controlli tecnici<br/>Protezione dei dati in transito<br/>technical_area: cryptography<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo89 logic
    nodo90["Controlli tecnici<br/>Backup e ripristino<br/>technical_area: backup_recovery<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo90 logic
    nodo91["Controlli tecnici<br/>Separazione delle copie di backup<br/>technical_area: backup_recovery<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo91 logic
    nodo92["Controlli tecnici<br/>Baseline di hardening<br/>technical_area: system_security<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo92 logic
    nodo93["Controlli tecnici<br/>Software supportato e aggiornato<br/>technical_area: patch_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo93 logic
    nodo94["Controlli tecnici<br/>Test degli aggiornamenti critici<br/>technical_area: patch_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo94 logic
    nodo95["Controlli tecnici<br/>Manutenzione e dismissione sicura<br/>technical_area: system_security<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo95 logic
    nodo96["Controlli tecnici<br/>Logging di sicurezza<br/>technical_area: logging_monitoring<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo96 logic
    nodo97["Controlli tecnici<br/>Accesso remoto e firewall<br/>technical_area: network_security<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo97 logic
    nodo98["Controlli tecnici<br/>Comunicazioni di emergenza protette<br/>technical_area: emergency_communications<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo98 logic
    nodo99["Controlli tecnici<br/>Monitoraggio di rete e accessi<br/>technical_area: security_monitoring<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo99 logic
    nodo100["Controlli tecnici<br/>Monitoraggio avanzato<br/>technical_area: security_monitoring<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo100 logic
    nodo101["Controlli tecnici<br/>Protezione endpoint<br/>technical_area: endpoint_security<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo101 logic
    nodo102["Regole di valutazione<br/>Completezza inventario hardware<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['hardware_inventory_complete']}<br/>verification_mode: direct_technical<br/>risk_clause: Completezza e granularità sono quelle definite dal perimetro di rischio."]
    class nodo102 logic
    nodo103["Regole di valutazione<br/>Inventario software e servizi<br/>evaluator: collection_inventory<br/>parameters_json: {'entity_type': 'SoftwareComponent', 'fields': ['name', 'version', 'authorized']}<br/>verification_mode: direct_technical<br/>risk_clause: Il livello di dettaglio dipende dal rischio e dall'architettura."]
    class nodo103 logic
    nodo104["Regole di valutazione<br/>Inventario e autorizzazione dei flussi<br/>evaluator: collection_inventory<br/>parameters_json: {'entity_type': 'NetworkFlow', 'fields': ['source', 'destination', 'transport_protocol', 'applicati…<br/>verification_mode: direct_technical<br/>risk_clause: Il perimetro dei flussi deriva dalla valutazione del rischio."]
    class nodo104 logic
    nodo105["Regole di valutazione<br/>Inventario tecnico dei servizi forniti da terzi<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['provider_services_inventory_complete']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Sono incluse le dipendenze pertinenti al rischio del sistema."]
    class nodo105 logic
    nodo106["Regole di valutazione<br/>Identificazione delle vulnerabilità da fonti monitorate<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['vulnerability_advisories_monitored']}<br/>verification_mode: direct_technical<br/>risk_clause: Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate."]
    class nodo106 logic
    nodo107["Regole di valutazione<br/>Vulnerability assessment approfondito<br/>evaluator: vulnerability_assessment<br/>parameters_json: {'properties': ['extended_vulnerability_assessment_performed']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte."]
    class nodo107 logic
    nodo108["Regole di valutazione<br/>Trattamento delle vulnerabilità rilevate<br/>evaluator: vulnerability_treatment<br/>parameters_json: {}<br/>verification_mode: direct_technical<br/>risk_clause: Priorità e termini sono quelli documentati nella valutazione del rischio."]
    class nodo108 logic
    nodo109["Regole di valutazione<br/>Monitoraggio dei canali dei fornitori critici<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['critical_software_supplier_channels_monitored']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Il software critico è individuato dall'inventario e dalla valutazione del rischio."]
    class nodo109 logic
    nodo110["Regole di valutazione<br/>Inventario e gestione delle utenze<br/>evaluator: collection_inventory<br/>parameters_json: {'entity_type': 'Account', 'fields': ['account_type', 'individual', 'authorized', 'credentials_mana…<br/>verification_mode: direct_technical<br/>risk_clause: Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio."]
    class nodo110 logic
    nodo111["Regole di valutazione<br/>MFA per accessi pertinenti al rischio<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'Account', 'properties': ['mfa_enabled'], 'selectors_any': {'privileged': true, 're…<br/>verification_mode: direct_technical<br/>risk_clause: L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi."]
    class nodo111 logic
    nodo112["Regole di valutazione<br/>Minimo privilegio e separazione amministrativa<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'Account', 'properties': ['least_privilege', 'separate_admin_account'], 'selectors_…<br/>verification_mode: direct_technical<br/>risk_clause: I privilegi ammessi dipendono dalle funzioni autorizzate."]
    class nodo112 logic
    nodo113["Regole di valutazione<br/>Protezione fisica documentabile<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['physical_protection_documented']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Le misure fisiche dipendono da ubicazione minacce e impatto."]
    class nodo113 logic
    nodo114["Regole di valutazione<br/>Cifratura dei supporti rimovibili<br/>evaluator: data_object_protection<br/>parameters_json: {'properties': []}<br/>verification_mode: direct_technical<br/>risk_clause: Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori peri…"]
    class nodo114 logic
    nodo115["Regole di valutazione<br/>Cifratura delle comunicazioni<br/>evaluator: cryptographic_configuration<br/>parameters_json: {'threshold_ref': 'tls_minimum'}<br/>verification_mode: direct_technical<br/>risk_clause: Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente d…"]
    class nodo115 logic
    nodo116["Regole di valutazione<br/>Backup conforme al piano e copie offline<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'BackupRecord', 'properties': ['frequency_within_plan', 'offline_copy']}<br/>verification_mode: direct_technical<br/>risk_clause: La frequenza proviene dai piani di continuità e ripristino dichiarati."]
    class nodo116 logic
    nodo117["Regole di valutazione<br/>Protezione e test di ripristino per il profilo essenziale<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'BackupRecord', 'properties': ['protected_copy', 'restore_test_successful']}<br/>verification_mode: direct_technical<br/>risk_clause: Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione."]
    class nodo117 logic
    nodo118["Regole di valutazione<br/>Baseline di hardening applicata<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['hardening_baseline_applied']}<br/>verification_mode: direct_technical<br/>risk_clause: La baseline è scelta in funzione della tecnologia e dello stato dell'arte."]
    class nodo118 logic
    nodo119["Regole di valutazione<br/>Software supportato e aggiornamenti entro il piano di rischio<br/>evaluator: supported_and_updated_software<br/>parameters_json: {'critical_patch_test_required': false}<br/>verification_mode: direct_technical<br/>risk_clause: Le scadenze di patching provengono dal piano di rischio dichiarato."]
    class nodo119 logic
    nodo120["Regole di valutazione<br/>Test delle patch critiche<br/>evaluator: supported_and_updated_software<br/>parameters_json: {'critical_patch_test_required': true}<br/>verification_mode: direct_technical<br/>risk_clause: Modalità e ambiente di test sono commisurati a rischio e compatibilità."]
    class nodo120 logic
    nodo121["Regole di valutazione<br/>Manutenzione e dismissione tracciate<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['maintenance_logged', 'secure_disposal_documented']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Le tecniche dipendono da supporto dati e rischio residuo."]
    class nodo121 logic
    nodo122["Regole di valutazione<br/>Logging di accessi amministrativi e remoti<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['admin_remote_access_logging', 'logs_protected', 'logs_centralized', 'log_retention…<br/>verification_mode: direct_technical<br/>risk_clause: Eventi e durata di conservazione provengono dal piano di logging e dal rischio."]
    class nodo122 logic
    nodo123["Regole di valutazione<br/>Accesso remoto governato e firewall attivo<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['remote_access_registry_complete', 'remote_access_protected', 'firewall_enabled']}<br/>verification_mode: direct_technical<br/>risk_clause: Regole e canali sono commisurati a esposizione e rischio."]
    class nodo123 logic
    nodo124["Regole di valutazione<br/>Capacità protetta per comunicazioni di emergenza<br/>evaluator: collection_booleans<br/>parameters_json: {'capability_types': ['emergency_communications'], 'entity_type': 'SecurityCapability', 'properties…<br/>verification_mode: evidence_assisted<br/>risk_clause: Canali e protezioni dipendono dagli scenari di crisi."]
    class nodo124 logic
    nodo125["Regole di valutazione<br/>Rilevamento degli incidenti di rete<br/>evaluator: collection_booleans<br/>parameters_json: {'capability_types': ['intrusion_detection'], 'entity_type': 'SecurityCapability', 'properties': ['…<br/>verification_mode: direct_technical<br/>risk_clause: La copertura della capacità di rilevamento è basata su architettura e rischio."]
    class nodo125 logic
    nodo126["Regole di valutazione<br/>Soglie e anomalie calibrate<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['anomaly_thresholds_configured']}<br/>verification_mode: direct_technical<br/>risk_clause: Le soglie sono calibrate sul comportamento atteso e non sono universali."]
    class nodo126 logic
    nodo127["Regole di valutazione<br/>Protezione endpoint attiva e monitorata<br/>evaluator: collection_booleans<br/>parameters_json: {'capability_types': ['endpoint_protection'], 'entity_type': 'SecurityCapability', 'properties': ['…<br/>verification_mode: direct_technical<br/>risk_clause: La capacità è selezionata in base al tipo di endpoint e al rischio."]
    class nodo127 logic
    nodo128["Esiti della valutazione<br/>d2bbd3a2-691c-51f2-b049-9400e7eeaeaf<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo128 result
    nodo129["Esiti della valutazione<br/>db6b747d-ed2c-56d9-a44e-a3d7bba80e3c<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'identificato', 'comparison_result': true, 'condition_origin': 'regulatory', 'manda…"]
    class nodo129 result
    nodo130["Esiti della valutazione<br/>21318f70-a095-51ea-afff-68297a2c2fb1<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'presente', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory…"]
    class nodo130 result
    nodo131["Esiti della valutazione<br/>68032e4d-3c55-5d5c-9e92-2c1bea0903f8<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: Dati o evidenze non consentono una verifica conclusiva.<br/>confidence_level: insufficient<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo131 result
    nodo132["Esiti della valutazione<br/>b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: Dati o evidenze non consentono una verifica conclusiva.<br/>confidence_level: insufficient<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo132 result
    nodo133["Esiti della valutazione<br/>3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo133 result
    nodo134["Esiti della valutazione<br/>f53750a1-b38c-5313-ae50-f0f28a7f8550<br/>technical_status: non_compliant<br/>governance_status: manual_review_required<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: insufficient<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo134 result
    nodo135["Esiti della valutazione<br/>bb194a5a-6411-5a0e-b7f2-8d000af407aa<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: Dati o evidenze non consentono una verifica conclusiva.<br/>confidence_level: insufficient<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo135 result
    nodo136["Esiti della valutazione<br/>bf852d65-376e-5d3f-8bff-069ec968bb8b<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: insufficient<br/>evaluated_facts_json: [{'comparison': 'presente', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory…"]
    class nodo136 result
    nodo137["Esiti della valutazione<br/>2497016d-98aa-50c0-b10a-86df9c6f3647<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo137 result
    nodo138["Esiti della valutazione<br/>24420cc8-ad6d-5614-ac2c-ee1b1c9dea45<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo138 result
    nodo139["Esiti della valutazione<br/>736d6caf-aace-5f7f-956d-3ee3454dd915<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: Dati o evidenze non consentono una verifica conclusiva.<br/>confidence_level: insufficient<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo139 result
    nodo140["Esiti della valutazione<br/>39e058e6-5280-5324-b082-6ef01f2e9d00<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: completezza dell'inventario DataObject non nota<br/>confidence_level: insufficient"]
    class nodo140 result
    nodo141["Esiti della valutazione<br/>6e2b2dc5-5977-5a3b-99ed-b40922a62e7c<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo141 result
    nodo142["Esiti della valutazione<br/>24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo142 result
    nodo143["Esiti della valutazione<br/>addb2b61-1c04-5192-a578-8b6e94c68c9e<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo143 result
    nodo144["Esiti della valutazione<br/>7148cb04-f822-547f-801d-368bd0a766c8<br/>technical_status: non_compliant<br/>governance_status: manual_review_required<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo144 result
    nodo145["Esiti della valutazione<br/>7921a7d9-e961-5f84-81d2-7222735a125c<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': '{supported}', 'comparison_result': false, 'condition_origin': 'regulatory', 'manda…"]
    class nodo145 result
    nodo146["Esiti della valutazione<br/>86104e8e-ed72-542f-b7b3-de52032ffa4b<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': '{supported}', 'comparison_result': false, 'condition_origin': 'regulatory', 'manda…"]
    class nodo146 result
    nodo147["Esiti della valutazione<br/>ae29b32b-98a8-5977-b4e7-8d70d6d4dd43<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo147 result
    nodo148["Esiti della valutazione<br/>fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo148 result
    nodo149["Esiti della valutazione<br/>0534ef1c-4ab5-586a-926e-8b24e75d2ee5<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo149 result
    nodo150["Esiti della valutazione<br/>c156bb48-3c77-5851-ac1f-b041c9fca5a3<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo150 result
    nodo151["Esiti della valutazione<br/>1b28aa3c-866b-5ecd-b2de-c9c6a84a9357<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo151 result
    nodo152["Esiti della valutazione<br/>66286b28-a64b-5036-b99e-cfefdd09ec2c<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'project_baseline', 'mandat…"]
    class nodo152 result
    nodo153["Esiti della valutazione<br/>45e763f5-3989-5177-9bbb-8bc07e7c4dcb<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo153 result
    nodo154["Esiti della valutazione<br/>de2c79d8-fd43-5ebf-8d5a-5c8896101d29<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo154 result
    nodo155["Esiti della valutazione<br/>3e075956-8a97-59f9-9453-a96d35311a9d<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo155 result
    nodo156["Esiti della valutazione<br/>dcaaa43d-fc5c-578a-864d-d64dcc363360<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo156 result
    nodo157["Esiti della valutazione<br/>21ef177c-0d23-5ae0-8cad-e0d3b809178f<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo157 result
    nodo158["Esiti della valutazione<br/>a2eb9293-638a-54f0-9836-9a9ed675558d<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo158 result
    nodo159["Esiti della valutazione<br/>02931dc5-a262-52ab-bf4a-19373c4f0050<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo159 result
    nodo160["Esiti della valutazione<br/>8cd984bf-5bdb-5675-b579-2eb4a5078bd4<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo160 result
    nodo161["Esiti della valutazione<br/>71ac75bb-5a78-56d8-8796-138c3aff6fb1<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo161 result
    nodo162["Esiti della valutazione<br/>9d2cbe7e-5702-558e-9d08-e6d5868283c1<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo162 result
    nodo163["Esiti della valutazione<br/>83f6d6b9-eeb9-500a-8a7c-3f135af47eed<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo163 result
    nodo164["Esiti della valutazione<br/>0003441d-fc06-5e81-848f-24b798b8a6a1<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo164 result
    nodo165["Esiti della valutazione<br/>947e7d7b-cf4d-5ca3-b2b6-95d01d698733<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo165 result
    nodo166["Esiti della valutazione<br/>810f76d0-8eb9-5119-acb9-7e7c52adce93<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo166 result
    nodo167["Esiti della valutazione<br/>e16edf55-f114-514a-b316-8421d19c5f56<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo167 result
    nodo168["Esiti della valutazione<br/>742f0a86-41c5-5fb4-a7cf-eedded238636<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo168 result
    nodo169["Esiti della valutazione<br/>afbdda04-a07f-594e-860c-04fa2533c2ac<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo169 result
    nodo170["Esiti della valutazione<br/>10b56a51-33a8-553e-b7ed-2a440834bcec<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo170 result
    nodo171["Esiti della valutazione<br/>a7882c14-37b9-5f2c-a01c-31a76aa326ff<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo171 result
    nodo172["Esiti della valutazione<br/>a65a4440-bd6f-592e-94e6-3198c2339d0f<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo172 result
    nodo173["Esiti della valutazione<br/>6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo173 result
    nodo174["Esiti della valutazione<br/>700d7d03-0cc6-5630-82da-9c51576a8d59<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo174 result
    nodo175["Esiti della valutazione<br/>78808e70-9f89-5283-b1c3-be1918e4807c<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo175 result
    nodo176["Esiti della valutazione<br/>d9451c7d-8f53-513b-a4b7-e612444693f0<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo176 result
    nodo177["Esiti della valutazione<br/>9b8a22f1-fafd-5bbd-87c9-c63519d2be46<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo177 result
    nodo178["Esiti della valutazione<br/>92682466-8a38-5c94-9e5e-3087118fccbc<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo178 result
    nodo179["Esiti della valutazione<br/>fec8881c-5784-5f1f-ac03-0beb3ef00ab0<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo179 result
    nodo6 -->|"espone"| nodo8
    nodo6 -->|"tratta"| nodo5
    nodo6 -->|"è gestito da"| nodo3
    nodo19 -->|"interessa"| nodo6
    nodo6 -->|"è protetto da"| nodo17
    nodo4 -->|"dipende da"| nodo6
    nodo1 -->|"descrive"| nodo2
    nodo102 -->|"implementa"| nodo76
    nodo102 -->|"deriva da"| nodo45
    nodo103 -->|"implementa"| nodo77
    nodo103 -->|"deriva da"| nodo46
    nodo104 -->|"implementa"| nodo78
    nodo104 -->|"deriva da"| nodo47
    nodo105 -->|"implementa"| nodo79
    nodo105 -->|"deriva da"| nodo48
    nodo106 -->|"implementa"| nodo80
    nodo106 -->|"deriva da"| nodo49
    nodo107 -->|"implementa"| nodo81
    nodo107 -->|"deriva da"| nodo50
    nodo108 -->|"implementa"| nodo82
    nodo108 -->|"deriva da"| nodo51
    nodo109 -->|"implementa"| nodo83
    nodo109 -->|"deriva da"| nodo52
    nodo110 -->|"implementa"| nodo84
    nodo110 -->|"deriva da"| nodo53
    nodo111 -->|"implementa"| nodo85
    nodo111 -->|"deriva da"| nodo54
    nodo112 -->|"implementa"| nodo86
    nodo112 -->|"deriva da"| nodo55
    nodo113 -->|"implementa"| nodo87
    nodo113 -->|"deriva da"| nodo56
    nodo114 -->|"implementa"| nodo88
    nodo114 -->|"deriva da"| nodo57
    nodo115 -->|"implementa"| nodo89
    nodo115 -->|"deriva da"| nodo58
    nodo116 -->|"implementa"| nodo90
    nodo116 -->|"deriva da"| nodo59
    nodo117 -->|"implementa"| nodo91
    nodo117 -->|"deriva da"| nodo60
    nodo118 -->|"implementa"| nodo92
    nodo118 -->|"deriva da"| nodo61
    nodo119 -->|"implementa"| nodo93
    nodo119 -->|"deriva da"| nodo62
    nodo120 -->|"implementa"| nodo94
    nodo120 -->|"deriva da"| nodo63
    nodo121 -->|"implementa"| nodo95
    nodo121 -->|"deriva da"| nodo64
    nodo122 -->|"implementa"| nodo96
    nodo122 -->|"deriva da"| nodo65
    nodo123 -->|"implementa"| nodo97
    nodo123 -->|"deriva da"| nodo66
    nodo124 -->|"implementa"| nodo98
    nodo124 -->|"deriva da"| nodo67
    nodo125 -->|"implementa"| nodo99
    nodo125 -->|"deriva da"| nodo68
    nodo126 -->|"implementa"| nodo100
    nodo126 -->|"deriva da"| nodo69
    nodo127 -->|"implementa"| nodo101
    nodo127 -->|"deriva da"| nodo70
    nodo128 -->|"valuta"| nodo6
    nodo128 -->|"è esito del controllo"| nodo76
    nodo128 -->|"è riconducibile al requisito"| nodo45
    nodo128 -->|"applica la regola"| nodo102
    nodo129 -->|"valuta"| nodo6
    nodo129 -->|"è esito del controllo"| nodo77
    nodo129 -->|"è riconducibile al requisito"| nodo46
    nodo129 -->|"applica la regola"| nodo103
    nodo130 -->|"valuta"| nodo6
    nodo130 -->|"è esito del controllo"| nodo78
    nodo130 -->|"è riconducibile al requisito"| nodo47
    nodo130 -->|"applica la regola"| nodo104
    nodo131 -->|"valuta"| nodo6
    nodo131 -->|"è esito del controllo"| nodo79
    nodo131 -->|"è riconducibile al requisito"| nodo48
    nodo131 -->|"applica la regola"| nodo105
    nodo132 -->|"valuta"| nodo6
    nodo132 -->|"è esito del controllo"| nodo80
    nodo132 -->|"è riconducibile al requisito"| nodo49
    nodo132 -->|"applica la regola"| nodo106
    nodo133 -->|"valuta"| nodo6
    nodo133 -->|"è esito del controllo"| nodo81
    nodo133 -->|"è riconducibile al requisito"| nodo50
    nodo133 -->|"applica la regola"| nodo107
    nodo134 -->|"valuta"| nodo6
    nodo134 -->|"è esito del controllo"| nodo82
    nodo134 -->|"è riconducibile al requisito"| nodo51
    nodo134 -->|"applica la regola"| nodo108
    nodo135 -->|"valuta"| nodo6
    nodo135 -->|"è esito del controllo"| nodo83
    nodo135 -->|"è riconducibile al requisito"| nodo52
    nodo135 -->|"applica la regola"| nodo109
    nodo136 -->|"valuta"| nodo6
    nodo136 -->|"è esito del controllo"| nodo84
    nodo136 -->|"è riconducibile al requisito"| nodo53
    nodo136 -->|"applica la regola"| nodo110
    nodo137 -->|"valuta"| nodo6
    nodo137 -->|"è esito del controllo"| nodo85
    nodo137 -->|"è riconducibile al requisito"| nodo54
    nodo137 -->|"applica la regola"| nodo111
    nodo138 -->|"valuta"| nodo6
    nodo138 -->|"è esito del controllo"| nodo86
    nodo138 -->|"è riconducibile al requisito"| nodo55
    nodo138 -->|"applica la regola"| nodo112
    nodo139 -->|"valuta"| nodo6
    nodo139 -->|"è esito del controllo"| nodo87
    nodo139 -->|"è riconducibile al requisito"| nodo56
    nodo139 -->|"applica la regola"| nodo113
    nodo140 -->|"valuta"| nodo6
    nodo140 -->|"è esito del controllo"| nodo88
    nodo140 -->|"è riconducibile al requisito"| nodo57
    nodo140 -->|"applica la regola"| nodo114
    nodo141 -->|"valuta"| nodo6
    nodo141 -->|"è esito del controllo"| nodo89
    nodo141 -->|"è riconducibile al requisito"| nodo58
    nodo141 -->|"applica la regola"| nodo115
    nodo142 -->|"valuta"| nodo6
    nodo142 -->|"è esito del controllo"| nodo90
    nodo142 -->|"è riconducibile al requisito"| nodo59
    nodo142 -->|"applica la regola"| nodo116
    nodo143 -->|"valuta"| nodo6
    nodo143 -->|"è esito del controllo"| nodo91
    nodo143 -->|"è riconducibile al requisito"| nodo60
    nodo143 -->|"applica la regola"| nodo117
    nodo144 -->|"valuta"| nodo6
    nodo144 -->|"è esito del controllo"| nodo92
    nodo144 -->|"è riconducibile al requisito"| nodo61
    nodo144 -->|"applica la regola"| nodo118
    nodo145 -->|"valuta"| nodo6
    nodo145 -->|"è esito del controllo"| nodo93
    nodo145 -->|"è riconducibile al requisito"| nodo62
    nodo145 -->|"applica la regola"| nodo119
    nodo146 -->|"valuta"| nodo6
    nodo146 -->|"è esito del controllo"| nodo94
    nodo146 -->|"è riconducibile al requisito"| nodo63
    nodo146 -->|"applica la regola"| nodo120
    nodo147 -->|"valuta"| nodo6
    nodo147 -->|"è esito del controllo"| nodo95
    nodo147 -->|"è riconducibile al requisito"| nodo64
    nodo147 -->|"applica la regola"| nodo121
    nodo148 -->|"valuta"| nodo6
    nodo148 -->|"è esito del controllo"| nodo96
    nodo148 -->|"è riconducibile al requisito"| nodo65
    nodo148 -->|"applica la regola"| nodo122
    nodo149 -->|"valuta"| nodo6
    nodo149 -->|"è esito del controllo"| nodo97
    nodo149 -->|"è riconducibile al requisito"| nodo66
    nodo149 -->|"applica la regola"| nodo123
    nodo150 -->|"valuta"| nodo6
    nodo150 -->|"è esito del controllo"| nodo98
    nodo150 -->|"è riconducibile al requisito"| nodo67
    nodo150 -->|"applica la regola"| nodo124
    nodo151 -->|"valuta"| nodo6
    nodo151 -->|"è esito del controllo"| nodo99
    nodo151 -->|"è riconducibile al requisito"| nodo68
    nodo151 -->|"applica la regola"| nodo125
    nodo152 -->|"valuta"| nodo6
    nodo152 -->|"è esito del controllo"| nodo100
    nodo152 -->|"è riconducibile al requisito"| nodo69
    nodo152 -->|"applica la regola"| nodo126
    nodo153 -->|"valuta"| nodo6
    nodo153 -->|"è esito del controllo"| nodo101
    nodo153 -->|"è riconducibile al requisito"| nodo70
    nodo153 -->|"applica la regola"| nodo127
    nodo154 -->|"valuta"| nodo7
    nodo154 -->|"è esito del controllo"| nodo76
    nodo154 -->|"è riconducibile al requisito"| nodo45
    nodo154 -->|"applica la regola"| nodo102
    nodo155 -->|"valuta"| nodo7
    nodo155 -->|"è esito del controllo"| nodo77
    nodo155 -->|"è riconducibile al requisito"| nodo46
    nodo155 -->|"applica la regola"| nodo103
    nodo156 -->|"valuta"| nodo7
    nodo156 -->|"è esito del controllo"| nodo78
    nodo156 -->|"è riconducibile al requisito"| nodo47
    nodo156 -->|"applica la regola"| nodo104
    nodo157 -->|"valuta"| nodo7
    nodo157 -->|"è esito del controllo"| nodo79
    nodo157 -->|"è riconducibile al requisito"| nodo48
    nodo157 -->|"applica la regola"| nodo105
    nodo158 -->|"valuta"| nodo7
    nodo158 -->|"è esito del controllo"| nodo80
    nodo158 -->|"è riconducibile al requisito"| nodo49
    nodo158 -->|"applica la regola"| nodo106
    nodo159 -->|"valuta"| nodo7
    nodo159 -->|"è esito del controllo"| nodo81
    nodo159 -->|"è riconducibile al requisito"| nodo50
    nodo159 -->|"applica la regola"| nodo107
    nodo160 -->|"valuta"| nodo7
    nodo160 -->|"è esito del controllo"| nodo82
    nodo160 -->|"è riconducibile al requisito"| nodo51
    nodo160 -->|"applica la regola"| nodo108
    nodo161 -->|"valuta"| nodo7
    nodo161 -->|"è esito del controllo"| nodo83
    nodo161 -->|"è riconducibile al requisito"| nodo52
    nodo161 -->|"applica la regola"| nodo109
    nodo162 -->|"valuta"| nodo7
    nodo162 -->|"è esito del controllo"| nodo84
    nodo162 -->|"è riconducibile al requisito"| nodo53
    nodo162 -->|"applica la regola"| nodo110
    nodo163 -->|"valuta"| nodo7
    nodo163 -->|"è esito del controllo"| nodo85
    nodo163 -->|"è riconducibile al requisito"| nodo54
    nodo163 -->|"applica la regola"| nodo111
    nodo164 -->|"valuta"| nodo7
    nodo164 -->|"è esito del controllo"| nodo86
    nodo164 -->|"è riconducibile al requisito"| nodo55
    nodo164 -->|"applica la regola"| nodo112
    nodo165 -->|"valuta"| nodo7
    nodo165 -->|"è esito del controllo"| nodo87
    nodo165 -->|"è riconducibile al requisito"| nodo56
    nodo165 -->|"applica la regola"| nodo113
    nodo166 -->|"valuta"| nodo7
    nodo166 -->|"è esito del controllo"| nodo88
    nodo166 -->|"è riconducibile al requisito"| nodo57
    nodo166 -->|"applica la regola"| nodo114
    nodo167 -->|"valuta"| nodo7
    nodo167 -->|"è esito del controllo"| nodo89
    nodo167 -->|"è riconducibile al requisito"| nodo58
    nodo167 -->|"applica la regola"| nodo115
    nodo168 -->|"valuta"| nodo7
    nodo168 -->|"è esito del controllo"| nodo90
    nodo168 -->|"è riconducibile al requisito"| nodo59
    nodo168 -->|"applica la regola"| nodo116
    nodo169 -->|"valuta"| nodo7
    nodo169 -->|"è esito del controllo"| nodo91
    nodo169 -->|"è riconducibile al requisito"| nodo60
    nodo169 -->|"applica la regola"| nodo117
    nodo170 -->|"valuta"| nodo7
    nodo170 -->|"è esito del controllo"| nodo92
    nodo170 -->|"è riconducibile al requisito"| nodo61
    nodo170 -->|"applica la regola"| nodo118
    nodo171 -->|"valuta"| nodo7
    nodo171 -->|"è esito del controllo"| nodo93
    nodo171 -->|"è riconducibile al requisito"| nodo62
    nodo171 -->|"applica la regola"| nodo119
    nodo172 -->|"valuta"| nodo7
    nodo172 -->|"è esito del controllo"| nodo94
    nodo172 -->|"è riconducibile al requisito"| nodo63
    nodo172 -->|"applica la regola"| nodo120
    nodo173 -->|"valuta"| nodo7
    nodo173 -->|"è esito del controllo"| nodo95
    nodo173 -->|"è riconducibile al requisito"| nodo64
    nodo173 -->|"applica la regola"| nodo121
    nodo174 -->|"valuta"| nodo7
    nodo174 -->|"è esito del controllo"| nodo96
    nodo174 -->|"è riconducibile al requisito"| nodo65
    nodo174 -->|"applica la regola"| nodo122
    nodo175 -->|"valuta"| nodo7
    nodo175 -->|"è esito del controllo"| nodo97
    nodo175 -->|"è riconducibile al requisito"| nodo66
    nodo175 -->|"applica la regola"| nodo123
    nodo176 -->|"valuta"| nodo7
    nodo176 -->|"è esito del controllo"| nodo98
    nodo176 -->|"è riconducibile al requisito"| nodo67
    nodo176 -->|"applica la regola"| nodo124
    nodo177 -->|"valuta"| nodo7
    nodo177 -->|"è esito del controllo"| nodo99
    nodo177 -->|"è riconducibile al requisito"| nodo68
    nodo177 -->|"applica la regola"| nodo125
    nodo178 -->|"valuta"| nodo7
    nodo178 -->|"è esito del controllo"| nodo100
    nodo178 -->|"è riconducibile al requisito"| nodo69
    nodo178 -->|"applica la regola"| nodo126
    nodo179 -->|"valuta"| nodo7
    nodo179 -->|"è esito del controllo"| nodo101
    nodo179 -->|"è riconducibile al requisito"| nodo70
    nodo179 -->|"applica la regola"| nodo127
```

## Inventario completo dei nodi e delle proprietà

Ogni riga seguente riporta una proprietà già presente in Neo4j. I valori sconosciuti restano esplicitamente indicati come tali.

| Tipo | Nodo | Proprietà | Valore |
|---|---|---|---|
| Dataset | Ambiente normalizzato - Manifattura Delta (`dataset-delta-normalized-2026`) | `description` | Output sintetico dei Moduli 1 e 2 per un'organizzazione essenziale con gap critici, informazioni mancanti e una deroga tecnica attiva. Organizzazione, persone e prodotti sono inventati; i riferimenti CVE sono reali e associati a dipendenze sintetiche esclusivamente a scopo dimostrativo. |
| Dataset | Ambiente normalizzato - Manifattura Delta (`dataset-delta-normalized-2026`) | `generated_at` | 2026-08-15T11:37:00+02:00 |
| Dataset | Ambiente normalizzato - Manifattura Delta (`dataset-delta-normalized-2026`) | `id` | dataset-delta-normalized-2026 |
| Dataset | Ambiente normalizzato - Manifattura Delta (`dataset-delta-normalized-2026`) | `name` | Ambiente normalizzato - Manifattura Delta |
| Dataset | Ambiente normalizzato - Manifattura Delta (`dataset-delta-normalized-2026`) | `source_systems` | CMDB, vulnerability-manager, IAM, backup-manager, network-manager, monitoring-platform, configuration-manager |
| Organizzazione | Manifattura Delta S.p.A. (`org-delta`) | `acn_specification` | Determinazione ACN 379907/2025 - specifiche di base vigenti |
| Organizzazione | Manifattura Delta S.p.A. (`org-delta`) | `id` | org-delta |
| Organizzazione | Manifattura Delta S.p.A. (`org-delta`) | `name` | Manifattura Delta S.p.A. |
| Organizzazione | Manifattura Delta S.p.A. (`org-delta`) | `nis_profile` | essential |
| Organizzazione | Manifattura Delta S.p.A. (`org-delta`) | `risk_assessment_reference` | RISK-DELTA-2026-07 |
| Responsabili | Responsabile Operations IT/OT (`owner-delta-ops`) | `contact_reference` | role://delta-system-owner |
| Responsabili | Responsabile Operations IT/OT (`owner-delta-ops`) | `id` | owner-delta-ops |
| Responsabili | Responsabile Operations IT/OT (`owner-delta-ops`) | `name` | Responsabile Operations IT/OT |
| Responsabili | Responsabile Operations IT/OT (`owner-delta-ops`) | `provenance_ids` | prov-governance |
| Responsabili | Responsabile Operations IT/OT (`owner-delta-ops`) | `role` | system-owner |
| Processi | Controllo produzione (`proc-delta-core`) | `asset_ids` | asset-delta-core |
| Processi | Controllo produzione (`proc-delta-core`) | `criticality` | critical |
| Processi | Controllo produzione (`proc-delta-core`) | `data_object_ids` | data-delta-core |
| Processi | Controllo produzione (`proc-delta-core`) | `description` | Servizio digitale a supporto del coordinamento della produzione e delle interfacce OT. |
| Processi | Controllo produzione (`proc-delta-core`) | `id` | proc-delta-core |
| Processi | Controllo produzione (`proc-delta-core`) | `name` | Controllo produzione |
| Processi | Controllo produzione (`proc-delta-core`) | `owner_id` | owner-delta-ops |
| Processi | Controllo produzione (`proc-delta-core`) | `provenance_ids` | prov-governance |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `asset_ids` | asset-delta-core |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `classification` | restricted |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `description` | Categoria sintetica; non contiene dati reali. |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_at_rest` | False |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_at_rest_observation_type` | direct |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_at_rest_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_at_rest_provenance_ids` | prov-config |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_at_rest_status` | known |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_in_transit` | False |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_in_transit_observation_type` | direct |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_in_transit_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_in_transit_provenance_ids` | prov-config |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encrypted_in_transit_status` | known |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encryption_configuration` | legacy local keys |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encryption_configuration_observation_type` | direct |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encryption_configuration_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encryption_configuration_provenance_ids` | prov-config |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `encryption_configuration_status` | known |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `id` | data-delta-core |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `name` | Dati di produzione sintetici |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `provenance_ids` | prov-config |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media` | False |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media_encrypted_provenance_ids` | prov-config |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media_encrypted_status` | not_applicable |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media_observation_type` | direct |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media_provenance_ids` | prov-config |
| Categorie di dati | Dati di produzione sintetici (`data-delta-core`) | `removable_media_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `admin_remote_access_logging` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `admin_remote_access_logging_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `admin_remote_access_logging_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `admin_remote_access_logging_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `admin_remote_access_logging_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `anomaly_thresholds_configured` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `anomaly_thresholds_configured_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `anomaly_thresholds_configured_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `anomaly_thresholds_configured_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `anomaly_thresholds_configured_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `asset_type` | server |
| Asset | Production Integration Server (`asset-delta-core`) | `critical_software_supplier_channels_monitored_status` | unknown |
| Asset | Production Integration Server (`asset-delta-core`) | `critical_software_supplier_channels_monitored_unknown_cause` | not_collected |
| Asset | Production Integration Server (`asset-delta-core`) | `criticality` | critical |
| Asset | Production Integration Server (`asset-delta-core`) | `data_object_ids` | data-delta-core |
| Asset | Production Integration Server (`asset-delta-core`) | `description` | Server legacy di integrazione tra sistemi IT e servizi di produzione. |
| Asset | Production Integration Server (`asset-delta-core`) | `environment` | production |
| Asset | Production Integration Server (`asset-delta-core`) | `evidence_ids` | ev-delta-asset, ev-delta-software, ev-delta-flow, ev-delta-scan, ev-delta-treatment, ev-delta-accessconfig, ev-delta-encryption, ev-delta-backup, ev-delta-restore, ev-delta-system, ev-delta-patch, ev-delta-maintenance, ev-delta-log, ev-delta-network, ev-delta-emergency, ev-delta-monitoring, ev-delta-endpoint |
| Asset | Production Integration Server (`asset-delta-core`) | `exposure_level` | critical |
| Asset | Production Integration Server (`asset-delta-core`) | `extended_vulnerability_assessment_performed` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `extended_vulnerability_assessment_performed_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `extended_vulnerability_assessment_performed_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `extended_vulnerability_assessment_performed_provenance_ids` | prov-scan |
| Asset | Production Integration Server (`asset-delta-core`) | `extended_vulnerability_assessment_performed_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `firewall_enabled` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `firewall_enabled_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `firewall_enabled_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `firewall_enabled_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `firewall_enabled_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `hardening_baseline_applied` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `hardening_baseline_applied_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `hardening_baseline_applied_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `hardening_baseline_applied_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `hardening_baseline_applied_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `hardware_inventory_complete` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `hardware_inventory_complete_observation_type` | evidence_based |
| Asset | Production Integration Server (`asset-delta-core`) | `hardware_inventory_complete_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `hardware_inventory_complete_provenance_ids` | prov-inventory |
| Asset | Production Integration Server (`asset-delta-core`) | `hardware_inventory_complete_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `hostname` | integration.delta.example.invalid |
| Asset | Production Integration Server (`asset-delta-core`) | `id` | asset-delta-core |
| Asset | Production Integration Server (`asset-delta-core`) | `impact_level` | critical |
| Asset | Production Integration Server (`asset-delta-core`) | `internet_exposed` | True |
| Asset | Production Integration Server (`asset-delta-core`) | `internet_exposed_observation_type` | evidence_based |
| Asset | Production Integration Server (`asset-delta-core`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `internet_exposed_provenance_ids` | prov-inventory |
| Asset | Production Integration Server (`asset-delta-core`) | `internet_exposed_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `ip_addresses` | 203.0.113.51 |
| Asset | Production Integration Server (`asset-delta-core`) | `lifecycle_status` | active |
| Asset | Production Integration Server (`asset-delta-core`) | `log_retention_within_plan` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `log_retention_within_plan_observation_type` | declared |
| Asset | Production Integration Server (`asset-delta-core`) | `log_retention_within_plan_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `log_retention_within_plan_provenance_ids` | prov-governance |
| Asset | Production Integration Server (`asset-delta-core`) | `log_retention_within_plan_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_centralized` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_centralized_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_centralized_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_centralized_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_centralized_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_protected` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_protected_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_protected_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_protected_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `logs_protected_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `mac_addresses` | nessuna |
| Asset | Production Integration Server (`asset-delta-core`) | `maintenance_logged` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `maintenance_logged_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `maintenance_logged_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `maintenance_logged_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `maintenance_logged_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `name` | Production Integration Server |
| Asset | Production Integration Server (`asset-delta-core`) | `network_segment` | legacy-production |
| Asset | Production Integration Server (`asset-delta-core`) | `network_segment_observation_type` | evidence_based |
| Asset | Production Integration Server (`asset-delta-core`) | `network_segment_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `network_segment_provenance_ids` | prov-inventory |
| Asset | Production Integration Server (`asset-delta-core`) | `network_segment_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `nis_relevant` | True |
| Asset | Production Integration Server (`asset-delta-core`) | `nis_relevant_observation_type` | declared |
| Asset | Production Integration Server (`asset-delta-core`) | `nis_relevant_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `nis_relevant_provenance_ids` | prov-governance |
| Asset | Production Integration Server (`asset-delta-core`) | `nis_relevant_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `operating_system` | LegacyExampleOS |
| Asset | Production Integration Server (`asset-delta-core`) | `operating_system_version` | 7.4 |
| Asset | Production Integration Server (`asset-delta-core`) | `owner_id` | owner-delta-ops |
| Asset | Production Integration Server (`asset-delta-core`) | `physical_protection_documented_status` | unknown |
| Asset | Production Integration Server (`asset-delta-core`) | `physical_protection_documented_unknown_cause` | not_declared |
| Asset | Production Integration Server (`asset-delta-core`) | `process_ids` | proc-delta-core |
| Asset | Production Integration Server (`asset-delta-core`) | `provenance_ids` | prov-inventory, prov-config, prov-governance |
| Asset | Production Integration Server (`asset-delta-core`) | `provider_services_inventory_complete_status` | unknown |
| Asset | Production Integration Server (`asset-delta-core`) | `provider_services_inventory_complete_unknown_cause` | not_declared |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_protected` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_protected_observation_type` | direct |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_protected_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_protected_provenance_ids` | prov-config |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_protected_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_registry_complete` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_registry_complete_observation_type` | declared |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_registry_complete_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_registry_complete_provenance_ids` | prov-governance |
| Asset | Production Integration Server (`asset-delta-core`) | `remote_access_registry_complete_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `risk_assessment_reference` | RISK-DELTA-2026-07 |
| Asset | Production Integration Server (`asset-delta-core`) | `secure_disposal_documented` | False |
| Asset | Production Integration Server (`asset-delta-core`) | `secure_disposal_documented_observation_type` | declared |
| Asset | Production Integration Server (`asset-delta-core`) | `secure_disposal_documented_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Production Integration Server (`asset-delta-core`) | `secure_disposal_documented_provenance_ids` | prov-governance |
| Asset | Production Integration Server (`asset-delta-core`) | `secure_disposal_documented_status` | known |
| Asset | Production Integration Server (`asset-delta-core`) | `service_ids` | svc-delta-https |
| Asset | Production Integration Server (`asset-delta-core`) | `support_status` | unsupported |
| Asset | Production Integration Server (`asset-delta-core`) | `vulnerability_advisories_monitored_status` | unknown |
| Asset | Production Integration Server (`asset-delta-core`) | `vulnerability_advisories_monitored_unknown_cause` | not_collected |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `asset_type` | database |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `criticality` | medium |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `data_object_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `description` | Asset rilevato dal Modulo 1 ma escluso dal perimetro tecnico NIS. |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `environment` | production |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `evidence_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `exposure_level` | low |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `hostname` | aux-delta.example.invalid |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `id` | asset-delta-aux |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `impact_level` | medium |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `internet_exposed` | False |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `internet_exposed_observation_type` | evidence_based |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `internet_exposed_provenance_ids` | prov-inventory |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `internet_exposed_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `ip_addresses` | 203.0.113.52 |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `lifecycle_status` | active |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `mac_addresses` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `name` | Sistema ausiliario fuori perimetro NIS |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `network_segment` | auxiliary |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `network_segment_observation_type` | evidence_based |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `network_segment_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `network_segment_provenance_ids` | prov-inventory |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `network_segment_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `nis_relevant` | False |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `nis_relevant_observation_type` | declared |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `nis_relevant_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `nis_relevant_provenance_ids` | prov-governance |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `nis_relevant_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `owner_id` | owner-delta-ops |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `process_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `properties_json` | {} |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `provenance_ids` | prov-inventory, prov-governance |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `risk_assessment_reference` | RISK-DELTA-2026-07 |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `service_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-delta-aux`) | `support_status` | supported |
| Servizi | HTTPS (`svc-delta-https`) | `application_protocol` | https |
| Servizi | HTTPS (`svc-delta-https`) | `asset_id` | asset-delta-core |
| Servizi | HTTPS (`svc-delta-https`) | `authorized` | True |
| Servizi | HTTPS (`svc-delta-https`) | `authorized_observation_type` | evidence_based |
| Servizi | HTTPS (`svc-delta-https`) | `authorized_observed_at` | 2026-08-14T06:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `authorized_provenance_ids` | prov-inventory |
| Servizi | HTTPS (`svc-delta-https`) | `authorized_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `certificate_expiration` | 2027-08-14T00:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `certificate_expiration_observation_type` | direct |
| Servizi | HTTPS (`svc-delta-https`) | `certificate_expiration_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `certificate_expiration_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `certificate_expiration_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `cryptographic_baseline_id` | CRYPTO-BASELINE-2026.1 |
| Servizi | HTTPS (`svc-delta-https`) | `encrypted` | False |
| Servizi | HTTPS (`svc-delta-https`) | `encrypted_observation_type` | direct |
| Servizi | HTTPS (`svc-delta-https`) | `encrypted_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `encrypted_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `encrypted_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `encryption_configuration` | TLSv1.0 legacy |
| Servizi | HTTPS (`svc-delta-https`) | `encryption_configuration_observation_type` | direct |
| Servizi | HTTPS (`svc-delta-https`) | `encryption_configuration_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `encryption_configuration_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `encryption_configuration_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `evidence_ids` | ev-delta-encryption |
| Servizi | HTTPS (`svc-delta-https`) | `id` | svc-delta-https |
| Servizi | HTTPS (`svc-delta-https`) | `internet_exposed` | True |
| Servizi | HTTPS (`svc-delta-https`) | `internet_exposed_observation_type` | evidence_based |
| Servizi | HTTPS (`svc-delta-https`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `internet_exposed_provenance_ids` | prov-inventory |
| Servizi | HTTPS (`svc-delta-https`) | `internet_exposed_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `name` | HTTPS |
| Servizi | HTTPS (`svc-delta-https`) | `obsolete_protocol` | True |
| Servizi | HTTPS (`svc-delta-https`) | `obsolete_protocol_observation_type` | direct |
| Servizi | HTTPS (`svc-delta-https`) | `obsolete_protocol_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `obsolete_protocol_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `obsolete_protocol_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `port` | 443 |
| Servizi | HTTPS (`svc-delta-https`) | `product` | DeltaIntegrator |
| Servizi | HTTPS (`svc-delta-https`) | `protocol` | tcp |
| Servizi | HTTPS (`svc-delta-https`) | `provenance_ids` | prov-inventory, prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `tls_enabled` | True |
| Servizi | HTTPS (`svc-delta-https`) | `tls_enabled_observation_type` | direct |
| Servizi | HTTPS (`svc-delta-https`) | `tls_enabled_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `tls_enabled_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `tls_enabled_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `tls_versions` | TLSv1.0 |
| Servizi | HTTPS (`svc-delta-https`) | `tls_versions_observation_type` | direct |
| Servizi | HTTPS (`svc-delta-https`) | `tls_versions_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-delta-https`) | `tls_versions_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-delta-https`) | `tls_versions_status` | known |
| Servizi | HTTPS (`svc-delta-https`) | `transport_protocol` | tcp |
| Servizi | HTTPS (`svc-delta-https`) | `version` | 3.1 |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `asset_id` | asset-delta-core |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `authorized` | True |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `authorized_observation_type` | declared |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `authorized_observed_at` | 2026-08-10T09:00:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `authorized_provenance_ids` | prov-governance |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `authorized_status` | known |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `critical_update_tested` | False |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `critical_update_tested_observation_type` | evidence_based |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `critical_update_tested_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `critical_update_tested_provenance_ids` | prov-patch |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `critical_update_tested_status` | known |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `evidence_ids` | ev-delta-software, ev-delta-patch |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `id` | software-delta-core |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `last_security_update_at` | 2025-12-10T01:00:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `last_security_update_at_observation_type` | evidence_based |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `last_security_update_at_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `last_security_update_at_provenance_ids` | prov-patch |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `last_security_update_at_status` | known |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `name` | DeltaIntegrator |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `provenance_ids` | prov-inventory, prov-patch |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `security_update_status` | overdue_against_risk_plan |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `security_update_status_observation_type` | evidence_based |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `security_update_status_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `security_update_status_provenance_ids` | prov-patch |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `security_update_status_status` | known |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `support_status` | unsupported |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `support_status_observation_type` | evidence_based |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `support_status_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `support_status_provenance_ids` | prov-patch |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `support_status_status` | known |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `version` | 3.1 |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `version_observation_type` | evidence_based |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `version_observed_at` | 2026-08-14T06:00:00Z |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `version_provenance_ids` | prov-inventory |
| Componenti software | DeltaIntegrator (`software-delta-core`) | `version_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `account_type` | administrator |
| Utenze | account-delta-admin (`account-delta-admin`) | `asset_id` | asset-delta-core |
| Utenze | account-delta-admin (`account-delta-admin`) | `authorized` | True |
| Utenze | account-delta-admin (`account-delta-admin`) | `authorized_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `authorized_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `authorized_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `authorized_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `credentials_managed` | False |
| Utenze | account-delta-admin (`account-delta-admin`) | `credentials_managed_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `credentials_managed_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `credentials_managed_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `credentials_managed_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `evidence_ids` | ev-delta-accessconfig |
| Utenze | account-delta-admin (`account-delta-admin`) | `id` | account-delta-admin |
| Utenze | account-delta-admin (`account-delta-admin`) | `individual` | True |
| Utenze | account-delta-admin (`account-delta-admin`) | `individual_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `individual_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `individual_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `individual_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `last_reviewed_at` | 2025-11-15T09:00:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `last_reviewed_at_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `last_reviewed_at_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `last_reviewed_at_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `last_reviewed_at_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `least_privilege` | False |
| Utenze | account-delta-admin (`account-delta-admin`) | `least_privilege_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `least_privilege_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `least_privilege_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `least_privilege_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `mfa_enabled` | False |
| Utenze | account-delta-admin (`account-delta-admin`) | `mfa_enabled_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `mfa_enabled_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `mfa_enabled_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `mfa_enabled_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `privileged` | True |
| Utenze | account-delta-admin (`account-delta-admin`) | `privileged_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `privileged_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `privileged_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `privileged_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `remote_access` | True |
| Utenze | account-delta-admin (`account-delta-admin`) | `remote_access_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `remote_access_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `remote_access_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `remote_access_status` | known |
| Utenze | account-delta-admin (`account-delta-admin`) | `separate_admin_account` | False |
| Utenze | account-delta-admin (`account-delta-admin`) | `separate_admin_account_observation_type` | evidence_based |
| Utenze | account-delta-admin (`account-delta-admin`) | `separate_admin_account_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-delta-admin (`account-delta-admin`) | `separate_admin_account_provenance_ids` | prov-access |
| Utenze | account-delta-admin (`account-delta-admin`) | `separate_admin_account_status` | known |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `application_protocol` | https |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `asset_id` | asset-delta-core |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `authorized` | False |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `authorized_observation_type` | evidence_based |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `authorized_observed_at` | 2026-08-14T06:30:00Z |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `authorized_provenance_ids` | prov-network |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `authorized_status` | known |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `destination` | asset-delta-core |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `direction` | inbound |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `encrypted` | False |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `encrypted_observation_type` | evidence_based |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `encrypted_observed_at` | 2026-08-14T06:30:00Z |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `encrypted_provenance_ids` | prov-network |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `encrypted_status` | known |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `evidence_ids` | ev-delta-flow |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `id` | flow-delta-https |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `port` | 443 |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `provenance_ids` | prov-network |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `source` | internet |
| Flussi di rete | flow-delta-https (`flow-delta-https`) | `transport_protocol` | tcp |
| Backup | backup-delta-core (`backup-delta-core`) | `asset_id` | asset-delta-core |
| Backup | backup-delta-core (`backup-delta-core`) | `evidence_ids` | ev-delta-backup, ev-delta-restore |
| Backup | backup-delta-core (`backup-delta-core`) | `frequency_within_plan` | False |
| Backup | backup-delta-core (`backup-delta-core`) | `frequency_within_plan_observation_type` | evidence_based |
| Backup | backup-delta-core (`backup-delta-core`) | `frequency_within_plan_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `frequency_within_plan_provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `frequency_within_plan_status` | known |
| Backup | backup-delta-core (`backup-delta-core`) | `id` | backup-delta-core |
| Backup | backup-delta-core (`backup-delta-core`) | `last_success_at` | 2026-08-09T23:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `last_success_at_observation_type` | evidence_based |
| Backup | backup-delta-core (`backup-delta-core`) | `last_success_at_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `last_success_at_provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `last_success_at_status` | known |
| Backup | backup-delta-core (`backup-delta-core`) | `offline_copy` | False |
| Backup | backup-delta-core (`backup-delta-core`) | `offline_copy_observation_type` | evidence_based |
| Backup | backup-delta-core (`backup-delta-core`) | `offline_copy_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `offline_copy_provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `offline_copy_status` | known |
| Backup | backup-delta-core (`backup-delta-core`) | `plan_reference` | BACKUP-DELTA-2026 |
| Backup | backup-delta-core (`backup-delta-core`) | `protected_copy` | False |
| Backup | backup-delta-core (`backup-delta-core`) | `protected_copy_observation_type` | evidence_based |
| Backup | backup-delta-core (`backup-delta-core`) | `protected_copy_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `protected_copy_provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `protected_copy_status` | known |
| Backup | backup-delta-core (`backup-delta-core`) | `provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_at` | 2026-02-10T08:00:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_at_observation_type` | evidence_based |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_at_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_at_provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_at_status` | known |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_successful` | False |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_successful_observation_type` | evidence_based |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_successful_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_successful_provenance_ids` | prov-backup |
| Backup | backup-delta-core (`backup-delta-core`) | `restore_test_successful_status` | known |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `asset_id` | asset-delta-core |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `capability_type` | emergency_communications |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `configuration_reference` | EMERGENCY-COMMS-DELTA-1 |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `configured` | False |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `configured_status` | known |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `enabled` | True |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `enabled_status` | known |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `evidence_ids` | ev-delta-emergency |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `id` | cap-delta-emergency |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `maintained` | False |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `maintained_status` | known |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `monitored` | True |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `monitored_status` | known |
| Capacità di sicurezza | cap-delta-emergency (`cap-delta-emergency`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `asset_id` | asset-delta-core |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `capability_type` | intrusion_detection |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `configured` | False |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `configured_status` | known |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `enabled` | False |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `enabled_status` | known |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `evidence_ids` | ev-delta-monitoring |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `id` | cap-delta-ids |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `maintained` | True |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `maintained_status` | known |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `monitored` | False |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `monitored_status` | known |
| Capacità di sicurezza | cap-delta-ids (`cap-delta-ids`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `asset_id` | asset-delta-core |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `capability_type` | traffic_filter |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `configured` | False |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `configured_status` | known |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `enabled` | True |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `enabled_status` | known |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `evidence_ids` | ev-delta-monitoring |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `id` | cap-delta-filter |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `maintained` | True |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `maintained_status` | known |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `monitored` | False |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `monitored_status` | known |
| Capacità di sicurezza | cap-delta-filter (`cap-delta-filter`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `asset_id` | asset-delta-core |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `capability_type` | access_monitoring |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `configured` | False |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `configured_status` | known |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `enabled` | False |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `enabled_status` | known |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `evidence_ids` | ev-delta-monitoring |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `id` | cap-delta-access-monitor |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `maintained` | True |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `maintained_status` | known |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `monitored` | False |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `monitored_status` | known |
| Capacità di sicurezza | cap-delta-access-monitor (`cap-delta-access-monitor`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `asset_id` | asset-delta-core |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `capability_type` | endpoint_protection |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `configured` | False |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `configured_status` | known |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `enabled` | False |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `enabled_status` | known |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `evidence_ids` | ev-delta-endpoint |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `id` | cap-delta-endpoint |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `maintained` | False |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `maintained_status` | known |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `monitored` | False |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `monitored_status` | known |
| Capacità di sicurezza | cap-delta-endpoint (`cap-delta-endpoint`) | `provenance_ids` | prov-config |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `approval_reference` | RISK-ACCEPTANCE-DELTA-2026-03 |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `asset_id` | asset-delta-core |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `compensating_measure` | Segmentazione temporanea e controllo manuale degli accessi in attesa di sostituzione. |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `control_id` | CTRL-PR-PS-01-E |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `evidence_ids` | ev-delta-system |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `id` | exception-delta-hardening |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `provenance_ids` | prov-governance |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `rationale` | Il componente legacy non supporta la baseline di hardening corrente senza impatto sul processo produttivo. |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `residual_risk` | high |
| Deroghe tecniche | exception-delta-hardening (`exception-delta-hardening`) | `valid_until` | 2026-10-31T23:59:59Z |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `accepted_exception` | True |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `accepted_exception_observation_type` | declared |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `accepted_exception_observed_at` | 2026-08-10T09:00:00Z |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `accepted_exception_provenance_ids` | prov-governance |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `accepted_exception_status` | known |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `asset_id` | asset-delta-core |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `component` | Log4j 2.14.1 usato da DeltaIntegrator |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `cve` | CVE-2021-44228 |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `cvss_score` | 10.0 |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `description` | Riferimento CVE reale applicato, esclusivamente a scopo dimostrativo, a Log4j 2.14.1 usato dal prodotto sintetico DeltaIntegrator. |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `detected_at` | 2026-08-02T05:00:00Z |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `evidence_ids` | ev-delta-scan, ev-delta-treatment |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `id` | vuln-delta-001 |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `patch_available` | True |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `patch_available_observation_type` | direct |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `patch_available_observed_at` | 2026-08-14T05:00:00Z |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `patch_available_provenance_ids` | prov-scan |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `patch_available_status` | known |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `provenance_ids` | prov-scan, prov-patch |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `remediation_due_date` | 2026-08-12T23:59:59Z |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `remediation_status` | open |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `remediation_status_observation_type` | evidence_based |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `remediation_status_observed_at` | 2026-08-14T07:30:00Z |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `remediation_status_provenance_ids` | prov-patch |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `remediation_status_status` | known |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `service_id` | svc-delta-https |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `severity` | critical |
| Vulnerabilità | Vulnerabilità critica su dipendenza Log4j legacy (`vuln-delta-001`) | `title` | Vulnerabilità critica su dipendenza Log4j legacy |
| Evidenze | Inventario asset (`ev-delta-asset`) | `asset_ids` | asset-delta-core |
| Evidenze | Inventario asset (`ev-delta-asset`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario asset (`ev-delta-asset`) | `content_json` | {} |
| Evidenze | Inventario asset (`ev-delta-asset`) | `control_ids` | CTRL-ID-AM-01 |
| Evidenze | Inventario asset (`ev-delta-asset`) | `description` | Inventario asset acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario asset (`ev-delta-asset`) | `evidence_type` | asset_inventory |
| Evidenze | Inventario asset (`ev-delta-asset`) | `id` | ev-delta-asset |
| Evidenze | Inventario asset (`ev-delta-asset`) | `provenance_ids` | prov-inventory |
| Evidenze | Inventario asset (`ev-delta-asset`) | `reliability` | high |
| Evidenze | Inventario asset (`ev-delta-asset`) | `service_ids` | nessuna |
| Evidenze | Inventario asset (`ev-delta-asset`) | `source` | CMDB |
| Evidenze | Inventario asset (`ev-delta-asset`) | `source_category` | asset_internal |
| Evidenze | Inventario asset (`ev-delta-asset`) | `title` | Inventario asset |
| Evidenze | Inventario asset (`ev-delta-asset`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Inventario asset (`ev-delta-asset`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario software (`ev-delta-software`) | `asset_ids` | asset-delta-core |
| Evidenze | Inventario software (`ev-delta-software`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario software (`ev-delta-software`) | `content_json` | {} |
| Evidenze | Inventario software (`ev-delta-software`) | `control_ids` | CTRL-ID-AM-02, CTRL-PR-PS-02 |
| Evidenze | Inventario software (`ev-delta-software`) | `description` | Inventario software acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario software (`ev-delta-software`) | `evidence_type` | software_inventory |
| Evidenze | Inventario software (`ev-delta-software`) | `id` | ev-delta-software |
| Evidenze | Inventario software (`ev-delta-software`) | `provenance_ids` | prov-inventory |
| Evidenze | Inventario software (`ev-delta-software`) | `reliability` | high |
| Evidenze | Inventario software (`ev-delta-software`) | `service_ids` | nessuna |
| Evidenze | Inventario software (`ev-delta-software`) | `source` | CMDB |
| Evidenze | Inventario software (`ev-delta-software`) | `source_category` | asset_internal |
| Evidenze | Inventario software (`ev-delta-software`) | `title` | Inventario software |
| Evidenze | Inventario software (`ev-delta-software`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario software (`ev-delta-software`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `asset_ids` | asset-delta-core |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `content_json` | {} |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `control_ids` | CTRL-ID-AM-03-E |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `description` | Inventario flussi di rete acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `evidence_type` | network_flow_inventory |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `id` | ev-delta-flow |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `provenance_ids` | prov-network |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `reliability` | high |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `service_ids` | nessuna |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `source` | network-manager |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `source_category` | asset_internal |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `title` | Inventario flussi di rete |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario flussi di rete (`ev-delta-flow`) | `vulnerability_ids` | nessuna |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `asset_ids` | asset-delta-core |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `content_json` | {"activity_description": "Vulnerability assessment autenticato.", "cve": "CVE-2021-44228", "impact_levels": ["critical"], "nvd_url": "https://nvd.nist.gov/vuln/detail/CVE-2021-44228", "outcomes": "Relazione strutturata con scostamenti critici.", "synthetic_context": "Organizzazione e prodotto sono inventati; il CVE è reale e la sua associazione a Log4j 2.14.1 usato da DeltaIntegrator è esclusivamente dimostrativa.", "vulnerabilities": ["vuln-delta-001"]} |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `control_ids` | CTRL-ID-RA-01, CTRL-ID-RA-01-E, CTRL-ID-RA-08 |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `description` | Scansione vulnerabilità acquisita e normalizzata dai moduli 1 e 2; il prodotto e l'associazione alla dipendenza sono sintetici. |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `evidence_type` | vulnerability_scan |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `id` | ev-delta-scan |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `provenance_ids` | prov-scan |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `reliability` | high |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `service_ids` | nessuna |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `source` | vulnerability-scanner |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `source_category` | asset_internal |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `title` | Scansione vulnerabilità |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Scansione vulnerabilità (`ev-delta-scan`) | `vulnerability_ids` | vuln-delta-001 |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `asset_ids` | asset-delta-core |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `content_json` | {} |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `control_ids` | CTRL-ID-RA-08 |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `description` | Registro trattamento vulnerabilità acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `evidence_type` | vulnerability_treatment |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `id` | ev-delta-treatment |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `provenance_ids` | prov-patch |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `reliability` | high |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `service_ids` | nessuna |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `source` | vulnerability-manager |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `source_category` | asset_internal |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `title` | Registro trattamento vulnerabilità |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro trattamento vulnerabilità (`ev-delta-treatment`) | `vulnerability_ids` | vuln-delta-001 |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `asset_ids` | asset-delta-core |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `content_json` | {} |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `control_ids` | CTRL-PR-AA-03, CTRL-PR-AA-05 |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `description` | Configurazione MFA e privilegi acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `evidence_type` | access_configuration |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `id` | ev-delta-accessconfig |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `provenance_ids` | prov-access |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `reliability` | high |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `service_ids` | nessuna |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `source` | IAM |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `source_category` | asset_internal |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `title` | Configurazione MFA e privilegi |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione MFA e privilegi (`ev-delta-accessconfig`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `asset_ids` | asset-delta-core |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `content_json` | {"baseline_id": "CRYPTO-BASELINE-2026.1"} |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `control_ids` | CTRL-PR-DS-01, CTRL-PR-DS-02 |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `description` | Configurazione cifratura acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `evidence_type` | encryption_configuration |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `id` | ev-delta-encryption |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `reliability` | high |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `service_ids` | svc-delta-https |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `source` | configuration-manager |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `source_category` | asset_internal |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `title` | Configurazione cifratura |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Configurazione cifratura (`ev-delta-encryption`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro backup (`ev-delta-backup`) | `asset_ids` | asset-delta-core |
| Evidenze | Registro backup (`ev-delta-backup`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro backup (`ev-delta-backup`) | `content_json` | {"plan_reference": "BACKUP-DELTA-2026"} |
| Evidenze | Registro backup (`ev-delta-backup`) | `control_ids` | CTRL-PR-DS-11, CTRL-PR-DS-11-E |
| Evidenze | Registro backup (`ev-delta-backup`) | `description` | Registro backup acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro backup (`ev-delta-backup`) | `evidence_type` | backup_record |
| Evidenze | Registro backup (`ev-delta-backup`) | `id` | ev-delta-backup |
| Evidenze | Registro backup (`ev-delta-backup`) | `provenance_ids` | prov-backup |
| Evidenze | Registro backup (`ev-delta-backup`) | `reliability` | high |
| Evidenze | Registro backup (`ev-delta-backup`) | `service_ids` | nessuna |
| Evidenze | Registro backup (`ev-delta-backup`) | `source` | backup-manager |
| Evidenze | Registro backup (`ev-delta-backup`) | `source_category` | asset_internal |
| Evidenze | Registro backup (`ev-delta-backup`) | `title` | Registro backup |
| Evidenze | Registro backup (`ev-delta-backup`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro backup (`ev-delta-backup`) | `vulnerability_ids` | nessuna |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `asset_ids` | asset-delta-core |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `content_json` | {} |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `control_ids` | CTRL-PR-DS-11-E |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `description` | Test di ripristino acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `evidence_type` | restore_test |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `id` | ev-delta-restore |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `provenance_ids` | prov-backup |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `reliability` | high |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `service_ids` | nessuna |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `source` | backup-manager |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `source_category` | asset_internal |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `title` | Test di ripristino |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Test di ripristino (`ev-delta-restore`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `asset_ids` | asset-delta-core |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `content_json` | {} |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `control_ids` | CTRL-PR-PS-01-E |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `description` | Configurazione e hardening acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `evidence_type` | system_configuration |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `id` | ev-delta-system |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `reliability` | high |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `service_ids` | nessuna |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `source` | configuration-manager |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `source_category` | asset_internal |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `title` | Configurazione e hardening |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione e hardening (`ev-delta-system`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro patching (`ev-delta-patch`) | `asset_ids` | asset-delta-core |
| Evidenze | Registro patching (`ev-delta-patch`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro patching (`ev-delta-patch`) | `content_json` | {} |
| Evidenze | Registro patching (`ev-delta-patch`) | `control_ids` | CTRL-PR-PS-02, CTRL-PR-PS-02-E |
| Evidenze | Registro patching (`ev-delta-patch`) | `description` | Registro patching acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro patching (`ev-delta-patch`) | `evidence_type` | patch_record |
| Evidenze | Registro patching (`ev-delta-patch`) | `id` | ev-delta-patch |
| Evidenze | Registro patching (`ev-delta-patch`) | `provenance_ids` | prov-patch |
| Evidenze | Registro patching (`ev-delta-patch`) | `reliability` | high |
| Evidenze | Registro patching (`ev-delta-patch`) | `service_ids` | nessuna |
| Evidenze | Registro patching (`ev-delta-patch`) | `source` | patch-manager |
| Evidenze | Registro patching (`ev-delta-patch`) | `source_category` | asset_internal |
| Evidenze | Registro patching (`ev-delta-patch`) | `title` | Registro patching |
| Evidenze | Registro patching (`ev-delta-patch`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro patching (`ev-delta-patch`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `asset_ids` | asset-delta-core |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `content_json` | {} |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `control_ids` | CTRL-PR-PS-03-E |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `description` | Registro manutenzione acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `evidence_type` | maintenance_record |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `id` | ev-delta-maintenance |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `provenance_ids` | prov-config |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `reliability` | high |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `service_ids` | nessuna |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `source` | configuration-manager |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `source_category` | asset_internal |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `title` | Registro manutenzione |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro manutenzione (`ev-delta-maintenance`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione logging (`ev-delta-log`) | `asset_ids` | asset-delta-core |
| Evidenze | Configurazione logging (`ev-delta-log`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione logging (`ev-delta-log`) | `content_json` | {} |
| Evidenze | Configurazione logging (`ev-delta-log`) | `control_ids` | CTRL-PR-PS-04 |
| Evidenze | Configurazione logging (`ev-delta-log`) | `description` | Configurazione logging acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione logging (`ev-delta-log`) | `evidence_type` | log_configuration |
| Evidenze | Configurazione logging (`ev-delta-log`) | `id` | ev-delta-log |
| Evidenze | Configurazione logging (`ev-delta-log`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione logging (`ev-delta-log`) | `reliability` | high |
| Evidenze | Configurazione logging (`ev-delta-log`) | `service_ids` | nessuna |
| Evidenze | Configurazione logging (`ev-delta-log`) | `source` | logging-platform |
| Evidenze | Configurazione logging (`ev-delta-log`) | `source_category` | asset_internal |
| Evidenze | Configurazione logging (`ev-delta-log`) | `title` | Configurazione logging |
| Evidenze | Configurazione logging (`ev-delta-log`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione logging (`ev-delta-log`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `asset_ids` | asset-delta-core |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `content_json` | {} |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `control_ids` | CTRL-PR-IR-01 |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `description` | Configurazione accessi remoti e firewall acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `evidence_type` | network_security |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `id` | ev-delta-network |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `provenance_ids` | prov-network |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `reliability` | high |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `service_ids` | nessuna |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `source` | network-manager |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `source_category` | asset_internal |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `title` | Configurazione accessi remoti e firewall |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione accessi remoti e firewall (`ev-delta-network`) | `vulnerability_ids` | nessuna |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `asset_ids` | asset-delta-core |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `content_json` | {} |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `control_ids` | CTRL-PR-IR-03-E |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `description` | Comunicazioni di emergenza acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `evidence_type` | emergency_communications |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `id` | ev-delta-emergency |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `provenance_ids` | prov-config |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `reliability` | high |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `service_ids` | nessuna |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `source` | crisis-platform |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `source_category` | asset_internal |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `title` | Comunicazioni di emergenza |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Comunicazioni di emergenza (`ev-delta-emergency`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `asset_ids` | asset-delta-core |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `content_json` | {} |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `control_ids` | CTRL-DE-CM-01, CTRL-DE-CM-01-E |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `description` | Configurazione monitoraggio acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `evidence_type` | monitoring_configuration |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `id` | ev-delta-monitoring |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `reliability` | high |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `service_ids` | nessuna |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `source` | monitoring-platform |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `source_category` | asset_internal |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `title` | Configurazione monitoraggio |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione monitoraggio (`ev-delta-monitoring`) | `vulnerability_ids` | nessuna |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `asset_ids` | asset-delta-core |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `content_json` | {} |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `control_ids` | CTRL-DE-CM-09 |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `description` | Protezione endpoint acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `evidence_type` | endpoint_protection |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `id` | ev-delta-endpoint |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `provenance_ids` | prov-config |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `reliability` | high |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `service_ids` | nessuna |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `source` | endpoint-platform |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `source_category` | asset_internal |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `title` | Protezione endpoint |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Protezione endpoint (`ev-delta-endpoint`) | `vulnerability_ids` | nessuna |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `collected_at` | 2026-08-14T06:00:00Z |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `id` | prov-inventory |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `method` | export autenticato |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `reliability` | high |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `source` | CMDB |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-inventory (`prov-inventory`) | `source_type` | inventory |
| Fonti e provenienza | prov-config (`prov-config`) | `collected_at` | 2026-08-14T07:00:00Z |
| Fonti e provenienza | prov-config (`prov-config`) | `id` | prov-config |
| Fonti e provenienza | prov-config (`prov-config`) | `method` | raccolta automatizzata |
| Fonti e provenienza | prov-config (`prov-config`) | `reliability` | high |
| Fonti e provenienza | prov-config (`prov-config`) | `source` | configuration-manager |
| Fonti e provenienza | prov-config (`prov-config`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-config (`prov-config`) | `source_type` | configuration |
| Fonti e provenienza | prov-governance (`prov-governance`) | `collected_at` | 2026-08-10T09:00:00Z |
| Fonti e provenienza | prov-governance (`prov-governance`) | `id` | prov-governance |
| Fonti e provenienza | prov-governance (`prov-governance`) | `method` | dichiarazione approvata |
| Fonti e provenienza | prov-governance (`prov-governance`) | `reliability` | medium |
| Fonti e provenienza | prov-governance (`prov-governance`) | `source` | registro governance |
| Fonti e provenienza | prov-governance (`prov-governance`) | `source_category` | declared |
| Fonti e provenienza | prov-governance (`prov-governance`) | `source_type` | declaration |
| Fonti e provenienza | prov-scan (`prov-scan`) | `collected_at` | 2026-08-14T05:00:00Z |
| Fonti e provenienza | prov-scan (`prov-scan`) | `id` | prov-scan |
| Fonti e provenienza | prov-scan (`prov-scan`) | `method` | scansione autenticata |
| Fonti e provenienza | prov-scan (`prov-scan`) | `reliability` | high |
| Fonti e provenienza | prov-scan (`prov-scan`) | `source` | vulnerability-scanner |
| Fonti e provenienza | prov-scan (`prov-scan`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-scan (`prov-scan`) | `source_type` | scan |
| Fonti e provenienza | prov-patch (`prov-patch`) | `collected_at` | 2026-08-14T07:30:00Z |
| Fonti e provenienza | prov-patch (`prov-patch`) | `id` | prov-patch |
| Fonti e provenienza | prov-patch (`prov-patch`) | `method` | export stato |
| Fonti e provenienza | prov-patch (`prov-patch`) | `reliability` | high |
| Fonti e provenienza | prov-patch (`prov-patch`) | `source` | patch-manager |
| Fonti e provenienza | prov-patch (`prov-patch`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-patch (`prov-patch`) | `source_type` | patching |
| Fonti e provenienza | prov-access (`prov-access`) | `collected_at` | 2026-08-14T07:45:00Z |
| Fonti e provenienza | prov-access (`prov-access`) | `id` | prov-access |
| Fonti e provenienza | prov-access (`prov-access`) | `method` | export utenze |
| Fonti e provenienza | prov-access (`prov-access`) | `reliability` | high |
| Fonti e provenienza | prov-access (`prov-access`) | `source` | IAM |
| Fonti e provenienza | prov-access (`prov-access`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-access (`prov-access`) | `source_type` | identity |
| Fonti e provenienza | prov-network (`prov-network`) | `collected_at` | 2026-08-14T06:30:00Z |
| Fonti e provenienza | prov-network (`prov-network`) | `id` | prov-network |
| Fonti e provenienza | prov-network (`prov-network`) | `method` | export configurazione |
| Fonti e provenienza | prov-network (`prov-network`) | `reliability` | high |
| Fonti e provenienza | prov-network (`prov-network`) | `source` | network-manager |
| Fonti e provenienza | prov-network (`prov-network`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-network (`prov-network`) | `source_type` | network |
| Fonti e provenienza | prov-backup (`prov-backup`) | `collected_at` | 2026-08-14T03:30:00Z |
| Fonti e provenienza | prov-backup (`prov-backup`) | `id` | prov-backup |
| Fonti e provenienza | prov-backup (`prov-backup`) | `method` | export job e test |
| Fonti e provenienza | prov-backup (`prov-backup`) | `reliability` | high |
| Fonti e provenienza | prov-backup (`prov-backup`) | `source` | backup-manager |
| Fonti e provenienza | prov-backup (`prov-backup`) | `source_category` | asset_internal |
| Fonti e provenienza | prov-backup (`prov-backup`) | `source_type` | backup |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `acn_measure` | ID.AM |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `acn_point` | ID.AM-01 |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `applicable_profiles` | important, essential |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `article_24_element` | sicurezza dei sistemi e gestione del rischio |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `control_ids` | CTRL-ID-AM-01 |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `description` | Inventariare i sistemi e componenti hardware rilevanti. |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `framework` | ACN-NIS2-IT |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `id` | REQ-ID-AM-01 |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `risk_clause` | Completezza e granularità dipendono da perimetro e valutazione del rischio. |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `scope_note` | Valutazione tecnica asset-centrica. |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.AM-01 punto 1 |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `title` | Inventario hardware |
| Requisiti | Inventario hardware (`REQ-ID-AM-01`) | `verification_mode` | direct_technical |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `acn_measure` | ID.AM |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `acn_point` | ID.AM-02 |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `applicable_profiles` | important, essential |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `article_24_element` | sicurezza dei sistemi e acquisizione |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `control_ids` | CTRL-ID-AM-02 |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `description` | Inventariare software e servizi installati o erogati. |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `framework` | ACN-NIS2-IT |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `id` | REQ-ID-AM-02 |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `risk_clause` | Il livello di dettaglio è proporzionato al rischio del sistema. |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `scope_note` | Valutazione tecnica asset-centrica. |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.AM-02 punto 1 |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `title` | Inventario software e servizi |
| Requisiti | Inventario software e servizi (`REQ-ID-AM-02`) | `verification_mode` | direct_technical |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `acn_measure` | ID.AM |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `acn_point` | ID.AM-03 |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `applicable_profiles` | essential |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `article_24_element` | sicurezza delle reti e dei sistemi |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `control_ids` | CTRL-ID-AM-03-E |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `description` | Inventariare e autorizzare i flussi di rete rilevanti. |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `id` | REQ-ID-AM-03-E |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `risk_clause` | Il perimetro dei flussi deriva dall'analisi del rischio. |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `scope_note` | Requisito aggiuntivo del profilo essenziale. |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.AM-03 punto 1 |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `title` | Inventario dei flussi di rete |
| Requisiti | Inventario dei flussi di rete (`REQ-ID-AM-03-E`) | `verification_mode` | direct_technical |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `acn_measure` | ID.AM |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `acn_point` | ID.AM-04 |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `applicable_profiles` | important, essential |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `article_24_element` | sicurezza della catena di approvvigionamento |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `control_ids` | CTRL-ID-AM-04 |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `description` | Registrare i servizi dei fornitori che supportano i sistemi NIS. |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `framework` | ACN-NIS2-IT |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `id` | REQ-ID-AM-04 |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `risk_clause` | Sono inclusi i servizi pertinenti al perimetro e alle dipendenze valutate. |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `scope_note` | Il checker verifica il record tecnico; non le clausole contrattuali. |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.AM-04 punto 1 |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `title` | Servizi dei fornitori |
| Requisiti | Servizi dei fornitori (`REQ-ID-AM-04`) | `verification_mode` | evidence_assisted |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `acn_measure` | ID.RA |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `acn_point` | ID.RA-01 |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `applicable_profiles` | important, essential |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `article_24_element` | gestione delle vulnerabilità e sicurezza dei sistemi |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `control_ids` | CTRL-ID-RA-01 |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `description` | Utilizzare le informazioni dei canali pertinenti per identificare vulnerabilità sui sistemi. |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `framework` | ACN-NIS2-IT |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `id` | REQ-ID-RA-01 |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `risk_clause` | Le fonti informative sono selezionate rispetto alle tecnologie e al rischio. |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `scope_note` | Il checker osserva il monitoraggio tecnico delle fonti selezionate. |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.RA-01 punto 1 |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `title` | Identificazione delle vulnerabilità |
| Requisiti | Identificazione delle vulnerabilità (`REQ-ID-RA-01`) | `verification_mode` | direct_technical |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `acn_measure` | ID.RA |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `acn_point` | ID.RA-01 |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `applicable_profiles` | essential |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `article_24_element` | gestione delle vulnerabilità |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `control_ids` | CTRL-ID-RA-01-E |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `description` | Applicare i punti aggiuntivi del profilo essenziale alla valutazione delle vulnerabilità. |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `id` | REQ-ID-RA-01-E |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `risk_clause` | Ambito e tecniche sono stabiliti dal rischio e dallo stato dell'arte. |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `scope_note` | Requisito aggiuntivo del profilo essenziale. |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.RA-01 punti 2 e 3 |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `title` | Approfondimenti di vulnerability assessment |
| Requisiti | Approfondimenti di vulnerability assessment (`REQ-ID-RA-01-E`) | `verification_mode` | evidence_assisted |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `acn_measure` | ID.RA |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `acn_point` | ID.RA-08 |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `applicable_profiles` | important, essential |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `article_24_element` | gestione delle vulnerabilità |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `control_ids` | CTRL-ID-RA-08 |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `description` | Registrare remediation; mitigazione o rischio accettato delle vulnerabilità rilevate. |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `framework` | ACN-NIS2-IT |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `id` | REQ-ID-RA-08 |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `risk_clause` | Tempi e trattamento derivano dalla criticità e dal piano di rischio approvato. |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `scope_note` | Remediation in corso non equivale a requisito soddisfatto. |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.RA-08 punti 1 e 2 |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `title` | Trattamento delle vulnerabilità |
| Requisiti | Trattamento delle vulnerabilità (`REQ-ID-RA-08`) | `verification_mode` | direct_technical |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `acn_measure` | ID.RA |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `acn_point` | ID.RA-08 |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `applicable_profiles` | essential |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `article_24_element` | gestione delle vulnerabilità |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `control_ids` | CTRL-ID-RA-08-E |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `description` | Monitorare i canali dei fornitori del software ritenuto critico. |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `id` | REQ-ID-RA-08-E |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie in uso. |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `scope_note` | Requisito aggiuntivo del profilo essenziale. |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN ID.RA-08 punto 5 |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `title` | Canali dei fornitori del software critico |
| Requisiti | Canali dei fornitori del software critico (`REQ-ID-RA-08-E`) | `verification_mode` | evidence_assisted |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `acn_measure` | PR.AA |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `acn_point` | PR.AA-01 |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `applicable_profiles` | important, essential |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `article_24_element` | controllo dell'accesso e gestione degli attivi |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `control_ids` | CTRL-PR-AA-01 |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `description` | Gestire identità; utenze e credenziali dei sistemi rilevanti. |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `framework` | ACN-NIS2-IT |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `id` | REQ-PR-AA-01 |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `risk_clause` | Ciclo di vita e revisioni sono definiti da ruolo e rischio. |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `scope_note` | Valutazione tecnica delle utenze normalizzate. |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.AA-01 punti 1, 2 e 3 |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `title` | Identità e credenziali |
| Requisiti | Identità e credenziali (`REQ-PR-AA-01`) | `verification_mode` | direct_technical |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `acn_measure` | PR.AA |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `acn_point` | PR.AA-03 |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `applicable_profiles` | important, essential |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `article_24_element` | controllo dell'accesso e autenticazione a più fattori |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `control_ids` | CTRL-PR-AA-03 |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `description` | Applicare autenticazione adeguata e MFA quando pertinente al rischio. |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `framework` | ACN-NIS2-IT |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `id` | REQ-PR-AA-03 |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `risk_clause` | La verifica MFA si applica a utenze privilegiate o remote di sistemi NIS rilevanti secondo il rischio. |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `scope_note` | Nessuna prescrizione MFA universale è inferita. |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.AA-03 punti 1 e 2 |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `title` | Autenticazione e MFA |
| Requisiti | Autenticazione e MFA (`REQ-PR-AA-03`) | `verification_mode` | direct_technical |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `acn_measure` | PR.AA |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `acn_point` | PR.AA-05 |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `applicable_profiles` | important, essential |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `article_24_element` | controllo dell'accesso |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `control_ids` | CTRL-PR-AA-05 |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `description` | Applicare minimo privilegio e separare le utenze amministrative. |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `framework` | ACN-NIS2-IT |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `id` | REQ-PR-AA-05 |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `risk_clause` | I privilegi sono commisurati alle funzioni autorizzate. |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `scope_note` | Valutazione tecnica delle utenze privilegiate. |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.AA-05 punti 1 e 2 |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `title` | Minimo privilegio e utenze amministrative |
| Requisiti | Minimo privilegio e utenze amministrative (`REQ-PR-AA-05`) | `verification_mode` | direct_technical |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `acn_measure` | PR.AA |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `acn_point` | PR.AA-06 |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `applicable_profiles` | important, essential |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `article_24_element` | sicurezza fisica dei sistemi |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `control_ids` | CTRL-PR-AA-06 |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `description` | Documentare la protezione fisica dei sistemi rilevanti. |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `framework` | ACN-NIS2-IT |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `id` | REQ-PR-AA-06 |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `risk_clause` | Le protezioni sono proporzionate a sede, asset e minacce fisiche. |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `scope_note` | Richiede evidenza documentale e supporto alla revisione. |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.AA-06 punto 1 |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `title` | Protezione fisica |
| Requisiti | Protezione fisica (`REQ-PR-AA-06`) | `verification_mode` | evidence_assisted |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `acn_measure` | PR.DS |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `acn_point` | PR.DS-01 |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `applicable_profiles` | important, essential |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `article_24_element` | cifratura e sicurezza dei dati |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `control_ids` | CTRL-PR-DS-01 |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `description` | Cifrare i supporti rimovibili pertinenti al sistema. |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `framework` | ACN-NIS2-IT |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `id` | REQ-PR-DS-01 |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `risk_clause` | Tecniche e ambito di cifratura derivano da classificazione e rischio. |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `scope_note` | Il checker osserva configurazioni; non prescrive algoritmi universali. |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.DS-01 punto 1 |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `title` | Cifratura dei supporti rimovibili |
| Requisiti | Cifratura dei supporti rimovibili (`REQ-PR-DS-01`) | `verification_mode` | direct_technical |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `acn_measure` | PR.DS |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `acn_point` | PR.DS-02 |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `applicable_profiles` | important, essential |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `article_24_element` | cifratura e sicurezza delle comunicazioni |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `control_ids` | CTRL-PR-DS-02 |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `description` | Proteggere i dati trasmessi sui flussi pertinenti. |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `framework` | ACN-NIS2-IT |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `id` | REQ-PR-DS-02 |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline crittografica versionata dichiarata. |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `scope_note` | La baseline crittografica è tecnica e non è presentata come testo NIS2. |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.DS-02 punto 1 |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `title` | Protezione dei dati in transito |
| Requisiti | Protezione dei dati in transito (`REQ-PR-DS-02`) | `verification_mode` | direct_technical |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `acn_measure` | PR.DS |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `acn_point` | PR.DS-11 |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `applicable_profiles` | important, essential |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `article_24_element` | continuità operativa backup e ripristino |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `control_ids` | CTRL-PR-DS-11 |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `description` | Eseguire backup periodici e conservarne copie offline per i sistemi rilevanti. |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `framework` | ACN-NIS2-IT |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `id` | REQ-PR-DS-11 |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino approvati. |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `scope_note` | Nessuna soglia temporale universale è codificata. |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.DS-11 punto 1 |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `title` | Backup periodici e copie offline |
| Requisiti | Backup periodici e copie offline (`REQ-PR-DS-11`) | `verification_mode` | direct_technical |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `acn_measure` | PR.DS |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `acn_point` | PR.DS-11 |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `applicable_profiles` | essential |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `article_24_element` | continuità operativa e ripristino |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `control_ids` | CTRL-PR-DS-11-E |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `description` | Proteggere i backup e verificarne periodicamente l'utilizzabilità mediante test di ripristino. |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `id` | REQ-PR-DS-11-E |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `risk_clause` | Le modalità di separazione sono definite rispetto agli scenari di perdita. |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `scope_note` | Requisito aggiuntivo del profilo essenziale. |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.DS-11 punti 3 e 4 |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `title` | Protezione e test dei backup |
| Requisiti | Protezione e test dei backup (`REQ-PR-DS-11-E`) | `verification_mode` | direct_technical |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `acn_measure` | PR.PS |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `acn_point` | PR.PS-01 |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `applicable_profiles` | essential |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `article_24_element` | sicurezza acquisizione sviluppo e manutenzione |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `control_ids` | CTRL-PR-PS-01-E |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `description` | Applicare configurazioni sicure e baseline di hardening ai sistemi rilevanti. |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `id` | REQ-PR-PS-01-E |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `risk_clause` | La baseline applicata è versionata e adeguata alla tecnologia. |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `scope_note` | Requisito del profilo essenziale. |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.PS-01 punto 1 |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `title` | Hardening |
| Requisiti | Hardening (`REQ-PR-PS-01-E`) | `verification_mode` | direct_technical |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `acn_measure` | PR.PS |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `acn_point` | PR.PS-02 |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `applicable_profiles` | important, essential |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `article_24_element` | gestione delle vulnerabilità e manutenzione |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `control_ids` | CTRL-PR-PS-02 |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `description` | Usare software supportato e applicare aggiornamenti secondo il piano di rischio. |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `framework` | ACN-NIS2-IT |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `id` | REQ-PR-PS-02 |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `risk_clause` | Le tempistiche di patching sono quelle del piano di rischio dichiarato. |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `scope_note` | Nessun numero di giorni è assunto come obbligo NIS2. |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.PS-02 punti 1 e 2 |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `title` | Software supportato e aggiornato |
| Requisiti | Software supportato e aggiornato (`REQ-PR-PS-02`) | `verification_mode` | direct_technical |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `acn_measure` | PR.PS |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `acn_point` | PR.PS-02 |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `applicable_profiles` | essential |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `article_24_element` | sicurezza della manutenzione |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `control_ids` | CTRL-PR-PS-02-E |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `description` | Verificare i punti aggiuntivi essenziali per il test delle patch critiche. |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `id` | REQ-PR-PS-02-E |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `risk_clause` | Modalità e ambiente di test dipendono da rischio e compatibilità. |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `scope_note` | Requisito aggiuntivo del profilo essenziale. |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.PS-02 punto 4 |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `title` | Test degli aggiornamenti critici |
| Requisiti | Test degli aggiornamenti critici (`REQ-PR-PS-02-E`) | `verification_mode` | direct_technical |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `acn_measure` | PR.PS |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `acn_point` | PR.PS-03 |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `applicable_profiles` | essential |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `article_24_element` | manutenzione sicura |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `control_ids` | CTRL-PR-PS-03-E |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `description` | Tracciare manutenzione e dismettere in sicurezza sistemi e supporti. |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `id` | REQ-PR-PS-03-E |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `risk_clause` | Procedure e tecniche di cancellazione dipendono da supporto e dati. |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `scope_note` | Requisito del profilo essenziale. |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.PS-03 punti 1 e 2 |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `title` | Manutenzione e dismissione sicura |
| Requisiti | Manutenzione e dismissione sicura (`REQ-PR-PS-03-E`) | `verification_mode` | evidence_assisted |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `acn_measure` | PR.PS |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `acn_point` | PR.PS-04 |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `applicable_profiles` | important, essential |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `article_24_element` | verifica efficacia e gestione degli incidenti |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `control_ids` | CTRL-PR-PS-04 |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `description` | Registrare accessi amministrativi e remoti e proteggere i log. |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `framework` | ACN-NIS2-IT |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `id` | REQ-PR-PS-04 |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `risk_clause` | Eventi e retention sono definiti dalla valutazione del rischio e dal piano di logging. |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `scope_note` | Logging generico senza accessi amministrativi/remoti non è sufficiente. |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.PS-04 punti 1, 2 e 3 |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `title` | Logging di sicurezza |
| Requisiti | Logging di sicurezza (`REQ-PR-PS-04`) | `verification_mode` | direct_technical |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `acn_measure` | PR.IR |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `acn_point` | PR.IR-01 |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `applicable_profiles` | important, essential |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `article_24_element` | sicurezza delle reti e controllo accessi |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `control_ids` | CTRL-PR-IR-01 |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `description` | Governare accessi remoti e proteggere i confini di rete. |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `framework` | ACN-NIS2-IT |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `id` | REQ-PR-IR-01 |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `risk_clause` | Regole e canali remoti sono commisurati a esposizione e rischio. |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `scope_note` | Valutazione delle configurazioni osservate. |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.IR-01 punti 1, 2 e 3 |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `title` | Accesso remoto e firewall |
| Requisiti | Accesso remoto e firewall (`REQ-PR-IR-01`) | `verification_mode` | direct_technical |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `acn_measure` | PR.IR |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `acn_point` | PR.IR-03 |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `applicable_profiles` | essential |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `article_24_element` | continuità operativa e comunicazioni di crisi |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `control_ids` | CTRL-PR-IR-03-E |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `description` | Predisporre capacità tecniche protette per le comunicazioni di emergenza. |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `id` | REQ-PR-IR-03-E |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `scope_note` | Requisito del profilo essenziale. |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.IR-03 punto 1 |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `title` | Comunicazioni di emergenza protette |
| Requisiti | Comunicazioni di emergenza protette (`REQ-PR-IR-03-E`) | `verification_mode` | evidence_assisted |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `acn_measure` | DE.CM |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `acn_point` | DE.CM-01 |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `applicable_profiles` | important, essential |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `article_24_element` | gestione e rilevamento degli incidenti |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `control_ids` | CTRL-DE-CM-01 |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `description` | Mantenere configurati e monitorati gli strumenti tecnici per rilevare tempestivamente gli incidenti significativi. |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `framework` | ACN-NIS2-IT |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `id` | REQ-DE-CM-01 |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `risk_clause` | Copertura e regole di rilevamento sono basate su architettura e rischio. |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `scope_note` | Valutazione di capacità tecniche osservabili. |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN DE.CM-01 punto 1 |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `title` | Strumenti per il rilevamento degli incidenti |
| Requisiti | Strumenti per il rilevamento degli incidenti (`REQ-DE-CM-01`) | `verification_mode` | direct_technical |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `acn_measure` | DE.CM |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `acn_point` | DE.CM-01 |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `applicable_profiles` | essential |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `article_24_element` | rilevamento degli incidenti |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `control_ids` | CTRL-DE-CM-01-E |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `description` | Applicare i punti aggiuntivi essenziali per soglie; anomalie e capacità di rilevamento. |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `framework` | ACN-NIS2-IT |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `id` | REQ-DE-CM-01-E |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e sul rischio. |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `scope_note` | Requisito aggiuntivo del profilo essenziale. |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN DE.CM-01 punto 6 |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `title` | Monitoraggio avanzato |
| Requisiti | Monitoraggio avanzato (`REQ-DE-CM-01-E`) | `verification_mode` | direct_technical |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `acn_measure` | DE.CM |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `acn_point` | DE.CM-09 |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `applicable_profiles` | important, essential |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `article_24_element` | prevenzione e rilevamento degli incidenti |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `control_ids` | CTRL-DE-CM-09 |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `description` | Proteggere e monitorare gli endpoint rilevanti. |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `framework` | ACN-NIS2-IT |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `id` | REQ-DE-CM-09 |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `risk_clause` | La capacità richiesta dipende dal tipo di endpoint e dal rischio. |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `scope_note` | Valutazione della capacità tecnica osservata. |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN DE.CM-09 punto 1 |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `title` | Protezione endpoint |
| Requisiti | Protezione endpoint (`REQ-DE-CM-09`) | `verification_mode` | direct_technical |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `acn_measure` | GV.PO |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `acn_point` | GV.PO-01 |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `applicable_profiles` | important, essential |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `article_24_element` | politiche di analisi dei rischi |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `control_ids` | nessuna |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `description` | Adozione e riesame delle politiche di gestione del rischio. |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `framework` | ACN-NIS2-IT |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `id` | REQ-MANUAL-POLICIES |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `manual_only_reason` | Richiede giudizio organizzativo e approvazione della governance. |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `risk_clause` | Valutazione organizzativa fuori dal perimetro del checker. |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `scope_note` | Documentato ma non valutato. |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN GV.PO-01 punti 1, 2 e 3 |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `title` | Politiche di sicurezza |
| Requisiti | Politiche di sicurezza (`REQ-MANUAL-POLICIES`) | `verification_mode` | manual_only |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `acn_measure` | PR.AT |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `acn_point` | PR.AT-01 |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `applicable_profiles` | important, essential |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `article_24_element` | formazione in materia di sicurezza informatica |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `control_ids` | nessuna |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `description` | Formazione in materia di sicurezza informatica. |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `framework` | ACN-NIS2-IT |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `id` | REQ-MANUAL-TRAINING |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `manual_only_reason` | Presenza e qualità della formazione richiedono verifica organizzativa. |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `risk_clause` | Programma proporzionato a ruoli e rischio. |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `scope_note` | Documentato ma non valutato. |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN PR.AT-01 punti 1, 2 e 3 |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `title` | Formazione e sensibilizzazione |
| Requisiti | Formazione e sensibilizzazione (`REQ-MANUAL-TRAINING`) | `verification_mode` | manual_only |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `acn_measure` | GV.SC |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `acn_point` | GV.SC-01 |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `applicable_profiles` | important, essential |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `article_24_element` | sicurezza della catena di approvvigionamento |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `control_ids` | nessuna |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `description` | Valutare e governare la sicurezza dei rapporti con i fornitori. |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `framework` | ACN-NIS2-IT |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `id` | REQ-MANUAL-SUPPLY |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `manual_only_reason` | Contratti e governance fornitori non sono verificabili a livello di asset. |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `risk_clause` | Profondità della due diligence basata sul rischio fornitore. |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `scope_note` | Documentato ma non valutato. |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN GV.SC-01 punto 1 (punto 2 per il solo profilo essenziale) |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `title` | Gestione contrattuale della supply chain |
| Requisiti | Gestione contrattuale della supply chain (`REQ-MANUAL-SUPPLY`) | `verification_mode` | manual_only |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `acn_measure` | RS.MA |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `acn_point` | RS.MA-01 |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `applicable_profiles` | important, essential |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `article_24_element` | gestione degli incidenti |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `control_ids` | nessuna |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `description` | Definire ruoli procedure e piani di risposta agli incidenti. |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `framework` | ACN-NIS2-IT |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `id` | REQ-MANUAL-INCIDENT |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `manual_only_reason` | Efficacia e responsabilità del piano richiedono revisione umana. |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `risk_clause` | Piano proporzionato agli scenari di incidente. |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `scope_note` | Documentato ma non valutato. |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN RS.MA-01 punti 1, 2 e 3 |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `title` | Piano di risposta agli incidenti |
| Requisiti | Piano di risposta agli incidenti (`REQ-MANUAL-INCIDENT`) | `verification_mode` | manual_only |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `acn_measure` | RC.RP |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `acn_point` | RC.RP-01 |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `applicable_profiles` | important, essential |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `article_24_element` | continuità operativa disaster recovery e gestione delle crisi |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `control_ids` | nessuna |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `description` | Governare continuità operativa disaster recovery e gestione delle crisi. |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `framework` | ACN-NIS2-IT |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `id` | REQ-MANUAL-BCP |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `manual_only_reason` | Il checker verifica singole capacità tecniche ma non l'adeguatezza del piano complessivo. |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `risk_clause` | Obiettivi e piani derivano dall'analisi d'impatto e dal rischio. |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `scope_note` | Documentato ma non valutato. |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `source_document` | Determinazione ACN 379907/2025 |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `source_reference` | D.Lgs. 138/2024 art. 24; ACN RC.RP-01 punto 1 |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `source_url` | https://www.acn.gov.it/portale/nis/la-normativa |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `source_version` | specifiche di base vigenti acquisite 2026-08-14 |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `title` | Continuità operativa e crisi |
| Requisiti | Continuità operativa e crisi (`REQ-MANUAL-BCP`) | `verification_mode` | manual_only |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `description` | Controllo tecnico normalizzato per inventario hardware. |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `id` | CTRL-ID-AM-01 |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `relevant_system_required` | True |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `required_evidence_types` | asset_inventory |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `required_properties` | asset.hardware_inventory_complete |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `requirement_id` | REQ-ID-AM-01 |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `rule_ids` | RULE-ID-AM-01 |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `technical_area` | asset_management |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `title` | Inventario hardware |
| Controlli tecnici | Inventario hardware (`CTRL-ID-AM-01`) | `verification_mode` | direct_technical |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `description` | Controllo tecnico normalizzato per inventario software e servizi. |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `id` | CTRL-ID-AM-02 |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `relevant_system_required` | True |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `required_evidence_types` | software_inventory |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `required_properties` | software_component.version, software_component.authorized |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `requirement_id` | REQ-ID-AM-02 |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `rule_ids` | RULE-ID-AM-02 |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `technical_area` | asset_management |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `title` | Inventario software e servizi |
| Controlli tecnici | Inventario software e servizi (`CTRL-ID-AM-02`) | `verification_mode` | direct_technical |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `description` | Controllo tecnico normalizzato per inventario dei flussi di rete. |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `id` | CTRL-ID-AM-03-E |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `relevant_system_required` | True |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `required_evidence_types` | network_flow_inventory |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `required_properties` | network_flow.authorized |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `requirement_id` | REQ-ID-AM-03-E |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `rule_ids` | RULE-ID-AM-03-E |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `technical_area` | asset_management |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `title` | Inventario dei flussi di rete |
| Controlli tecnici | Inventario dei flussi di rete (`CTRL-ID-AM-03-E`) | `verification_mode` | direct_technical |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `description` | Controllo tecnico normalizzato per servizi dei fornitori. |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `id` | CTRL-ID-AM-04 |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `relevant_system_required` | True |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `required_evidence_types` | provider_service_inventory |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `required_properties` | asset.provider_services_inventory_complete |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `requirement_id` | REQ-ID-AM-04 |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `rule_ids` | RULE-ID-AM-04 |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `technical_area` | supply_chain_technical |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `title` | Servizi dei fornitori |
| Controlli tecnici | Servizi dei fornitori (`CTRL-ID-AM-04`) | `verification_mode` | evidence_assisted |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `description` | Controllo tecnico normalizzato per valutazione delle vulnerabilità. |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `id` | CTRL-ID-RA-01 |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `relevant_system_required` | True |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `required_evidence_types` | vulnerability_management |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `required_properties` | asset.vulnerability_advisories_monitored |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `requirement_id` | REQ-ID-RA-01 |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `rule_ids` | RULE-ID-RA-01 |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `technical_area` | vulnerability_management |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `title` | Valutazione delle vulnerabilità |
| Controlli tecnici | Valutazione delle vulnerabilità (`CTRL-ID-RA-01`) | `verification_mode` | direct_technical |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `description` | Controllo tecnico normalizzato per assessment approfondito delle vulnerabilità. |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `id` | CTRL-ID-RA-01-E |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `relevant_system_required` | True |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `required_evidence_types` | vulnerability_scan |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `required_properties` | asset.extended_vulnerability_assessment_performed |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `requirement_id` | REQ-ID-RA-01-E |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `rule_ids` | RULE-ID-RA-01-E |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `technical_area` | vulnerability_management |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `title` | Assessment approfondito delle vulnerabilità |
| Controlli tecnici | Assessment approfondito delle vulnerabilità (`CTRL-ID-RA-01-E`) | `verification_mode` | evidence_assisted |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `description` | Controllo tecnico normalizzato per trattamento delle vulnerabilità. |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `id` | CTRL-ID-RA-08 |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `relevant_system_required` | True |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `required_evidence_types` | vulnerability_management, vulnerability_treatment |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `required_properties` | asset.vulnerability_advisories_monitored, vulnerability.remediation_status |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `requirement_id` | REQ-ID-RA-08 |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `rule_ids` | RULE-ID-RA-08 |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `technical_area` | vulnerability_management |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `title` | Trattamento delle vulnerabilità |
| Controlli tecnici | Trattamento delle vulnerabilità (`CTRL-ID-RA-08`) | `verification_mode` | direct_technical |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `description` | Controllo tecnico normalizzato per monitoraggio avanzato delle vulnerabilità. |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `id` | CTRL-ID-RA-08-E |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `relevant_system_required` | True |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `required_evidence_types` | vulnerability_management |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `required_properties` | asset.critical_software_supplier_channels_monitored |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `requirement_id` | REQ-ID-RA-08-E |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `rule_ids` | RULE-ID-RA-08-E |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `technical_area` | vulnerability_management |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `title` | Monitoraggio avanzato delle vulnerabilità |
| Controlli tecnici | Monitoraggio avanzato delle vulnerabilità (`CTRL-ID-RA-08-E`) | `verification_mode` | evidence_assisted |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `description` | Controllo tecnico normalizzato per identità e credenziali. |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `id` | CTRL-PR-AA-01 |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `relevant_system_required` | True |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `required_evidence_types` | access_review |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `required_properties` | account.individual, account.authorized, account.credentials_managed |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `requirement_id` | REQ-PR-AA-01 |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `rule_ids` | RULE-PR-AA-01 |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `technical_area` | access_control |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `title` | Identità e credenziali |
| Controlli tecnici | Identità e credenziali (`CTRL-PR-AA-01`) | `verification_mode` | direct_technical |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `description` | Controllo tecnico normalizzato per autenticazione e mfa. |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `id` | CTRL-PR-AA-03 |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `relevant_system_required` | True |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `required_evidence_types` | access_configuration |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `required_properties` | account.mfa_enabled |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `requirement_id` | REQ-PR-AA-03 |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `rule_ids` | RULE-PR-AA-03 |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `technical_area` | access_control |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `title` | Autenticazione e MFA |
| Controlli tecnici | Autenticazione e MFA (`CTRL-PR-AA-03`) | `verification_mode` | direct_technical |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `description` | Controllo tecnico normalizzato per minimo privilegio e account amministrativi. |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `id` | CTRL-PR-AA-05 |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `relevant_system_required` | True |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `required_evidence_types` | access_configuration |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `required_properties` | account.least_privilege, account.separate_admin_account |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `requirement_id` | REQ-PR-AA-05 |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `rule_ids` | RULE-PR-AA-05 |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `technical_area` | access_control |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `title` | Minimo privilegio e account amministrativi |
| Controlli tecnici | Minimo privilegio e account amministrativi (`CTRL-PR-AA-05`) | `verification_mode` | direct_technical |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `description` | Controllo tecnico normalizzato per protezione fisica. |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `id` | CTRL-PR-AA-06 |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `relevant_system_required` | True |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `required_evidence_types` | physical_security |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `required_properties` | asset.physical_protection_documented |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `requirement_id` | REQ-PR-AA-06 |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `rule_ids` | RULE-PR-AA-06 |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `technical_area` | physical_security |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `title` | Protezione fisica |
| Controlli tecnici | Protezione fisica (`CTRL-PR-AA-06`) | `verification_mode` | evidence_assisted |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `description` | Controllo tecnico normalizzato per protezione dei dati a riposo. |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `id` | CTRL-PR-DS-01 |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `relevant_system_required` | True |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `required_evidence_types` | encryption_configuration |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `required_properties` | nessuna |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `requirement_id` | REQ-PR-DS-01 |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `rule_ids` | RULE-PR-DS-01 |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `technical_area` | data_protection |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `title` | Protezione dei dati a riposo |
| Controlli tecnici | Protezione dei dati a riposo (`CTRL-PR-DS-01`) | `verification_mode` | direct_technical |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `description` | Controllo tecnico normalizzato per protezione dei dati in transito. |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `id` | CTRL-PR-DS-02 |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `relevant_system_required` | True |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `required_evidence_types` | encryption_configuration |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `required_properties` | service.encrypted, service.tls_enabled, service.tls_versions |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `requirement_id` | REQ-PR-DS-02 |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `rule_ids` | RULE-PR-DS-02 |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `technical_area` | cryptography |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `title` | Protezione dei dati in transito |
| Controlli tecnici | Protezione dei dati in transito (`CTRL-PR-DS-02`) | `verification_mode` | direct_technical |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `description` | Controllo tecnico normalizzato per backup e ripristino. |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `id` | CTRL-PR-DS-11 |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `relevant_system_required` | True |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `required_evidence_types` | backup_record |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `required_properties` | backup.frequency_within_plan, backup.offline_copy |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `requirement_id` | REQ-PR-DS-11 |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `rule_ids` | RULE-PR-DS-11 |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `technical_area` | backup_recovery |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `title` | Backup e ripristino |
| Controlli tecnici | Backup e ripristino (`CTRL-PR-DS-11`) | `verification_mode` | direct_technical |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `description` | Controllo tecnico normalizzato per separazione delle copie di backup. |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `id` | CTRL-PR-DS-11-E |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `relevant_system_required` | True |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `required_evidence_types` | backup_record, restore_test |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `required_properties` | backup.protected_copy, backup.restore_test_successful |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `requirement_id` | REQ-PR-DS-11-E |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `rule_ids` | RULE-PR-DS-11-E |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `technical_area` | backup_recovery |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `title` | Separazione delle copie di backup |
| Controlli tecnici | Separazione delle copie di backup (`CTRL-PR-DS-11-E`) | `verification_mode` | direct_technical |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `description` | Controllo tecnico normalizzato per baseline di hardening. |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `id` | CTRL-PR-PS-01-E |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `relevant_system_required` | True |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `required_evidence_types` | system_configuration |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `required_properties` | asset.hardening_baseline_applied |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `requirement_id` | REQ-PR-PS-01-E |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `rule_ids` | RULE-PR-PS-01-E |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `technical_area` | system_security |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `title` | Baseline di hardening |
| Controlli tecnici | Baseline di hardening (`CTRL-PR-PS-01-E`) | `verification_mode` | direct_technical |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `description` | Controllo tecnico normalizzato per software supportato e aggiornato. |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `id` | CTRL-PR-PS-02 |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `relevant_system_required` | True |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `required_evidence_types` | software_inventory, patch_record |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `required_properties` | software_component.support_status, software_component.security_update_status |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `requirement_id` | REQ-PR-PS-02 |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `rule_ids` | RULE-PR-PS-02 |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `technical_area` | patch_management |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `title` | Software supportato e aggiornato |
| Controlli tecnici | Software supportato e aggiornato (`CTRL-PR-PS-02`) | `verification_mode` | direct_technical |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `description` | Controllo tecnico normalizzato per test degli aggiornamenti critici. |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `id` | CTRL-PR-PS-02-E |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `relevant_system_required` | True |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `required_evidence_types` | patch_record |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `required_properties` | software_component.support_status, software_component.security_update_status, software_component.critical_update_tested |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `requirement_id` | REQ-PR-PS-02-E |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `rule_ids` | RULE-PR-PS-02-E |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `technical_area` | patch_management |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `title` | Test degli aggiornamenti critici |
| Controlli tecnici | Test degli aggiornamenti critici (`CTRL-PR-PS-02-E`) | `verification_mode` | direct_technical |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `description` | Controllo tecnico normalizzato per manutenzione e dismissione sicura. |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `id` | CTRL-PR-PS-03-E |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `relevant_system_required` | True |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `required_evidence_types` | maintenance_record |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `required_properties` | asset.maintenance_logged, asset.secure_disposal_documented |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `requirement_id` | REQ-PR-PS-03-E |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `rule_ids` | RULE-PR-PS-03-E |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `technical_area` | system_security |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `title` | Manutenzione e dismissione sicura |
| Controlli tecnici | Manutenzione e dismissione sicura (`CTRL-PR-PS-03-E`) | `verification_mode` | evidence_assisted |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `description` | Controllo tecnico normalizzato per logging di sicurezza. |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `id` | CTRL-PR-PS-04 |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `relevant_system_required` | True |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `required_evidence_types` | log_configuration |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `required_properties` | asset.admin_remote_access_logging, asset.logs_protected, asset.logs_centralized, asset.log_retention_within_plan |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `requirement_id` | REQ-PR-PS-04 |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `rule_ids` | RULE-PR-PS-04 |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `technical_area` | logging_monitoring |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `title` | Logging di sicurezza |
| Controlli tecnici | Logging di sicurezza (`CTRL-PR-PS-04`) | `verification_mode` | direct_technical |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `description` | Controllo tecnico normalizzato per accesso remoto e firewall. |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `id` | CTRL-PR-IR-01 |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `relevant_system_required` | True |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `required_evidence_types` | network_security |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `required_properties` | asset.remote_access_registry_complete, asset.remote_access_protected, asset.firewall_enabled |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `requirement_id` | REQ-PR-IR-01 |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `rule_ids` | RULE-PR-IR-01 |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `technical_area` | network_security |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `title` | Accesso remoto e firewall |
| Controlli tecnici | Accesso remoto e firewall (`CTRL-PR-IR-01`) | `verification_mode` | direct_technical |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `description` | Controllo tecnico normalizzato per comunicazioni di emergenza protette. |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `id` | CTRL-PR-IR-03-E |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `relevant_system_required` | True |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `required_evidence_types` | emergency_communications |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `required_properties` | security_capability.enabled, security_capability.configured, security_capability.maintained |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `requirement_id` | REQ-PR-IR-03-E |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `rule_ids` | RULE-PR-IR-03-E |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `technical_area` | emergency_communications |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `title` | Comunicazioni di emergenza protette |
| Controlli tecnici | Comunicazioni di emergenza protette (`CTRL-PR-IR-03-E`) | `verification_mode` | evidence_assisted |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `description` | Controllo tecnico normalizzato per monitoraggio di rete e accessi. |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `id` | CTRL-DE-CM-01 |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `relevant_system_required` | True |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `required_evidence_types` | monitoring_configuration |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `required_properties` | security_capability.enabled, security_capability.configured, security_capability.monitored |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `requirement_id` | REQ-DE-CM-01 |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `rule_ids` | RULE-DE-CM-01 |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `technical_area` | security_monitoring |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `title` | Monitoraggio di rete e accessi |
| Controlli tecnici | Monitoraggio di rete e accessi (`CTRL-DE-CM-01`) | `verification_mode` | direct_technical |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `applicable_profiles` | essential |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `description` | Controllo tecnico normalizzato per monitoraggio avanzato. |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `id` | CTRL-DE-CM-01-E |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `relevant_system_required` | True |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `required_evidence_types` | monitoring_configuration |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `required_properties` | asset.anomaly_thresholds_configured |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `requirement_id` | REQ-DE-CM-01-E |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `rule_ids` | RULE-DE-CM-01-E |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `technical_area` | security_monitoring |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `title` | Monitoraggio avanzato |
| Controlli tecnici | Monitoraggio avanzato (`CTRL-DE-CM-01-E`) | `verification_mode` | direct_technical |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `applicable_asset_types` | server, workstation, network_device, application, database, cloud_service, storage, virtual_machine, container_host, security_device, other |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `applicable_profiles` | important, essential |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `description` | Controllo tecnico normalizzato per protezione endpoint. |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `id` | CTRL-DE-CM-09 |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `relevant_system_required` | True |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `required_evidence_types` | endpoint_protection |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `required_properties` | security_capability.enabled, security_capability.configured, security_capability.maintained, security_capability.monitored |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `requirement_id` | REQ-DE-CM-09 |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `rule_ids` | RULE-DE-CM-09 |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `technical_area` | endpoint_security |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `title` | Protezione endpoint |
| Controlli tecnici | Protezione endpoint (`CTRL-DE-CM-09`) | `verification_mode` | direct_technical |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `applicability_json` | {} |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `conditions_json` | [{"id": "RULE-ID-AM-01:asset.hardware_inventory_complete", "mandatory": true, "origin": "regulatory", "path": "asset.hardware_inventory_complete", "remediation": "Completare e validare il record inventariale dell'asset.", "selector": {}}] |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `control_id` | CTRL-ID-AM-01 |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `description` | Verifica che il sistema NIS rilevante sia presente nell'inventario tecnico qualificato. |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `evaluator` | asset_properties |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `id` | RULE-ID-AM-01 |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `parameters_json` | {"properties": ["hardware_inventory_complete"]} |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `recommendation` | Completare e validare il record inventariale dell'asset. |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `relevant_system_required` | True |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `required_evidence_types` | asset_inventory |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `required_properties` | asset.hardware_inventory_complete |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `requirement_id` | REQ-ID-AM-01 |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `title` | Completezza inventario hardware |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `verification_mode` | direct_technical |
| Regole di valutazione | Completezza inventario hardware (`RULE-ID-AM-01`) | `version` | 2.1.0 |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `applicability_json` | {} |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `conditions_json` | [{"id": "AM02-SYSTEM", "mandatory": true, "origin": "regulatory", "path": "Asset.name", "remediation": "Identificare il sistema nel registro inventariale.", "selector": {}}, {"id": "AM02-SERVICE", "mandatory": true, "origin": "regulatory", "path": "Service.authorized", "remediation": "Censire e autorizzare i servizi erogati.", "selector": {}}, {"id": "AM02-SOFTWARE-NAME", "mandatory": true, "origin": "regulatory", "path": "SoftwareComponent.name", "remediation": "Identificare ogni componente software.", "selector": {}}, {"id": "AM02-SOFTWARE-VERSION", "mandatory": true, "origin": "regulatory", "path": "SoftwareComponent.version", "remediation": "Registrare la versione del componente software.", "selector": {}}, {"id": "AM02-SOFTWARE-AUTH", "mandatory": true, "origin": "regulatory", "path": "SoftwareComponent.authorized", "remediation": "Autorizzare o rimuovere il componente software.", "selector": {}}] |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `control_id` | CTRL-ID-AM-02 |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `description` | Verifica presenza versione e autorizzazione dei componenti software osservati. |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `evaluator` | collection_inventory |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `id` | RULE-ID-AM-02 |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `parameters_json` | {"entity_type": "SoftwareComponent", "fields": ["name", "version", "authorized"]} |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `recommendation` | Censire componenti versioni e stato di autorizzazione. |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `relevant_system_required` | True |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `required_evidence_types` | software_inventory |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `required_properties` | software_component.version, software_component.authorized |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `requirement_id` | REQ-ID-AM-02 |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `title` | Inventario software e servizi |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `verification_mode` | direct_technical |
| Regole di valutazione | Inventario software e servizi (`RULE-ID-AM-02`) | `version` | 2.1.0 |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `applicability_json` | {} |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `conditions_json` | [{"id": "RULE-ID-AM-03-E:network_flow.authorized", "mandatory": true, "origin": "regulatory", "path": "network_flow.authorized", "remediation": "Documentare origine destinazione protocolli e autorizzazione dei flussi.", "selector": {}}] |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `control_id` | CTRL-ID-AM-03-E |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `description` | Verifica i record dei flussi di rete rilevanti per il profilo essenziale. |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `evaluator` | collection_inventory |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `id` | RULE-ID-AM-03-E |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `parameters_json` | {"entity_type": "NetworkFlow", "fields": ["source", "destination", "transport_protocol", "application_protocol", "authorized"]} |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `recommendation` | Documentare origine destinazione protocolli e autorizzazione dei flussi. |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `relevant_system_required` | True |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `required_evidence_types` | network_flow_inventory |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `required_properties` | network_flow.authorized |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `requirement_id` | REQ-ID-AM-03-E |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `title` | Inventario e autorizzazione dei flussi |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `verification_mode` | direct_technical |
| Regole di valutazione | Inventario e autorizzazione dei flussi (`RULE-ID-AM-03-E`) | `version` | 2.1.0 |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `applicability_json` | {} |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `conditions_json` | [{"id": "RULE-ID-AM-04:asset.provider_services_inventory_complete", "mandatory": true, "origin": "regulatory", "path": "asset.provider_services_inventory_complete", "remediation": "Completare l'elenco dei servizi dei fornitori che supportano l'asset.", "selector": {}}] |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `control_id` | CTRL-ID-AM-04 |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `description` | Verifica che le dipendenze tecniche dai fornitori siano censite. |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `evaluator` | asset_properties |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `id` | RULE-ID-AM-04 |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `parameters_json` | {"properties": ["provider_services_inventory_complete"]} |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `recommendation` | Completare l'elenco dei servizi dei fornitori che supportano l'asset. |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `relevant_system_required` | True |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `required_evidence_types` | provider_service_inventory |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `required_properties` | asset.provider_services_inventory_complete |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `requirement_id` | REQ-ID-AM-04 |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `title` | Inventario tecnico dei servizi forniti da terzi |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `verification_mode` | evidence_assisted |
| Regole di valutazione | Inventario tecnico dei servizi forniti da terzi (`RULE-ID-AM-04`) | `version` | 2.1.0 |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `applicability_json` | {} |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `conditions_json` | [{"id": "RULE-ID-RA-01:asset.vulnerability_advisories_monitored", "mandatory": true, "origin": "regulatory", "path": "asset.vulnerability_advisories_monitored", "remediation": "Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate.", "selector": {}}] |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `control_id` | CTRL-ID-RA-01 |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `description` | Verifica che le fonti ACN CERT e ISAC pertinenti siano monitorate per identificare vulnerabilità. |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `evaluator` | asset_properties |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `id` | RULE-ID-RA-01 |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `parameters_json` | {"properties": ["vulnerability_advisories_monitored"]} |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `recommendation` | Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate. |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `relevant_system_required` | True |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `required_evidence_types` | vulnerability_management |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `required_properties` | asset.vulnerability_advisories_monitored |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `requirement_id` | REQ-ID-RA-01 |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `title` | Identificazione delle vulnerabilità da fonti monitorate |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `verification_mode` | direct_technical |
| Regole di valutazione | Identificazione delle vulnerabilità da fonti monitorate (`RULE-ID-RA-01`) | `version` | 2.1.0 |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `applicability_json` | {} |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `conditions_json` | [{"id": "RULE-ID-RA-01-E:asset.extended_vulnerability_assessment_performed", "mandatory": true, "origin": "regulatory", "path": "asset.extended_vulnerability_assessment_performed", "remediation": "Documentare l'approfondimento applicato al vulnerability assessment.", "selector": {}}] |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `control_id` | CTRL-ID-RA-01-E |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `description` | Verifica l'evidenza delle attività aggiuntive previste per il profilo essenziale. |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `evaluator` | vulnerability_assessment |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `id` | RULE-ID-RA-01-E |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `parameters_json` | {"properties": ["extended_vulnerability_assessment_performed"]} |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `recommendation` | Documentare l'approfondimento applicato al vulnerability assessment. |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `relevant_system_required` | True |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `required_evidence_types` | vulnerability_scan |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `required_properties` | asset.extended_vulnerability_assessment_performed |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `requirement_id` | REQ-ID-RA-01-E |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `title` | Vulnerability assessment approfondito |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `verification_mode` | evidence_assisted |
| Regole di valutazione | Vulnerability assessment approfondito (`RULE-ID-RA-01-E`) | `version` | 2.1.0 |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `applicability_json` | {} |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `conditions_json` | [{"id": "RULE-ID-RA-08:asset.vulnerability_advisories_monitored", "mandatory": true, "origin": "regulatory", "path": "asset.vulnerability_advisories_monitored", "remediation": "Remediare o mitigare e registrare il rischio residuo.", "selector": {}}, {"id": "RULE-ID-RA-08:vulnerability.remediation_status", "mandatory": true, "origin": "regulatory", "path": "vulnerability.remediation_status", "remediation": "Remediare o mitigare e registrare il rischio residuo.", "selector": {}}] |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `control_id` | CTRL-ID-RA-08 |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `description` | Verifica monitoraggio delle fonti e remediation o mitigazione; in corso non è soddisfacimento. |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `evaluator` | vulnerability_treatment |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `id` | RULE-ID-RA-08 |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `parameters_json` | {} |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `recommendation` | Remediare o mitigare e registrare il rischio residuo. |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `relevant_system_required` | True |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `required_evidence_types` | vulnerability_management, vulnerability_treatment |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `required_properties` | asset.vulnerability_advisories_monitored, vulnerability.remediation_status |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `requirement_id` | REQ-ID-RA-08 |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `title` | Trattamento delle vulnerabilità rilevate |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `verification_mode` | direct_technical |
| Regole di valutazione | Trattamento delle vulnerabilità rilevate (`RULE-ID-RA-08`) | `version` | 2.1.0 |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `applicability_json` | {} |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `conditions_json` | [{"id": "RULE-ID-RA-08-E:asset.critical_software_supplier_channels_monitored", "mandatory": true, "origin": "regulatory", "path": "asset.critical_software_supplier_channels_monitored", "remediation": "Monitorare e documentare i canali dei fornitori del software critico.", "selector": {}}] |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `control_id` | CTRL-ID-RA-08-E |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `description` | Verifica il monitoraggio dei canali dei fornitori del software ritenuto critico. |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `evaluator` | asset_properties |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `id` | RULE-ID-RA-08-E |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `parameters_json` | {"properties": ["critical_software_supplier_channels_monitored"]} |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `recommendation` | Monitorare e documentare i canali dei fornitori del software critico. |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `relevant_system_required` | True |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `required_evidence_types` | vulnerability_management |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `required_properties` | asset.critical_software_supplier_channels_monitored |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `requirement_id` | REQ-ID-RA-08-E |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `title` | Monitoraggio dei canali dei fornitori critici |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `verification_mode` | evidence_assisted |
| Regole di valutazione | Monitoraggio dei canali dei fornitori critici (`RULE-ID-RA-08-E`) | `version` | 2.1.0 |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `applicability_json` | {} |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `conditions_json` | [{"id": "RULE-PR-AA-01:account.individual", "mandatory": true, "origin": "regulatory", "path": "account.individual", "remediation": "Censire e revisionare le utenze e il ciclo di vita delle credenziali.", "selector": {}}, {"id": "RULE-PR-AA-01:account.authorized", "mandatory": true, "origin": "regulatory", "path": "account.authorized", "remediation": "Censire e revisionare le utenze e il ciclo di vita delle credenziali.", "selector": {}}, {"id": "RULE-PR-AA-01:account.credentials_managed", "mandatory": true, "origin": "regulatory", "path": "account.credentials_managed", "remediation": "Censire e revisionare le utenze e il ciclo di vita delle credenziali.", "selector": {}}] |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `control_id` | CTRL-PR-AA-01 |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `description` | Verifica record individuali autorizzati e credenziali gestite. |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `evaluator` | collection_inventory |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `id` | RULE-PR-AA-01 |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `parameters_json` | {"entity_type": "Account", "fields": ["account_type", "individual", "authorized", "credentials_managed", "last_reviewed_at"]} |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `recommendation` | Censire e revisionare le utenze e il ciclo di vita delle credenziali. |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `relevant_system_required` | True |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `required_evidence_types` | access_review |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `required_properties` | account.individual, account.authorized, account.credentials_managed |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `requirement_id` | REQ-PR-AA-01 |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `title` | Inventario e gestione delle utenze |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `verification_mode` | direct_technical |
| Regole di valutazione | Inventario e gestione delle utenze (`RULE-PR-AA-01`) | `version` | 2.1.0 |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `applicability_json` | {} |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `applicable_profiles` | important, essential |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `conditions_json` | [{"id": "RULE-PR-AA-03:account.mfa_enabled", "mandatory": true, "origin": "regulatory", "path": "account.mfa_enabled", "remediation": "Applicare MFA agli accessi privilegiati o remoti individuati dal rischio.", "selector": {}}] |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `control_id` | CTRL-PR-AA-03 |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `description` | Valuta MFA soltanto per utenze privilegiate o di accesso remoto su sistemi NIS rilevanti. |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `empty_collection_policy` | not_applicable |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `evaluator` | collection_booleans |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `id` | RULE-PR-AA-03 |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `parameters_json` | {"entity_type": "Account", "properties": ["mfa_enabled"], "selectors_any": {"privileged": true, "remote_access": true}} |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `recommendation` | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `relevant_system_required` | True |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `required_evidence_types` | access_configuration |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `required_properties` | account.mfa_enabled |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `requirement_id` | REQ-PR-AA-03 |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `title` | MFA per accessi pertinenti al rischio |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `verification_mode` | direct_technical |
| Regole di valutazione | MFA per accessi pertinenti al rischio (`RULE-PR-AA-03`) | `version` | 2.1.0 |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `applicability_json` | {} |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `conditions_json` | [{"id": "RULE-PR-AA-05:account.least_privilege", "mandatory": true, "origin": "regulatory", "path": "account.least_privilege", "remediation": "Ridurre i privilegi e separare le credenziali amministrative.", "selector": {}}, {"id": "RULE-PR-AA-05:account.separate_admin_account", "mandatory": true, "origin": "regulatory", "path": "account.separate_admin_account", "remediation": "Ridurre i privilegi e separare le credenziali amministrative.", "selector": {}}] |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `control_id` | CTRL-PR-AA-05 |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `description` | Verifica privilegi minimi e account amministrativo separato. |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `empty_collection_policy` | not_applicable |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `evaluator` | collection_booleans |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `id` | RULE-PR-AA-05 |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `parameters_json` | {"entity_type": "Account", "properties": ["least_privilege", "separate_admin_account"], "selectors_any": {"privileged": true}} |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `recommendation` | Ridurre i privilegi e separare le credenziali amministrative. |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `relevant_system_required` | True |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `required_evidence_types` | access_configuration |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `required_properties` | account.least_privilege, account.separate_admin_account |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `requirement_id` | REQ-PR-AA-05 |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `title` | Minimo privilegio e separazione amministrativa |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `verification_mode` | direct_technical |
| Regole di valutazione | Minimo privilegio e separazione amministrativa (`RULE-PR-AA-05`) | `version` | 2.1.0 |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `applicability_json` | {} |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `conditions_json` | [{"id": "RULE-PR-AA-06:asset.physical_protection_documented", "mandatory": true, "origin": "regulatory", "path": "asset.physical_protection_documented", "remediation": "Acquisire evidenza corrente delle protezioni fisiche applicabili.", "selector": {}}] |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `control_id` | CTRL-PR-AA-06 |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `description` | Verifica la presenza di configurazione ed evidenza della protezione fisica. |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `evaluator` | asset_properties |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `id` | RULE-PR-AA-06 |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `parameters_json` | {"properties": ["physical_protection_documented"]} |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `recommendation` | Acquisire evidenza corrente delle protezioni fisiche applicabili. |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `relevant_system_required` | True |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `required_evidence_types` | physical_security |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `required_properties` | asset.physical_protection_documented |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `requirement_id` | REQ-PR-AA-06 |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `title` | Protezione fisica documentabile |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `verification_mode` | evidence_assisted |
| Regole di valutazione | Protezione fisica documentabile (`RULE-PR-AA-06`) | `version` | 2.1.0 |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `applicability_json` | {"has_removable_media": true} |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `conditions_json` | [{"id": "DS01-REMOVABLE-ENCRYPTED", "mandatory": true, "origin": "regulatory", "path": "DataObject.removable_media_encrypted", "remediation": "Cifrare i supporti rimovibili autorizzati.", "selector": {}}] |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `control_id` | CTRL-PR-DS-01 |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `description` | Verifica la cifratura dei supporti rimovibili dichiarati per l'asset. |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `evaluator` | data_object_protection |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `id` | RULE-PR-DS-01 |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `parameters_json` | {"properties": []} |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `recommendation` | Cifrare i supporti rimovibili secondo classificazione e baseline approvata. |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `relevant_system_required` | True |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `required_evidence_types` | encryption_configuration |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `required_properties` | nessuna |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `requirement_id` | REQ-PR-DS-01 |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `title` | Cifratura dei supporti rimovibili |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `verification_mode` | direct_technical |
| Regole di valutazione | Cifratura dei supporti rimovibili (`RULE-PR-DS-01`) | `version` | 2.1.0 |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `applicability_json` | {"has_internet_exposed_services": true} |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `conditions_json` | [{"id": "RULE-PR-DS-02:service.encrypted", "mandatory": true, "origin": "regulatory", "path": "service.encrypted", "remediation": "Allineare i protocolli alla baseline crittografica approvata.", "selector": {}}, {"id": "RULE-PR-DS-02:service.tls_enabled", "mandatory": true, "origin": "project_baseline", "path": "service.tls_enabled", "remediation": "Abilitare TLS sui servizi esposti cui si applica la baseline.", "selector": {}}, {"id": "RULE-PR-DS-02:service.tls_versions", "mandatory": true, "origin": "project_baseline", "path": "service.tls_versions", "remediation": "Allineare i protocolli alla baseline crittografica approvata.", "selector": {}}] |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `control_id` | CTRL-PR-DS-02 |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `description` | Confronta le configurazioni osservate con una baseline crittografica versionata. |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `evaluator` | cryptographic_configuration |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `id` | RULE-PR-DS-02 |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `parameters_json` | {"threshold_ref": "tls_minimum"} |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `recommendation` | Allineare i protocolli alla baseline crittografica approvata. |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `relevant_system_required` | True |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `required_evidence_types` | encryption_configuration |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `required_properties` | service.encrypted, service.tls_enabled, service.tls_versions |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `requirement_id` | REQ-PR-DS-02 |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `title` | Cifratura delle comunicazioni |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `verification_mode` | direct_technical |
| Regole di valutazione | Cifratura delle comunicazioni (`RULE-PR-DS-02`) | `version` | 2.1.0 |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `applicability_json` | {} |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `conditions_json` | [{"id": "RULE-PR-DS-11:backup.frequency_within_plan", "mandatory": true, "origin": "regulatory", "path": "backup.frequency_within_plan", "remediation": "Adeguare frequenza e copie offline al piano approvato.", "selector": {}}, {"id": "RULE-PR-DS-11:backup.offline_copy", "mandatory": true, "origin": "regulatory", "path": "backup.offline_copy", "remediation": "Adeguare frequenza e copie offline al piano approvato.", "selector": {}}] |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `control_id` | CTRL-PR-DS-11 |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `description` | Verifica periodicità rispetto al piano e presenza di copie offline. |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `evaluator` | collection_booleans |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `id` | RULE-PR-DS-11 |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `parameters_json` | {"entity_type": "BackupRecord", "properties": ["frequency_within_plan", "offline_copy"]} |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `recommendation` | Adeguare frequenza e copie offline al piano approvato. |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `relevant_system_required` | True |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `required_evidence_types` | backup_record |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `required_properties` | backup.frequency_within_plan, backup.offline_copy |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `requirement_id` | REQ-PR-DS-11 |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `title` | Backup conforme al piano e copie offline |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `verification_mode` | direct_technical |
| Regole di valutazione | Backup conforme al piano e copie offline (`RULE-PR-DS-11`) | `version` | 2.1.0 |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `applicability_json` | {} |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `conditions_json` | [{"id": "RULE-PR-DS-11-E:backup.protected_copy", "mandatory": true, "origin": "regulatory", "path": "backup.protected_copy", "remediation": "Proteggere le copie e completare con successo le prove di ripristino pianificate.", "selector": {}}, {"id": "RULE-PR-DS-11-E:backup.restore_test_successful", "mandatory": true, "origin": "regulatory", "path": "backup.restore_test_successful", "remediation": "Proteggere le copie e completare con successo le prove di ripristino pianificate.", "selector": {}}] |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `control_id` | CTRL-PR-DS-11-E |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `description` | Verifica protezione delle copie e riuscita delle prove periodiche di ripristino. |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `evaluator` | collection_booleans |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `id` | RULE-PR-DS-11-E |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `parameters_json` | {"entity_type": "BackupRecord", "properties": ["protected_copy", "restore_test_successful"]} |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `recommendation` | Proteggere le copie e completare con successo le prove di ripristino pianificate. |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `relevant_system_required` | True |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `required_evidence_types` | backup_record, restore_test |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `required_properties` | backup.protected_copy, backup.restore_test_successful |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `requirement_id` | REQ-PR-DS-11-E |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `title` | Protezione e test di ripristino per il profilo essenziale |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `verification_mode` | direct_technical |
| Regole di valutazione | Protezione e test di ripristino per il profilo essenziale (`RULE-PR-DS-11-E`) | `version` | 2.1.0 |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `applicability_json` | {} |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `conditions_json` | [{"id": "RULE-PR-PS-01-E:asset.hardening_baseline_applied", "mandatory": true, "origin": "regulatory", "path": "asset.hardening_baseline_applied", "remediation": "Applicare e versionare una baseline di hardening appropriata.", "selector": {}}] |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `control_id` | CTRL-PR-PS-01-E |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `description` | Verifica l'applicazione di una baseline tecnica versionata. |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `evaluator` | asset_properties |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `id` | RULE-PR-PS-01-E |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `parameters_json` | {"properties": ["hardening_baseline_applied"]} |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `recommendation` | Applicare e versionare una baseline di hardening appropriata. |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `relevant_system_required` | True |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `required_evidence_types` | system_configuration |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `required_properties` | asset.hardening_baseline_applied |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `requirement_id` | REQ-PR-PS-01-E |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `title` | Baseline di hardening applicata |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `verification_mode` | direct_technical |
| Regole di valutazione | Baseline di hardening applicata (`RULE-PR-PS-01-E`) | `version` | 2.1.0 |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `applicability_json` | {} |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `conditions_json` | [{"id": "RULE-PR-PS-02:software_component.support_status", "mandatory": true, "origin": "regulatory", "path": "software_component.support_status", "remediation": "Sostituire software fuori supporto e rispettare i termini del piano di patching.", "selector": {}}, {"id": "RULE-PR-PS-02:software_component.security_update_status", "mandatory": true, "origin": "regulatory", "path": "software_component.security_update_status", "remediation": "Sostituire software fuori supporto e rispettare i termini del piano di patching.", "selector": {}}] |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `control_id` | CTRL-PR-PS-02 |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `description` | Verifica supporto e stato aggiornamenti senza imporre una soglia universale. |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `empty_collection_policy` | not_applicable |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `evaluator` | supported_and_updated_software |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `id` | RULE-PR-PS-02 |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `parameters_json` | {"critical_patch_test_required": false} |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `recommendation` | Sostituire software fuori supporto e rispettare i termini del piano di patching. |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `relevant_system_required` | True |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `required_evidence_types` | software_inventory, patch_record |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `required_properties` | software_component.support_status, software_component.security_update_status |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `requirement_id` | REQ-PR-PS-02 |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `title` | Software supportato e aggiornamenti entro il piano di rischio |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `verification_mode` | direct_technical |
| Regole di valutazione | Software supportato e aggiornamenti entro il piano di rischio (`RULE-PR-PS-02`) | `version` | 2.1.0 |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `applicability_json` | {} |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `conditions_json` | [{"id": "RULE-PR-PS-02-E:software_component.support_status", "mandatory": true, "origin": "regulatory", "path": "software_component.support_status", "remediation": "Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista.", "selector": {}}, {"id": "RULE-PR-PS-02-E:software_component.security_update_status", "mandatory": true, "origin": "regulatory", "path": "software_component.security_update_status", "remediation": "Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista.", "selector": {}}, {"id": "RULE-PR-PS-02-E:software_component.critical_update_tested", "mandatory": true, "origin": "regulatory", "path": "software_component.critical_update_tested", "remediation": "Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista.", "selector": {}}] |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `control_id` | CTRL-PR-PS-02-E |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `description` | Verifica che gli aggiornamenti critici siano stati testati secondo il processo approvato. |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `empty_collection_policy` | not_applicable |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `evaluator` | supported_and_updated_software |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `id` | RULE-PR-PS-02-E |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `parameters_json` | {"critical_patch_test_required": true} |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `recommendation` | Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista. |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `relevant_system_required` | True |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `required_evidence_types` | patch_record |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `required_properties` | software_component.support_status, software_component.security_update_status, software_component.critical_update_tested |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `requirement_id` | REQ-PR-PS-02-E |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `title` | Test delle patch critiche |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `verification_mode` | direct_technical |
| Regole di valutazione | Test delle patch critiche (`RULE-PR-PS-02-E`) | `version` | 2.1.0 |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `applicability_json` | {} |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `conditions_json` | [{"id": "RULE-PR-PS-03-E:asset.maintenance_logged", "mandatory": true, "origin": "regulatory", "path": "asset.maintenance_logged", "remediation": "Registrare manutenzione e procedure di dismissione sicura.", "selector": {}}, {"id": "RULE-PR-PS-03-E:asset.secure_disposal_documented", "mandatory": true, "origin": "regulatory", "path": "asset.secure_disposal_documented", "remediation": "Registrare manutenzione e procedure di dismissione sicura.", "selector": {}}] |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `control_id` | CTRL-PR-PS-03-E |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `description` | Verifica evidenza tecnica di manutenzione e dismissione sicura. |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `evaluator` | asset_properties |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `id` | RULE-PR-PS-03-E |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `parameters_json` | {"properties": ["maintenance_logged", "secure_disposal_documented"]} |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `recommendation` | Registrare manutenzione e procedure di dismissione sicura. |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `relevant_system_required` | True |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `required_evidence_types` | maintenance_record |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `required_properties` | asset.maintenance_logged, asset.secure_disposal_documented |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `requirement_id` | REQ-PR-PS-03-E |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `title` | Manutenzione e dismissione tracciate |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `verification_mode` | evidence_assisted |
| Regole di valutazione | Manutenzione e dismissione tracciate (`RULE-PR-PS-03-E`) | `version` | 2.1.0 |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `applicability_json` | {} |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `conditions_json` | [{"id": "RULE-PR-PS-04:asset.admin_remote_access_logging", "mandatory": true, "origin": "regulatory", "path": "asset.admin_remote_access_logging", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato.", "selector": {}}, {"id": "RULE-PR-PS-04:asset.logs_protected", "mandatory": true, "origin": "regulatory", "path": "asset.logs_protected", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato.", "selector": {}}, {"id": "RULE-PR-PS-04:asset.logs_centralized", "mandatory": false, "origin": "regulatory", "path": "asset.logs_centralized", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato.", "selector": {}}, {"id": "RULE-PR-PS-04:asset.log_retention_within_plan", "mandatory": true, "origin": "project_baseline", "path": "asset.log_retention_within_plan", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato.", "selector": {}}] |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `control_id` | CTRL-PR-PS-04 |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `description` | Verifica eventi rilevanti protezione centralizzazione e retention conforme al piano. |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `evaluator` | asset_properties |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `id` | RULE-PR-PS-04 |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `parameters_json` | {"properties": ["admin_remote_access_logging", "logs_protected", "logs_centralized", "log_retention_within_plan"]} |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `recommendation` | Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato. |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `relevant_system_required` | True |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `required_evidence_types` | log_configuration |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `required_properties` | asset.admin_remote_access_logging, asset.logs_protected, asset.logs_centralized, asset.log_retention_within_plan |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `requirement_id` | REQ-PR-PS-04 |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `title` | Logging di accessi amministrativi e remoti |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `verification_mode` | direct_technical |
| Regole di valutazione | Logging di accessi amministrativi e remoti (`RULE-PR-PS-04`) | `version` | 2.1.0 |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `applicability_json` | {} |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `conditions_json` | [{"id": "RULE-PR-IR-01:asset.remote_access_registry_complete", "mandatory": true, "origin": "regulatory", "path": "asset.remote_access_registry_complete", "remediation": "Governare gli accessi remoti e applicare regole firewall approvate.", "selector": {}}, {"id": "RULE-PR-IR-01:asset.remote_access_protected", "mandatory": true, "origin": "regulatory", "path": "asset.remote_access_protected", "remediation": "Governare gli accessi remoti e applicare regole firewall approvate.", "selector": {}}, {"id": "RULE-PR-IR-01:asset.firewall_enabled", "mandatory": true, "origin": "regulatory", "path": "asset.firewall_enabled", "remediation": "Governare gli accessi remoti e applicare regole firewall approvate.", "selector": {}}] |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `control_id` | CTRL-PR-IR-01 |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `description` | Verifica elenco degli accessi remoti canali protetti e protezione del confine. |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `evaluator` | asset_properties |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `id` | RULE-PR-IR-01 |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `parameters_json` | {"properties": ["remote_access_registry_complete", "remote_access_protected", "firewall_enabled"]} |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `recommendation` | Governare gli accessi remoti e applicare regole firewall approvate. |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `relevant_system_required` | True |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `required_evidence_types` | network_security |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `required_properties` | asset.remote_access_registry_complete, asset.remote_access_protected, asset.firewall_enabled |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `requirement_id` | REQ-PR-IR-01 |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `title` | Accesso remoto governato e firewall attivo |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `verification_mode` | direct_technical |
| Regole di valutazione | Accesso remoto governato e firewall attivo (`RULE-PR-IR-01`) | `version` | 2.1.0 |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `applicability_json` | {} |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `conditions_json` | [{"id": "RULE-PR-IR-03-E:security_capability.enabled", "mandatory": true, "origin": "regulatory", "path": "security_capability.enabled", "remediation": "Predisporre testare e mantenere comunicazioni di emergenza protette.", "selector": {}}, {"id": "RULE-PR-IR-03-E:security_capability.configured", "mandatory": true, "origin": "regulatory", "path": "security_capability.configured", "remediation": "Predisporre testare e mantenere comunicazioni di emergenza protette.", "selector": {}}, {"id": "RULE-PR-IR-03-E:security_capability.maintained", "mandatory": true, "origin": "regulatory", "path": "security_capability.maintained", "remediation": "Predisporre testare e mantenere comunicazioni di emergenza protette.", "selector": {}}] |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `control_id` | CTRL-PR-IR-03-E |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `description` | Verifica configurazione e manutenzione della capacità di comunicazione di emergenza. |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `evaluator` | collection_booleans |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `id` | RULE-PR-IR-03-E |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `parameters_json` | {"capability_types": ["emergency_communications"], "entity_type": "SecurityCapability", "properties": ["enabled", "configured", "maintained"]} |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `recommendation` | Predisporre testare e mantenere comunicazioni di emergenza protette. |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `relevant_system_required` | True |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `required_evidence_types` | emergency_communications |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `required_properties` | security_capability.enabled, security_capability.configured, security_capability.maintained |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `requirement_id` | REQ-PR-IR-03-E |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `title` | Capacità protetta per comunicazioni di emergenza |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `verification_mode` | evidence_assisted |
| Regole di valutazione | Capacità protetta per comunicazioni di emergenza (`RULE-PR-IR-03-E`) | `version` | 2.1.0 |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `applicability_json` | {} |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `conditions_json` | [{"id": "RULE-DE-CM-01:security_capability.enabled", "mandatory": true, "origin": "regulatory", "path": "security_capability.enabled", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.", "selector": {}}, {"id": "RULE-DE-CM-01:security_capability.configured", "mandatory": true, "origin": "regulatory", "path": "security_capability.configured", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.", "selector": {}}, {"id": "RULE-DE-CM-01:security_capability.monitored", "mandatory": true, "origin": "regulatory", "path": "security_capability.monitored", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti.", "selector": {}}] |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `control_id` | CTRL-DE-CM-01 |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `description` | Verifica la capacità tecnica comune di rilevare tempestivamente eventi potenzialmente avversi. |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `evaluator` | collection_booleans |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `id` | RULE-DE-CM-01 |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `parameters_json` | {"capability_types": ["intrusion_detection"], "entity_type": "SecurityCapability", "properties": ["enabled", "configured", "monitored"]} |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `recommendation` | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `relevant_system_required` | True |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `required_evidence_types` | monitoring_configuration |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `required_properties` | security_capability.enabled, security_capability.configured, security_capability.monitored |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `requirement_id` | REQ-DE-CM-01 |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `title` | Rilevamento degli incidenti di rete |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `verification_mode` | direct_technical |
| Regole di valutazione | Rilevamento degli incidenti di rete (`RULE-DE-CM-01`) | `version` | 2.1.0 |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `applicability_json` | {} |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `applicable_profiles` | essential |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `conditions_json` | [{"id": "RULE-DE-CM-01-E:asset.anomaly_thresholds_configured", "mandatory": true, "origin": "project_baseline", "path": "asset.anomaly_thresholds_configured", "remediation": "Calibrare e riesaminare soglie e regole di anomalia.", "selector": {}}] |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `control_id` | CTRL-DE-CM-01-E |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `description` | Verifica la configurazione delle soglie previste per il profilo essenziale. |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `empty_collection_policy` | not_verifiable |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `evaluator` | asset_properties |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `id` | RULE-DE-CM-01-E |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `parameters_json` | {"properties": ["anomaly_thresholds_configured"]} |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `recommendation` | Calibrare e riesaminare soglie e regole di anomalia. |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `relevant_system_required` | True |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `required_evidence_types` | monitoring_configuration |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `required_properties` | asset.anomaly_thresholds_configured |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `requirement_id` | REQ-DE-CM-01-E |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `title` | Soglie e anomalie calibrate |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `verification_mode` | direct_technical |
| Regole di valutazione | Soglie e anomalie calibrate (`RULE-DE-CM-01-E`) | `version` | 2.1.0 |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `allowed_outcomes` | compliant, non_compliant, not_verifiable, not_applicable |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `applicability_json` | {} |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `applicable_profiles` | important, essential |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `conditions_json` | [{"id": "RULE-DE-CM-09:security_capability.enabled", "mandatory": true, "origin": "regulatory", "path": "security_capability.enabled", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata.", "selector": {}}, {"id": "RULE-DE-CM-09:security_capability.configured", "mandatory": true, "origin": "regulatory", "path": "security_capability.configured", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata.", "selector": {}}, {"id": "RULE-DE-CM-09:security_capability.maintained", "mandatory": true, "origin": "regulatory", "path": "security_capability.maintained", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata.", "selector": {}}, {"id": "RULE-DE-CM-09:security_capability.monitored", "mandatory": true, "origin": "regulatory", "path": "security_capability.monitored", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata.", "selector": {}}] |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `control_id` | CTRL-DE-CM-09 |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `decision_policy_json` | {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"} |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `description` | Verifica capacità endpoint abilitata configurata mantenuta e monitorata. |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `empty_collection_policy` | non_compliant |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `evaluator` | collection_booleans |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `id` | RULE-DE-CM-09 |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `information_actions_json` | {"collection_failed": "Correggere il collector e ripetere l'acquisizione.", "not_declared": "Acquisire e dichiarare il dato mancante.", "source_unavailable": "Ripristinare o sostituire la fonte informativa.", "stale_information": "Aggiornare l'evidenza o il dato scaduto."} |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `messages_json` | {"compliant": "Le condizioni tecniche osservabili della regola risultano soddisfatte.", "manual_review_required": "Una deroga o un rischio accettato richiede revisione manuale.", "non_compliant": "È stato osservato uno scostamento tecnico rispetto alla regola.", "not_applicable": "La regola non è applicabile al profilo o al sistema.", "not_verifiable": "Dati o evidenze non consentono una verifica conclusiva.", "partially_compliant": "Solo una parte delle condizioni tecniche risulta soddisfatta."} |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `parameters_json` | {"capability_types": ["endpoint_protection"], "entity_type": "SecurityCapability", "properties": ["enabled", "configured", "maintained", "monitored"]} |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `recommendation` | Installare configurare mantenere e monitorare la protezione endpoint appropriata. |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `relevant_system_required` | True |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `required_evidence_types` | endpoint_protection |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `required_properties` | security_capability.enabled, security_capability.configured, security_capability.maintained, security_capability.monitored |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `requirement_id` | REQ-DE-CM-09 |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `title` | Protezione endpoint attiva e monitorata |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `verification_mode` | direct_technical |
| Regole di valutazione | Protezione endpoint attiva e monitorata (`RULE-DE-CM-09`) | `version` | 2.1.0 |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `acn_point` | ID.AM-01 |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `confidence_level` | medium |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `conflicting_information` | nessuna |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `control_id` | CTRL-ID-AM-01 |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `decision_policy` | all_required |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-asset"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": false, "path": "asset.hardware_inventory_complete", "provenance_ids": ["prov-inventory"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-asset.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `errors` | nessuna |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": false, "path": "asset.hardware_inventory_complete", "provenance_ids": ["prov-inventory"], "value_status": "known"}] |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `evidence_ids` | ev-delta-asset |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `governance_status` | none |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `id` | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `information_actions` | nessuna |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.hardware_inventory_complete", "remediation": "Completare e validare il record inventariale dell'asset."}] |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `missing_information` | nessuna |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `nis_profile` | essential |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `recommendation` | Completare e validare il record inventariale dell'asset. |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `requirement_id` | REQ-ID-AM-01 |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `rule_id` | RULE-ID-AM-01 |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `selector_decisions` | nessuna |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `technical_remediations` | Completare e validare il record inventariale dell'asset. |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `technical_status` | non_compliant |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `thresholds_used_json` | {"evidence.ev-delta-asset.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | d2bbd3a2-691c-51f2-b049-9400e7eeaeaf (`d2bbd3a2-691c-51f2-b049-9400e7eeaeaf`) | `verification_mode` | direct_technical |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `acn_point` | ID.AM-02 |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `confidence_level` | low |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `control_id` | CTRL-ID-AM-02 |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `decision_policy` | all_required |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-software"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "identificato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "Production Integration Server", "path": "Asset.asset-delta-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "HTTPS", "path": "Service.svc-delta-https.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "Service.svc-delta-https.authorized", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "DeltaIntegrator", "path": "SoftwareComponent.software-delta-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": "3.1", "path": "SoftwareComponent.software-delta-core.version", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "SoftwareComponent.software-delta-core.authorized", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-delta-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `errors` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `evaluated_facts_json` | [{"comparison": "identificato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "Production Integration Server", "path": "Asset.asset-delta-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "HTTPS", "path": "Service.svc-delta-https.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "Service.svc-delta-https.authorized", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "DeltaIntegrator", "path": "SoftwareComponent.software-delta-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": "3.1", "path": "SoftwareComponent.software-delta-core.version", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "SoftwareComponent.software-delta-core.authorized", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `evidence_ids` | ev-delta-software |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `governance_status` | none |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `id` | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `information_actions` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `known_violations` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `missing_information` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `nis_profile` | essential |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `requirement_id` | REQ-ID-AM-02 |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `rule_id` | RULE-ID-AM-02 |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `technical_remediations` | nessuna |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `technical_status` | compliant |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `thresholds_used_json` | {"evidence.ev-delta-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | db6b747d-ed2c-56d9-a44e-a3d7bba80e3c (`db6b747d-ed2c-56d9-a44e-a3d7bba80e3c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `acn_point` | ID.AM-03 |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `confidence_level` | medium |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `control_id` | CTRL-ID-AM-03-E |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `decision_policy` | all_required |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-flow"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "internet", "path": "NetworkFlow.flow-delta-https.source", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "asset-delta-core", "path": "NetworkFlow.flow-delta-https.destination", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "tcp", "path": "NetworkFlow.flow-delta-https.transport_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "https", "path": "NetworkFlow.flow-delta-https.application_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:30:00Z", "observed_value": false, "path": "NetworkFlow.flow-delta-https.authorized", "provenance_ids": ["prov-network"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-flow.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `errors` | nessuna |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `evaluated_facts_json` | [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "internet", "path": "NetworkFlow.flow-delta-https.source", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "asset-delta-core", "path": "NetworkFlow.flow-delta-https.destination", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "tcp", "path": "NetworkFlow.flow-delta-https.transport_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "https", "path": "NetworkFlow.flow-delta-https.application_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:30:00Z", "observed_value": false, "path": "NetworkFlow.flow-delta-https.authorized", "provenance_ids": ["prov-network"], "value_status": "known"}] |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `evidence_ids` | ev-delta-flow |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `governance_status` | none |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `id` | 21318f70-a095-51ea-afff-68297a2c2fb1 |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `information_actions` | nessuna |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `known_violations_json` | [{"comparison": "presente e autorizzato", "observed_value": false, "path": "NetworkFlow.flow-delta-https.authorized", "remediation": "Documentare origine destinazione protocolli e autorizzazione dei flussi."}] |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `missing_information` | nessuna |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `nis_profile` | essential |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `recommendation` | Documentare origine destinazione protocolli e autorizzazione dei flussi. |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `requirement_id` | REQ-ID-AM-03-E |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `rule_id` | RULE-ID-AM-03-E |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `technical_remediations` | Documentare origine destinazione protocolli e autorizzazione dei flussi. |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `technical_status` | non_compliant |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `thresholds_used_json` | {"evidence.ev-delta-flow.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 21318f70-a095-51ea-afff-68297a2c2fb1 (`21318f70-a095-51ea-afff-68297a2c2fb1`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `acn_point` | ID.AM-04 |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `confidence_level` | insufficient |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `control_id` | CTRL-ID-AM-04 |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `decision_policy` | all_required |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.provider_services_inventory_complete", "provenance_ids": [], "value_status": "unknown"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `errors` | nessuna |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.provider_services_inventory_complete", "provenance_ids": [], "value_status": "unknown"}] |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `governance_status` | none |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `id` | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `information_actions` | Acquisire e dichiarare il dato mancante., Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `known_violations` | nessuna |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `missing_information` | asset.provider_services_inventory_complete, asset.provider_services_inventory_complete:not_declared, evidence.provider_service_inventory |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `nis_profile` | essential |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `reason` | Dati o evidenze non consentono una verifica conclusiva. |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `recommendation` | Completare l'elenco dei servizi dei fornitori che supportano l'asset. |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `requirement_id` | REQ-ID-AM-04 |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `rule_id` | RULE-ID-AM-04 |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `technical_status` | not_verifiable |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 68032e4d-3c55-5d5c-9e92-2c1bea0903f8 (`68032e4d-3c55-5d5c-9e92-2c1bea0903f8`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `confidence_level` | insufficient |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `control_id` | CTRL-ID-RA-01 |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `decision_policy` | all_required |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": [], "value_status": "unknown"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `errors` | nessuna |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": [], "value_status": "unknown"}] |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `evidence_ids` | nessuna |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `governance_status` | none |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `id` | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `known_violations` | nessuna |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `missing_information` | asset.vulnerability_advisories_monitored, asset.vulnerability_advisories_monitored:not_collected, evidence.vulnerability_management |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `nis_profile` | essential |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `reason` | Dati o evidenze non consentono una verifica conclusiva. |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `recommendation` | Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate. |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `requirement_id` | REQ-ID-RA-01 |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `rule_id` | RULE-ID-RA-01 |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `technical_status` | not_verifiable |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `thresholds_used_json` | {} |
| Esiti della valutazione | b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84 (`b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `confidence_level` | high |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `control_id` | CTRL-ID-RA-01-E |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `decision_policy` | all_required |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-scan"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": false, "path": "asset.extended_vulnerability_assessment_performed", "provenance_ids": ["prov-scan"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-scan.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `errors` | nessuna |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": false, "path": "asset.extended_vulnerability_assessment_performed", "provenance_ids": ["prov-scan"], "value_status": "known"}] |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `evidence_ids` | ev-delta-scan |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `governance_status` | none |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `id` | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `information_actions` | nessuna |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.extended_vulnerability_assessment_performed", "remediation": "Documentare l'approfondimento applicato al vulnerability assessment."}] |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `missing_information` | nessuna |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `nis_profile` | essential |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `recommendation` | Documentare l'approfondimento applicato al vulnerability assessment. |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `requirement_id` | REQ-ID-RA-01-E |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `rule_id` | RULE-ID-RA-01-E |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `technical_remediations` | Documentare l'approfondimento applicato al vulnerability assessment. |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `technical_status` | non_compliant |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `thresholds_used_json` | {"evidence.ev-delta-scan.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab (`3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `confidence_level` | insufficient |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `conflicting_information` | nessuna |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `control_id` | CTRL-ID-RA-08 |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `decision_policy` | all_required |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-treatment"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": [], "value_status": "unknown"}, {"comparison": "remediated o mitigated", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "open", "path": "Vulnerability.vuln-delta-001.remediation_status", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "manual_review_required", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-treatment.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `errors` | nessuna |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": [], "value_status": "unknown"}, {"comparison": "remediated o mitigated", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "open", "path": "Vulnerability.vuln-delta-001.remediation_status", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `evidence_ids` | ev-delta-treatment |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `governance_status` | manual_review_required |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `id` | f53750a1-b38c-5313-ae50-f0f28a7f8550 |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `known_violations_json` | [{"comparison": "remediated o mitigated", "observed_value": "open", "path": "Vulnerability.vuln-delta-001.remediation_status", "remediation": "Remediare o mitigare e registrare il rischio residuo."}] |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `missing_information` | asset.vulnerability_advisories_monitored, asset.vulnerability_advisories_monitored:not_collected, evidence.vulnerability_management |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `nis_profile` | essential |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `recommendation` | Remediare o mitigare e registrare il rischio residuo. |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `requirement_id` | REQ-ID-RA-08 |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `rule_id` | RULE-ID-RA-08 |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `selector_decisions` | nessuna |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `technical_remediations` | Remediare o mitigare e registrare il rischio residuo. |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `technical_status` | non_compliant |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `thresholds_used_json` | {"evidence.ev-delta-treatment.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | f53750a1-b38c-5313-ae50-f0f28a7f8550 (`f53750a1-b38c-5313-ae50-f0f28a7f8550`) | `verification_mode` | direct_technical |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `confidence_level` | insufficient |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `conflicting_information` | nessuna |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `control_id` | CTRL-ID-RA-08-E |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `decision_policy` | all_required |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.critical_software_supplier_channels_monitored", "provenance_ids": [], "value_status": "unknown"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `errors` | nessuna |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.critical_software_supplier_channels_monitored", "provenance_ids": [], "value_status": "unknown"}] |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `evidence_ids` | nessuna |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `governance_status` | none |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `id` | bb194a5a-6411-5a0e-b7f2-8d000af407aa |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `known_violations` | nessuna |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `missing_information` | asset.critical_software_supplier_channels_monitored, asset.critical_software_supplier_channels_monitored:not_collected, evidence.vulnerability_management |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `nis_profile` | essential |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `reason` | Dati o evidenze non consentono una verifica conclusiva. |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `recommendation` | Monitorare e documentare i canali dei fornitori del software critico. |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `requirement_id` | REQ-ID-RA-08-E |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `rule_id` | RULE-ID-RA-08-E |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `selector_decisions` | nessuna |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `technical_remediations` | nessuna |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `technical_status` | not_verifiable |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `thresholds_used_json` | {} |
| Esiti della valutazione | bb194a5a-6411-5a0e-b7f2-8d000af407aa (`bb194a5a-6411-5a0e-b7f2-8d000af407aa`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `acn_point` | PR.AA-01 |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `confidence_level` | insufficient |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `control_id` | CTRL-PR-AA-01 |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `decision_policy` | all_required |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-core", "conditions": [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "administrator", "path": "Account.account-delta-admin.account_type", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-delta-admin.individual", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-delta-admin.authorized", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.credentials_managed", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": "2025-11-15T09:00:00Z", "path": "Account.account-delta-admin.last_reviewed_at", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `errors` | nessuna |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `evaluated_facts_json` | [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "administrator", "path": "Account.account-delta-admin.account_type", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-delta-admin.individual", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-delta-admin.authorized", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.credentials_managed", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": "2025-11-15T09:00:00Z", "path": "Account.account-delta-admin.last_reviewed_at", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `evidence_ids` | nessuna |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `governance_status` | none |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `id` | bf852d65-376e-5d3f-8bff-069ec968bb8b |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `known_violations_json` | [{"comparison": "presente e autorizzato", "observed_value": false, "path": "Account.account-delta-admin.credentials_managed", "remediation": "Censire e revisionare le utenze e il ciclo di vita delle credenziali."}] |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `missing_information` | evidence.access_review |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `nis_profile` | essential |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `recommendation` | Censire e revisionare le utenze e il ciclo di vita delle credenziali. |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `requirement_id` | REQ-PR-AA-01 |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `rule_id` | RULE-PR-AA-01 |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `technical_remediations` | Censire e revisionare le utenze e il ciclo di vita delle credenziali. |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `technical_status` | non_compliant |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `thresholds_used_json` | {} |
| Esiti della valutazione | bf852d65-376e-5d3f-8bff-069ec968bb8b (`bf852d65-376e-5d3f-8bff-069ec968bb8b`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `acn_point` | PR.AA-03 |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `confidence_level` | medium |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `control_id` | CTRL-PR-AA-03 |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `decision_policy` | all_required |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-accessconfig"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.mfa_enabled", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": ["account-delta-admin"], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-03", "rule_version": "2.1.0", "selector_decisions": [{"conflicting_information": [], "entity_id": "account-delta-admin", "evaluated_fields": ["privileged", "remote_access"], "missing_information": [], "selector_type": "any", "status": "selected"}], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `errors` | nessuna |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.mfa_enabled", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `evidence_ids` | ev-delta-accessconfig |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `governance_status` | none |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `id` | 2497016d-98aa-50c0-b10a-86df9c6f3647 |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `information_actions` | nessuna |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "Account.account-delta-admin.mfa_enabled", "remediation": "Applicare MFA agli accessi privilegiati o remoti individuati dal rischio."}] |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `missing_information` | nessuna |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `nis_profile` | essential |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `recommendation` | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `requirement_id` | REQ-PR-AA-03 |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `rule_id` | RULE-PR-AA-03 |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `selector_decisions_json` | [{"conflicting_information": [], "entity_id": "account-delta-admin", "evaluated_fields": ["privileged", "remote_access"], "missing_information": [], "selector_type": "any", "status": "selected"}] |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `technical_remediations` | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `technical_status` | non_compliant |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `thresholds_used_json` | {"evidence.ev-delta-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 2497016d-98aa-50c0-b10a-86df9c6f3647 (`2497016d-98aa-50c0-b10a-86df9c6f3647`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `acn_point` | PR.AA-05 |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `confidence_level` | medium |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `control_id` | CTRL-PR-AA-05 |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `decision_policy` | all_required |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-accessconfig"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.least_privilege", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.separate_admin_account", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": ["account-delta-admin"], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-05", "rule_version": "2.1.0", "selector_decisions": [{"conflicting_information": [], "entity_id": "account-delta-admin", "evaluated_fields": ["privileged"], "missing_information": [], "selector_type": "any", "status": "selected"}], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `errors` | nessuna |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.least_privilege", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-delta-admin.separate_admin_account", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `evidence_ids` | ev-delta-accessconfig |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `governance_status` | none |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `id` | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `information_actions` | nessuna |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "Account.account-delta-admin.least_privilege", "remediation": "Ridurre i privilegi e separare le credenziali amministrative."}, {"comparison": "true", "observed_value": false, "path": "Account.account-delta-admin.separate_admin_account", "remediation": "Ridurre i privilegi e separare le credenziali amministrative."}] |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `missing_information` | nessuna |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `nis_profile` | essential |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `recommendation` | Ridurre i privilegi e separare le credenziali amministrative. |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `requirement_id` | REQ-PR-AA-05 |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `rule_id` | RULE-PR-AA-05 |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `selector_decisions_json` | [{"conflicting_information": [], "entity_id": "account-delta-admin", "evaluated_fields": ["privileged"], "missing_information": [], "selector_type": "any", "status": "selected"}] |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `technical_remediations` | Ridurre i privilegi e separare le credenziali amministrative. |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `technical_status` | non_compliant |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `thresholds_used_json` | {"evidence.ev-delta-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 24420cc8-ad6d-5614-ac2c-ee1b1c9dea45 (`24420cc8-ad6d-5614-ac2c-ee1b1c9dea45`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `acn_point` | PR.AA-06 |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `confidence_level` | insufficient |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `control_id` | CTRL-PR-AA-06 |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `decision_policy` | all_required |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.physical_protection_documented", "provenance_ids": [], "value_status": "unknown"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-06", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `errors` | nessuna |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": null, "path": "asset.physical_protection_documented", "provenance_ids": [], "value_status": "unknown"}] |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `governance_status` | none |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `id` | 736d6caf-aace-5f7f-956d-3ee3454dd915 |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `information_actions` | Acquisire e dichiarare il dato mancante., Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `known_violations` | nessuna |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `missing_information` | asset.physical_protection_documented, asset.physical_protection_documented:not_declared, evidence.physical_security |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `nis_profile` | essential |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `reason` | Dati o evidenze non consentono una verifica conclusiva. |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `recommendation` | Acquisire evidenza corrente delle protezioni fisiche applicabili. |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `requirement_id` | REQ-PR-AA-06 |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `rule_id` | RULE-PR-AA-06 |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `technical_status` | not_verifiable |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 736d6caf-aace-5f7f-956d-3ee3454dd915 (`736d6caf-aace-5f7f-956d-3ee3454dd915`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `acn_point` | PR.DS-01 |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `confidence_level` | insufficient |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `control_id` | CTRL-PR-DS-01 |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `decision_policy` | all_required |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `errors` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `governance_status` | none |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `id` | 39e058e6-5280-5324-b082-6ef01f2e9d00 |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `known_violations` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `missing_information` | DataObject.inventory_status |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `nis_profile` | essential |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `reason` | completezza dell'inventario DataObject non nota |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `recommendation` | Cifrare i supporti rimovibili secondo classificazione e baseline approvata. |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `requirement_id` | REQ-PR-DS-01 |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `rule_id` | RULE-PR-DS-01 |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `technical_status` | not_verifiable |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 39e058e6-5280-5324-b082-6ef01f2e9d00 (`39e058e6-5280-5324-b082-6ef01f2e9d00`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `acn_point` | PR.DS-02 |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `confidence_level` | high |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `control_id` | CTRL-PR-DS-02 |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `decision_policy` | all_required |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-encryption"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "Service.svc-delta-https.encrypted", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-delta-https.tls_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "baseline crittografica", "comparison_result": false, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": ["TLSv1.0"], "path": "Service.svc-delta-https.tls_versions", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "evidence.ev-delta-encryption.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `errors` | nessuna |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "Service.svc-delta-https.encrypted", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-delta-https.tls_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "baseline crittografica", "comparison_result": false, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": ["TLSv1.0"], "path": "Service.svc-delta-https.tls_versions", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `evidence_ids` | ev-delta-encryption |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `governance_status` | none |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `id` | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `information_actions` | nessuna |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "Service.svc-delta-https.encrypted", "remediation": "Allineare i protocolli alla baseline crittografica approvata."}, {"comparison": "baseline crittografica", "observed_value": ["TLSv1.0"], "path": "Service.svc-delta-https.tls_versions", "remediation": "Allineare i protocolli alla baseline crittografica approvata."}] |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `missing_information` | nessuna |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `nis_profile` | essential |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `recommendation` | Allineare i protocolli alla baseline crittografica approvata. |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `requirement_id` | REQ-PR-DS-02 |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `rule_id` | RULE-PR-DS-02 |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `technical_remediations` | Allineare i protocolli alla baseline crittografica approvata. |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `technical_status` | non_compliant |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `thresholds_used_json` | {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "evidence.ev-delta-encryption.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}} |
| Esiti della valutazione | 6e2b2dc5-5977-5a3b-99ed-b40922a62e7c (`6e2b2dc5-5977-5a3b-99ed-b40922a62e7c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `confidence_level` | medium |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `control_id` | CTRL-PR-DS-11 |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `decision_policy` | all_required |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-backup"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.frequency_within_plan", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.offline_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `errors` | nessuna |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.frequency_within_plan", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.offline_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}] |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `evidence_ids` | ev-delta-backup |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `governance_status` | none |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `id` | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `information_actions` | nessuna |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "BackupRecord.backup-delta-core.frequency_within_plan", "remediation": "Adeguare frequenza e copie offline al piano approvato."}, {"comparison": "true", "observed_value": false, "path": "BackupRecord.backup-delta-core.offline_copy", "remediation": "Adeguare frequenza e copie offline al piano approvato."}] |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `missing_information` | nessuna |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `nis_profile` | essential |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `recommendation` | Adeguare frequenza e copie offline al piano approvato. |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `requirement_id` | REQ-PR-DS-11 |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `rule_id` | RULE-PR-DS-11 |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `technical_remediations` | Adeguare frequenza e copie offline al piano approvato. |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `technical_status` | non_compliant |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `thresholds_used_json` | {"evidence.ev-delta-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d (`24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `confidence_level` | medium |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `control_id` | CTRL-PR-DS-11-E |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `decision_policy` | all_required |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-backup", "ev-delta-restore"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.protected_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.restore_test_successful", "provenance_ids": ["prov-backup"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-delta-restore.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `errors` | nessuna |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.protected_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": false, "path": "BackupRecord.backup-delta-core.restore_test_successful", "provenance_ids": ["prov-backup"], "value_status": "known"}] |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `evidence_ids` | ev-delta-backup, ev-delta-restore |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `governance_status` | none |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `id` | addb2b61-1c04-5192-a578-8b6e94c68c9e |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `information_actions` | nessuna |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "BackupRecord.backup-delta-core.protected_copy", "remediation": "Proteggere le copie e completare con successo le prove di ripristino pianificate."}, {"comparison": "true", "observed_value": false, "path": "BackupRecord.backup-delta-core.restore_test_successful", "remediation": "Proteggere le copie e completare con successo le prove di ripristino pianificate."}] |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `missing_information` | nessuna |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `nis_profile` | essential |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `recommendation` | Proteggere le copie e completare con successo le prove di ripristino pianificate. |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `requirement_id` | REQ-PR-DS-11-E |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `rule_id` | RULE-PR-DS-11-E |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `technical_remediations` | Proteggere le copie e completare con successo le prove di ripristino pianificate. |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `technical_status` | non_compliant |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `thresholds_used_json` | {"evidence.ev-delta-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-delta-restore.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}} |
| Esiti della valutazione | addb2b61-1c04-5192-a578-8b6e94c68c9e (`addb2b61-1c04-5192-a578-8b6e94c68c9e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `acn_point` | PR.PS-01 |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `confidence_level` | high |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `control_id` | CTRL-PR-PS-01-E |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `decision_policy` | all_required |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-system"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.hardening_baseline_applied", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "manual_review_required", "nis_profile": "essential", "rule_id": "RULE-PR-PS-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-system.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `errors` | nessuna |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.hardening_baseline_applied", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `evidence_ids` | ev-delta-system |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `governance_status` | manual_review_required |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `id` | 7148cb04-f822-547f-801d-368bd0a766c8 |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `information_actions` | nessuna |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.hardening_baseline_applied", "remediation": "Applicare e versionare una baseline di hardening appropriata."}] |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `missing_information` | nessuna |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `nis_profile` | essential |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `recommendation` | Applicare e versionare una baseline di hardening appropriata. |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `requirement_id` | REQ-PR-PS-01-E |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `rule_id` | RULE-PR-PS-01-E |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `technical_exception_id` | exception-delta-hardening |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `technical_remediations` | Applicare e versionare una baseline di hardening appropriata. |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `technical_status` | non_compliant |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `thresholds_used_json` | {"evidence.ev-delta-system.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 7148cb04-f822-547f-801d-368bd0a766c8 (`7148cb04-f822-547f-801d-368bd0a766c8`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `confidence_level` | medium |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `control_id` | CTRL-PR-PS-02 |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `decision_policy` | all_required |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-patch", "ev-delta-software"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "{supported}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "unsupported", "path": "SoftwareComponent.software-delta-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-delta-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-delta-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `errors` | nessuna |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `evaluated_facts_json` | [{"comparison": "{supported}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "unsupported", "path": "SoftwareComponent.software-delta-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-delta-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `evidence_ids` | ev-delta-patch, ev-delta-software |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `governance_status` | none |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `id` | 7921a7d9-e961-5f84-81d2-7222735a125c |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `information_actions` | nessuna |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `known_violations_json` | [{"comparison": "{supported}", "observed_value": "unsupported", "path": "SoftwareComponent.software-delta-core.support_status", "remediation": "Sostituire software fuori supporto e rispettare i termini del piano di patching."}, {"comparison": "{current, within_risk_plan}", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-delta-core.security_update_status", "remediation": "Sostituire software fuori supporto e rispettare i termini del piano di patching."}] |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `missing_information` | nessuna |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `nis_profile` | essential |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `recommendation` | Sostituire software fuori supporto e rispettare i termini del piano di patching. |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `requirement_id` | REQ-PR-PS-02 |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `rule_id` | RULE-PR-PS-02 |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `technical_remediations` | Sostituire software fuori supporto e rispettare i termini del piano di patching. |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `technical_status` | non_compliant |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `thresholds_used_json` | {"evidence.ev-delta-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-delta-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 7921a7d9-e961-5f84-81d2-7222735a125c (`7921a7d9-e961-5f84-81d2-7222735a125c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `confidence_level` | medium |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `control_id` | CTRL-PR-PS-02-E |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `decision_policy` | all_required |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-patch"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "{supported}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "unsupported", "path": "SoftwareComponent.software-delta-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-delta-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": false, "path": "SoftwareComponent.software-delta-core.critical_update_tested", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `errors` | nessuna |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `evaluated_facts_json` | [{"comparison": "{supported}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "unsupported", "path": "SoftwareComponent.software-delta-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-delta-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": false, "path": "SoftwareComponent.software-delta-core.critical_update_tested", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `evidence_ids` | ev-delta-patch |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `governance_status` | none |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `id` | 86104e8e-ed72-542f-b7b3-de52032ffa4b |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `information_actions` | nessuna |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `known_violations_json` | [{"comparison": "{supported}", "observed_value": "unsupported", "path": "SoftwareComponent.software-delta-core.support_status", "remediation": "Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista."}, {"comparison": "{current, within_risk_plan}", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-delta-core.security_update_status", "remediation": "Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista."}, {"comparison": "true", "observed_value": false, "path": "SoftwareComponent.software-delta-core.critical_update_tested", "remediation": "Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista."}] |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `missing_information` | nessuna |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `nis_profile` | essential |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `recommendation` | Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista. |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `requirement_id` | REQ-PR-PS-02-E |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `rule_id` | RULE-PR-PS-02-E |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `technical_remediations` | Testare e tracciare gli aggiornamenti critici prima della distribuzione prevista. |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `technical_status` | non_compliant |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `thresholds_used_json` | {"evidence.ev-delta-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 86104e8e-ed72-542f-b7b3-de52032ffa4b (`86104e8e-ed72-542f-b7b3-de52032ffa4b`) | `verification_mode` | direct_technical |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `acn_point` | PR.PS-03 |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `confidence_level` | low |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `conflicting_information` | nessuna |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `control_id` | CTRL-PR-PS-03-E |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `decision_policy` | all_required |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-maintenance"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.maintenance_logged", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.secure_disposal_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-maintenance.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `errors` | nessuna |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.maintenance_logged", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.secure_disposal_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `evidence_ids` | ev-delta-maintenance |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `governance_status` | none |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `id` | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `information_actions` | nessuna |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.maintenance_logged", "remediation": "Registrare manutenzione e procedure di dismissione sicura."}, {"comparison": "true", "observed_value": false, "path": "asset.secure_disposal_documented", "remediation": "Registrare manutenzione e procedure di dismissione sicura."}] |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `missing_information` | nessuna |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `nis_profile` | essential |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `recommendation` | Registrare manutenzione e procedure di dismissione sicura. |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `requirement_id` | REQ-PR-PS-03-E |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `rule_id` | RULE-PR-PS-03-E |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `selector_decisions` | nessuna |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `technical_remediations` | Registrare manutenzione e procedure di dismissione sicura. |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `technical_status` | non_compliant |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `thresholds_used_json` | {"evidence.ev-delta-maintenance.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | ae29b32b-98a8-5977-b4e7-8d70d6d4dd43 (`ae29b32b-98a8-5977-b4e7-8d70d6d4dd43`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `acn_point` | PR.PS-04 |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `confidence_level` | low |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `conflicting_information` | nessuna |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `control_id` | CTRL-PR-PS-04 |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `decision_policy` | all_required |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-log"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.admin_remote_access_logging", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.logs_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": false, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.logs_centralized", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.log_retention_within_plan", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-log.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `errors` | nessuna |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.admin_remote_access_logging", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.logs_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": false, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.logs_centralized", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.log_retention_within_plan", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `evidence_ids` | ev-delta-log |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `governance_status` | none |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `id` | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `information_actions` | nessuna |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.admin_remote_access_logging", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato."}, {"comparison": "true", "observed_value": false, "path": "asset.logs_protected", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato."}, {"comparison": "true", "observed_value": false, "path": "asset.log_retention_within_plan", "remediation": "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato."}] |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `missing_information` | nessuna |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `nis_profile` | essential |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `recommendation` | Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato. |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `requirement_id` | REQ-PR-PS-04 |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `rule_id` | RULE-PR-PS-04 |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `selector_decisions` | nessuna |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `technical_remediations` | Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato. |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `technical_status` | non_compliant |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `thresholds_used_json` | {"evidence.ev-delta-log.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f (`fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `acn_point` | PR.IR-01 |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `confidence_level` | low |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `control_id` | CTRL-PR-IR-01 |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `decision_policy` | all_required |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-network"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.remote_access_registry_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.remote_access_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.firewall_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-network.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `errors` | nessuna |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.remote_access_registry_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.remote_access_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.firewall_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `evidence_ids` | ev-delta-network |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `governance_status` | none |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `id` | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `information_actions` | nessuna |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.remote_access_registry_complete", "remediation": "Governare gli accessi remoti e applicare regole firewall approvate."}, {"comparison": "true", "observed_value": false, "path": "asset.remote_access_protected", "remediation": "Governare gli accessi remoti e applicare regole firewall approvate."}, {"comparison": "true", "observed_value": false, "path": "asset.firewall_enabled", "remediation": "Governare gli accessi remoti e applicare regole firewall approvate."}] |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `missing_information` | nessuna |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `nis_profile` | essential |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `recommendation` | Governare gli accessi remoti e applicare regole firewall approvate. |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `requirement_id` | REQ-PR-IR-01 |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `rule_id` | RULE-PR-IR-01 |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `technical_remediations` | Governare gli accessi remoti e applicare regole firewall approvate. |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `technical_status` | non_compliant |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `thresholds_used_json` | {"evidence.ev-delta-network.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 0534ef1c-4ab5-586a-926e-8b24e75d2ee5 (`0534ef1c-4ab5-586a-926e-8b24e75d2ee5`) | `verification_mode` | direct_technical |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `acn_point` | PR.IR-03 |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `confidence_level` | high |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `conflicting_information` | nessuna |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `control_id` | CTRL-PR-IR-03-E |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `decision_policy` | all_required |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-emergency"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-delta-emergency.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-emergency.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-emergency.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-emergency.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `errors` | nessuna |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-delta-emergency.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-emergency.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-emergency.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `evidence_ids` | ev-delta-emergency |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `governance_status` | none |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `id` | c156bb48-3c77-5851-ac1f-b041c9fca5a3 |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `information_actions` | nessuna |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-emergency.configured", "remediation": "Predisporre testare e mantenere comunicazioni di emergenza protette."}, {"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-emergency.maintained", "remediation": "Predisporre testare e mantenere comunicazioni di emergenza protette."}] |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `missing_information` | nessuna |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `nis_profile` | essential |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `recommendation` | Predisporre testare e mantenere comunicazioni di emergenza protette. |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `requirement_id` | REQ-PR-IR-03-E |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `rule_id` | RULE-PR-IR-03-E |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `selector_decisions` | nessuna |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `technical_remediations` | Predisporre testare e mantenere comunicazioni di emergenza protette. |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `technical_status` | non_compliant |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `thresholds_used_json` | {"evidence.ev-delta-emergency.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | c156bb48-3c77-5851-ac1f-b041c9fca5a3 (`c156bb48-3c77-5851-ac1f-b041c9fca5a3`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `confidence_level` | high |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `control_id` | CTRL-DE-CM-01 |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `decision_policy` | all_required |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-monitoring"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `errors` | nessuna |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `evidence_ids` | ev-delta-monitoring |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `governance_status` | none |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `id` | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `information_actions` | nessuna |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.enabled", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti."}, {"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.configured", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti."}, {"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-ids.monitored", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti."}] |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `missing_information` | nessuna |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `nis_profile` | essential |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `recommendation` | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `requirement_id` | REQ-DE-CM-01 |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `rule_id` | RULE-DE-CM-01 |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `technical_remediations` | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `technical_status` | non_compliant |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `thresholds_used_json` | {"evidence.ev-delta-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 1b28aa3c-866b-5ecd-b2de-c9c6a84a9357 (`1b28aa3c-866b-5ecd-b2de-c9c6a84a9357`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `confidence_level` | high |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `control_id` | CTRL-DE-CM-01-E |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `decision_policy` | all_required |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-monitoring"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.anomaly_thresholds_configured", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `errors` | nessuna |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.anomaly_thresholds_configured", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `evidence_ids` | ev-delta-monitoring |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `governance_status` | none |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `id` | 66286b28-a64b-5036-b99e-cfefdd09ec2c |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `information_actions` | nessuna |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.anomaly_thresholds_configured", "remediation": "Calibrare e riesaminare soglie e regole di anomalia."}] |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `missing_information` | nessuna |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `nis_profile` | essential |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `recommendation` | Calibrare e riesaminare soglie e regole di anomalia. |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `requirement_id` | REQ-DE-CM-01-E |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `rule_id` | RULE-DE-CM-01-E |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `technical_remediations` | Calibrare e riesaminare soglie e regole di anomalia. |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `technical_status` | non_compliant |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `thresholds_used_json` | {"evidence.ev-delta-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 66286b28-a64b-5036-b99e-cfefdd09ec2c (`66286b28-a64b-5036-b99e-cfefdd09ec2c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `acn_point` | DE.CM-09 |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `asset_id` | asset-delta-core |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `confidence_level` | high |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `control_id` | CTRL-DE-CM-09 |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `decision_policy` | all_required |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-delta-endpoint"], "asset_id": "asset-delta-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-09", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-delta-endpoint.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `errors` | nessuna |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `evidence_ids` | ev-delta-endpoint |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `governance_status` | none |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `id` | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `information_actions` | nessuna |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.enabled", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata."}, {"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.configured", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata."}, {"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.maintained", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata."}, {"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-delta-endpoint.monitored", "remediation": "Installare configurare mantenere e monitorare la protezione endpoint appropriata."}] |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `missing_information` | nessuna |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `nis_profile` | essential |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `recommendation` | Installare configurare mantenere e monitorare la protezione endpoint appropriata. |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `requirement_id` | REQ-DE-CM-09 |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `rule_id` | RULE-DE-CM-09 |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `technical_remediations` | Installare configurare mantenere e monitorare la protezione endpoint appropriata. |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `technical_status` | non_compliant |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `thresholds_used_json` | {"evidence.ev-delta-endpoint.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 45e763f5-3989-5177-9bbb-8bc07e7c4dcb (`45e763f5-3989-5177-9bbb-8bc07e7c4dcb`) | `verification_mode` | direct_technical |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `acn_point` | ID.AM-01 |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `confidence_level` | insufficient |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `conflicting_information` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `control_id` | CTRL-ID-AM-01 |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `decision_policy` | all_required |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `errors` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `evidence_ids` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `governance_status` | none |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `id` | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `information_actions` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `known_violations` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `missing_information` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `nis_profile` | essential |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `requirement_id` | REQ-ID-AM-01 |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `rule_id` | RULE-ID-AM-01 |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `selector_decisions` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `technical_remediations` | nessuna |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `technical_status` | not_applicable |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `thresholds_used_json` | {} |
| Esiti della valutazione | de2c79d8-fd43-5ebf-8d5a-5c8896101d29 (`de2c79d8-fd43-5ebf-8d5a-5c8896101d29`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `acn_point` | ID.AM-02 |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `confidence_level` | insufficient |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `control_id` | CTRL-ID-AM-02 |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `decision_policy` | all_required |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `errors` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `governance_status` | none |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `id` | 3e075956-8a97-59f9-9453-a96d35311a9d |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `information_actions` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `known_violations` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `missing_information` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `nis_profile` | essential |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `requirement_id` | REQ-ID-AM-02 |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `rule_id` | RULE-ID-AM-02 |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `technical_status` | not_applicable |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 3e075956-8a97-59f9-9453-a96d35311a9d (`3e075956-8a97-59f9-9453-a96d35311a9d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `acn_point` | ID.AM-03 |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `confidence_level` | insufficient |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `conflicting_information` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `control_id` | CTRL-ID-AM-03-E |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `decision_policy` | all_required |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `errors` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `evidence_ids` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `governance_status` | none |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `id` | dcaaa43d-fc5c-578a-864d-d64dcc363360 |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `information_actions` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `known_violations` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `missing_information` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `nis_profile` | essential |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `requirement_id` | REQ-ID-AM-03-E |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `rule_id` | RULE-ID-AM-03-E |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `selector_decisions` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `technical_remediations` | nessuna |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `technical_status` | not_applicable |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `thresholds_used_json` | {} |
| Esiti della valutazione | dcaaa43d-fc5c-578a-864d-d64dcc363360 (`dcaaa43d-fc5c-578a-864d-d64dcc363360`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `acn_point` | ID.AM-04 |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `confidence_level` | insufficient |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `control_id` | CTRL-ID-AM-04 |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `decision_policy` | all_required |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `errors` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `governance_status` | none |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `id` | 21ef177c-0d23-5ae0-8cad-e0d3b809178f |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `information_actions` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `known_violations` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `missing_information` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `nis_profile` | essential |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `requirement_id` | REQ-ID-AM-04 |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `rule_id` | RULE-ID-AM-04 |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `technical_status` | not_applicable |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 21ef177c-0d23-5ae0-8cad-e0d3b809178f (`21ef177c-0d23-5ae0-8cad-e0d3b809178f`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `confidence_level` | insufficient |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `control_id` | CTRL-ID-RA-01 |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `decision_policy` | all_required |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `errors` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `evidence_ids` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `governance_status` | none |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `id` | a2eb9293-638a-54f0-9836-9a9ed675558d |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `information_actions` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `known_violations` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `missing_information` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `nis_profile` | essential |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `requirement_id` | REQ-ID-RA-01 |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `rule_id` | RULE-ID-RA-01 |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `technical_status` | not_applicable |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `thresholds_used_json` | {} |
| Esiti della valutazione | a2eb9293-638a-54f0-9836-9a9ed675558d (`a2eb9293-638a-54f0-9836-9a9ed675558d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `confidence_level` | insufficient |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `control_id` | CTRL-ID-RA-01-E |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `decision_policy` | all_required |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `errors` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `governance_status` | none |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `id` | 02931dc5-a262-52ab-bf4a-19373c4f0050 |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `information_actions` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `known_violations` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `missing_information` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `nis_profile` | essential |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `requirement_id` | REQ-ID-RA-01-E |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `rule_id` | RULE-ID-RA-01-E |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `technical_status` | not_applicable |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 02931dc5-a262-52ab-bf4a-19373c4f0050 (`02931dc5-a262-52ab-bf4a-19373c4f0050`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `confidence_level` | insufficient |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `control_id` | CTRL-ID-RA-08 |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `decision_policy` | all_required |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `errors` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `governance_status` | none |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `id` | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `information_actions` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `known_violations` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `missing_information` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `nis_profile` | essential |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `requirement_id` | REQ-ID-RA-08 |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `rule_id` | RULE-ID-RA-08 |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `technical_status` | not_applicable |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 8cd984bf-5bdb-5675-b579-2eb4a5078bd4 (`8cd984bf-5bdb-5675-b579-2eb4a5078bd4`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `confidence_level` | insufficient |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `control_id` | CTRL-ID-RA-08-E |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `decision_policy` | all_required |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `errors` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `governance_status` | none |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `id` | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `information_actions` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `known_violations` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `missing_information` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `nis_profile` | essential |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `requirement_id` | REQ-ID-RA-08-E |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `rule_id` | RULE-ID-RA-08-E |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `technical_status` | not_applicable |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 71ac75bb-5a78-56d8-8796-138c3aff6fb1 (`71ac75bb-5a78-56d8-8796-138c3aff6fb1`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `acn_point` | PR.AA-01 |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `confidence_level` | insufficient |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `control_id` | CTRL-PR-AA-01 |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `decision_policy` | all_required |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `errors` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `governance_status` | none |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `id` | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `information_actions` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `known_violations` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `missing_information` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `nis_profile` | essential |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `requirement_id` | REQ-PR-AA-01 |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `rule_id` | RULE-PR-AA-01 |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `technical_status` | not_applicable |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 9d2cbe7e-5702-558e-9d08-e6d5868283c1 (`9d2cbe7e-5702-558e-9d08-e6d5868283c1`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `acn_point` | PR.AA-03 |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `confidence_level` | insufficient |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `control_id` | CTRL-PR-AA-03 |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `decision_policy` | all_required |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-03", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `errors` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `governance_status` | none |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `id` | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `information_actions` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `known_violations` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `missing_information` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `nis_profile` | essential |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `requirement_id` | REQ-PR-AA-03 |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `rule_id` | RULE-PR-AA-03 |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `technical_status` | not_applicable |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 83f6d6b9-eeb9-500a-8a7c-3f135af47eed (`83f6d6b9-eeb9-500a-8a7c-3f135af47eed`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `acn_point` | PR.AA-05 |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `confidence_level` | insufficient |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `control_id` | CTRL-PR-AA-05 |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `decision_policy` | all_required |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-05", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `errors` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `governance_status` | none |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `id` | 0003441d-fc06-5e81-848f-24b798b8a6a1 |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `information_actions` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `known_violations` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `missing_information` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `nis_profile` | essential |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `requirement_id` | REQ-PR-AA-05 |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `rule_id` | RULE-PR-AA-05 |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `technical_status` | not_applicable |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 0003441d-fc06-5e81-848f-24b798b8a6a1 (`0003441d-fc06-5e81-848f-24b798b8a6a1`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `acn_point` | PR.AA-06 |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `confidence_level` | insufficient |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `control_id` | CTRL-PR-AA-06 |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `decision_policy` | all_required |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-06", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `errors` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `governance_status` | none |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `id` | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `information_actions` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `known_violations` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `missing_information` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `nis_profile` | essential |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `requirement_id` | REQ-PR-AA-06 |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `rule_id` | RULE-PR-AA-06 |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `technical_status` | not_applicable |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 947e7d7b-cf4d-5ca3-b2b6-95d01d698733 (`947e7d7b-cf4d-5ca3-b2b6-95d01d698733`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `acn_point` | PR.DS-01 |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `confidence_level` | insufficient |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `control_id` | CTRL-PR-DS-01 |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `decision_policy` | all_required |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `errors` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `governance_status` | none |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `id` | 810f76d0-8eb9-5119-acb9-7e7c52adce93 |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `information_actions` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `known_violations` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `missing_information` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `nis_profile` | essential |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `requirement_id` | REQ-PR-DS-01 |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `rule_id` | RULE-PR-DS-01 |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `technical_status` | not_applicable |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 810f76d0-8eb9-5119-acb9-7e7c52adce93 (`810f76d0-8eb9-5119-acb9-7e7c52adce93`) | `verification_mode` | direct_technical |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `acn_point` | PR.DS-02 |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `confidence_level` | insufficient |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `conflicting_information` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `control_id` | CTRL-PR-DS-02 |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `decision_policy` | all_required |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {"origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `errors` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `evidence_ids` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `governance_status` | none |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `id` | e16edf55-f114-514a-b316-8421d19c5f56 |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `information_actions` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `known_violations` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `missing_information` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `nis_profile` | essential |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `requirement_id` | REQ-PR-DS-02 |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `rule_id` | RULE-PR-DS-02 |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `selector_decisions` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `technical_remediations` | nessuna |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `technical_status` | not_applicable |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `thresholds_used_json` | {"origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}} |
| Esiti della valutazione | e16edf55-f114-514a-b316-8421d19c5f56 (`e16edf55-f114-514a-b316-8421d19c5f56`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `confidence_level` | insufficient |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `control_id` | CTRL-PR-DS-11 |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `decision_policy` | all_required |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `errors` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `governance_status` | none |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `id` | 742f0a86-41c5-5fb4-a7cf-eedded238636 |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `information_actions` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `known_violations` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `missing_information` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `nis_profile` | essential |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `requirement_id` | REQ-PR-DS-11 |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `rule_id` | RULE-PR-DS-11 |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `technical_status` | not_applicable |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 742f0a86-41c5-5fb4-a7cf-eedded238636 (`742f0a86-41c5-5fb4-a7cf-eedded238636`) | `verification_mode` | direct_technical |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `confidence_level` | insufficient |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `conflicting_information` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `control_id` | CTRL-PR-DS-11-E |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `decision_policy` | all_required |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `errors` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `evidence_ids` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `governance_status` | none |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `id` | afbdda04-a07f-594e-860c-04fa2533c2ac |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `information_actions` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `known_violations` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `missing_information` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `nis_profile` | essential |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `requirement_id` | REQ-PR-DS-11-E |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `rule_id` | RULE-PR-DS-11-E |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `selector_decisions` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `technical_remediations` | nessuna |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `technical_status` | not_applicable |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `thresholds_used_json` | {} |
| Esiti della valutazione | afbdda04-a07f-594e-860c-04fa2533c2ac (`afbdda04-a07f-594e-860c-04fa2533c2ac`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `acn_point` | PR.PS-01 |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `confidence_level` | insufficient |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `control_id` | CTRL-PR-PS-01-E |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `decision_policy` | all_required |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `errors` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `governance_status` | none |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `id` | 10b56a51-33a8-553e-b7ed-2a440834bcec |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `information_actions` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `known_violations` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `missing_information` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `nis_profile` | essential |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `requirement_id` | REQ-PR-PS-01-E |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `rule_id` | RULE-PR-PS-01-E |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `technical_status` | not_applicable |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 10b56a51-33a8-553e-b7ed-2a440834bcec (`10b56a51-33a8-553e-b7ed-2a440834bcec`) | `verification_mode` | direct_technical |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `confidence_level` | insufficient |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `control_id` | CTRL-PR-PS-02 |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `decision_policy` | all_required |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `errors` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `evidence_ids` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `governance_status` | none |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `id` | a7882c14-37b9-5f2c-a01c-31a76aa326ff |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `information_actions` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `known_violations` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `missing_information` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `nis_profile` | essential |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `requirement_id` | REQ-PR-PS-02 |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `rule_id` | RULE-PR-PS-02 |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `technical_status` | not_applicable |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `thresholds_used_json` | {} |
| Esiti della valutazione | a7882c14-37b9-5f2c-a01c-31a76aa326ff (`a7882c14-37b9-5f2c-a01c-31a76aa326ff`) | `verification_mode` | direct_technical |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `confidence_level` | insufficient |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `control_id` | CTRL-PR-PS-02-E |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `decision_policy` | all_required |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `errors` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `evidence_ids` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `governance_status` | none |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `id` | a65a4440-bd6f-592e-94e6-3198c2339d0f |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `information_actions` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `known_violations` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `missing_information` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `nis_profile` | essential |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `requirement_id` | REQ-PR-PS-02-E |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `rule_id` | RULE-PR-PS-02-E |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `technical_status` | not_applicable |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `thresholds_used_json` | {} |
| Esiti della valutazione | a65a4440-bd6f-592e-94e6-3198c2339d0f (`a65a4440-bd6f-592e-94e6-3198c2339d0f`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `acn_point` | PR.PS-03 |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `confidence_level` | insufficient |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `control_id` | CTRL-PR-PS-03-E |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `decision_policy` | all_required |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `errors` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `governance_status` | none |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `id` | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `information_actions` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `known_violations` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `missing_information` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `nis_profile` | essential |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `requirement_id` | REQ-PR-PS-03-E |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `rule_id` | RULE-PR-PS-03-E |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `technical_status` | not_applicable |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e (`6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `acn_point` | PR.PS-04 |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `confidence_level` | insufficient |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `control_id` | CTRL-PR-PS-04 |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `decision_policy` | all_required |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `errors` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `governance_status` | none |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `id` | 700d7d03-0cc6-5630-82da-9c51576a8d59 |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `information_actions` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `known_violations` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `missing_information` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `nis_profile` | essential |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `requirement_id` | REQ-PR-PS-04 |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `rule_id` | RULE-PR-PS-04 |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `technical_status` | not_applicable |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 700d7d03-0cc6-5630-82da-9c51576a8d59 (`700d7d03-0cc6-5630-82da-9c51576a8d59`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `acn_point` | PR.IR-01 |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `confidence_level` | insufficient |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `control_id` | CTRL-PR-IR-01 |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `decision_policy` | all_required |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `errors` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `governance_status` | none |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `id` | 78808e70-9f89-5283-b1c3-be1918e4807c |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `information_actions` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `known_violations` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `missing_information` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `nis_profile` | essential |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `requirement_id` | REQ-PR-IR-01 |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `rule_id` | RULE-PR-IR-01 |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `technical_status` | not_applicable |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 78808e70-9f89-5283-b1c3-be1918e4807c (`78808e70-9f89-5283-b1c3-be1918e4807c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `acn_point` | PR.IR-03 |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `confidence_level` | insufficient |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `conflicting_information` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `control_id` | CTRL-PR-IR-03-E |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `decision_policy` | all_required |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `errors` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `evidence_ids` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `governance_status` | none |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `id` | d9451c7d-8f53-513b-a4b7-e612444693f0 |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `information_actions` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `known_violations` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `missing_information` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `nis_profile` | essential |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `requirement_id` | REQ-PR-IR-03-E |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `rule_id` | RULE-PR-IR-03-E |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `selector_decisions` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `technical_remediations` | nessuna |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `technical_status` | not_applicable |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `thresholds_used_json` | {} |
| Esiti della valutazione | d9451c7d-8f53-513b-a4b7-e612444693f0 (`d9451c7d-8f53-513b-a4b7-e612444693f0`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `confidence_level` | insufficient |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `control_id` | CTRL-DE-CM-01 |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `decision_policy` | all_required |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `errors` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `governance_status` | none |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `id` | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `information_actions` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `known_violations` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `missing_information` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `nis_profile` | essential |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `requirement_id` | REQ-DE-CM-01 |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `rule_id` | RULE-DE-CM-01 |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `technical_status` | not_applicable |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 9b8a22f1-fafd-5bbd-87c9-c63519d2be46 (`9b8a22f1-fafd-5bbd-87c9-c63519d2be46`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `confidence_level` | insufficient |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `control_id` | CTRL-DE-CM-01-E |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `decision_policy` | all_required |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `errors` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `governance_status` | none |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `id` | 92682466-8a38-5c94-9e5e-3087118fccbc |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `information_actions` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `known_violations` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `missing_information` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `nis_profile` | essential |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `requirement_id` | REQ-DE-CM-01-E |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `rule_id` | RULE-DE-CM-01-E |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `technical_status` | not_applicable |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 92682466-8a38-5c94-9e5e-3087118fccbc (`92682466-8a38-5c94-9e5e-3087118fccbc`) | `verification_mode` | direct_technical |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `acn_point` | DE.CM-09 |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `assessment_id` | scenario-delta-essential-critical |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `asset_id` | asset-delta-aux |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `confidence_level` | insufficient |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `conflicting_information` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `control_id` | CTRL-DE-CM-09 |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `decision_policy` | all_required |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-delta-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-09", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `errors` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `evidence_ids` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `governance_status` | none |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `id` | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `information_actions` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `known_violations` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `missing_information` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `nis_profile` | essential |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `requirement_id` | REQ-DE-CM-09 |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `rule_id` | RULE-DE-CM-09 |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `selector_decisions` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `technical_remediations` | nessuna |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `technical_status` | not_applicable |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `thresholds_used_json` | {} |
| Esiti della valutazione | fec8881c-5784-5f1f-ac03-0beb3ef00ab0 (`fec8881c-5784-5f1f-ac03-0beb3ef00ab0`) | `verification_mode` | direct_technical |

## Inventario completo delle relazioni

| Nodo di partenza | Relazione | Nodo di arrivo |
|---|---|---|
| `asset-delta-core` | espone (`EXPOSES`) | `svc-delta-https` |
| `asset-delta-core` | tratta (`PROCESSES`) | `data-delta-core` |
| `asset-delta-core` | è gestito da (`MANAGED_BY`) | `owner-delta-ops` |
| `vuln-delta-001` | interessa (`AFFECTS`) | `asset-delta-core` |
| `asset-delta-core` | è protetto da (`PROTECTED_BY`) | `cap-delta-endpoint` |
| `proc-delta-core` | dipende da (`DEPENDS_ON`) | `asset-delta-core` |
| `dataset-delta-normalized-2026` | descrive (`DESCRIBES`) | `org-delta` |
| `RULE-ID-AM-01` | implementa (`IMPLEMENTS`) | `CTRL-ID-AM-01` |
| `RULE-ID-AM-01` | deriva da (`DERIVES_FROM`) | `REQ-ID-AM-01` |
| `RULE-ID-AM-02` | implementa (`IMPLEMENTS`) | `CTRL-ID-AM-02` |
| `RULE-ID-AM-02` | deriva da (`DERIVES_FROM`) | `REQ-ID-AM-02` |
| `RULE-ID-AM-03-E` | implementa (`IMPLEMENTS`) | `CTRL-ID-AM-03-E` |
| `RULE-ID-AM-03-E` | deriva da (`DERIVES_FROM`) | `REQ-ID-AM-03-E` |
| `RULE-ID-AM-04` | implementa (`IMPLEMENTS`) | `CTRL-ID-AM-04` |
| `RULE-ID-AM-04` | deriva da (`DERIVES_FROM`) | `REQ-ID-AM-04` |
| `RULE-ID-RA-01` | implementa (`IMPLEMENTS`) | `CTRL-ID-RA-01` |
| `RULE-ID-RA-01` | deriva da (`DERIVES_FROM`) | `REQ-ID-RA-01` |
| `RULE-ID-RA-01-E` | implementa (`IMPLEMENTS`) | `CTRL-ID-RA-01-E` |
| `RULE-ID-RA-01-E` | deriva da (`DERIVES_FROM`) | `REQ-ID-RA-01-E` |
| `RULE-ID-RA-08` | implementa (`IMPLEMENTS`) | `CTRL-ID-RA-08` |
| `RULE-ID-RA-08` | deriva da (`DERIVES_FROM`) | `REQ-ID-RA-08` |
| `RULE-ID-RA-08-E` | implementa (`IMPLEMENTS`) | `CTRL-ID-RA-08-E` |
| `RULE-ID-RA-08-E` | deriva da (`DERIVES_FROM`) | `REQ-ID-RA-08-E` |
| `RULE-PR-AA-01` | implementa (`IMPLEMENTS`) | `CTRL-PR-AA-01` |
| `RULE-PR-AA-01` | deriva da (`DERIVES_FROM`) | `REQ-PR-AA-01` |
| `RULE-PR-AA-03` | implementa (`IMPLEMENTS`) | `CTRL-PR-AA-03` |
| `RULE-PR-AA-03` | deriva da (`DERIVES_FROM`) | `REQ-PR-AA-03` |
| `RULE-PR-AA-05` | implementa (`IMPLEMENTS`) | `CTRL-PR-AA-05` |
| `RULE-PR-AA-05` | deriva da (`DERIVES_FROM`) | `REQ-PR-AA-05` |
| `RULE-PR-AA-06` | implementa (`IMPLEMENTS`) | `CTRL-PR-AA-06` |
| `RULE-PR-AA-06` | deriva da (`DERIVES_FROM`) | `REQ-PR-AA-06` |
| `RULE-PR-DS-01` | implementa (`IMPLEMENTS`) | `CTRL-PR-DS-01` |
| `RULE-PR-DS-01` | deriva da (`DERIVES_FROM`) | `REQ-PR-DS-01` |
| `RULE-PR-DS-02` | implementa (`IMPLEMENTS`) | `CTRL-PR-DS-02` |
| `RULE-PR-DS-02` | deriva da (`DERIVES_FROM`) | `REQ-PR-DS-02` |
| `RULE-PR-DS-11` | implementa (`IMPLEMENTS`) | `CTRL-PR-DS-11` |
| `RULE-PR-DS-11` | deriva da (`DERIVES_FROM`) | `REQ-PR-DS-11` |
| `RULE-PR-DS-11-E` | implementa (`IMPLEMENTS`) | `CTRL-PR-DS-11-E` |
| `RULE-PR-DS-11-E` | deriva da (`DERIVES_FROM`) | `REQ-PR-DS-11-E` |
| `RULE-PR-PS-01-E` | implementa (`IMPLEMENTS`) | `CTRL-PR-PS-01-E` |
| `RULE-PR-PS-01-E` | deriva da (`DERIVES_FROM`) | `REQ-PR-PS-01-E` |
| `RULE-PR-PS-02` | implementa (`IMPLEMENTS`) | `CTRL-PR-PS-02` |
| `RULE-PR-PS-02` | deriva da (`DERIVES_FROM`) | `REQ-PR-PS-02` |
| `RULE-PR-PS-02-E` | implementa (`IMPLEMENTS`) | `CTRL-PR-PS-02-E` |
| `RULE-PR-PS-02-E` | deriva da (`DERIVES_FROM`) | `REQ-PR-PS-02-E` |
| `RULE-PR-PS-03-E` | implementa (`IMPLEMENTS`) | `CTRL-PR-PS-03-E` |
| `RULE-PR-PS-03-E` | deriva da (`DERIVES_FROM`) | `REQ-PR-PS-03-E` |
| `RULE-PR-PS-04` | implementa (`IMPLEMENTS`) | `CTRL-PR-PS-04` |
| `RULE-PR-PS-04` | deriva da (`DERIVES_FROM`) | `REQ-PR-PS-04` |
| `RULE-PR-IR-01` | implementa (`IMPLEMENTS`) | `CTRL-PR-IR-01` |
| `RULE-PR-IR-01` | deriva da (`DERIVES_FROM`) | `REQ-PR-IR-01` |
| `RULE-PR-IR-03-E` | implementa (`IMPLEMENTS`) | `CTRL-PR-IR-03-E` |
| `RULE-PR-IR-03-E` | deriva da (`DERIVES_FROM`) | `REQ-PR-IR-03-E` |
| `RULE-DE-CM-01` | implementa (`IMPLEMENTS`) | `CTRL-DE-CM-01` |
| `RULE-DE-CM-01` | deriva da (`DERIVES_FROM`) | `REQ-DE-CM-01` |
| `RULE-DE-CM-01-E` | implementa (`IMPLEMENTS`) | `CTRL-DE-CM-01-E` |
| `RULE-DE-CM-01-E` | deriva da (`DERIVES_FROM`) | `REQ-DE-CM-01-E` |
| `RULE-DE-CM-09` | implementa (`IMPLEMENTS`) | `CTRL-DE-CM-09` |
| `RULE-DE-CM-09` | deriva da (`DERIVES_FROM`) | `REQ-DE-CM-09` |
| `d2bbd3a2-691c-51f2-b049-9400e7eeaeaf` | valuta (`EVALUATES`) | `asset-delta-core` |
| `d2bbd3a2-691c-51f2-b049-9400e7eeaeaf` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-01` |
| `d2bbd3a2-691c-51f2-b049-9400e7eeaeaf` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-01` |
| `d2bbd3a2-691c-51f2-b049-9400e7eeaeaf` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-01` |
| `db6b747d-ed2c-56d9-a44e-a3d7bba80e3c` | valuta (`EVALUATES`) | `asset-delta-core` |
| `db6b747d-ed2c-56d9-a44e-a3d7bba80e3c` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-02` |
| `db6b747d-ed2c-56d9-a44e-a3d7bba80e3c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-02` |
| `db6b747d-ed2c-56d9-a44e-a3d7bba80e3c` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-02` |
| `21318f70-a095-51ea-afff-68297a2c2fb1` | valuta (`EVALUATES`) | `asset-delta-core` |
| `21318f70-a095-51ea-afff-68297a2c2fb1` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-03-E` |
| `21318f70-a095-51ea-afff-68297a2c2fb1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-03-E` |
| `21318f70-a095-51ea-afff-68297a2c2fb1` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-03-E` |
| `68032e4d-3c55-5d5c-9e92-2c1bea0903f8` | valuta (`EVALUATES`) | `asset-delta-core` |
| `68032e4d-3c55-5d5c-9e92-2c1bea0903f8` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-04` |
| `68032e4d-3c55-5d5c-9e92-2c1bea0903f8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-04` |
| `68032e4d-3c55-5d5c-9e92-2c1bea0903f8` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-04` |
| `b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84` | valuta (`EVALUATES`) | `asset-delta-core` |
| `b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01` |
| `b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01` |
| `b8878be5-37e9-5e8a-9d6d-4c5c1ae66c84` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01` |
| `3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab` | valuta (`EVALUATES`) | `asset-delta-core` |
| `3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01-E` |
| `3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01-E` |
| `3c5c3fcf-4fed-5831-8a2f-1f2b7db58cab` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01-E` |
| `f53750a1-b38c-5313-ae50-f0f28a7f8550` | valuta (`EVALUATES`) | `asset-delta-core` |
| `f53750a1-b38c-5313-ae50-f0f28a7f8550` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08` |
| `f53750a1-b38c-5313-ae50-f0f28a7f8550` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08` |
| `f53750a1-b38c-5313-ae50-f0f28a7f8550` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08` |
| `bb194a5a-6411-5a0e-b7f2-8d000af407aa` | valuta (`EVALUATES`) | `asset-delta-core` |
| `bb194a5a-6411-5a0e-b7f2-8d000af407aa` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08-E` |
| `bb194a5a-6411-5a0e-b7f2-8d000af407aa` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08-E` |
| `bb194a5a-6411-5a0e-b7f2-8d000af407aa` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08-E` |
| `bf852d65-376e-5d3f-8bff-069ec968bb8b` | valuta (`EVALUATES`) | `asset-delta-core` |
| `bf852d65-376e-5d3f-8bff-069ec968bb8b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-01` |
| `bf852d65-376e-5d3f-8bff-069ec968bb8b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-01` |
| `bf852d65-376e-5d3f-8bff-069ec968bb8b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-01` |
| `2497016d-98aa-50c0-b10a-86df9c6f3647` | valuta (`EVALUATES`) | `asset-delta-core` |
| `2497016d-98aa-50c0-b10a-86df9c6f3647` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-03` |
| `2497016d-98aa-50c0-b10a-86df9c6f3647` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-03` |
| `2497016d-98aa-50c0-b10a-86df9c6f3647` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-03` |
| `24420cc8-ad6d-5614-ac2c-ee1b1c9dea45` | valuta (`EVALUATES`) | `asset-delta-core` |
| `24420cc8-ad6d-5614-ac2c-ee1b1c9dea45` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-05` |
| `24420cc8-ad6d-5614-ac2c-ee1b1c9dea45` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-05` |
| `24420cc8-ad6d-5614-ac2c-ee1b1c9dea45` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-05` |
| `736d6caf-aace-5f7f-956d-3ee3454dd915` | valuta (`EVALUATES`) | `asset-delta-core` |
| `736d6caf-aace-5f7f-956d-3ee3454dd915` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-06` |
| `736d6caf-aace-5f7f-956d-3ee3454dd915` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-06` |
| `736d6caf-aace-5f7f-956d-3ee3454dd915` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-06` |
| `39e058e6-5280-5324-b082-6ef01f2e9d00` | valuta (`EVALUATES`) | `asset-delta-core` |
| `39e058e6-5280-5324-b082-6ef01f2e9d00` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-01` |
| `39e058e6-5280-5324-b082-6ef01f2e9d00` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-01` |
| `39e058e6-5280-5324-b082-6ef01f2e9d00` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-01` |
| `6e2b2dc5-5977-5a3b-99ed-b40922a62e7c` | valuta (`EVALUATES`) | `asset-delta-core` |
| `6e2b2dc5-5977-5a3b-99ed-b40922a62e7c` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-02` |
| `6e2b2dc5-5977-5a3b-99ed-b40922a62e7c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-02` |
| `6e2b2dc5-5977-5a3b-99ed-b40922a62e7c` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-02` |
| `24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d` | valuta (`EVALUATES`) | `asset-delta-core` |
| `24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11` |
| `24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11` |
| `24184803-e3b0-5a1c-8b0e-7b97d6b7cd3d` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11` |
| `addb2b61-1c04-5192-a578-8b6e94c68c9e` | valuta (`EVALUATES`) | `asset-delta-core` |
| `addb2b61-1c04-5192-a578-8b6e94c68c9e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11-E` |
| `addb2b61-1c04-5192-a578-8b6e94c68c9e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11-E` |
| `addb2b61-1c04-5192-a578-8b6e94c68c9e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11-E` |
| `7148cb04-f822-547f-801d-368bd0a766c8` | valuta (`EVALUATES`) | `asset-delta-core` |
| `7148cb04-f822-547f-801d-368bd0a766c8` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-01-E` |
| `7148cb04-f822-547f-801d-368bd0a766c8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-01-E` |
| `7148cb04-f822-547f-801d-368bd0a766c8` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-01-E` |
| `7921a7d9-e961-5f84-81d2-7222735a125c` | valuta (`EVALUATES`) | `asset-delta-core` |
| `7921a7d9-e961-5f84-81d2-7222735a125c` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02` |
| `7921a7d9-e961-5f84-81d2-7222735a125c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02` |
| `7921a7d9-e961-5f84-81d2-7222735a125c` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02` |
| `86104e8e-ed72-542f-b7b3-de52032ffa4b` | valuta (`EVALUATES`) | `asset-delta-core` |
| `86104e8e-ed72-542f-b7b3-de52032ffa4b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02-E` |
| `86104e8e-ed72-542f-b7b3-de52032ffa4b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02-E` |
| `86104e8e-ed72-542f-b7b3-de52032ffa4b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02-E` |
| `ae29b32b-98a8-5977-b4e7-8d70d6d4dd43` | valuta (`EVALUATES`) | `asset-delta-core` |
| `ae29b32b-98a8-5977-b4e7-8d70d6d4dd43` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-03-E` |
| `ae29b32b-98a8-5977-b4e7-8d70d6d4dd43` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-03-E` |
| `ae29b32b-98a8-5977-b4e7-8d70d6d4dd43` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-03-E` |
| `fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f` | valuta (`EVALUATES`) | `asset-delta-core` |
| `fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-04` |
| `fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-04` |
| `fd9a4b0a-fba8-50a8-8593-3c2f9ff36b7f` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-04` |
| `0534ef1c-4ab5-586a-926e-8b24e75d2ee5` | valuta (`EVALUATES`) | `asset-delta-core` |
| `0534ef1c-4ab5-586a-926e-8b24e75d2ee5` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-01` |
| `0534ef1c-4ab5-586a-926e-8b24e75d2ee5` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-01` |
| `0534ef1c-4ab5-586a-926e-8b24e75d2ee5` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-01` |
| `c156bb48-3c77-5851-ac1f-b041c9fca5a3` | valuta (`EVALUATES`) | `asset-delta-core` |
| `c156bb48-3c77-5851-ac1f-b041c9fca5a3` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-03-E` |
| `c156bb48-3c77-5851-ac1f-b041c9fca5a3` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-03-E` |
| `c156bb48-3c77-5851-ac1f-b041c9fca5a3` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-03-E` |
| `1b28aa3c-866b-5ecd-b2de-c9c6a84a9357` | valuta (`EVALUATES`) | `asset-delta-core` |
| `1b28aa3c-866b-5ecd-b2de-c9c6a84a9357` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01` |
| `1b28aa3c-866b-5ecd-b2de-c9c6a84a9357` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01` |
| `1b28aa3c-866b-5ecd-b2de-c9c6a84a9357` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01` |
| `66286b28-a64b-5036-b99e-cfefdd09ec2c` | valuta (`EVALUATES`) | `asset-delta-core` |
| `66286b28-a64b-5036-b99e-cfefdd09ec2c` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01-E` |
| `66286b28-a64b-5036-b99e-cfefdd09ec2c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01-E` |
| `66286b28-a64b-5036-b99e-cfefdd09ec2c` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01-E` |
| `45e763f5-3989-5177-9bbb-8bc07e7c4dcb` | valuta (`EVALUATES`) | `asset-delta-core` |
| `45e763f5-3989-5177-9bbb-8bc07e7c4dcb` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-09` |
| `45e763f5-3989-5177-9bbb-8bc07e7c4dcb` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-09` |
| `45e763f5-3989-5177-9bbb-8bc07e7c4dcb` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-09` |
| `de2c79d8-fd43-5ebf-8d5a-5c8896101d29` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `de2c79d8-fd43-5ebf-8d5a-5c8896101d29` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-01` |
| `de2c79d8-fd43-5ebf-8d5a-5c8896101d29` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-01` |
| `de2c79d8-fd43-5ebf-8d5a-5c8896101d29` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-01` |
| `3e075956-8a97-59f9-9453-a96d35311a9d` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `3e075956-8a97-59f9-9453-a96d35311a9d` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-02` |
| `3e075956-8a97-59f9-9453-a96d35311a9d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-02` |
| `3e075956-8a97-59f9-9453-a96d35311a9d` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-02` |
| `dcaaa43d-fc5c-578a-864d-d64dcc363360` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `dcaaa43d-fc5c-578a-864d-d64dcc363360` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-03-E` |
| `dcaaa43d-fc5c-578a-864d-d64dcc363360` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-03-E` |
| `dcaaa43d-fc5c-578a-864d-d64dcc363360` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-03-E` |
| `21ef177c-0d23-5ae0-8cad-e0d3b809178f` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `21ef177c-0d23-5ae0-8cad-e0d3b809178f` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-04` |
| `21ef177c-0d23-5ae0-8cad-e0d3b809178f` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-04` |
| `21ef177c-0d23-5ae0-8cad-e0d3b809178f` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-04` |
| `a2eb9293-638a-54f0-9836-9a9ed675558d` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `a2eb9293-638a-54f0-9836-9a9ed675558d` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01` |
| `a2eb9293-638a-54f0-9836-9a9ed675558d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01` |
| `a2eb9293-638a-54f0-9836-9a9ed675558d` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01` |
| `02931dc5-a262-52ab-bf4a-19373c4f0050` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `02931dc5-a262-52ab-bf4a-19373c4f0050` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01-E` |
| `02931dc5-a262-52ab-bf4a-19373c4f0050` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01-E` |
| `02931dc5-a262-52ab-bf4a-19373c4f0050` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01-E` |
| `8cd984bf-5bdb-5675-b579-2eb4a5078bd4` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `8cd984bf-5bdb-5675-b579-2eb4a5078bd4` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08` |
| `8cd984bf-5bdb-5675-b579-2eb4a5078bd4` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08` |
| `8cd984bf-5bdb-5675-b579-2eb4a5078bd4` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08` |
| `71ac75bb-5a78-56d8-8796-138c3aff6fb1` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `71ac75bb-5a78-56d8-8796-138c3aff6fb1` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08-E` |
| `71ac75bb-5a78-56d8-8796-138c3aff6fb1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08-E` |
| `71ac75bb-5a78-56d8-8796-138c3aff6fb1` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08-E` |
| `9d2cbe7e-5702-558e-9d08-e6d5868283c1` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `9d2cbe7e-5702-558e-9d08-e6d5868283c1` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-01` |
| `9d2cbe7e-5702-558e-9d08-e6d5868283c1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-01` |
| `9d2cbe7e-5702-558e-9d08-e6d5868283c1` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-01` |
| `83f6d6b9-eeb9-500a-8a7c-3f135af47eed` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `83f6d6b9-eeb9-500a-8a7c-3f135af47eed` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-03` |
| `83f6d6b9-eeb9-500a-8a7c-3f135af47eed` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-03` |
| `83f6d6b9-eeb9-500a-8a7c-3f135af47eed` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-03` |
| `0003441d-fc06-5e81-848f-24b798b8a6a1` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `0003441d-fc06-5e81-848f-24b798b8a6a1` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-05` |
| `0003441d-fc06-5e81-848f-24b798b8a6a1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-05` |
| `0003441d-fc06-5e81-848f-24b798b8a6a1` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-05` |
| `947e7d7b-cf4d-5ca3-b2b6-95d01d698733` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `947e7d7b-cf4d-5ca3-b2b6-95d01d698733` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-06` |
| `947e7d7b-cf4d-5ca3-b2b6-95d01d698733` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-06` |
| `947e7d7b-cf4d-5ca3-b2b6-95d01d698733` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-06` |
| `810f76d0-8eb9-5119-acb9-7e7c52adce93` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `810f76d0-8eb9-5119-acb9-7e7c52adce93` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-01` |
| `810f76d0-8eb9-5119-acb9-7e7c52adce93` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-01` |
| `810f76d0-8eb9-5119-acb9-7e7c52adce93` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-01` |
| `e16edf55-f114-514a-b316-8421d19c5f56` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `e16edf55-f114-514a-b316-8421d19c5f56` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-02` |
| `e16edf55-f114-514a-b316-8421d19c5f56` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-02` |
| `e16edf55-f114-514a-b316-8421d19c5f56` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-02` |
| `742f0a86-41c5-5fb4-a7cf-eedded238636` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `742f0a86-41c5-5fb4-a7cf-eedded238636` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11` |
| `742f0a86-41c5-5fb4-a7cf-eedded238636` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11` |
| `742f0a86-41c5-5fb4-a7cf-eedded238636` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11` |
| `afbdda04-a07f-594e-860c-04fa2533c2ac` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `afbdda04-a07f-594e-860c-04fa2533c2ac` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11-E` |
| `afbdda04-a07f-594e-860c-04fa2533c2ac` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11-E` |
| `afbdda04-a07f-594e-860c-04fa2533c2ac` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11-E` |
| `10b56a51-33a8-553e-b7ed-2a440834bcec` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `10b56a51-33a8-553e-b7ed-2a440834bcec` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-01-E` |
| `10b56a51-33a8-553e-b7ed-2a440834bcec` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-01-E` |
| `10b56a51-33a8-553e-b7ed-2a440834bcec` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-01-E` |
| `a7882c14-37b9-5f2c-a01c-31a76aa326ff` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `a7882c14-37b9-5f2c-a01c-31a76aa326ff` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02` |
| `a7882c14-37b9-5f2c-a01c-31a76aa326ff` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02` |
| `a7882c14-37b9-5f2c-a01c-31a76aa326ff` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02` |
| `a65a4440-bd6f-592e-94e6-3198c2339d0f` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `a65a4440-bd6f-592e-94e6-3198c2339d0f` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02-E` |
| `a65a4440-bd6f-592e-94e6-3198c2339d0f` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02-E` |
| `a65a4440-bd6f-592e-94e6-3198c2339d0f` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02-E` |
| `6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-03-E` |
| `6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-03-E` |
| `6f8a9ad1-3bb0-5f4d-9abd-bccdd5d0716e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-03-E` |
| `700d7d03-0cc6-5630-82da-9c51576a8d59` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `700d7d03-0cc6-5630-82da-9c51576a8d59` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-04` |
| `700d7d03-0cc6-5630-82da-9c51576a8d59` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-04` |
| `700d7d03-0cc6-5630-82da-9c51576a8d59` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-04` |
| `78808e70-9f89-5283-b1c3-be1918e4807c` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `78808e70-9f89-5283-b1c3-be1918e4807c` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-01` |
| `78808e70-9f89-5283-b1c3-be1918e4807c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-01` |
| `78808e70-9f89-5283-b1c3-be1918e4807c` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-01` |
| `d9451c7d-8f53-513b-a4b7-e612444693f0` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `d9451c7d-8f53-513b-a4b7-e612444693f0` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-03-E` |
| `d9451c7d-8f53-513b-a4b7-e612444693f0` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-03-E` |
| `d9451c7d-8f53-513b-a4b7-e612444693f0` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-03-E` |
| `9b8a22f1-fafd-5bbd-87c9-c63519d2be46` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `9b8a22f1-fafd-5bbd-87c9-c63519d2be46` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01` |
| `9b8a22f1-fafd-5bbd-87c9-c63519d2be46` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01` |
| `9b8a22f1-fafd-5bbd-87c9-c63519d2be46` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01` |
| `92682466-8a38-5c94-9e5e-3087118fccbc` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `92682466-8a38-5c94-9e5e-3087118fccbc` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01-E` |
| `92682466-8a38-5c94-9e5e-3087118fccbc` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01-E` |
| `92682466-8a38-5c94-9e5e-3087118fccbc` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01-E` |
| `fec8881c-5784-5f1f-ac03-0beb3ef00ab0` | valuta (`EVALUATES`) | `asset-delta-aux` |
| `fec8881c-5784-5f1f-ac03-0beb3ef00ab0` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-09` |
| `fec8881c-5784-5f1f-ac03-0beb3ef00ab0` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-09` |
| `fec8881c-5784-5f1f-ac03-0beb3ef00ab0` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-09` |
