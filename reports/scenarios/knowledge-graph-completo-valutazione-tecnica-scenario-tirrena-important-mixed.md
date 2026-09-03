# Knowledge Graph completo — assessment `scenario-tirrena-important-mixed`

> Questa vista rappresenta lo stesso grafo Neo4j usato dalla pipeline per valutare il sottoinsieme tecnico ACN selezionato. Non rappresenta il catalogo completo delle misure ACN e non aggiunge dati, ipotesi o nuovi calcoli.

## Come leggere il grafo

- I nodi azzurri descrivono il contesto e gli asset osservati.
- I nodi verdi descrivono evidenze e provenienza delle informazioni.
- I nodi arancioni descrivono requisiti, controlli e regole di confronto.
- I nodi viola sono gli esiti prodotti e persistiti dopo la valutazione.

Il grafo contiene **182 nodi** e **267 relazioni**.

## Vista complessiva

```mermaid
flowchart TB
    classDef context fill:#e3f2fd,stroke:#1565c0,color:#0d47a1
    classDef evidence fill:#e0f2f1,stroke:#00796b,color:#004d40
    classDef logic fill:#fff3e0,stroke:#ef6c00,color:#5d4037
    classDef result fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c
    nodo1["Dataset<br/>Ambiente normalizzato - Logistica Tirrena"]
    class nodo1 context
    nodo2["Organizzazione<br/>Logistica Tirrena S.r.l."]
    class nodo2 context
    nodo3["Responsabili<br/>Responsabile Sistemi Informativi"]
    class nodo3 context
    nodo4["Processi<br/>Piattaforma logistica"]
    class nodo4 context
    nodo5["Categorie di dati<br/>Dati logistici e clienti sintetici"]
    class nodo5 context
    nodo6["Asset<br/>Logistics Application Server<br/>admin_remote_access_logging: True<br/>admin_remote_access_logging_observation_type: direct<br/>admin_remote_access_logging_observed_at: 2026-08-14T07:00:00Z<br/>admin_remote_access_logging_status: known<br/>anomaly_thresholds_configured: False<br/>anomaly_thresholds_configured_observation_type: direct<br/>anomaly_thresholds_configured_observed_at: 2026-08-14T07:00:00Z<br/>anomaly_thresholds_configured_status: known<br/>critical_software_supplier_channels_monitored: False<br/>critical_software_supplier_channels_monitored_observation_type: direct<br/>critical_software_supplier_channels_monitored_observed_at: 2026-08-14T05:00:00Z<br/>critical_software_supplier_channels_monitored_status: known<br/>exposure_level: high<br/>extended_vulnerability_assessment_performed: False<br/>extended_vulnerability_assessment_performed_observation_type: direct<br/>extended_vulnerability_assessment_performed_observed_at: 2026-08-14T05:00:00Z<br/>extended_vulnerability_assessment_performed_status: known<br/>firewall_enabled: True<br/>firewall_enabled_observation_type: direct<br/>firewall_enabled_observed_at: 2026-08-14T07:00:00Z<br/>firewall_enabled_status: known<br/>hardening_baseline_applied: False<br/>hardening_baseline_applied_observation_type: direct<br/>hardening_baseline_applied_observed_at: 2026-08-14T07:00:00Z<br/>hardening_baseline_applied_status: known<br/>hardware_inventory_complete: True<br/>hardware_inventory_complete_observation_type: evidence_based<br/>hardware_inventory_complete_observed_at: 2026-08-14T06:00:00Z<br/>hardware_inventory_complete_status: known<br/>impact_level: critical<br/>internet_exposed_observation_type: evidence_based<br/>internet_exposed_observed_at: 2026-08-14T06:00:00Z<br/>log_retention_within_plan: True<br/>log_retention_within_plan_observation_type: declared<br/>log_retention_within_plan_observed_at: 2026-08-10T09:00:00Z<br/>log_retention_within_plan_status: known<br/>logs_centralized: False<br/>logs_centralized_observation_type: direct<br/>logs_centralized_observed_at: 2026-08-14T07:00:00Z<br/>logs_centralized_status: known<br/>logs_protected: True<br/>logs_protected_observation_type: direct<br/>logs_protected_observed_at: 2026-08-14T07:00:00Z<br/>logs_protected_status: known<br/>maintenance_logged: False<br/>maintenance_logged_observation_type: direct<br/>maintenance_logged_observed_at: 2026-08-14T07:00:00Z<br/>maintenance_logged_status: known<br/>network_segment_observation_type: evidence_based<br/>network_segment_observed_at: 2026-08-14T06:00:00Z<br/>nis_relevant: True<br/>nis_relevant_observation_type: declared<br/>nis_relevant_observed_at: 2026-08-10T09:00:00Z<br/>nis_relevant_status: known<br/>operating_system: ExampleLinux<br/>operating_system_version: 11.9<br/>physical_protection_documented: True<br/>physical_protection_documented_observation_type: declared<br/>physical_protection_documented_observed_at: 2026-08-10T09:00:00Z<br/>physical_protection_documented_status: known<br/>provider_services_inventory_complete: False<br/>provider_services_inventory_complete_observation_type: declared<br/>provider_services_inventory_complete_observed_at: 2026-08-10T09:00:00Z<br/>provider_services_inventory_complete_status: known<br/>remote_access_protected: True<br/>remote_access_protected_observation_type: direct<br/>remote_access_protected_observed_at: 2026-08-14T07:00:00Z<br/>remote_access_protected_status: known<br/>remote_access_registry_complete: True<br/>remote_access_registry_complete_observation_type: declared<br/>remote_access_registry_complete_observed_at: 2026-08-10T09:00:00Z<br/>remote_access_registry_complete_status: known<br/>risk_assessment_reference: RISK-TIRRENA-2026-05<br/>secure_disposal_documented: False<br/>secure_disposal_documented_observation_type: declared<br/>secure_disposal_documented_observed_at: 2026-08-10T09:00:00Z<br/>secure_disposal_documented_status: known<br/>support_status: supported<br/>vulnerability_advisories_monitored: False<br/>vulnerability_advisories_monitored_observation_type: direct<br/>vulnerability_advisories_monitored_observed_at: 2026-08-14T05:00:00Z<br/>vulnerability_advisories_monitored_status: known"]
    class nodo6 context
    nodo7["Asset<br/>Sistema ausiliario fuori perimetro NIS<br/>exposure_level: low<br/>impact_level: medium<br/>internet_exposed_observation_type: evidence_based<br/>internet_exposed_observed_at: 2026-08-14T06:00:00Z<br/>network_segment_observation_type: evidence_based<br/>network_segment_observed_at: 2026-08-14T06:00:00Z<br/>nis_relevant: False<br/>nis_relevant_observation_type: declared<br/>nis_relevant_observed_at: 2026-08-10T09:00:00Z<br/>nis_relevant_status: known<br/>properties_json: {}<br/>risk_assessment_reference: RISK-TIRRENA-2026-05<br/>support_status: supported"]
    class nodo7 context
    nodo8["Servizi<br/>HTTPS"]
    class nodo8 context
    nodo9["Componenti software<br/>TirrenaPortal"]
    class nodo9 context
    nodo10["Utenze<br/>account-tirrena-admin"]
    class nodo10 context
    nodo11["Flussi di rete<br/>flow-tirrena-https"]
    class nodo11 context
    nodo12["Backup<br/>backup-tirrena-core"]
    class nodo12 context
    nodo13["Capacità di sicurezza<br/>cap-tirrena-emergency"]
    class nodo13 context
    nodo14["Capacità di sicurezza<br/>cap-tirrena-ids"]
    class nodo14 context
    nodo15["Capacità di sicurezza<br/>cap-tirrena-filter"]
    class nodo15 context
    nodo16["Capacità di sicurezza<br/>cap-tirrena-access-monitor"]
    class nodo16 context
    nodo17["Capacità di sicurezza<br/>cap-tirrena-endpoint"]
    class nodo17 context
    nodo18["Vulnerabilità<br/>Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione"]
    class nodo18 context
    nodo19["Evidenze<br/>Inventario asset<br/>evidence_type: asset_inventory<br/>source: CMDB<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo19 evidence
    nodo20["Evidenze<br/>Inventario software<br/>evidence_type: software_inventory<br/>source: CMDB<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo20 evidence
    nodo21["Evidenze<br/>Inventario flussi di rete<br/>evidence_type: network_flow_inventory<br/>source: network-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo21 evidence
    nodo22["Evidenze<br/>Inventario servizi fornitori<br/>evidence_type: provider_service_inventory<br/>source: service-catalog<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: medium<br/>content_json: {}"]
    class nodo22 evidence
    nodo23["Evidenze<br/>Scansione vulnerabilità<br/>evidence_type: vulnerability_scan<br/>source: vulnerability-scanner<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'activity_description': 'Vulnerability assessment autenticato.', 'cve': 'CVE-2021-41773', 'impact_…"]
    class nodo23 evidence
    nodo24["Evidenze<br/>Registro trattamento vulnerabilità<br/>evidence_type: vulnerability_treatment<br/>source: vulnerability-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo24 evidence
    nodo25["Evidenze<br/>Monitoraggio advisory vulnerabilità<br/>evidence_type: vulnerability_management<br/>source: vulnerability-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo25 evidence
    nodo26["Evidenze<br/>Revisione identità e accessi<br/>evidence_type: access_review<br/>source: IAM<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo26 evidence
    nodo27["Evidenze<br/>Configurazione MFA e privilegi<br/>evidence_type: access_configuration<br/>source: IAM<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo27 evidence
    nodo28["Evidenze<br/>Evidenza protezione fisica<br/>evidence_type: physical_security<br/>source: facilities<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: medium<br/>content_json: {}"]
    class nodo28 evidence
    nodo29["Evidenze<br/>Configurazione cifratura<br/>evidence_type: encryption_configuration<br/>source: configuration-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'baseline_id': 'CRYPTO-BASELINE-2026.1'}"]
    class nodo29 evidence
    nodo30["Evidenze<br/>Registro backup<br/>evidence_type: backup_record<br/>source: backup-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'plan_reference': 'BACKUP-TIRRENA-2026'}"]
    class nodo30 evidence
    nodo31["Evidenze<br/>Test di ripristino<br/>evidence_type: restore_test<br/>source: backup-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo31 evidence
    nodo32["Evidenze<br/>Configurazione e hardening<br/>evidence_type: system_configuration<br/>source: configuration-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo32 evidence
    nodo33["Evidenze<br/>Registro patching<br/>evidence_type: patch_record<br/>source: patch-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo33 evidence
    nodo34["Evidenze<br/>Registro manutenzione<br/>evidence_type: maintenance_record<br/>source: configuration-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo34 evidence
    nodo35["Evidenze<br/>Configurazione logging<br/>evidence_type: log_configuration<br/>source: logging-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo35 evidence
    nodo36["Evidenze<br/>Configurazione accessi remoti e firewall<br/>evidence_type: network_security<br/>source: network-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo36 evidence
    nodo37["Evidenze<br/>Comunicazioni di emergenza<br/>evidence_type: emergency_communications<br/>source: crisis-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo37 evidence
    nodo38["Evidenze<br/>Configurazione monitoraggio<br/>evidence_type: monitoring_configuration<br/>source: monitoring-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo38 evidence
    nodo39["Evidenze<br/>Protezione endpoint<br/>evidence_type: endpoint_protection<br/>source: endpoint-platform<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo39 evidence
    nodo40["Fonti e provenienza<br/>prov-inventory<br/>source: CMDB<br/>method: export autenticato<br/>collected_at: 2026-08-14T06:00:00Z<br/>reliability: high"]
    class nodo40 evidence
    nodo41["Fonti e provenienza<br/>prov-config<br/>source: configuration-manager<br/>method: raccolta automatizzata<br/>collected_at: 2026-08-14T07:00:00Z<br/>reliability: high"]
    class nodo41 evidence
    nodo42["Fonti e provenienza<br/>prov-governance<br/>source: registro governance<br/>method: dichiarazione approvata<br/>collected_at: 2026-08-10T09:00:00Z<br/>reliability: medium"]
    class nodo42 evidence
    nodo43["Fonti e provenienza<br/>prov-scan<br/>source: vulnerability-scanner<br/>method: scansione autenticata<br/>collected_at: 2026-08-14T05:00:00Z<br/>reliability: high"]
    class nodo43 evidence
    nodo44["Fonti e provenienza<br/>prov-patch<br/>source: patch-manager<br/>method: export stato<br/>collected_at: 2026-08-14T07:30:00Z<br/>reliability: high"]
    class nodo44 evidence
    nodo45["Fonti e provenienza<br/>prov-access<br/>source: IAM<br/>method: export utenze<br/>collected_at: 2026-08-14T07:45:00Z<br/>reliability: high"]
    class nodo45 evidence
    nodo46["Fonti e provenienza<br/>prov-network<br/>source: network-manager<br/>method: export configurazione<br/>collected_at: 2026-08-14T06:30:00Z<br/>reliability: high"]
    class nodo46 evidence
    nodo47["Fonti e provenienza<br/>prov-backup<br/>source: backup-manager<br/>method: export job e test<br/>collected_at: 2026-08-14T03:30:00Z<br/>reliability: high"]
    class nodo47 evidence
    nodo48["Requisiti<br/>Inventario hardware<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-01 punto 1"]
    class nodo48 logic
    nodo49["Requisiti<br/>Inventario software e servizi<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-02 punto 1"]
    class nodo49 logic
    nodo50["Requisiti<br/>Inventario dei flussi di rete<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-03 punto 1"]
    class nodo50 logic
    nodo51["Requisiti<br/>Servizi dei fornitori<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.AM-04 punto 1"]
    class nodo51 logic
    nodo52["Requisiti<br/>Identificazione delle vulnerabilità<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-01 punto 1"]
    class nodo52 logic
    nodo53["Requisiti<br/>Approfondimenti di vulnerability assessment<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-01 punti 2 e 3"]
    class nodo53 logic
    nodo54["Requisiti<br/>Trattamento delle vulnerabilità<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-08 punti 1 e 2"]
    class nodo54 logic
    nodo55["Requisiti<br/>Canali dei fornitori del software critico<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN ID.RA-08 punto 5"]
    class nodo55 logic
    nodo56["Requisiti<br/>Identità e credenziali<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-01 punti 1, 2 e 3"]
    class nodo56 logic
    nodo57["Requisiti<br/>Autenticazione e MFA<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-03 punti 1 e 2"]
    class nodo57 logic
    nodo58["Requisiti<br/>Minimo privilegio e utenze amministrative<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-05 punti 1 e 2"]
    class nodo58 logic
    nodo59["Requisiti<br/>Protezione fisica<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AA-06 punto 1"]
    class nodo59 logic
    nodo60["Requisiti<br/>Cifratura dei supporti rimovibili<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-01 punto 1"]
    class nodo60 logic
    nodo61["Requisiti<br/>Protezione dei dati in transito<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-02 punto 1"]
    class nodo61 logic
    nodo62["Requisiti<br/>Backup periodici e copie offline<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-11 punto 1"]
    class nodo62 logic
    nodo63["Requisiti<br/>Protezione e test dei backup<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.DS-11 punti 3 e 4"]
    class nodo63 logic
    nodo64["Requisiti<br/>Hardening<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-01 punto 1"]
    class nodo64 logic
    nodo65["Requisiti<br/>Software supportato e aggiornato<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-02 punti 1 e 2"]
    class nodo65 logic
    nodo66["Requisiti<br/>Test degli aggiornamenti critici<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-02 punto 4"]
    class nodo66 logic
    nodo67["Requisiti<br/>Manutenzione e dismissione sicura<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-03 punti 1 e 2"]
    class nodo67 logic
    nodo68["Requisiti<br/>Logging di sicurezza<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.PS-04 punti 1, 2 e 3"]
    class nodo68 logic
    nodo69["Requisiti<br/>Accesso remoto e firewall<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.IR-01 punti 1, 2 e 3"]
    class nodo69 logic
    nodo70["Requisiti<br/>Comunicazioni di emergenza protette<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.IR-03 punto 1"]
    class nodo70 logic
    nodo71["Requisiti<br/>Strumenti per il rilevamento degli incidenti<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN DE.CM-01 punto 1"]
    class nodo71 logic
    nodo72["Requisiti<br/>Monitoraggio avanzato<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN DE.CM-01 punto 6"]
    class nodo72 logic
    nodo73["Requisiti<br/>Protezione endpoint<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN DE.CM-09 punto 1"]
    class nodo73 logic
    nodo74["Requisiti<br/>Politiche di sicurezza<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN GV.PO-01 punti 1, 2 e 3"]
    class nodo74 logic
    nodo75["Requisiti<br/>Formazione e sensibilizzazione<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN PR.AT-01 punti 1, 2 e 3"]
    class nodo75 logic
    nodo76["Requisiti<br/>Gestione contrattuale della supply chain<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN GV.SC-01 punto 1 (punto 2 per il solo profilo essenziale)"]
    class nodo76 logic
    nodo77["Requisiti<br/>Piano di risposta agli incidenti<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN RS.MA-01 punti 1, 2 e 3"]
    class nodo77 logic
    nodo78["Requisiti<br/>Continuità operativa e crisi<br/>source_reference: D.Lgs. 138/2024 art. 24; ACN RC.RP-01 punto 1"]
    class nodo78 logic
    nodo79["Controlli tecnici<br/>Inventario hardware<br/>technical_area: asset_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo79 logic
    nodo80["Controlli tecnici<br/>Inventario software e servizi<br/>technical_area: asset_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo80 logic
    nodo81["Controlli tecnici<br/>Inventario dei flussi di rete<br/>technical_area: asset_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo81 logic
    nodo82["Controlli tecnici<br/>Servizi dei fornitori<br/>technical_area: supply_chain_technical<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['important', 'essential']"]
    class nodo82 logic
    nodo83["Controlli tecnici<br/>Valutazione delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo83 logic
    nodo84["Controlli tecnici<br/>Assessment approfondito delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo84 logic
    nodo85["Controlli tecnici<br/>Trattamento delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo85 logic
    nodo86["Controlli tecnici<br/>Monitoraggio avanzato delle vulnerabilità<br/>technical_area: vulnerability_management<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo86 logic
    nodo87["Controlli tecnici<br/>Identità e credenziali<br/>technical_area: access_control<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo87 logic
    nodo88["Controlli tecnici<br/>Autenticazione e MFA<br/>technical_area: access_control<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo88 logic
    nodo89["Controlli tecnici<br/>Minimo privilegio e account amministrativi<br/>technical_area: access_control<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo89 logic
    nodo90["Controlli tecnici<br/>Protezione fisica<br/>technical_area: physical_security<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['important', 'essential']"]
    class nodo90 logic
    nodo91["Controlli tecnici<br/>Protezione dei dati a riposo<br/>technical_area: data_protection<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo91 logic
    nodo92["Controlli tecnici<br/>Protezione dei dati in transito<br/>technical_area: cryptography<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo92 logic
    nodo93["Controlli tecnici<br/>Backup e ripristino<br/>technical_area: backup_recovery<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo93 logic
    nodo94["Controlli tecnici<br/>Separazione delle copie di backup<br/>technical_area: backup_recovery<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo94 logic
    nodo95["Controlli tecnici<br/>Baseline di hardening<br/>technical_area: system_security<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo95 logic
    nodo96["Controlli tecnici<br/>Software supportato e aggiornato<br/>technical_area: patch_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo96 logic
    nodo97["Controlli tecnici<br/>Test degli aggiornamenti critici<br/>technical_area: patch_management<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo97 logic
    nodo98["Controlli tecnici<br/>Manutenzione e dismissione sicura<br/>technical_area: system_security<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo98 logic
    nodo99["Controlli tecnici<br/>Logging di sicurezza<br/>technical_area: logging_monitoring<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo99 logic
    nodo100["Controlli tecnici<br/>Accesso remoto e firewall<br/>technical_area: network_security<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo100 logic
    nodo101["Controlli tecnici<br/>Comunicazioni di emergenza protette<br/>technical_area: emergency_communications<br/>verification_mode: evidence_assisted<br/>applicable_profiles: ['essential']"]
    class nodo101 logic
    nodo102["Controlli tecnici<br/>Monitoraggio di rete e accessi<br/>technical_area: security_monitoring<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo102 logic
    nodo103["Controlli tecnici<br/>Monitoraggio avanzato<br/>technical_area: security_monitoring<br/>verification_mode: direct_technical<br/>applicable_profiles: ['essential']"]
    class nodo103 logic
    nodo104["Controlli tecnici<br/>Protezione endpoint<br/>technical_area: endpoint_security<br/>verification_mode: direct_technical<br/>applicable_profiles: ['important', 'essential']"]
    class nodo104 logic
    nodo105["Regole di valutazione<br/>Completezza inventario hardware<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['hardware_inventory_complete']}<br/>verification_mode: direct_technical<br/>risk_clause: Completezza e granularità sono quelle definite dal perimetro di rischio."]
    class nodo105 logic
    nodo106["Regole di valutazione<br/>Inventario software e servizi<br/>evaluator: collection_inventory<br/>parameters_json: {'entity_type': 'SoftwareComponent', 'fields': ['name', 'version', 'authorized']}<br/>verification_mode: direct_technical<br/>risk_clause: Il livello di dettaglio dipende dal rischio e dall'architettura."]
    class nodo106 logic
    nodo107["Regole di valutazione<br/>Inventario e autorizzazione dei flussi<br/>evaluator: collection_inventory<br/>parameters_json: {'entity_type': 'NetworkFlow', 'fields': ['source', 'destination', 'transport_protocol', 'applicati…<br/>verification_mode: direct_technical<br/>risk_clause: Il perimetro dei flussi deriva dalla valutazione del rischio."]
    class nodo107 logic
    nodo108["Regole di valutazione<br/>Inventario tecnico dei servizi forniti da terzi<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['provider_services_inventory_complete']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Sono incluse le dipendenze pertinenti al rischio del sistema."]
    class nodo108 logic
    nodo109["Regole di valutazione<br/>Identificazione delle vulnerabilità da fonti monitorate<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['vulnerability_advisories_monitored']}<br/>verification_mode: direct_technical<br/>risk_clause: Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate."]
    class nodo109 logic
    nodo110["Regole di valutazione<br/>Vulnerability assessment approfondito<br/>evaluator: vulnerability_assessment<br/>parameters_json: {'properties': ['extended_vulnerability_assessment_performed']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte."]
    class nodo110 logic
    nodo111["Regole di valutazione<br/>Trattamento delle vulnerabilità rilevate<br/>evaluator: vulnerability_treatment<br/>parameters_json: {}<br/>verification_mode: direct_technical<br/>risk_clause: Priorità e termini sono quelli documentati nella valutazione del rischio."]
    class nodo111 logic
    nodo112["Regole di valutazione<br/>Monitoraggio dei canali dei fornitori critici<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['critical_software_supplier_channels_monitored']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Il software critico è individuato dall'inventario e dalla valutazione del rischio."]
    class nodo112 logic
    nodo113["Regole di valutazione<br/>Inventario e gestione delle utenze<br/>evaluator: collection_inventory<br/>parameters_json: {'entity_type': 'Account', 'fields': ['account_type', 'individual', 'authorized', 'credentials_mana…<br/>verification_mode: direct_technical<br/>risk_clause: Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio."]
    class nodo113 logic
    nodo114["Regole di valutazione<br/>MFA per accessi pertinenti al rischio<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'Account', 'properties': ['mfa_enabled'], 'selectors_any': {'privileged': true, 're…<br/>verification_mode: direct_technical<br/>risk_clause: L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi."]
    class nodo114 logic
    nodo115["Regole di valutazione<br/>Minimo privilegio e separazione amministrativa<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'Account', 'properties': ['least_privilege', 'separate_admin_account'], 'selectors_…<br/>verification_mode: direct_technical<br/>risk_clause: I privilegi ammessi dipendono dalle funzioni autorizzate."]
    class nodo115 logic
    nodo116["Regole di valutazione<br/>Protezione fisica documentabile<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['physical_protection_documented']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Le misure fisiche dipendono da ubicazione minacce e impatto."]
    class nodo116 logic
    nodo117["Regole di valutazione<br/>Cifratura dei supporti rimovibili<br/>evaluator: data_object_protection<br/>parameters_json: {'properties': []}<br/>verification_mode: direct_technical<br/>risk_clause: Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori peri…"]
    class nodo117 logic
    nodo118["Regole di valutazione<br/>Cifratura delle comunicazioni<br/>evaluator: cryptographic_configuration<br/>parameters_json: {'threshold_ref': 'tls_minimum'}<br/>verification_mode: direct_technical<br/>risk_clause: Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente d…"]
    class nodo118 logic
    nodo119["Regole di valutazione<br/>Backup conforme al piano e copie offline<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'BackupRecord', 'properties': ['frequency_within_plan', 'offline_copy']}<br/>verification_mode: direct_technical<br/>risk_clause: La frequenza proviene dai piani di continuità e ripristino dichiarati."]
    class nodo119 logic
    nodo120["Regole di valutazione<br/>Protezione e test di ripristino per il profilo essenziale<br/>evaluator: collection_booleans<br/>parameters_json: {'entity_type': 'BackupRecord', 'properties': ['protected_copy', 'restore_test_successful']}<br/>verification_mode: direct_technical<br/>risk_clause: Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione."]
    class nodo120 logic
    nodo121["Regole di valutazione<br/>Baseline di hardening applicata<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['hardening_baseline_applied']}<br/>verification_mode: direct_technical<br/>risk_clause: La baseline è scelta in funzione della tecnologia e dello stato dell'arte."]
    class nodo121 logic
    nodo122["Regole di valutazione<br/>Software supportato e aggiornamenti entro il piano di rischio<br/>evaluator: supported_and_updated_software<br/>parameters_json: {'critical_patch_test_required': false}<br/>verification_mode: direct_technical<br/>risk_clause: Le scadenze di patching provengono dal piano di rischio dichiarato."]
    class nodo122 logic
    nodo123["Regole di valutazione<br/>Test delle patch critiche<br/>evaluator: supported_and_updated_software<br/>parameters_json: {'critical_patch_test_required': true}<br/>verification_mode: direct_technical<br/>risk_clause: Modalità e ambiente di test sono commisurati a rischio e compatibilità."]
    class nodo123 logic
    nodo124["Regole di valutazione<br/>Manutenzione e dismissione tracciate<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['maintenance_logged', 'secure_disposal_documented']}<br/>verification_mode: evidence_assisted<br/>risk_clause: Le tecniche dipendono da supporto dati e rischio residuo."]
    class nodo124 logic
    nodo125["Regole di valutazione<br/>Logging di accessi amministrativi e remoti<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['admin_remote_access_logging', 'logs_protected', 'logs_centralized', 'log_retention…<br/>verification_mode: direct_technical<br/>risk_clause: Eventi e durata di conservazione provengono dal piano di logging e dal rischio."]
    class nodo125 logic
    nodo126["Regole di valutazione<br/>Accesso remoto governato e firewall attivo<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['remote_access_registry_complete', 'remote_access_protected', 'firewall_enabled']}<br/>verification_mode: direct_technical<br/>risk_clause: Regole e canali sono commisurati a esposizione e rischio."]
    class nodo126 logic
    nodo127["Regole di valutazione<br/>Capacità protetta per comunicazioni di emergenza<br/>evaluator: collection_booleans<br/>parameters_json: {'capability_types': ['emergency_communications'], 'entity_type': 'SecurityCapability', 'properties…<br/>verification_mode: evidence_assisted<br/>risk_clause: Canali e protezioni dipendono dagli scenari di crisi."]
    class nodo127 logic
    nodo128["Regole di valutazione<br/>Rilevamento degli incidenti di rete<br/>evaluator: collection_booleans<br/>parameters_json: {'capability_types': ['intrusion_detection'], 'entity_type': 'SecurityCapability', 'properties': ['…<br/>verification_mode: direct_technical<br/>risk_clause: La copertura della capacità di rilevamento è basata su architettura e rischio."]
    class nodo128 logic
    nodo129["Regole di valutazione<br/>Soglie e anomalie calibrate<br/>evaluator: asset_properties<br/>parameters_json: {'properties': ['anomaly_thresholds_configured']}<br/>verification_mode: direct_technical<br/>risk_clause: Le soglie sono calibrate sul comportamento atteso e non sono universali."]
    class nodo129 logic
    nodo130["Regole di valutazione<br/>Protezione endpoint attiva e monitorata<br/>evaluator: collection_booleans<br/>parameters_json: {'capability_types': ['endpoint_protection'], 'entity_type': 'SecurityCapability', 'properties': ['…<br/>verification_mode: direct_technical<br/>risk_clause: La capacità è selezionata in base al tipo di endpoint e al rischio."]
    class nodo130 logic
    nodo131["Esiti della valutazione<br/>a44647f2-4f8e-56ef-8682-31e0ad08e8e8<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo131 result
    nodo132["Esiti della valutazione<br/>55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'identificato', 'comparison_result': true, 'condition_origin': 'regulatory', 'manda…"]
    class nodo132 result
    nodo133["Esiti della valutazione<br/>be815e68-0a0f-581e-9f74-364b6a8847ad<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo133 result
    nodo134["Esiti della valutazione<br/>a70a78ab-5a03-5642-a8c5-a57866f5821c<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo134 result
    nodo135["Esiti della valutazione<br/>2d9abb01-0ddf-5142-b5ab-7cb86875b224<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo135 result
    nodo136["Esiti della valutazione<br/>f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo136 result
    nodo137["Esiti della valutazione<br/>eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo137 result
    nodo138["Esiti della valutazione<br/>205a77ed-ada0-5e9c-8557-d4ea0017b903<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo138 result
    nodo139["Esiti della valutazione<br/>fa454414-a9e2-535c-9497-9ac4415bc59c<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'presente', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory…"]
    class nodo139 result
    nodo140["Esiti della valutazione<br/>8e46657c-f989-5b2c-b588-26c8c32d158f<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': false, 'condition_origin': 'regulatory', 'mandatory': …"]
    class nodo140 result
    nodo141["Esiti della valutazione<br/>2b1955d6-62a0-517e-97c4-f990424bb297<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo141 result
    nodo142["Esiti della valutazione<br/>559b88af-ecc6-5668-aa4f-d19a04fe3485<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo142 result
    nodo143["Esiti della valutazione<br/>7ba70886-b3b0-58d8-a187-ef463799b3f3<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: completezza dell'inventario DataObject non nota<br/>confidence_level: insufficient"]
    class nodo143 result
    nodo144["Esiti della valutazione<br/>00bf1516-3e72-53ac-8911-d7382db61447<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo144 result
    nodo145["Esiti della valutazione<br/>8a0156bc-de29-5ad4-bf70-42f3514870c5<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo145 result
    nodo146["Esiti della valutazione<br/>731cc9c5-9524-5890-a2b1-566fea73fa0e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo146 result
    nodo147["Esiti della valutazione<br/>eda26dfc-17ea-5e61-a4bb-154399162614<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo147 result
    nodo148["Esiti della valutazione<br/>07719946-df9e-5c56-8839-4d2b76b06b4d<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': '{supported}', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandat…"]
    class nodo148 result
    nodo149["Esiti della valutazione<br/>df584b2a-0168-53e1-a18e-da04a2b8d48d<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo149 result
    nodo150["Esiti della valutazione<br/>fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo150 result
    nodo151["Esiti della valutazione<br/>1acfe9c1-4f51-506f-af58-a0f757a2d0bf<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo151 result
    nodo152["Esiti della valutazione<br/>b59021f7-343c-5906-9d16-e0a8099d5d59<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo152 result
    nodo153["Esiti della valutazione<br/>5226b494-6d6b-582d-a360-466cccf3a174<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo153 result
    nodo154["Esiti della valutazione<br/>e8204856-2ac4-5c65-a7ab-5b045b912409<br/>technical_status: non_compliant<br/>governance_status: none<br/>reason: È stato osservato uno scostamento tecnico rispetto alla regola.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo154 result
    nodo155["Esiti della valutazione<br/>2d2f7129-a328-5048-9016-cea40115bbcd<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo155 result
    nodo156["Esiti della valutazione<br/>89844673-034b-52ef-8f77-151499e8a739<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo156 result
    nodo157["Esiti della valutazione<br/>dfd29122-ac86-5531-b455-0e6b077e9806<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo157 result
    nodo158["Esiti della valutazione<br/>b56bb304-afd8-5a42-a1d4-c3ce0746b3e8<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo158 result
    nodo159["Esiti della valutazione<br/>444cd16d-e3d2-5e06-a084-63404a068fd1<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo159 result
    nodo160["Esiti della valutazione<br/>2846f635-2869-574e-a89b-b819634d4033<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo160 result
    nodo161["Esiti della valutazione<br/>c82878c6-83b2-51c1-97d1-452736ce5f5e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo161 result
    nodo162["Esiti della valutazione<br/>775cb338-4ecd-57b7-8b28-0a3747e96dff<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo162 result
    nodo163["Esiti della valutazione<br/>7215db4f-2cc1-5729-b6ee-304925724a8f<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo163 result
    nodo164["Esiti della valutazione<br/>0f4c28ea-e292-573b-93e4-c8f0207cebf8<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo164 result
    nodo165["Esiti della valutazione<br/>c0f62629-f4d2-59fb-abcd-b206a2513520<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo165 result
    nodo166["Esiti della valutazione<br/>1aa8b496-67e8-5900-b5bf-188efb671504<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo166 result
    nodo167["Esiti della valutazione<br/>65c49e4d-e897-54d0-9231-394c3f2f9fb8<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo167 result
    nodo168["Esiti della valutazione<br/>43b5335f-0ff6-52cb-ba27-4d4f63637fb2<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo168 result
    nodo169["Esiti della valutazione<br/>cc2b6b47-b917-5a5f-b2a2-826611be3f99<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo169 result
    nodo170["Esiti della valutazione<br/>a841b157-eb08-5805-8877-eb9dc5075e55<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo170 result
    nodo171["Esiti della valutazione<br/>9dadd369-6053-5ef2-9ee0-e3b2417f08d1<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo171 result
    nodo172["Esiti della valutazione<br/>2bea3c87-21c8-5ca1-b452-245417ddf30b<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo172 result
    nodo173["Esiti della valutazione<br/>7ef5d4b1-d7b8-5614-867f-766a93d42e13<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo173 result
    nodo174["Esiti della valutazione<br/>199820e3-4364-5646-9ae7-2a5a33dcd44a<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo174 result
    nodo175["Esiti della valutazione<br/>1a2603fe-fd55-5cdb-b205-b377ebe541da<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo175 result
    nodo176["Esiti della valutazione<br/>8be78386-a273-5b24-81ea-93ec9e49b14b<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo176 result
    nodo177["Esiti della valutazione<br/>8f942f3d-9a51-589c-bd85-2ff86478a85f<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo177 result
    nodo178["Esiti della valutazione<br/>472471bf-6a43-5150-a52b-0932e01f9507<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo178 result
    nodo179["Esiti della valutazione<br/>c06f3fa7-decb-5b9c-a7b1-97ca87007e60<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo179 result
    nodo180["Esiti della valutazione<br/>4225fae1-3054-5829-9cfa-cb3ab5fe8233<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo180 result
    nodo181["Esiti della valutazione<br/>ac6b7338-3a9f-5363-aedc-b55a5ffb64a8<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: regola esclusa dal profilo ACN important<br/>confidence_level: insufficient"]
    class nodo181 result
    nodo182["Esiti della valutazione<br/>2f4db68d-32de-5697-955a-ac141a53e05e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo182 result
    nodo6 -->|"espone"| nodo8
    nodo6 -->|"tratta"| nodo5
    nodo6 -->|"è gestito da"| nodo3
    nodo18 -->|"interessa"| nodo6
    nodo6 -->|"è protetto da"| nodo17
    nodo4 -->|"dipende da"| nodo6
    nodo1 -->|"descrive"| nodo2
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
    nodo128 -->|"implementa"| nodo102
    nodo128 -->|"deriva da"| nodo71
    nodo129 -->|"implementa"| nodo103
    nodo129 -->|"deriva da"| nodo72
    nodo130 -->|"implementa"| nodo104
    nodo130 -->|"deriva da"| nodo73
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
    nodo154 -->|"valuta"| nodo6
    nodo154 -->|"è esito del controllo"| nodo102
    nodo154 -->|"è riconducibile al requisito"| nodo71
    nodo154 -->|"applica la regola"| nodo128
    nodo155 -->|"valuta"| nodo6
    nodo155 -->|"è esito del controllo"| nodo103
    nodo155 -->|"è riconducibile al requisito"| nodo72
    nodo155 -->|"applica la regola"| nodo129
    nodo156 -->|"valuta"| nodo6
    nodo156 -->|"è esito del controllo"| nodo104
    nodo156 -->|"è riconducibile al requisito"| nodo73
    nodo156 -->|"applica la regola"| nodo130
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
    nodo180 -->|"valuta"| nodo7
    nodo180 -->|"è esito del controllo"| nodo102
    nodo180 -->|"è riconducibile al requisito"| nodo71
    nodo180 -->|"applica la regola"| nodo128
    nodo181 -->|"valuta"| nodo7
    nodo181 -->|"è esito del controllo"| nodo103
    nodo181 -->|"è riconducibile al requisito"| nodo72
    nodo181 -->|"applica la regola"| nodo129
    nodo182 -->|"valuta"| nodo7
    nodo182 -->|"è esito del controllo"| nodo104
    nodo182 -->|"è riconducibile al requisito"| nodo73
    nodo182 -->|"applica la regola"| nodo130
```

## Inventario completo dei nodi e delle proprietà

Ogni riga seguente riporta una proprietà già presente in Neo4j. I valori sconosciuti restano esplicitamente indicati come tali.

| Tipo | Nodo | Proprietà | Valore |
|---|---|---|---|
| Dataset | Ambiente normalizzato - Logistica Tirrena (`dataset-tirrena-normalized-2026`) | `description` | Output sintetico dei Moduli 1 e 2 per un'organizzazione importante con controlli tecnici eterogenei: alcune misure mature, altre incomplete o non conformi. Organizzazione, persone e prodotti sono inventati; i riferimenti CVE sono reali e associati a dipendenze sintetiche esclusivamente a scopo dimostrativo. |
| Dataset | Ambiente normalizzato - Logistica Tirrena (`dataset-tirrena-normalized-2026`) | `generated_at` | 2026-08-15T11:37:00+02:00 |
| Dataset | Ambiente normalizzato - Logistica Tirrena (`dataset-tirrena-normalized-2026`) | `id` | dataset-tirrena-normalized-2026 |
| Dataset | Ambiente normalizzato - Logistica Tirrena (`dataset-tirrena-normalized-2026`) | `name` | Ambiente normalizzato - Logistica Tirrena |
| Dataset | Ambiente normalizzato - Logistica Tirrena (`dataset-tirrena-normalized-2026`) | `source_systems` | CMDB, vulnerability-manager, IAM, backup-manager, network-manager, monitoring-platform, configuration-manager |
| Organizzazione | Logistica Tirrena S.r.l. (`org-tirrena`) | `acn_specification` | Determinazione ACN 379907/2025 - specifiche di base vigenti |
| Organizzazione | Logistica Tirrena S.r.l. (`org-tirrena`) | `id` | org-tirrena |
| Organizzazione | Logistica Tirrena S.r.l. (`org-tirrena`) | `name` | Logistica Tirrena S.r.l. |
| Organizzazione | Logistica Tirrena S.r.l. (`org-tirrena`) | `nis_profile` | important |
| Organizzazione | Logistica Tirrena S.r.l. (`org-tirrena`) | `risk_assessment_reference` | RISK-TIRRENA-2026-05 |
| Responsabili | Responsabile Sistemi Informativi (`owner-tirrena-ops`) | `contact_reference` | role://tirrena-system-owner |
| Responsabili | Responsabile Sistemi Informativi (`owner-tirrena-ops`) | `id` | owner-tirrena-ops |
| Responsabili | Responsabile Sistemi Informativi (`owner-tirrena-ops`) | `name` | Responsabile Sistemi Informativi |
| Responsabili | Responsabile Sistemi Informativi (`owner-tirrena-ops`) | `provenance_ids` | prov-governance |
| Responsabili | Responsabile Sistemi Informativi (`owner-tirrena-ops`) | `role` | system-owner |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `asset_ids` | asset-tirrena-core |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `criticality` | critical |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `data_object_ids` | data-tirrena-core |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `description` | Gestione di ordini, tracciamento spedizioni e coordinamento dei magazzini. |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `id` | proc-tirrena-core |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `name` | Piattaforma logistica |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `owner_id` | owner-tirrena-ops |
| Processi | Piattaforma logistica (`proc-tirrena-core`) | `provenance_ids` | prov-governance |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `asset_ids` | asset-tirrena-core |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `classification` | confidential |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `description` | Categoria sintetica; non contiene dati reali. |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_at_rest` | True |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_at_rest_observation_type` | direct |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_at_rest_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_at_rest_provenance_ids` | prov-config |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_at_rest_status` | known |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_in_transit` | True |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_in_transit_observation_type` | direct |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_in_transit_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_in_transit_provenance_ids` | prov-config |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encrypted_in_transit_status` | known |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encryption_configuration` | AES-256 managed keys |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encryption_configuration_observation_type` | direct |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encryption_configuration_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encryption_configuration_provenance_ids` | prov-config |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `encryption_configuration_status` | known |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `id` | data-tirrena-core |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `name` | Dati logistici e clienti sintetici |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `provenance_ids` | prov-config |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media` | False |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media_encrypted_provenance_ids` | prov-config |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media_encrypted_status` | not_applicable |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media_observation_type` | direct |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media_provenance_ids` | prov-config |
| Categorie di dati | Dati logistici e clienti sintetici (`data-tirrena-core`) | `removable_media_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `admin_remote_access_logging` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `admin_remote_access_logging_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `admin_remote_access_logging_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `admin_remote_access_logging_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `admin_remote_access_logging_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `anomaly_thresholds_configured` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `anomaly_thresholds_configured_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `anomaly_thresholds_configured_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `anomaly_thresholds_configured_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `anomaly_thresholds_configured_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `asset_type` | server |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `critical_software_supplier_channels_monitored` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `critical_software_supplier_channels_monitored_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `critical_software_supplier_channels_monitored_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `critical_software_supplier_channels_monitored_provenance_ids` | prov-scan |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `critical_software_supplier_channels_monitored_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `criticality` | critical |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `data_object_ids` | data-tirrena-core |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `description` | Server applicativo centrale per la piattaforma logistica. |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `environment` | production |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `evidence_ids` | ev-tirrena-asset, ev-tirrena-software, ev-tirrena-flow, ev-tirrena-provider, ev-tirrena-scan, ev-tirrena-treatment, ev-tirrena-vulnmanagement, ev-tirrena-accessreview, ev-tirrena-accessconfig, ev-tirrena-physical, ev-tirrena-encryption, ev-tirrena-backup, ev-tirrena-restore, ev-tirrena-system, ev-tirrena-patch, ev-tirrena-maintenance, ev-tirrena-log, ev-tirrena-network, ev-tirrena-emergency, ev-tirrena-monitoring, ev-tirrena-endpoint |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `exposure_level` | high |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `extended_vulnerability_assessment_performed` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `extended_vulnerability_assessment_performed_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `extended_vulnerability_assessment_performed_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `extended_vulnerability_assessment_performed_provenance_ids` | prov-scan |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `extended_vulnerability_assessment_performed_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `firewall_enabled` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `firewall_enabled_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `firewall_enabled_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `firewall_enabled_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `firewall_enabled_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardening_baseline_applied` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardening_baseline_applied_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardening_baseline_applied_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardening_baseline_applied_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardening_baseline_applied_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardware_inventory_complete` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardware_inventory_complete_observation_type` | evidence_based |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardware_inventory_complete_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardware_inventory_complete_provenance_ids` | prov-inventory |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hardware_inventory_complete_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `hostname` | app.tirrena.example.invalid |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `id` | asset-tirrena-core |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `impact_level` | critical |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `internet_exposed` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `internet_exposed_observation_type` | evidence_based |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `internet_exposed_provenance_ids` | prov-inventory |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `internet_exposed_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `ip_addresses` | 198.51.100.41 |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `lifecycle_status` | active |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `log_retention_within_plan` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `log_retention_within_plan_observation_type` | declared |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `log_retention_within_plan_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `log_retention_within_plan_provenance_ids` | prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `log_retention_within_plan_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_centralized` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_centralized_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_centralized_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_centralized_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_centralized_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_protected` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_protected_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_protected_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_protected_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `logs_protected_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `mac_addresses` | nessuna |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `maintenance_logged` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `maintenance_logged_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `maintenance_logged_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `maintenance_logged_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `maintenance_logged_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `name` | Logistics Application Server |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `network_segment` | business-services |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `network_segment_observation_type` | evidence_based |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `network_segment_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `network_segment_provenance_ids` | prov-inventory |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `network_segment_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `nis_relevant` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `nis_relevant_observation_type` | declared |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `nis_relevant_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `nis_relevant_provenance_ids` | prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `nis_relevant_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `operating_system` | ExampleLinux |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `operating_system_version` | 11.9 |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `owner_id` | owner-tirrena-ops |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `physical_protection_documented` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `physical_protection_documented_observation_type` | declared |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `physical_protection_documented_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `physical_protection_documented_provenance_ids` | prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `physical_protection_documented_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `process_ids` | proc-tirrena-core |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `provenance_ids` | prov-inventory, prov-config, prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `provider_services_inventory_complete` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `provider_services_inventory_complete_observation_type` | declared |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `provider_services_inventory_complete_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `provider_services_inventory_complete_provenance_ids` | prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `provider_services_inventory_complete_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_protected` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_protected_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_protected_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_protected_provenance_ids` | prov-config |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_protected_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_registry_complete` | True |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_registry_complete_observation_type` | declared |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_registry_complete_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_registry_complete_provenance_ids` | prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `remote_access_registry_complete_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `risk_assessment_reference` | RISK-TIRRENA-2026-05 |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `secure_disposal_documented` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `secure_disposal_documented_observation_type` | declared |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `secure_disposal_documented_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `secure_disposal_documented_provenance_ids` | prov-governance |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `secure_disposal_documented_status` | known |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `service_ids` | svc-tirrena-https |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `support_status` | supported |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `vulnerability_advisories_monitored` | False |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `vulnerability_advisories_monitored_observation_type` | direct |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `vulnerability_advisories_monitored_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `vulnerability_advisories_monitored_provenance_ids` | prov-scan |
| Asset | Logistics Application Server (`asset-tirrena-core`) | `vulnerability_advisories_monitored_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `asset_type` | database |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `criticality` | medium |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `data_object_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `description` | Asset rilevato dal Modulo 1 ma escluso dal perimetro tecnico NIS. |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `environment` | production |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `evidence_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `exposure_level` | low |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `hostname` | aux-tirrena.example.invalid |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `id` | asset-tirrena-aux |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `impact_level` | medium |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `internet_exposed` | False |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `internet_exposed_observation_type` | evidence_based |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `internet_exposed_provenance_ids` | prov-inventory |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `internet_exposed_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `ip_addresses` | 198.51.100.42 |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `lifecycle_status` | active |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `mac_addresses` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `name` | Sistema ausiliario fuori perimetro NIS |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `network_segment` | auxiliary |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `network_segment_observation_type` | evidence_based |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `network_segment_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `network_segment_provenance_ids` | prov-inventory |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `network_segment_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `nis_relevant` | False |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `nis_relevant_observation_type` | declared |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `nis_relevant_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `nis_relevant_provenance_ids` | prov-governance |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `nis_relevant_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `owner_id` | owner-tirrena-ops |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `process_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `properties_json` | {} |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `provenance_ids` | prov-inventory, prov-governance |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `risk_assessment_reference` | RISK-TIRRENA-2026-05 |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `service_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-tirrena-aux`) | `support_status` | supported |
| Servizi | HTTPS (`svc-tirrena-https`) | `application_protocol` | https |
| Servizi | HTTPS (`svc-tirrena-https`) | `asset_id` | asset-tirrena-core |
| Servizi | HTTPS (`svc-tirrena-https`) | `authorized` | True |
| Servizi | HTTPS (`svc-tirrena-https`) | `authorized_observation_type` | evidence_based |
| Servizi | HTTPS (`svc-tirrena-https`) | `authorized_observed_at` | 2026-08-14T06:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `authorized_provenance_ids` | prov-inventory |
| Servizi | HTTPS (`svc-tirrena-https`) | `authorized_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `certificate_expiration` | 2027-08-14T00:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `certificate_expiration_observation_type` | direct |
| Servizi | HTTPS (`svc-tirrena-https`) | `certificate_expiration_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `certificate_expiration_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `certificate_expiration_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `cryptographic_baseline_id` | CRYPTO-BASELINE-2026.1 |
| Servizi | HTTPS (`svc-tirrena-https`) | `encrypted` | True |
| Servizi | HTTPS (`svc-tirrena-https`) | `encrypted_observation_type` | direct |
| Servizi | HTTPS (`svc-tirrena-https`) | `encrypted_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `encrypted_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `encrypted_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `encryption_configuration` | TLSv1.2/TLSv1.3 |
| Servizi | HTTPS (`svc-tirrena-https`) | `encryption_configuration_observation_type` | direct |
| Servizi | HTTPS (`svc-tirrena-https`) | `encryption_configuration_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `encryption_configuration_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `encryption_configuration_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `evidence_ids` | ev-tirrena-encryption |
| Servizi | HTTPS (`svc-tirrena-https`) | `id` | svc-tirrena-https |
| Servizi | HTTPS (`svc-tirrena-https`) | `internet_exposed` | True |
| Servizi | HTTPS (`svc-tirrena-https`) | `internet_exposed_observation_type` | evidence_based |
| Servizi | HTTPS (`svc-tirrena-https`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `internet_exposed_provenance_ids` | prov-inventory |
| Servizi | HTTPS (`svc-tirrena-https`) | `internet_exposed_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `name` | HTTPS |
| Servizi | HTTPS (`svc-tirrena-https`) | `obsolete_protocol` | False |
| Servizi | HTTPS (`svc-tirrena-https`) | `obsolete_protocol_observation_type` | direct |
| Servizi | HTTPS (`svc-tirrena-https`) | `obsolete_protocol_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `obsolete_protocol_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `obsolete_protocol_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `port` | 443 |
| Servizi | HTTPS (`svc-tirrena-https`) | `product` | TirrenaPortal |
| Servizi | HTTPS (`svc-tirrena-https`) | `protocol` | tcp |
| Servizi | HTTPS (`svc-tirrena-https`) | `provenance_ids` | prov-inventory, prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_enabled` | True |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_enabled_observation_type` | direct |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_enabled_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_enabled_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_enabled_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_versions` | TLSv1.2, TLSv1.3 |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_versions_observation_type` | direct |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_versions_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_versions_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-tirrena-https`) | `tls_versions_status` | known |
| Servizi | HTTPS (`svc-tirrena-https`) | `transport_protocol` | tcp |
| Servizi | HTTPS (`svc-tirrena-https`) | `version` | 6.2 |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `asset_id` | asset-tirrena-core |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `authorized` | True |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `authorized_observation_type` | declared |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `authorized_observed_at` | 2026-08-10T09:00:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `authorized_provenance_ids` | prov-governance |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `authorized_status` | known |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `critical_update_tested` | True |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `critical_update_tested_observation_type` | evidence_based |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `critical_update_tested_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `critical_update_tested_provenance_ids` | prov-patch |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `critical_update_tested_status` | known |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `evidence_ids` | ev-tirrena-software, ev-tirrena-patch |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `id` | software-tirrena-core |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `last_security_update_at` | 2026-06-25T01:00:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `last_security_update_at_observation_type` | evidence_based |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `last_security_update_at_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `last_security_update_at_provenance_ids` | prov-patch |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `last_security_update_at_status` | known |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `name` | TirrenaPortal |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `provenance_ids` | prov-inventory, prov-patch |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `security_update_status` | overdue_against_risk_plan |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `security_update_status_observation_type` | evidence_based |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `security_update_status_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `security_update_status_provenance_ids` | prov-patch |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `security_update_status_status` | known |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `support_status` | supported |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `support_status_observation_type` | evidence_based |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `support_status_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `support_status_provenance_ids` | prov-patch |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `support_status_status` | known |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `version` | 6.2 |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `version_observation_type` | evidence_based |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `version_observed_at` | 2026-08-14T06:00:00Z |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `version_provenance_ids` | prov-inventory |
| Componenti software | TirrenaPortal (`software-tirrena-core`) | `version_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `account_type` | administrator |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `asset_id` | asset-tirrena-core |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `authorized` | True |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `authorized_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `authorized_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `authorized_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `authorized_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `credentials_managed` | True |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `credentials_managed_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `credentials_managed_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `credentials_managed_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `credentials_managed_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `evidence_ids` | ev-tirrena-accessreview, ev-tirrena-accessconfig |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `id` | account-tirrena-admin |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `individual` | True |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `individual_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `individual_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `individual_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `individual_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `last_reviewed_at` | 2026-07-28T09:00:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `last_reviewed_at_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `last_reviewed_at_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `last_reviewed_at_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `last_reviewed_at_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `least_privilege` | True |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `least_privilege_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `least_privilege_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `least_privilege_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `least_privilege_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `mfa_enabled` | False |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `mfa_enabled_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `mfa_enabled_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `mfa_enabled_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `mfa_enabled_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `privileged` | True |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `privileged_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `privileged_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `privileged_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `privileged_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `remote_access` | True |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `remote_access_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `remote_access_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `remote_access_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `remote_access_status` | known |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `separate_admin_account` | False |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `separate_admin_account_observation_type` | evidence_based |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `separate_admin_account_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `separate_admin_account_provenance_ids` | prov-access |
| Utenze | account-tirrena-admin (`account-tirrena-admin`) | `separate_admin_account_status` | known |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `application_protocol` | https |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `asset_id` | asset-tirrena-core |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `authorized` | True |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `authorized_observation_type` | evidence_based |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `authorized_observed_at` | 2026-08-14T06:30:00Z |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `authorized_provenance_ids` | prov-network |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `authorized_status` | known |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `destination` | asset-tirrena-core |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `direction` | inbound |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `encrypted` | True |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `encrypted_observation_type` | evidence_based |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `encrypted_observed_at` | 2026-08-14T06:30:00Z |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `encrypted_provenance_ids` | prov-network |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `encrypted_status` | known |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `evidence_ids` | ev-tirrena-flow |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `id` | flow-tirrena-https |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `port` | 443 |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `provenance_ids` | prov-network |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `source` | internet |
| Flussi di rete | flow-tirrena-https (`flow-tirrena-https`) | `transport_protocol` | tcp |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `asset_id` | asset-tirrena-core |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `evidence_ids` | ev-tirrena-backup, ev-tirrena-restore |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `frequency_within_plan` | True |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `frequency_within_plan_observation_type` | evidence_based |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `frequency_within_plan_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `frequency_within_plan_provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `frequency_within_plan_status` | known |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `id` | backup-tirrena-core |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `last_success_at` | 2026-08-14T23:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `last_success_at_observation_type` | evidence_based |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `last_success_at_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `last_success_at_provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `last_success_at_status` | known |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `offline_copy` | True |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `offline_copy_observation_type` | evidence_based |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `offline_copy_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `offline_copy_provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `offline_copy_status` | known |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `plan_reference` | BACKUP-TIRRENA-2026 |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `protected_copy` | True |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `protected_copy_observation_type` | evidence_based |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `protected_copy_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `protected_copy_provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `protected_copy_status` | known |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_at` | 2026-06-18T08:00:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_at_observation_type` | evidence_based |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_at_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_at_provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_at_status` | known |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_successful` | False |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_successful_observation_type` | evidence_based |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_successful_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_successful_provenance_ids` | prov-backup |
| Backup | backup-tirrena-core (`backup-tirrena-core`) | `restore_test_successful_status` | known |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `asset_id` | asset-tirrena-core |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `capability_type` | emergency_communications |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `configuration_reference` | EMERGENCY-COMMS-TIRRENA-1 |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `configured` | False |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `configured_status` | known |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `enabled` | True |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `enabled_status` | known |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `evidence_ids` | ev-tirrena-emergency |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `id` | cap-tirrena-emergency |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `maintained` | True |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `maintained_status` | known |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `monitored` | True |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `monitored_status` | known |
| Capacità di sicurezza | cap-tirrena-emergency (`cap-tirrena-emergency`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `asset_id` | asset-tirrena-core |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `capability_type` | intrusion_detection |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `configured` | True |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `configured_status` | known |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `enabled` | True |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `enabled_status` | known |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `evidence_ids` | ev-tirrena-monitoring |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `id` | cap-tirrena-ids |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `maintained` | True |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `maintained_status` | known |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `monitored` | False |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `monitored_status` | known |
| Capacità di sicurezza | cap-tirrena-ids (`cap-tirrena-ids`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `asset_id` | asset-tirrena-core |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `capability_type` | traffic_filter |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `configured` | True |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `configured_status` | known |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `enabled` | True |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `enabled_status` | known |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `evidence_ids` | ev-tirrena-monitoring |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `id` | cap-tirrena-filter |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `maintained` | True |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `maintained_status` | known |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `monitored` | True |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `monitored_status` | known |
| Capacità di sicurezza | cap-tirrena-filter (`cap-tirrena-filter`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `asset_id` | asset-tirrena-core |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `capability_type` | access_monitoring |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `configured` | True |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `configured_status` | known |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `enabled` | True |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `enabled_status` | known |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `evidence_ids` | ev-tirrena-monitoring |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `id` | cap-tirrena-access-monitor |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `maintained` | True |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `maintained_status` | known |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `monitored` | True |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `monitored_status` | known |
| Capacità di sicurezza | cap-tirrena-access-monitor (`cap-tirrena-access-monitor`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `asset_id` | asset-tirrena-core |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `capability_type` | endpoint_protection |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `configured` | True |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `configured_status` | known |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `enabled` | True |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `enabled_status` | known |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `evidence_ids` | ev-tirrena-endpoint |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `id` | cap-tirrena-endpoint |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `maintained` | True |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `maintained_status` | known |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `monitored` | True |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `monitored_status` | known |
| Capacità di sicurezza | cap-tirrena-endpoint (`cap-tirrena-endpoint`) | `provenance_ids` | prov-config |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `accepted_exception` | False |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `accepted_exception_observation_type` | declared |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `accepted_exception_observed_at` | 2026-08-10T09:00:00Z |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `accepted_exception_provenance_ids` | prov-governance |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `accepted_exception_status` | known |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `asset_id` | asset-tirrena-core |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `component` | Apache HTTP Server 2.4.49 usato da TirrenaPortal |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `cve` | CVE-2021-41773 |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `cvss_score` | 7.5 |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `description` | Riferimento CVE reale applicato, esclusivamente a scopo dimostrativo, ad Apache HTTP Server 2.4.49 usato dal prodotto sintetico TirrenaPortal. |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `detected_at` | 2026-08-09T05:00:00Z |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `evidence_ids` | ev-tirrena-scan, ev-tirrena-treatment |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `id` | vuln-tirrena-001 |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `patch_available` | True |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `patch_available_observation_type` | direct |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `patch_available_observed_at` | 2026-08-14T05:00:00Z |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `patch_available_provenance_ids` | prov-scan |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `patch_available_status` | known |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `provenance_ids` | prov-scan, prov-patch |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `remediation_due_date` | 2026-08-22T23:59:59Z |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `remediation_status` | in_progress |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `remediation_status_observation_type` | evidence_based |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `remediation_status_observed_at` | 2026-08-14T07:30:00Z |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `remediation_status_provenance_ids` | prov-patch |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `remediation_status_status` | known |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `service_id` | svc-tirrena-https |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `severity` | high |
| Vulnerabilità | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione (`vuln-tirrena-001`) | `title` | Aggiornamento Apache HTTP Server in attesa di finestra di manutenzione |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `content_json` | {} |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `control_ids` | CTRL-ID-AM-01 |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `description` | Inventario asset acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `evidence_type` | asset_inventory |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `id` | ev-tirrena-asset |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `provenance_ids` | prov-inventory |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `reliability` | high |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `service_ids` | nessuna |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `source` | CMDB |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `source_category` | asset_internal |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `title` | Inventario asset |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Inventario asset (`ev-tirrena-asset`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario software (`ev-tirrena-software`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Inventario software (`ev-tirrena-software`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario software (`ev-tirrena-software`) | `content_json` | {} |
| Evidenze | Inventario software (`ev-tirrena-software`) | `control_ids` | CTRL-ID-AM-02, CTRL-PR-PS-02 |
| Evidenze | Inventario software (`ev-tirrena-software`) | `description` | Inventario software acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario software (`ev-tirrena-software`) | `evidence_type` | software_inventory |
| Evidenze | Inventario software (`ev-tirrena-software`) | `id` | ev-tirrena-software |
| Evidenze | Inventario software (`ev-tirrena-software`) | `provenance_ids` | prov-inventory |
| Evidenze | Inventario software (`ev-tirrena-software`) | `reliability` | high |
| Evidenze | Inventario software (`ev-tirrena-software`) | `service_ids` | nessuna |
| Evidenze | Inventario software (`ev-tirrena-software`) | `source` | CMDB |
| Evidenze | Inventario software (`ev-tirrena-software`) | `source_category` | asset_internal |
| Evidenze | Inventario software (`ev-tirrena-software`) | `title` | Inventario software |
| Evidenze | Inventario software (`ev-tirrena-software`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario software (`ev-tirrena-software`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `content_json` | {} |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `control_ids` | CTRL-ID-AM-03-E |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `description` | Inventario flussi di rete acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `evidence_type` | network_flow_inventory |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `id` | ev-tirrena-flow |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `provenance_ids` | prov-network |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `reliability` | high |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `service_ids` | nessuna |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `source` | network-manager |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `source_category` | asset_internal |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `title` | Inventario flussi di rete |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario flussi di rete (`ev-tirrena-flow`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `content_json` | {} |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `control_ids` | CTRL-ID-AM-04 |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `description` | Inventario servizi fornitori acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `evidence_type` | provider_service_inventory |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `id` | ev-tirrena-provider |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `provenance_ids` | prov-governance |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `reliability` | medium |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `service_ids` | nessuna |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `source` | service-catalog |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `source_category` | declared |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `title` | Inventario servizi fornitori |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario servizi fornitori (`ev-tirrena-provider`) | `vulnerability_ids` | nessuna |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `content_json` | {"activity_description": "Vulnerability assessment autenticato.", "cve": "CVE-2021-41773", "impact_levels": ["high"], "nvd_url": "https://nvd.nist.gov/vuln/detail/CVE-2021-41773", "outcomes": "Relazione strutturata dello scenario dimostrativo.", "synthetic_context": "Organizzazione e prodotto sono inventati; il CVE è reale e la sua associazione ad Apache HTTP Server 2.4.49 usato da TirrenaPortal è esclusivamente dimostrativa.", "vulnerabilities": ["vuln-tirrena-001"]} |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `control_ids` | CTRL-ID-RA-01, CTRL-ID-RA-01-E, CTRL-ID-RA-08 |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `description` | Scansione vulnerabilità acquisita e normalizzata dai moduli 1 e 2; il prodotto e l'associazione alla dipendenza sono sintetici. |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `evidence_type` | vulnerability_scan |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `id` | ev-tirrena-scan |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `provenance_ids` | prov-scan |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `reliability` | high |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `service_ids` | nessuna |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `source` | vulnerability-scanner |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `source_category` | asset_internal |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `title` | Scansione vulnerabilità |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Scansione vulnerabilità (`ev-tirrena-scan`) | `vulnerability_ids` | vuln-tirrena-001 |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `content_json` | {} |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `control_ids` | CTRL-ID-RA-08 |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `description` | Registro trattamento vulnerabilità acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `evidence_type` | vulnerability_treatment |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `id` | ev-tirrena-treatment |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `provenance_ids` | prov-patch |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `reliability` | high |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `service_ids` | nessuna |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `source` | vulnerability-manager |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `source_category` | asset_internal |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `title` | Registro trattamento vulnerabilità |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro trattamento vulnerabilità (`ev-tirrena-treatment`) | `vulnerability_ids` | vuln-tirrena-001 |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `content_json` | {} |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `control_ids` | CTRL-ID-RA-01, CTRL-ID-RA-08, CTRL-ID-RA-08-E |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `description` | Monitoraggio advisory vulnerabilità acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `evidence_type` | vulnerability_management |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `id` | ev-tirrena-vulnmanagement |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `provenance_ids` | prov-scan |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `reliability` | high |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `service_ids` | nessuna |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `source` | vulnerability-manager |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `source_category` | asset_internal |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `title` | Monitoraggio advisory vulnerabilità |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-tirrena-vulnmanagement`) | `vulnerability_ids` | nessuna |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `content_json` | {} |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `control_ids` | CTRL-PR-AA-01 |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `description` | Revisione identità e accessi acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `evidence_type` | access_review |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `id` | ev-tirrena-accessreview |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `provenance_ids` | prov-access |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `reliability` | high |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `service_ids` | nessuna |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `source` | IAM |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `source_category` | asset_internal |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `title` | Revisione identità e accessi |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Revisione identità e accessi (`ev-tirrena-accessreview`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `content_json` | {} |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `control_ids` | CTRL-PR-AA-03, CTRL-PR-AA-05 |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `description` | Configurazione MFA e privilegi acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `evidence_type` | access_configuration |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `id` | ev-tirrena-accessconfig |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `provenance_ids` | prov-access |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `reliability` | high |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `service_ids` | nessuna |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `source` | IAM |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `source_category` | asset_internal |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `title` | Configurazione MFA e privilegi |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione MFA e privilegi (`ev-tirrena-accessconfig`) | `vulnerability_ids` | nessuna |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `content_json` | {} |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `control_ids` | CTRL-PR-AA-06 |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `description` | Evidenza protezione fisica acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `evidence_type` | physical_security |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `id` | ev-tirrena-physical |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `provenance_ids` | prov-governance |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `reliability` | medium |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `service_ids` | nessuna |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `source` | facilities |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `source_category` | declared |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `title` | Evidenza protezione fisica |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Evidenza protezione fisica (`ev-tirrena-physical`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `content_json` | {"baseline_id": "CRYPTO-BASELINE-2026.1"} |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `control_ids` | CTRL-PR-DS-01, CTRL-PR-DS-02 |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `description` | Configurazione cifratura acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `evidence_type` | encryption_configuration |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `id` | ev-tirrena-encryption |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `reliability` | high |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `service_ids` | svc-tirrena-https |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `source` | configuration-manager |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `source_category` | asset_internal |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `title` | Configurazione cifratura |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Configurazione cifratura (`ev-tirrena-encryption`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `content_json` | {"plan_reference": "BACKUP-TIRRENA-2026"} |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `control_ids` | CTRL-PR-DS-11, CTRL-PR-DS-11-E |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `description` | Registro backup acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `evidence_type` | backup_record |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `id` | ev-tirrena-backup |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `provenance_ids` | prov-backup |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `reliability` | high |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `service_ids` | nessuna |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `source` | backup-manager |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `source_category` | asset_internal |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `title` | Registro backup |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro backup (`ev-tirrena-backup`) | `vulnerability_ids` | nessuna |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `content_json` | {} |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `control_ids` | CTRL-PR-DS-11-E |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `description` | Test di ripristino acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `evidence_type` | restore_test |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `id` | ev-tirrena-restore |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `provenance_ids` | prov-backup |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `reliability` | high |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `service_ids` | nessuna |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `source` | backup-manager |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `source_category` | asset_internal |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `title` | Test di ripristino |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Test di ripristino (`ev-tirrena-restore`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `content_json` | {} |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `control_ids` | CTRL-PR-PS-01-E |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `description` | Configurazione e hardening acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `evidence_type` | system_configuration |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `id` | ev-tirrena-system |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `reliability` | high |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `service_ids` | nessuna |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `source` | configuration-manager |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `source_category` | asset_internal |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `title` | Configurazione e hardening |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione e hardening (`ev-tirrena-system`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `content_json` | {} |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `control_ids` | CTRL-PR-PS-02, CTRL-PR-PS-02-E |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `description` | Registro patching acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `evidence_type` | patch_record |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `id` | ev-tirrena-patch |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `provenance_ids` | prov-patch |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `reliability` | high |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `service_ids` | nessuna |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `source` | patch-manager |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `source_category` | asset_internal |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `title` | Registro patching |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro patching (`ev-tirrena-patch`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `content_json` | {} |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `control_ids` | CTRL-PR-PS-03-E |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `description` | Registro manutenzione acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `evidence_type` | maintenance_record |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `id` | ev-tirrena-maintenance |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `provenance_ids` | prov-config |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `reliability` | high |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `service_ids` | nessuna |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `source` | configuration-manager |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `source_category` | asset_internal |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `title` | Registro manutenzione |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro manutenzione (`ev-tirrena-maintenance`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `content_json` | {} |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `control_ids` | CTRL-PR-PS-04 |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `description` | Configurazione logging acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `evidence_type` | log_configuration |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `id` | ev-tirrena-log |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `reliability` | high |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `service_ids` | nessuna |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `source` | logging-platform |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `source_category` | asset_internal |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `title` | Configurazione logging |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione logging (`ev-tirrena-log`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `content_json` | {} |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `control_ids` | CTRL-PR-IR-01 |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `description` | Configurazione accessi remoti e firewall acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `evidence_type` | network_security |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `id` | ev-tirrena-network |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `provenance_ids` | prov-network |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `reliability` | high |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `service_ids` | nessuna |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `source` | network-manager |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `source_category` | asset_internal |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `title` | Configurazione accessi remoti e firewall |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione accessi remoti e firewall (`ev-tirrena-network`) | `vulnerability_ids` | nessuna |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `content_json` | {} |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `control_ids` | CTRL-PR-IR-03-E |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `description` | Comunicazioni di emergenza acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `evidence_type` | emergency_communications |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `id` | ev-tirrena-emergency |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `provenance_ids` | prov-config |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `reliability` | high |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `service_ids` | nessuna |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `source` | crisis-platform |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `source_category` | asset_internal |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `title` | Comunicazioni di emergenza |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Comunicazioni di emergenza (`ev-tirrena-emergency`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `content_json` | {} |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `control_ids` | CTRL-DE-CM-01, CTRL-DE-CM-01-E |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `description` | Configurazione monitoraggio acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `evidence_type` | monitoring_configuration |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `id` | ev-tirrena-monitoring |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `reliability` | high |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `service_ids` | nessuna |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `source` | monitoring-platform |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `source_category` | asset_internal |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `title` | Configurazione monitoraggio |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione monitoraggio (`ev-tirrena-monitoring`) | `vulnerability_ids` | nessuna |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `asset_ids` | asset-tirrena-core |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `content_json` | {} |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `control_ids` | CTRL-DE-CM-09 |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `description` | Protezione endpoint acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `evidence_type` | endpoint_protection |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `id` | ev-tirrena-endpoint |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `provenance_ids` | prov-config |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `reliability` | high |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `service_ids` | nessuna |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `source` | endpoint-platform |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `source_category` | asset_internal |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `title` | Protezione endpoint |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Protezione endpoint (`ev-tirrena-endpoint`) | `vulnerability_ids` | nessuna |
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
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `acn_point` | ID.AM-01 |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `confidence_level` | medium |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `control_id` | CTRL-ID-AM-01 |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `decision_policy` | all_required |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-asset"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "asset.hardware_inventory_complete", "provenance_ids": ["prov-inventory"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-asset.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `errors` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "asset.hardware_inventory_complete", "provenance_ids": ["prov-inventory"], "value_status": "known"}] |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `evidence_ids` | ev-tirrena-asset |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `governance_status` | none |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `id` | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `information_actions` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `known_violations` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `missing_information` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `nis_profile` | important |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `requirement_id` | REQ-ID-AM-01 |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `rule_id` | RULE-ID-AM-01 |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `technical_status` | compliant |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `thresholds_used_json` | {"evidence.ev-tirrena-asset.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | a44647f2-4f8e-56ef-8682-31e0ad08e8e8 (`a44647f2-4f8e-56ef-8682-31e0ad08e8e8`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `acn_point` | ID.AM-02 |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `confidence_level` | low |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `control_id` | CTRL-ID-AM-02 |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `decision_policy` | all_required |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-software"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "identificato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "Logistics Application Server", "path": "Asset.asset-tirrena-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "HTTPS", "path": "Service.svc-tirrena-https.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "Service.svc-tirrena-https.authorized", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "TirrenaPortal", "path": "SoftwareComponent.software-tirrena-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": "6.2", "path": "SoftwareComponent.software-tirrena-core.version", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "SoftwareComponent.software-tirrena-core.authorized", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `errors` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `evaluated_facts_json` | [{"comparison": "identificato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "Logistics Application Server", "path": "Asset.asset-tirrena-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "HTTPS", "path": "Service.svc-tirrena-https.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "Service.svc-tirrena-https.authorized", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "TirrenaPortal", "path": "SoftwareComponent.software-tirrena-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": "6.2", "path": "SoftwareComponent.software-tirrena-core.version", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "SoftwareComponent.software-tirrena-core.authorized", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `evidence_ids` | ev-tirrena-software |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `governance_status` | none |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `id` | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `information_actions` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `known_violations` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `missing_information` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `nis_profile` | important |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `requirement_id` | REQ-ID-AM-02 |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `rule_id` | RULE-ID-AM-02 |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `technical_status` | compliant |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `thresholds_used_json` | {"evidence.ev-tirrena-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9 (`55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9`) | `verification_mode` | direct_technical |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `acn_point` | ID.AM-03 |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `confidence_level` | insufficient |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `conflicting_information` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `control_id` | CTRL-ID-AM-03-E |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `decision_policy` | all_required |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `errors` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `evidence_ids` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `governance_status` | none |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `id` | be815e68-0a0f-581e-9f74-364b6a8847ad |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `information_actions` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `known_violations` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `missing_information` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `nis_profile` | important |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `requirement_id` | REQ-ID-AM-03-E |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `rule_id` | RULE-ID-AM-03-E |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `selector_decisions` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `technical_remediations` | nessuna |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `technical_status` | not_applicable |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `thresholds_used_json` | {} |
| Esiti della valutazione | be815e68-0a0f-581e-9f74-364b6a8847ad (`be815e68-0a0f-581e-9f74-364b6a8847ad`) | `verification_mode` | direct_technical |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `acn_point` | ID.AM-04 |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `confidence_level` | low |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `control_id` | CTRL-ID-AM-04 |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `decision_policy` | all_required |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-provider"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.provider_services_inventory_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-provider.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `errors` | nessuna |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": false, "path": "asset.provider_services_inventory_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `evidence_ids` | ev-tirrena-provider |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `governance_status` | none |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `id` | a70a78ab-5a03-5642-a8c5-a57866f5821c |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `information_actions` | nessuna |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.provider_services_inventory_complete", "remediation": "Completare l'elenco dei servizi dei fornitori che supportano l'asset."}] |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `missing_information` | nessuna |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `nis_profile` | important |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `recommendation` | Completare l'elenco dei servizi dei fornitori che supportano l'asset. |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `requirement_id` | REQ-ID-AM-04 |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `rule_id` | RULE-ID-AM-04 |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `technical_remediations` | Completare l'elenco dei servizi dei fornitori che supportano l'asset. |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `technical_status` | non_compliant |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `thresholds_used_json` | {"evidence.ev-tirrena-provider.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | a70a78ab-5a03-5642-a8c5-a57866f5821c (`a70a78ab-5a03-5642-a8c5-a57866f5821c`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `confidence_level` | high |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `control_id` | CTRL-ID-RA-01 |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `decision_policy` | all_required |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-vulnmanagement"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": false, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `errors` | nessuna |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": false, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}] |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `evidence_ids` | ev-tirrena-vulnmanagement |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `governance_status` | none |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `id` | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `information_actions` | nessuna |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.vulnerability_advisories_monitored", "remediation": "Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate."}] |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `missing_information` | nessuna |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `nis_profile` | important |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `recommendation` | Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate. |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `requirement_id` | REQ-ID-RA-01 |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `rule_id` | RULE-ID-RA-01 |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `technical_remediations` | Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate. |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `technical_status` | non_compliant |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `thresholds_used_json` | {"evidence.ev-tirrena-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | 2d9abb01-0ddf-5142-b5ab-7cb86875b224 (`2d9abb01-0ddf-5142-b5ab-7cb86875b224`) | `verification_mode` | direct_technical |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `confidence_level` | insufficient |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `conflicting_information` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `control_id` | CTRL-ID-RA-01-E |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `decision_policy` | all_required |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `errors` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `evidence_ids` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `governance_status` | none |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `id` | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `information_actions` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `known_violations` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `missing_information` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `nis_profile` | important |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `requirement_id` | REQ-ID-RA-01-E |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `rule_id` | RULE-ID-RA-01-E |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `selector_decisions` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `technical_remediations` | nessuna |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `technical_status` | not_applicable |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `thresholds_used_json` | {} |
| Esiti della valutazione | f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84 (`f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `confidence_level` | medium |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `control_id` | CTRL-ID-RA-08 |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `decision_policy` | all_required |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-treatment", "ev-tirrena-vulnmanagement"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": false, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}, {"comparison": "remediated o mitigated", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "in_progress", "path": "Vulnerability.vuln-tirrena-001.remediation_status", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-08", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-treatment.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-tirrena-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `errors` | nessuna |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": false, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}, {"comparison": "remediated o mitigated", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "in_progress", "path": "Vulnerability.vuln-tirrena-001.remediation_status", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `evidence_ids` | ev-tirrena-treatment, ev-tirrena-vulnmanagement |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `governance_status` | none |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `id` | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `information_actions` | nessuna |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "asset.vulnerability_advisories_monitored", "remediation": "Remediare o mitigare e registrare il rischio residuo."}, {"comparison": "remediated o mitigated", "observed_value": "in_progress", "path": "Vulnerability.vuln-tirrena-001.remediation_status", "remediation": "Remediare o mitigare e registrare il rischio residuo."}] |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `missing_information` | nessuna |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `nis_profile` | important |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `recommendation` | Remediare o mitigare e registrare il rischio residuo. |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `requirement_id` | REQ-ID-RA-08 |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `rule_id` | RULE-ID-RA-08 |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `technical_remediations` | Remediare o mitigare e registrare il rischio residuo. |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `technical_status` | non_compliant |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `thresholds_used_json` | {"evidence.ev-tirrena-treatment.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-tirrena-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b (`eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `confidence_level` | insufficient |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `control_id` | CTRL-ID-RA-08-E |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `decision_policy` | all_required |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-08-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `errors` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `governance_status` | none |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `id` | 205a77ed-ada0-5e9c-8557-d4ea0017b903 |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `information_actions` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `known_violations` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `missing_information` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `nis_profile` | important |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `requirement_id` | REQ-ID-RA-08-E |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `rule_id` | RULE-ID-RA-08-E |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `technical_status` | not_applicable |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 205a77ed-ada0-5e9c-8557-d4ea0017b903 (`205a77ed-ada0-5e9c-8557-d4ea0017b903`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `acn_point` | PR.AA-01 |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `confidence_level` | medium |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `control_id` | CTRL-PR-AA-01 |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `decision_policy` | all_required |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-accessreview"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "administrator", "path": "Account.account-tirrena-admin.account_type", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.individual", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.authorized", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.credentials_managed", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": "2026-07-28T09:00:00Z", "path": "Account.account-tirrena-admin.last_reviewed_at", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-accessreview.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `errors` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `evaluated_facts_json` | [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "administrator", "path": "Account.account-tirrena-admin.account_type", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.individual", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.authorized", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.credentials_managed", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": "2026-07-28T09:00:00Z", "path": "Account.account-tirrena-admin.last_reviewed_at", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `evidence_ids` | ev-tirrena-accessreview |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `governance_status` | none |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `id` | fa454414-a9e2-535c-9497-9ac4415bc59c |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `information_actions` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `known_violations` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `missing_information` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `nis_profile` | important |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `requirement_id` | REQ-PR-AA-01 |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `rule_id` | RULE-PR-AA-01 |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `technical_remediations` | nessuna |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `technical_status` | compliant |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `thresholds_used_json` | {"evidence.ev-tirrena-accessreview.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}} |
| Esiti della valutazione | fa454414-a9e2-535c-9497-9ac4415bc59c (`fa454414-a9e2-535c-9497-9ac4415bc59c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `acn_point` | PR.AA-03 |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `confidence_level` | medium |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `control_id` | CTRL-PR-AA-03 |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `decision_policy` | all_required |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-accessconfig"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-tirrena-admin.mfa_enabled", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": ["account-tirrena-admin"], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-03", "rule_version": "2.1.0", "selector_decisions": [{"conflicting_information": [], "entity_id": "account-tirrena-admin", "evaluated_fields": ["privileged", "remote_access"], "missing_information": [], "selector_type": "any", "status": "selected"}], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `errors` | nessuna |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-tirrena-admin.mfa_enabled", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `evidence_ids` | ev-tirrena-accessconfig |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `governance_status` | none |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `id` | 8e46657c-f989-5b2c-b588-26c8c32d158f |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `information_actions` | nessuna |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "Account.account-tirrena-admin.mfa_enabled", "remediation": "Applicare MFA agli accessi privilegiati o remoti individuati dal rischio."}] |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `missing_information` | nessuna |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `nis_profile` | important |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `recommendation` | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `requirement_id` | REQ-PR-AA-03 |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `rule_id` | RULE-PR-AA-03 |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `selector_decisions_json` | [{"conflicting_information": [], "entity_id": "account-tirrena-admin", "evaluated_fields": ["privileged", "remote_access"], "missing_information": [], "selector_type": "any", "status": "selected"}] |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `technical_remediations` | Applicare MFA agli accessi privilegiati o remoti individuati dal rischio. |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `technical_status` | non_compliant |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `thresholds_used_json` | {"evidence.ev-tirrena-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 8e46657c-f989-5b2c-b588-26c8c32d158f (`8e46657c-f989-5b2c-b588-26c8c32d158f`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `acn_point` | PR.AA-05 |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `confidence_level` | medium |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `control_id` | CTRL-PR-AA-05 |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `decision_policy` | all_required |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-accessconfig"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.least_privilege", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-tirrena-admin.separate_admin_account", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": ["account-tirrena-admin"], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-05", "rule_version": "2.1.0", "selector_decisions": [{"conflicting_information": [], "entity_id": "account-tirrena-admin", "evaluated_fields": ["privileged"], "missing_information": [], "selector_type": "any", "status": "selected"}], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `errors` | nessuna |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-tirrena-admin.least_privilege", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": false, "path": "Account.account-tirrena-admin.separate_admin_account", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `evidence_ids` | ev-tirrena-accessconfig |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `governance_status` | none |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `id` | 2b1955d6-62a0-517e-97c4-f990424bb297 |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `information_actions` | nessuna |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "Account.account-tirrena-admin.separate_admin_account", "remediation": "Ridurre i privilegi e separare le credenziali amministrative."}] |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `missing_information` | nessuna |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `nis_profile` | important |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `recommendation` | Ridurre i privilegi e separare le credenziali amministrative. |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `requirement_id` | REQ-PR-AA-05 |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `rule_id` | RULE-PR-AA-05 |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `selector_decisions_json` | [{"conflicting_information": [], "entity_id": "account-tirrena-admin", "evaluated_fields": ["privileged"], "missing_information": [], "selector_type": "any", "status": "selected"}] |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `technical_remediations` | Ridurre i privilegi e separare le credenziali amministrative. |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `technical_status` | non_compliant |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `thresholds_used_json` | {"evidence.ev-tirrena-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 2b1955d6-62a0-517e-97c4-f990424bb297 (`2b1955d6-62a0-517e-97c4-f990424bb297`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `acn_point` | PR.AA-06 |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `confidence_level` | low |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `control_id` | CTRL-PR-AA-06 |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `decision_policy` | all_required |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-physical"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.physical_protection_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-06", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-physical.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `errors` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.physical_protection_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `evidence_ids` | ev-tirrena-physical |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `governance_status` | none |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `id` | 559b88af-ecc6-5668-aa4f-d19a04fe3485 |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `information_actions` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `known_violations` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `missing_information` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `nis_profile` | important |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `requirement_id` | REQ-PR-AA-06 |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `rule_id` | RULE-PR-AA-06 |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `technical_status` | compliant |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `thresholds_used_json` | {"evidence.ev-tirrena-physical.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | 559b88af-ecc6-5668-aa4f-d19a04fe3485 (`559b88af-ecc6-5668-aa4f-d19a04fe3485`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `acn_point` | PR.DS-01 |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `confidence_level` | insufficient |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `control_id` | CTRL-PR-DS-01 |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `decision_policy` | all_required |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `errors` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `governance_status` | none |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `id` | 7ba70886-b3b0-58d8-a187-ef463799b3f3 |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `known_violations` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `missing_information` | DataObject.inventory_status |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `nis_profile` | important |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `reason` | completezza dell'inventario DataObject non nota |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `recommendation` | Cifrare i supporti rimovibili secondo classificazione e baseline approvata. |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `requirement_id` | REQ-PR-DS-01 |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `rule_id` | RULE-PR-DS-01 |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `technical_status` | not_verifiable |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 7ba70886-b3b0-58d8-a187-ef463799b3f3 (`7ba70886-b3b0-58d8-a187-ef463799b3f3`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `acn_point` | PR.DS-02 |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `confidence_level` | high |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `control_id` | CTRL-PR-DS-02 |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `decision_policy` | all_required |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-encryption"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-tirrena-https.encrypted", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-tirrena-https.tls_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "baseline crittografica", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": ["TLSv1.2", "TLSv1.3"], "path": "Service.svc-tirrena-https.tls_versions", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "evidence.ev-tirrena-encryption.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `errors` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-tirrena-https.encrypted", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-tirrena-https.tls_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "baseline crittografica", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": ["TLSv1.2", "TLSv1.3"], "path": "Service.svc-tirrena-https.tls_versions", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `evidence_ids` | ev-tirrena-encryption |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `governance_status` | none |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `id` | 00bf1516-3e72-53ac-8911-d7382db61447 |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `information_actions` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `known_violations` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `missing_information` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `nis_profile` | important |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `requirement_id` | REQ-PR-DS-02 |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `rule_id` | RULE-PR-DS-02 |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `technical_status` | compliant |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `thresholds_used_json` | {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "evidence.ev-tirrena-encryption.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}} |
| Esiti della valutazione | 00bf1516-3e72-53ac-8911-d7382db61447 (`00bf1516-3e72-53ac-8911-d7382db61447`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `confidence_level` | medium |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `control_id` | CTRL-PR-DS-11 |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `decision_policy` | all_required |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-backup"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-tirrena-core.frequency_within_plan", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-tirrena-core.offline_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-11", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `errors` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-tirrena-core.frequency_within_plan", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-tirrena-core.offline_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}] |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `evidence_ids` | ev-tirrena-backup |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `governance_status` | none |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `id` | 8a0156bc-de29-5ad4-bf70-42f3514870c5 |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `information_actions` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `known_violations` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `missing_information` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `nis_profile` | important |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `requirement_id` | REQ-PR-DS-11 |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `rule_id` | RULE-PR-DS-11 |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `technical_status` | compliant |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `thresholds_used_json` | {"evidence.ev-tirrena-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 8a0156bc-de29-5ad4-bf70-42f3514870c5 (`8a0156bc-de29-5ad4-bf70-42f3514870c5`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `confidence_level` | insufficient |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `control_id` | CTRL-PR-DS-11-E |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `decision_policy` | all_required |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-11-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `errors` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `governance_status` | none |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `id` | 731cc9c5-9524-5890-a2b1-566fea73fa0e |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `information_actions` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `known_violations` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `missing_information` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `nis_profile` | important |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `requirement_id` | REQ-PR-DS-11-E |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `rule_id` | RULE-PR-DS-11-E |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `technical_status` | not_applicable |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 731cc9c5-9524-5890-a2b1-566fea73fa0e (`731cc9c5-9524-5890-a2b1-566fea73fa0e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `acn_point` | PR.PS-01 |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `confidence_level` | insufficient |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `conflicting_information` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `control_id` | CTRL-PR-PS-01-E |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `decision_policy` | all_required |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `errors` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `evidence_ids` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `governance_status` | none |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `id` | eda26dfc-17ea-5e61-a4bb-154399162614 |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `information_actions` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `known_violations` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `missing_information` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `nis_profile` | important |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `requirement_id` | REQ-PR-PS-01-E |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `rule_id` | RULE-PR-PS-01-E |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `selector_decisions` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `technical_remediations` | nessuna |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `technical_status` | not_applicable |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `thresholds_used_json` | {} |
| Esiti della valutazione | eda26dfc-17ea-5e61-a4bb-154399162614 (`eda26dfc-17ea-5e61-a4bb-154399162614`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `confidence_level` | medium |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `control_id` | CTRL-PR-PS-02 |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `decision_policy` | all_required |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-patch", "ev-tirrena-software"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "{supported}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "supported", "path": "SoftwareComponent.software-tirrena-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-tirrena-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-tirrena-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `errors` | nessuna |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `evaluated_facts_json` | [{"comparison": "{supported}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "supported", "path": "SoftwareComponent.software-tirrena-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-tirrena-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `evidence_ids` | ev-tirrena-patch, ev-tirrena-software |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `governance_status` | none |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `id` | 07719946-df9e-5c56-8839-4d2b76b06b4d |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `information_actions` | nessuna |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `known_violations_json` | [{"comparison": "{current, within_risk_plan}", "observed_value": "overdue_against_risk_plan", "path": "SoftwareComponent.software-tirrena-core.security_update_status", "remediation": "Sostituire software fuori supporto e rispettare i termini del piano di patching."}] |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `missing_information` | nessuna |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `nis_profile` | important |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `recommendation` | Sostituire software fuori supporto e rispettare i termini del piano di patching. |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `requirement_id` | REQ-PR-PS-02 |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `rule_id` | RULE-PR-PS-02 |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `technical_remediations` | Sostituire software fuori supporto e rispettare i termini del piano di patching. |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `technical_status` | non_compliant |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `thresholds_used_json` | {"evidence.ev-tirrena-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-tirrena-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 07719946-df9e-5c56-8839-4d2b76b06b4d (`07719946-df9e-5c56-8839-4d2b76b06b4d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `confidence_level` | insufficient |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `control_id` | CTRL-PR-PS-02-E |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `decision_policy` | all_required |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-02-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `errors` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `evidence_ids` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `governance_status` | none |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `id` | df584b2a-0168-53e1-a18e-da04a2b8d48d |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `information_actions` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `known_violations` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `missing_information` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `nis_profile` | important |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `requirement_id` | REQ-PR-PS-02-E |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `rule_id` | RULE-PR-PS-02-E |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `technical_status` | not_applicable |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `thresholds_used_json` | {} |
| Esiti della valutazione | df584b2a-0168-53e1-a18e-da04a2b8d48d (`df584b2a-0168-53e1-a18e-da04a2b8d48d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `acn_point` | PR.PS-03 |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `confidence_level` | insufficient |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `conflicting_information` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `control_id` | CTRL-PR-PS-03-E |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `decision_policy` | all_required |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `errors` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `evidence_ids` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `governance_status` | none |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `id` | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `information_actions` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `known_violations` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `missing_information` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `nis_profile` | important |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `requirement_id` | REQ-PR-PS-03-E |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `rule_id` | RULE-PR-PS-03-E |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `selector_decisions` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `technical_remediations` | nessuna |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `technical_status` | not_applicable |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `thresholds_used_json` | {} |
| Esiti della valutazione | fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26 (`fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `acn_point` | PR.PS-04 |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `confidence_level` | low |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `control_id` | CTRL-PR-PS-04 |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `decision_policy` | all_required |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-log"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.admin_remote_access_logging", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.logs_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": false, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.logs_centralized", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.log_retention_within_plan", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-log.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `errors` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.admin_remote_access_logging", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.logs_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": false, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "asset.logs_centralized", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.log_retention_within_plan", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `evidence_ids` | ev-tirrena-log |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `governance_status` | none |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `id` | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `information_actions` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `known_violations` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `missing_information` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `nis_profile` | important |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `requirement_id` | REQ-PR-PS-04 |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `rule_id` | RULE-PR-PS-04 |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `technical_status` | compliant |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `thresholds_used_json` | {"evidence.ev-tirrena-log.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 1acfe9c1-4f51-506f-af58-a0f757a2d0bf (`1acfe9c1-4f51-506f-af58-a0f757a2d0bf`) | `verification_mode` | direct_technical |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `acn_point` | PR.IR-01 |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `confidence_level` | low |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `control_id` | CTRL-PR-IR-01 |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `decision_policy` | all_required |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-network"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.remote_access_registry_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.remote_access_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.firewall_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-IR-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-network.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `errors` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.remote_access_registry_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.remote_access_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.firewall_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `evidence_ids` | ev-tirrena-network |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `governance_status` | none |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `id` | b59021f7-343c-5906-9d16-e0a8099d5d59 |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `information_actions` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `known_violations` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `missing_information` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `nis_profile` | important |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `requirement_id` | REQ-PR-IR-01 |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `rule_id` | RULE-PR-IR-01 |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `technical_status` | compliant |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `thresholds_used_json` | {"evidence.ev-tirrena-network.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | b59021f7-343c-5906-9d16-e0a8099d5d59 (`b59021f7-343c-5906-9d16-e0a8099d5d59`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `acn_point` | PR.IR-03 |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `confidence_level` | insufficient |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `control_id` | CTRL-PR-IR-03-E |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `decision_policy` | all_required |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-IR-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `errors` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `governance_status` | none |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `id` | 5226b494-6d6b-582d-a360-466cccf3a174 |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `information_actions` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `known_violations` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `missing_information` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `nis_profile` | important |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `requirement_id` | REQ-PR-IR-03-E |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `rule_id` | RULE-PR-IR-03-E |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `technical_status` | not_applicable |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 5226b494-6d6b-582d-a360-466cccf3a174 (`5226b494-6d6b-582d-a360-466cccf3a174`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `confidence_level` | high |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `conflicting_information` | nessuna |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `control_id` | CTRL-DE-CM-01 |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `decision_policy` | all_required |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-monitoring"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-ids.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-ids.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-tirrena-ids.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-DE-CM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "non_compliant", "thresholds": {"evidence.ev-tirrena-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `errors` | nessuna |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-ids.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-ids.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": false, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": false, "path": "SecurityCapability.cap-tirrena-ids.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `evidence_ids` | ev-tirrena-monitoring |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `governance_status` | none |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `id` | e8204856-2ac4-5c65-a7ab-5b045b912409 |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `information_actions` | nessuna |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `known_violations_json` | [{"comparison": "true", "observed_value": false, "path": "SecurityCapability.cap-tirrena-ids.monitored", "remediation": "Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti."}] |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `missing_information` | nessuna |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `nis_profile` | important |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `reason` | È stato osservato uno scostamento tecnico rispetto alla regola. |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `recommendation` | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `requirement_id` | REQ-DE-CM-01 |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `rule_id` | RULE-DE-CM-01 |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `selector_decisions` | nessuna |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `technical_remediations` | Abilitare e monitorare le capacità di rilevamento e filtraggio pertinenti. |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `technical_status` | non_compliant |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `thresholds_used_json` | {"evidence.ev-tirrena-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | e8204856-2ac4-5c65-a7ab-5b045b912409 (`e8204856-2ac4-5c65-a7ab-5b045b912409`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `confidence_level` | insufficient |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `control_id` | CTRL-DE-CM-01-E |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `decision_policy` | all_required |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-DE-CM-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `errors` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `governance_status` | none |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `id` | 2d2f7129-a328-5048-9016-cea40115bbcd |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `information_actions` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `known_violations` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `missing_information` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `nis_profile` | important |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `requirement_id` | REQ-DE-CM-01-E |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `rule_id` | RULE-DE-CM-01-E |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `technical_status` | not_applicable |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 2d2f7129-a328-5048-9016-cea40115bbcd (`2d2f7129-a328-5048-9016-cea40115bbcd`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `acn_point` | DE.CM-09 |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `asset_id` | asset-tirrena-core |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `confidence_level` | high |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `control_id` | CTRL-DE-CM-09 |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `decision_policy` | all_required |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-tirrena-endpoint"], "asset_id": "asset-tirrena-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-DE-CM-09", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-tirrena-endpoint.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `errors` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-tirrena-endpoint.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `evidence_ids` | ev-tirrena-endpoint |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `governance_status` | none |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `id` | 89844673-034b-52ef-8f77-151499e8a739 |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `information_actions` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `known_violations` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `missing_information` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `nis_profile` | important |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `requirement_id` | REQ-DE-CM-09 |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `rule_id` | RULE-DE-CM-09 |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `technical_status` | compliant |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `thresholds_used_json` | {"evidence.ev-tirrena-endpoint.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 89844673-034b-52ef-8f77-151499e8a739 (`89844673-034b-52ef-8f77-151499e8a739`) | `verification_mode` | direct_technical |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `acn_point` | ID.AM-01 |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `confidence_level` | insufficient |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `conflicting_information` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `control_id` | CTRL-ID-AM-01 |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `decision_policy` | all_required |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `errors` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `evidence_ids` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `governance_status` | none |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `id` | dfd29122-ac86-5531-b455-0e6b077e9806 |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `information_actions` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `known_violations` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `missing_information` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `nis_profile` | important |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `requirement_id` | REQ-ID-AM-01 |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `rule_id` | RULE-ID-AM-01 |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `selector_decisions` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `technical_remediations` | nessuna |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `technical_status` | not_applicable |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `thresholds_used_json` | {} |
| Esiti della valutazione | dfd29122-ac86-5531-b455-0e6b077e9806 (`dfd29122-ac86-5531-b455-0e6b077e9806`) | `verification_mode` | direct_technical |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `acn_point` | ID.AM-02 |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `confidence_level` | insufficient |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `control_id` | CTRL-ID-AM-02 |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `decision_policy` | all_required |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `errors` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `evidence_ids` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `governance_status` | none |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `id` | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `information_actions` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `known_violations` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `missing_information` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `nis_profile` | important |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `requirement_id` | REQ-ID-AM-02 |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `rule_id` | RULE-ID-AM-02 |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `technical_status` | not_applicable |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `thresholds_used_json` | {} |
| Esiti della valutazione | b56bb304-afd8-5a42-a1d4-c3ce0746b3e8 (`b56bb304-afd8-5a42-a1d4-c3ce0746b3e8`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `acn_point` | ID.AM-03 |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `confidence_level` | insufficient |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `control_id` | CTRL-ID-AM-03-E |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `decision_policy` | all_required |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `errors` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `governance_status` | none |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `id` | 444cd16d-e3d2-5e06-a084-63404a068fd1 |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `information_actions` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `known_violations` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `missing_information` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `nis_profile` | important |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `requirement_id` | REQ-ID-AM-03-E |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `rule_id` | RULE-ID-AM-03-E |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `technical_status` | not_applicable |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 444cd16d-e3d2-5e06-a084-63404a068fd1 (`444cd16d-e3d2-5e06-a084-63404a068fd1`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `acn_point` | ID.AM-04 |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `confidence_level` | insufficient |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `control_id` | CTRL-ID-AM-04 |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `decision_policy` | all_required |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-AM-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `errors` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `governance_status` | none |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `id` | 2846f635-2869-574e-a89b-b819634d4033 |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `information_actions` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `known_violations` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `missing_information` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `nis_profile` | important |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `requirement_id` | REQ-ID-AM-04 |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `rule_id` | RULE-ID-AM-04 |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `technical_status` | not_applicable |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 2846f635-2869-574e-a89b-b819634d4033 (`2846f635-2869-574e-a89b-b819634d4033`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `confidence_level` | insufficient |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `control_id` | CTRL-ID-RA-01 |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `decision_policy` | all_required |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `errors` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `governance_status` | none |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `id` | c82878c6-83b2-51c1-97d1-452736ce5f5e |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `information_actions` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `known_violations` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `missing_information` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `nis_profile` | important |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `requirement_id` | REQ-ID-RA-01 |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `rule_id` | RULE-ID-RA-01 |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `technical_status` | not_applicable |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | c82878c6-83b2-51c1-97d1-452736ce5f5e (`c82878c6-83b2-51c1-97d1-452736ce5f5e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `confidence_level` | insufficient |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `control_id` | CTRL-ID-RA-01-E |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `decision_policy` | all_required |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `errors` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `governance_status` | none |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `id` | 775cb338-4ecd-57b7-8b28-0a3747e96dff |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `information_actions` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `known_violations` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `missing_information` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `nis_profile` | important |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `requirement_id` | REQ-ID-RA-01-E |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `rule_id` | RULE-ID-RA-01-E |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `technical_status` | not_applicable |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 775cb338-4ecd-57b7-8b28-0a3747e96dff (`775cb338-4ecd-57b7-8b28-0a3747e96dff`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `confidence_level` | insufficient |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `control_id` | CTRL-ID-RA-08 |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `decision_policy` | all_required |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-08", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `errors` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `governance_status` | none |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `id` | 7215db4f-2cc1-5729-b6ee-304925724a8f |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `information_actions` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `known_violations` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `missing_information` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `nis_profile` | important |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `requirement_id` | REQ-ID-RA-08 |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `rule_id` | RULE-ID-RA-08 |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `technical_status` | not_applicable |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 7215db4f-2cc1-5729-b6ee-304925724a8f (`7215db4f-2cc1-5729-b6ee-304925724a8f`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `confidence_level` | insufficient |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `control_id` | CTRL-ID-RA-08-E |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `decision_policy` | all_required |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-ID-RA-08-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `errors` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `governance_status` | none |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `id` | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `information_actions` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `known_violations` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `missing_information` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `nis_profile` | important |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `requirement_id` | REQ-ID-RA-08-E |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `rule_id` | RULE-ID-RA-08-E |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `technical_status` | not_applicable |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 0f4c28ea-e292-573b-93e4-c8f0207cebf8 (`0f4c28ea-e292-573b-93e4-c8f0207cebf8`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `acn_point` | PR.AA-01 |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `confidence_level` | insufficient |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `conflicting_information` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `control_id` | CTRL-PR-AA-01 |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `decision_policy` | all_required |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `errors` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `evidence_ids` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `governance_status` | none |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `id` | c0f62629-f4d2-59fb-abcd-b206a2513520 |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `information_actions` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `known_violations` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `missing_information` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `nis_profile` | important |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `requirement_id` | REQ-PR-AA-01 |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `rule_id` | RULE-PR-AA-01 |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `selector_decisions` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `technical_remediations` | nessuna |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `technical_status` | not_applicable |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `thresholds_used_json` | {} |
| Esiti della valutazione | c0f62629-f4d2-59fb-abcd-b206a2513520 (`c0f62629-f4d2-59fb-abcd-b206a2513520`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `acn_point` | PR.AA-03 |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `confidence_level` | insufficient |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `control_id` | CTRL-PR-AA-03 |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `decision_policy` | all_required |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-03", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `errors` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `governance_status` | none |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `id` | 1aa8b496-67e8-5900-b5bf-188efb671504 |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `information_actions` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `known_violations` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `missing_information` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `nis_profile` | important |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `requirement_id` | REQ-PR-AA-03 |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `rule_id` | RULE-PR-AA-03 |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `technical_status` | not_applicable |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 1aa8b496-67e8-5900-b5bf-188efb671504 (`1aa8b496-67e8-5900-b5bf-188efb671504`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `acn_point` | PR.AA-05 |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `confidence_level` | insufficient |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `control_id` | CTRL-PR-AA-05 |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `decision_policy` | all_required |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-05", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `errors` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `governance_status` | none |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `id` | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `information_actions` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `known_violations` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `missing_information` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `nis_profile` | important |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `requirement_id` | REQ-PR-AA-05 |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `rule_id` | RULE-PR-AA-05 |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `technical_status` | not_applicable |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 65c49e4d-e897-54d0-9231-394c3f2f9fb8 (`65c49e4d-e897-54d0-9231-394c3f2f9fb8`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `acn_point` | PR.AA-06 |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `confidence_level` | insufficient |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `control_id` | CTRL-PR-AA-06 |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `decision_policy` | all_required |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-AA-06", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `errors` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `governance_status` | none |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `id` | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `information_actions` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `known_violations` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `missing_information` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `nis_profile` | important |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `requirement_id` | REQ-PR-AA-06 |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `rule_id` | RULE-PR-AA-06 |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `technical_status` | not_applicable |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 43b5335f-0ff6-52cb-ba27-4d4f63637fb2 (`43b5335f-0ff6-52cb-ba27-4d4f63637fb2`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `acn_point` | PR.DS-01 |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `confidence_level` | insufficient |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `conflicting_information` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `control_id` | CTRL-PR-DS-01 |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `decision_policy` | all_required |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `errors` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `evidence_ids` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `governance_status` | none |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `id` | cc2b6b47-b917-5a5f-b2a2-826611be3f99 |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `information_actions` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `known_violations` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `missing_information` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `nis_profile` | important |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `requirement_id` | REQ-PR-DS-01 |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `rule_id` | RULE-PR-DS-01 |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `selector_decisions` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `technical_remediations` | nessuna |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `technical_status` | not_applicable |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `thresholds_used_json` | {} |
| Esiti della valutazione | cc2b6b47-b917-5a5f-b2a2-826611be3f99 (`cc2b6b47-b917-5a5f-b2a2-826611be3f99`) | `verification_mode` | direct_technical |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `acn_point` | PR.DS-02 |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `confidence_level` | insufficient |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `control_id` | CTRL-PR-DS-02 |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `decision_policy` | all_required |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {"origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `errors` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `evidence_ids` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `governance_status` | none |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `id` | a841b157-eb08-5805-8877-eb9dc5075e55 |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `information_actions` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `known_violations` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `missing_information` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `nis_profile` | important |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `requirement_id` | REQ-PR-DS-02 |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `rule_id` | RULE-PR-DS-02 |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `technical_status` | not_applicable |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `thresholds_used_json` | {"origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}} |
| Esiti della valutazione | a841b157-eb08-5805-8877-eb9dc5075e55 (`a841b157-eb08-5805-8877-eb9dc5075e55`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `confidence_level` | insufficient |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `control_id` | CTRL-PR-DS-11 |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `decision_policy` | all_required |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-11", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `errors` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `governance_status` | none |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `id` | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `information_actions` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `known_violations` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `missing_information` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `nis_profile` | important |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `requirement_id` | REQ-PR-DS-11 |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `rule_id` | RULE-PR-DS-11 |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `technical_status` | not_applicable |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 9dadd369-6053-5ef2-9ee0-e3b2417f08d1 (`9dadd369-6053-5ef2-9ee0-e3b2417f08d1`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `confidence_level` | insufficient |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `control_id` | CTRL-PR-DS-11-E |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `decision_policy` | all_required |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-DS-11-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `errors` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `governance_status` | none |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `id` | 2bea3c87-21c8-5ca1-b452-245417ddf30b |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `information_actions` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `known_violations` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `missing_information` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `nis_profile` | important |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `requirement_id` | REQ-PR-DS-11-E |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `rule_id` | RULE-PR-DS-11-E |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `technical_status` | not_applicable |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 2bea3c87-21c8-5ca1-b452-245417ddf30b (`2bea3c87-21c8-5ca1-b452-245417ddf30b`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `acn_point` | PR.PS-01 |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `confidence_level` | insufficient |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `control_id` | CTRL-PR-PS-01-E |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `decision_policy` | all_required |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `errors` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `governance_status` | none |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `id` | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `information_actions` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `known_violations` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `missing_information` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `nis_profile` | important |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `requirement_id` | REQ-PR-PS-01-E |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `rule_id` | RULE-PR-PS-01-E |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `technical_status` | not_applicable |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 7ef5d4b1-d7b8-5614-867f-766a93d42e13 (`7ef5d4b1-d7b8-5614-867f-766a93d42e13`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `confidence_level` | insufficient |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `control_id` | CTRL-PR-PS-02 |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `decision_policy` | all_required |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `errors` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `governance_status` | none |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `id` | 199820e3-4364-5646-9ae7-2a5a33dcd44a |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `information_actions` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `known_violations` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `missing_information` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `nis_profile` | important |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `requirement_id` | REQ-PR-PS-02 |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `rule_id` | RULE-PR-PS-02 |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `technical_status` | not_applicable |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 199820e3-4364-5646-9ae7-2a5a33dcd44a (`199820e3-4364-5646-9ae7-2a5a33dcd44a`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `confidence_level` | insufficient |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `control_id` | CTRL-PR-PS-02-E |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `decision_policy` | all_required |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-02-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `errors` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `governance_status` | none |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `id` | 1a2603fe-fd55-5cdb-b205-b377ebe541da |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `information_actions` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `known_violations` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `missing_information` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `nis_profile` | important |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `requirement_id` | REQ-PR-PS-02-E |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `rule_id` | RULE-PR-PS-02-E |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `technical_status` | not_applicable |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 1a2603fe-fd55-5cdb-b205-b377ebe541da (`1a2603fe-fd55-5cdb-b205-b377ebe541da`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `acn_point` | PR.PS-03 |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `confidence_level` | insufficient |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `control_id` | CTRL-PR-PS-03-E |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `decision_policy` | all_required |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `errors` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `governance_status` | none |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `id` | 8be78386-a273-5b24-81ea-93ec9e49b14b |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `information_actions` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `known_violations` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `missing_information` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `nis_profile` | important |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `requirement_id` | REQ-PR-PS-03-E |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `rule_id` | RULE-PR-PS-03-E |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `technical_status` | not_applicable |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 8be78386-a273-5b24-81ea-93ec9e49b14b (`8be78386-a273-5b24-81ea-93ec9e49b14b`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `acn_point` | PR.PS-04 |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `confidence_level` | insufficient |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `control_id` | CTRL-PR-PS-04 |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `decision_policy` | all_required |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-PS-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `errors` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `governance_status` | none |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `id` | 8f942f3d-9a51-589c-bd85-2ff86478a85f |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `information_actions` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `known_violations` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `missing_information` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `nis_profile` | important |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `requirement_id` | REQ-PR-PS-04 |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `rule_id` | RULE-PR-PS-04 |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `technical_status` | not_applicable |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 8f942f3d-9a51-589c-bd85-2ff86478a85f (`8f942f3d-9a51-589c-bd85-2ff86478a85f`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `acn_point` | PR.IR-01 |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `confidence_level` | insufficient |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `control_id` | CTRL-PR-IR-01 |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `decision_policy` | all_required |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-IR-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `errors` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `governance_status` | none |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `id` | 472471bf-6a43-5150-a52b-0932e01f9507 |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `information_actions` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `known_violations` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `missing_information` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `nis_profile` | important |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `requirement_id` | REQ-PR-IR-01 |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `rule_id` | RULE-PR-IR-01 |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `technical_status` | not_applicable |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 472471bf-6a43-5150-a52b-0932e01f9507 (`472471bf-6a43-5150-a52b-0932e01f9507`) | `verification_mode` | direct_technical |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `acn_point` | PR.IR-03 |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `confidence_level` | insufficient |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `conflicting_information` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `control_id` | CTRL-PR-IR-03-E |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `decision_policy` | all_required |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-PR-IR-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `errors` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `evidence_ids` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `governance_status` | none |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `id` | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `information_actions` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `known_violations` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `missing_information` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `nis_profile` | important |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `requirement_id` | REQ-PR-IR-03-E |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `rule_id` | RULE-PR-IR-03-E |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `selector_decisions` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `technical_remediations` | nessuna |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `technical_status` | not_applicable |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `thresholds_used_json` | {} |
| Esiti della valutazione | c06f3fa7-decb-5b9c-a7b1-97ca87007e60 (`c06f3fa7-decb-5b9c-a7b1-97ca87007e60`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `confidence_level` | insufficient |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `control_id` | CTRL-DE-CM-01 |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `decision_policy` | all_required |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-DE-CM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `errors` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `governance_status` | none |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `id` | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `information_actions` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `known_violations` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `missing_information` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `nis_profile` | important |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `requirement_id` | REQ-DE-CM-01 |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `rule_id` | RULE-DE-CM-01 |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `technical_status` | not_applicable |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 4225fae1-3054-5829-9cfa-cb3ab5fe8233 (`4225fae1-3054-5829-9cfa-cb3ab5fe8233`) | `verification_mode` | direct_technical |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `confidence_level` | insufficient |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `control_id` | CTRL-DE-CM-01-E |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `decision_policy` | all_required |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-DE-CM-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `errors` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `evidence_ids` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `governance_status` | none |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `id` | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `information_actions` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `known_violations` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `missing_information` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `nis_profile` | important |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `reason` | regola esclusa dal profilo ACN important |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `requirement_id` | REQ-DE-CM-01-E |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `rule_id` | RULE-DE-CM-01-E |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `technical_status` | not_applicable |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `thresholds_used_json` | {} |
| Esiti della valutazione | ac6b7338-3a9f-5363-aedc-b55a5ffb64a8 (`ac6b7338-3a9f-5363-aedc-b55a5ffb64a8`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `acn_point` | DE.CM-09 |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `assessment_id` | scenario-tirrena-important-mixed |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `asset_id` | asset-tirrena-aux |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `confidence_level` | insufficient |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `control_id` | CTRL-DE-CM-09 |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `decision_policy` | all_required |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-tirrena-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "important", "rule_id": "RULE-DE-CM-09", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `errors` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `governance_status` | none |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `id` | 2f4db68d-32de-5697-955a-ac141a53e05e |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `information_actions` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `known_violations` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `missing_information` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `nis_profile` | important |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `requirement_id` | REQ-DE-CM-09 |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `rule_id` | RULE-DE-CM-09 |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `technical_status` | not_applicable |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 2f4db68d-32de-5697-955a-ac141a53e05e (`2f4db68d-32de-5697-955a-ac141a53e05e`) | `verification_mode` | direct_technical |

## Inventario completo delle relazioni

| Nodo di partenza | Relazione | Nodo di arrivo |
|---|---|---|
| `asset-tirrena-core` | espone (`EXPOSES`) | `svc-tirrena-https` |
| `asset-tirrena-core` | tratta (`PROCESSES`) | `data-tirrena-core` |
| `asset-tirrena-core` | è gestito da (`MANAGED_BY`) | `owner-tirrena-ops` |
| `vuln-tirrena-001` | interessa (`AFFECTS`) | `asset-tirrena-core` |
| `asset-tirrena-core` | è protetto da (`PROTECTED_BY`) | `cap-tirrena-endpoint` |
| `proc-tirrena-core` | dipende da (`DEPENDS_ON`) | `asset-tirrena-core` |
| `dataset-tirrena-normalized-2026` | descrive (`DESCRIBES`) | `org-tirrena` |
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
| `a44647f2-4f8e-56ef-8682-31e0ad08e8e8` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `a44647f2-4f8e-56ef-8682-31e0ad08e8e8` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-01` |
| `a44647f2-4f8e-56ef-8682-31e0ad08e8e8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-01` |
| `a44647f2-4f8e-56ef-8682-31e0ad08e8e8` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-01` |
| `55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-02` |
| `55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-02` |
| `55a9c7f2-8c32-5cdd-8ed4-389bbe336bb9` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-02` |
| `be815e68-0a0f-581e-9f74-364b6a8847ad` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `be815e68-0a0f-581e-9f74-364b6a8847ad` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-03-E` |
| `be815e68-0a0f-581e-9f74-364b6a8847ad` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-03-E` |
| `be815e68-0a0f-581e-9f74-364b6a8847ad` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-03-E` |
| `a70a78ab-5a03-5642-a8c5-a57866f5821c` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `a70a78ab-5a03-5642-a8c5-a57866f5821c` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-04` |
| `a70a78ab-5a03-5642-a8c5-a57866f5821c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-04` |
| `a70a78ab-5a03-5642-a8c5-a57866f5821c` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-04` |
| `2d9abb01-0ddf-5142-b5ab-7cb86875b224` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `2d9abb01-0ddf-5142-b5ab-7cb86875b224` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01` |
| `2d9abb01-0ddf-5142-b5ab-7cb86875b224` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01` |
| `2d9abb01-0ddf-5142-b5ab-7cb86875b224` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01` |
| `f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01-E` |
| `f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01-E` |
| `f67afb34-d1ed-5a2e-ac8b-3e9e0c7c3e84` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01-E` |
| `eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08` |
| `eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08` |
| `eeca2b0d-b8fe-5e8f-9329-9f4e4b151a0b` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08` |
| `205a77ed-ada0-5e9c-8557-d4ea0017b903` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `205a77ed-ada0-5e9c-8557-d4ea0017b903` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08-E` |
| `205a77ed-ada0-5e9c-8557-d4ea0017b903` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08-E` |
| `205a77ed-ada0-5e9c-8557-d4ea0017b903` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08-E` |
| `fa454414-a9e2-535c-9497-9ac4415bc59c` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `fa454414-a9e2-535c-9497-9ac4415bc59c` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-01` |
| `fa454414-a9e2-535c-9497-9ac4415bc59c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-01` |
| `fa454414-a9e2-535c-9497-9ac4415bc59c` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-01` |
| `8e46657c-f989-5b2c-b588-26c8c32d158f` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `8e46657c-f989-5b2c-b588-26c8c32d158f` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-03` |
| `8e46657c-f989-5b2c-b588-26c8c32d158f` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-03` |
| `8e46657c-f989-5b2c-b588-26c8c32d158f` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-03` |
| `2b1955d6-62a0-517e-97c4-f990424bb297` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `2b1955d6-62a0-517e-97c4-f990424bb297` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-05` |
| `2b1955d6-62a0-517e-97c4-f990424bb297` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-05` |
| `2b1955d6-62a0-517e-97c4-f990424bb297` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-05` |
| `559b88af-ecc6-5668-aa4f-d19a04fe3485` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `559b88af-ecc6-5668-aa4f-d19a04fe3485` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-06` |
| `559b88af-ecc6-5668-aa4f-d19a04fe3485` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-06` |
| `559b88af-ecc6-5668-aa4f-d19a04fe3485` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-06` |
| `7ba70886-b3b0-58d8-a187-ef463799b3f3` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `7ba70886-b3b0-58d8-a187-ef463799b3f3` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-01` |
| `7ba70886-b3b0-58d8-a187-ef463799b3f3` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-01` |
| `7ba70886-b3b0-58d8-a187-ef463799b3f3` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-01` |
| `00bf1516-3e72-53ac-8911-d7382db61447` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `00bf1516-3e72-53ac-8911-d7382db61447` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-02` |
| `00bf1516-3e72-53ac-8911-d7382db61447` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-02` |
| `00bf1516-3e72-53ac-8911-d7382db61447` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-02` |
| `8a0156bc-de29-5ad4-bf70-42f3514870c5` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `8a0156bc-de29-5ad4-bf70-42f3514870c5` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11` |
| `8a0156bc-de29-5ad4-bf70-42f3514870c5` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11` |
| `8a0156bc-de29-5ad4-bf70-42f3514870c5` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11` |
| `731cc9c5-9524-5890-a2b1-566fea73fa0e` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `731cc9c5-9524-5890-a2b1-566fea73fa0e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11-E` |
| `731cc9c5-9524-5890-a2b1-566fea73fa0e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11-E` |
| `731cc9c5-9524-5890-a2b1-566fea73fa0e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11-E` |
| `eda26dfc-17ea-5e61-a4bb-154399162614` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `eda26dfc-17ea-5e61-a4bb-154399162614` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-01-E` |
| `eda26dfc-17ea-5e61-a4bb-154399162614` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-01-E` |
| `eda26dfc-17ea-5e61-a4bb-154399162614` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-01-E` |
| `07719946-df9e-5c56-8839-4d2b76b06b4d` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `07719946-df9e-5c56-8839-4d2b76b06b4d` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02` |
| `07719946-df9e-5c56-8839-4d2b76b06b4d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02` |
| `07719946-df9e-5c56-8839-4d2b76b06b4d` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02` |
| `df584b2a-0168-53e1-a18e-da04a2b8d48d` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `df584b2a-0168-53e1-a18e-da04a2b8d48d` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02-E` |
| `df584b2a-0168-53e1-a18e-da04a2b8d48d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02-E` |
| `df584b2a-0168-53e1-a18e-da04a2b8d48d` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02-E` |
| `fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-03-E` |
| `fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-03-E` |
| `fc42a4fe-51c9-5fa6-b1e5-bbaf6fa39f26` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-03-E` |
| `1acfe9c1-4f51-506f-af58-a0f757a2d0bf` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `1acfe9c1-4f51-506f-af58-a0f757a2d0bf` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-04` |
| `1acfe9c1-4f51-506f-af58-a0f757a2d0bf` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-04` |
| `1acfe9c1-4f51-506f-af58-a0f757a2d0bf` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-04` |
| `b59021f7-343c-5906-9d16-e0a8099d5d59` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `b59021f7-343c-5906-9d16-e0a8099d5d59` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-01` |
| `b59021f7-343c-5906-9d16-e0a8099d5d59` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-01` |
| `b59021f7-343c-5906-9d16-e0a8099d5d59` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-01` |
| `5226b494-6d6b-582d-a360-466cccf3a174` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `5226b494-6d6b-582d-a360-466cccf3a174` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-03-E` |
| `5226b494-6d6b-582d-a360-466cccf3a174` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-03-E` |
| `5226b494-6d6b-582d-a360-466cccf3a174` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-03-E` |
| `e8204856-2ac4-5c65-a7ab-5b045b912409` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `e8204856-2ac4-5c65-a7ab-5b045b912409` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01` |
| `e8204856-2ac4-5c65-a7ab-5b045b912409` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01` |
| `e8204856-2ac4-5c65-a7ab-5b045b912409` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01` |
| `2d2f7129-a328-5048-9016-cea40115bbcd` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `2d2f7129-a328-5048-9016-cea40115bbcd` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01-E` |
| `2d2f7129-a328-5048-9016-cea40115bbcd` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01-E` |
| `2d2f7129-a328-5048-9016-cea40115bbcd` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01-E` |
| `89844673-034b-52ef-8f77-151499e8a739` | valuta (`EVALUATES`) | `asset-tirrena-core` |
| `89844673-034b-52ef-8f77-151499e8a739` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-09` |
| `89844673-034b-52ef-8f77-151499e8a739` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-09` |
| `89844673-034b-52ef-8f77-151499e8a739` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-09` |
| `dfd29122-ac86-5531-b455-0e6b077e9806` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `dfd29122-ac86-5531-b455-0e6b077e9806` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-01` |
| `dfd29122-ac86-5531-b455-0e6b077e9806` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-01` |
| `dfd29122-ac86-5531-b455-0e6b077e9806` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-01` |
| `b56bb304-afd8-5a42-a1d4-c3ce0746b3e8` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `b56bb304-afd8-5a42-a1d4-c3ce0746b3e8` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-02` |
| `b56bb304-afd8-5a42-a1d4-c3ce0746b3e8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-02` |
| `b56bb304-afd8-5a42-a1d4-c3ce0746b3e8` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-02` |
| `444cd16d-e3d2-5e06-a084-63404a068fd1` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `444cd16d-e3d2-5e06-a084-63404a068fd1` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-03-E` |
| `444cd16d-e3d2-5e06-a084-63404a068fd1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-03-E` |
| `444cd16d-e3d2-5e06-a084-63404a068fd1` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-03-E` |
| `2846f635-2869-574e-a89b-b819634d4033` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `2846f635-2869-574e-a89b-b819634d4033` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-04` |
| `2846f635-2869-574e-a89b-b819634d4033` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-04` |
| `2846f635-2869-574e-a89b-b819634d4033` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-04` |
| `c82878c6-83b2-51c1-97d1-452736ce5f5e` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `c82878c6-83b2-51c1-97d1-452736ce5f5e` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01` |
| `c82878c6-83b2-51c1-97d1-452736ce5f5e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01` |
| `c82878c6-83b2-51c1-97d1-452736ce5f5e` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01` |
| `775cb338-4ecd-57b7-8b28-0a3747e96dff` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `775cb338-4ecd-57b7-8b28-0a3747e96dff` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01-E` |
| `775cb338-4ecd-57b7-8b28-0a3747e96dff` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01-E` |
| `775cb338-4ecd-57b7-8b28-0a3747e96dff` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01-E` |
| `7215db4f-2cc1-5729-b6ee-304925724a8f` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `7215db4f-2cc1-5729-b6ee-304925724a8f` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08` |
| `7215db4f-2cc1-5729-b6ee-304925724a8f` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08` |
| `7215db4f-2cc1-5729-b6ee-304925724a8f` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08` |
| `0f4c28ea-e292-573b-93e4-c8f0207cebf8` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `0f4c28ea-e292-573b-93e4-c8f0207cebf8` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08-E` |
| `0f4c28ea-e292-573b-93e4-c8f0207cebf8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08-E` |
| `0f4c28ea-e292-573b-93e4-c8f0207cebf8` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08-E` |
| `c0f62629-f4d2-59fb-abcd-b206a2513520` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `c0f62629-f4d2-59fb-abcd-b206a2513520` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-01` |
| `c0f62629-f4d2-59fb-abcd-b206a2513520` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-01` |
| `c0f62629-f4d2-59fb-abcd-b206a2513520` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-01` |
| `1aa8b496-67e8-5900-b5bf-188efb671504` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `1aa8b496-67e8-5900-b5bf-188efb671504` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-03` |
| `1aa8b496-67e8-5900-b5bf-188efb671504` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-03` |
| `1aa8b496-67e8-5900-b5bf-188efb671504` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-03` |
| `65c49e4d-e897-54d0-9231-394c3f2f9fb8` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `65c49e4d-e897-54d0-9231-394c3f2f9fb8` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-05` |
| `65c49e4d-e897-54d0-9231-394c3f2f9fb8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-05` |
| `65c49e4d-e897-54d0-9231-394c3f2f9fb8` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-05` |
| `43b5335f-0ff6-52cb-ba27-4d4f63637fb2` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `43b5335f-0ff6-52cb-ba27-4d4f63637fb2` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-06` |
| `43b5335f-0ff6-52cb-ba27-4d4f63637fb2` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-06` |
| `43b5335f-0ff6-52cb-ba27-4d4f63637fb2` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-06` |
| `cc2b6b47-b917-5a5f-b2a2-826611be3f99` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `cc2b6b47-b917-5a5f-b2a2-826611be3f99` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-01` |
| `cc2b6b47-b917-5a5f-b2a2-826611be3f99` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-01` |
| `cc2b6b47-b917-5a5f-b2a2-826611be3f99` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-01` |
| `a841b157-eb08-5805-8877-eb9dc5075e55` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `a841b157-eb08-5805-8877-eb9dc5075e55` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-02` |
| `a841b157-eb08-5805-8877-eb9dc5075e55` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-02` |
| `a841b157-eb08-5805-8877-eb9dc5075e55` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-02` |
| `9dadd369-6053-5ef2-9ee0-e3b2417f08d1` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `9dadd369-6053-5ef2-9ee0-e3b2417f08d1` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11` |
| `9dadd369-6053-5ef2-9ee0-e3b2417f08d1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11` |
| `9dadd369-6053-5ef2-9ee0-e3b2417f08d1` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11` |
| `2bea3c87-21c8-5ca1-b452-245417ddf30b` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `2bea3c87-21c8-5ca1-b452-245417ddf30b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11-E` |
| `2bea3c87-21c8-5ca1-b452-245417ddf30b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11-E` |
| `2bea3c87-21c8-5ca1-b452-245417ddf30b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11-E` |
| `7ef5d4b1-d7b8-5614-867f-766a93d42e13` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `7ef5d4b1-d7b8-5614-867f-766a93d42e13` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-01-E` |
| `7ef5d4b1-d7b8-5614-867f-766a93d42e13` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-01-E` |
| `7ef5d4b1-d7b8-5614-867f-766a93d42e13` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-01-E` |
| `199820e3-4364-5646-9ae7-2a5a33dcd44a` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `199820e3-4364-5646-9ae7-2a5a33dcd44a` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02` |
| `199820e3-4364-5646-9ae7-2a5a33dcd44a` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02` |
| `199820e3-4364-5646-9ae7-2a5a33dcd44a` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02` |
| `1a2603fe-fd55-5cdb-b205-b377ebe541da` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `1a2603fe-fd55-5cdb-b205-b377ebe541da` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02-E` |
| `1a2603fe-fd55-5cdb-b205-b377ebe541da` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02-E` |
| `1a2603fe-fd55-5cdb-b205-b377ebe541da` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02-E` |
| `8be78386-a273-5b24-81ea-93ec9e49b14b` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `8be78386-a273-5b24-81ea-93ec9e49b14b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-03-E` |
| `8be78386-a273-5b24-81ea-93ec9e49b14b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-03-E` |
| `8be78386-a273-5b24-81ea-93ec9e49b14b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-03-E` |
| `8f942f3d-9a51-589c-bd85-2ff86478a85f` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `8f942f3d-9a51-589c-bd85-2ff86478a85f` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-04` |
| `8f942f3d-9a51-589c-bd85-2ff86478a85f` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-04` |
| `8f942f3d-9a51-589c-bd85-2ff86478a85f` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-04` |
| `472471bf-6a43-5150-a52b-0932e01f9507` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `472471bf-6a43-5150-a52b-0932e01f9507` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-01` |
| `472471bf-6a43-5150-a52b-0932e01f9507` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-01` |
| `472471bf-6a43-5150-a52b-0932e01f9507` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-01` |
| `c06f3fa7-decb-5b9c-a7b1-97ca87007e60` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `c06f3fa7-decb-5b9c-a7b1-97ca87007e60` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-03-E` |
| `c06f3fa7-decb-5b9c-a7b1-97ca87007e60` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-03-E` |
| `c06f3fa7-decb-5b9c-a7b1-97ca87007e60` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-03-E` |
| `4225fae1-3054-5829-9cfa-cb3ab5fe8233` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `4225fae1-3054-5829-9cfa-cb3ab5fe8233` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01` |
| `4225fae1-3054-5829-9cfa-cb3ab5fe8233` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01` |
| `4225fae1-3054-5829-9cfa-cb3ab5fe8233` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01` |
| `ac6b7338-3a9f-5363-aedc-b55a5ffb64a8` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `ac6b7338-3a9f-5363-aedc-b55a5ffb64a8` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01-E` |
| `ac6b7338-3a9f-5363-aedc-b55a5ffb64a8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01-E` |
| `ac6b7338-3a9f-5363-aedc-b55a5ffb64a8` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01-E` |
| `2f4db68d-32de-5697-955a-ac141a53e05e` | valuta (`EVALUATES`) | `asset-tirrena-aux` |
| `2f4db68d-32de-5697-955a-ac141a53e05e` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-09` |
| `2f4db68d-32de-5697-955a-ac141a53e05e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-09` |
| `2f4db68d-32de-5697-955a-ac141a53e05e` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-09` |
