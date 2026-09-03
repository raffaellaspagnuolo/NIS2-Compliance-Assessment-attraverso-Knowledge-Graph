# Knowledge Graph completo — assessment `scenario-aurora-essential-mature`

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
    nodo1["Dataset<br/>Ambiente normalizzato - Aurora Salute"]
    class nodo1 context
    nodo2["Organizzazione<br/>Aurora Salute S.p.A."]
    class nodo2 context
    nodo3["Responsabili<br/>Responsabile Infrastrutture e Sicurezza"]
    class nodo3 context
    nodo4["Processi<br/>Servizio clinico digitale"]
    class nodo4 context
    nodo5["Categorie di dati<br/>Dati operativi sanitari sintetici"]
    class nodo5 context
    nodo6["Asset<br/>Core Clinical Gateway<br/>admin_remote_access_logging: True<br/>admin_remote_access_logging_observation_type: direct<br/>admin_remote_access_logging_observed_at: 2026-08-14T07:00:00Z<br/>admin_remote_access_logging_status: known<br/>anomaly_thresholds_configured: True<br/>anomaly_thresholds_configured_observation_type: direct<br/>anomaly_thresholds_configured_observed_at: 2026-08-14T07:00:00Z<br/>anomaly_thresholds_configured_status: known<br/>critical_software_supplier_channels_monitored: True<br/>critical_software_supplier_channels_monitored_observation_type: direct<br/>critical_software_supplier_channels_monitored_observed_at: 2026-08-14T05:00:00Z<br/>critical_software_supplier_channels_monitored_status: known<br/>exposure_level: high<br/>extended_vulnerability_assessment_performed: True<br/>extended_vulnerability_assessment_performed_observation_type: direct<br/>extended_vulnerability_assessment_performed_observed_at: 2026-08-14T05:00:00Z<br/>extended_vulnerability_assessment_performed_status: known<br/>firewall_enabled: True<br/>firewall_enabled_observation_type: direct<br/>firewall_enabled_observed_at: 2026-08-14T07:00:00Z<br/>firewall_enabled_status: known<br/>hardening_baseline_applied: True<br/>hardening_baseline_applied_observation_type: direct<br/>hardening_baseline_applied_observed_at: 2026-08-14T07:00:00Z<br/>hardening_baseline_applied_status: known<br/>hardware_inventory_complete: True<br/>hardware_inventory_complete_observation_type: evidence_based<br/>hardware_inventory_complete_observed_at: 2026-08-14T06:00:00Z<br/>hardware_inventory_complete_status: known<br/>impact_level: critical<br/>internet_exposed_observation_type: evidence_based<br/>internet_exposed_observed_at: 2026-08-14T06:00:00Z<br/>log_retention_within_plan: True<br/>log_retention_within_plan_observation_type: declared<br/>log_retention_within_plan_observed_at: 2026-08-10T09:00:00Z<br/>log_retention_within_plan_status: known<br/>logs_centralized: True<br/>logs_centralized_observation_type: direct<br/>logs_centralized_observed_at: 2026-08-14T07:00:00Z<br/>logs_centralized_status: known<br/>logs_protected: True<br/>logs_protected_observation_type: direct<br/>logs_protected_observed_at: 2026-08-14T07:00:00Z<br/>logs_protected_status: known<br/>maintenance_logged: True<br/>maintenance_logged_observation_type: direct<br/>maintenance_logged_observed_at: 2026-08-14T07:00:00Z<br/>maintenance_logged_status: known<br/>network_segment_observation_type: evidence_based<br/>network_segment_observed_at: 2026-08-14T06:00:00Z<br/>nis_relevant: True<br/>nis_relevant_observation_type: declared<br/>nis_relevant_observed_at: 2026-08-10T09:00:00Z<br/>nis_relevant_status: known<br/>operating_system: ExampleLinux<br/>operating_system_version: 12.4<br/>physical_protection_documented: True<br/>physical_protection_documented_observation_type: declared<br/>physical_protection_documented_observed_at: 2026-08-10T09:00:00Z<br/>physical_protection_documented_status: known<br/>provider_services_inventory_complete: True<br/>provider_services_inventory_complete_observation_type: declared<br/>provider_services_inventory_complete_observed_at: 2026-08-10T09:00:00Z<br/>provider_services_inventory_complete_status: known<br/>remote_access_protected: True<br/>remote_access_protected_observation_type: direct<br/>remote_access_protected_observed_at: 2026-08-14T07:00:00Z<br/>remote_access_protected_status: known<br/>remote_access_registry_complete: True<br/>remote_access_registry_complete_observation_type: declared<br/>remote_access_registry_complete_observed_at: 2026-08-10T09:00:00Z<br/>remote_access_registry_complete_status: known<br/>risk_assessment_reference: RISK-AURORA-2026-02<br/>secure_disposal_documented: True<br/>secure_disposal_documented_observation_type: declared<br/>secure_disposal_documented_observed_at: 2026-08-10T09:00:00Z<br/>secure_disposal_documented_status: known<br/>support_status: supported<br/>vulnerability_advisories_monitored: True<br/>vulnerability_advisories_monitored_observation_type: direct<br/>vulnerability_advisories_monitored_observed_at: 2026-08-14T05:00:00Z<br/>vulnerability_advisories_monitored_status: known"]
    class nodo6 context
    nodo7["Asset<br/>Sistema ausiliario fuori perimetro NIS<br/>exposure_level: low<br/>impact_level: medium<br/>internet_exposed_observation_type: evidence_based<br/>internet_exposed_observed_at: 2026-08-14T06:00:00Z<br/>network_segment_observation_type: evidence_based<br/>network_segment_observed_at: 2026-08-14T06:00:00Z<br/>nis_relevant: False<br/>nis_relevant_observation_type: declared<br/>nis_relevant_observed_at: 2026-08-10T09:00:00Z<br/>nis_relevant_status: known<br/>properties_json: {}<br/>risk_assessment_reference: RISK-AURORA-2026-02<br/>support_status: supported"]
    class nodo7 context
    nodo8["Servizi<br/>HTTPS"]
    class nodo8 context
    nodo9["Componenti software<br/>AuroraGateway"]
    class nodo9 context
    nodo10["Utenze<br/>account-aurora-admin"]
    class nodo10 context
    nodo11["Flussi di rete<br/>flow-aurora-https"]
    class nodo11 context
    nodo12["Backup<br/>backup-aurora-core"]
    class nodo12 context
    nodo13["Capacità di sicurezza<br/>cap-aurora-emergency"]
    class nodo13 context
    nodo14["Capacità di sicurezza<br/>cap-aurora-ids"]
    class nodo14 context
    nodo15["Capacità di sicurezza<br/>cap-aurora-filter"]
    class nodo15 context
    nodo16["Capacità di sicurezza<br/>cap-aurora-access-monitor"]
    class nodo16 context
    nodo17["Capacità di sicurezza<br/>cap-aurora-endpoint"]
    class nodo17 context
    nodo18["Vulnerabilità<br/>Dipendenza HTTP/2 aggiornata dopo advisory"]
    class nodo18 context
    nodo19["Evidenze<br/>Inventario asset<br/>evidence_type: asset_inventory<br/>source: CMDB<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo19 evidence
    nodo20["Evidenze<br/>Inventario software<br/>evidence_type: software_inventory<br/>source: CMDB<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo20 evidence
    nodo21["Evidenze<br/>Inventario flussi di rete<br/>evidence_type: network_flow_inventory<br/>source: network-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {}"]
    class nodo21 evidence
    nodo22["Evidenze<br/>Inventario servizi fornitori<br/>evidence_type: provider_service_inventory<br/>source: service-catalog<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: medium<br/>content_json: {}"]
    class nodo22 evidence
    nodo23["Evidenze<br/>Scansione vulnerabilità<br/>evidence_type: vulnerability_scan<br/>source: vulnerability-scanner<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'activity_description': 'Vulnerability assessment autenticato e riesame manuale.', 'cve': 'CVE-202…"]
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
    nodo30["Evidenze<br/>Registro backup<br/>evidence_type: backup_record<br/>source: backup-manager<br/>collected_at: 2026-08-14T08:00:00Z<br/>reliability: high<br/>content_json: {'plan_reference': 'BACKUP-AURORA-2026'}"]
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
    nodo131["Esiti della valutazione<br/>8cdb8a9a-4f57-56d5-a48c-b79c9b01e297<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo131 result
    nodo132["Esiti della valutazione<br/>134c76f6-829c-54f4-8a20-bb2658caed81<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'identificato', 'comparison_result': true, 'condition_origin': 'regulatory', 'manda…"]
    class nodo132 result
    nodo133["Esiti della valutazione<br/>b868dcad-1d71-59a7-bc03-919729465688<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'presente', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory…"]
    class nodo133 result
    nodo134["Esiti della valutazione<br/>b69beb1f-d755-507a-bf1e-cdc747b2f0b8<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo134 result
    nodo135["Esiti della valutazione<br/>ae8c53db-9242-5d62-a2b4-86acdf5a15a2<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo135 result
    nodo136["Esiti della valutazione<br/>cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo136 result
    nodo137["Esiti della valutazione<br/>9876425a-cf3f-5d29-b6ef-cc59cdeca1fa<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo137 result
    nodo138["Esiti della valutazione<br/>e0506187-5d20-5d37-b92e-6878f7cac413<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo138 result
    nodo139["Esiti della valutazione<br/>a284ba8d-6d80-587f-acaa-eb0379ad632b<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'presente', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory…"]
    class nodo139 result
    nodo140["Esiti della valutazione<br/>3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo140 result
    nodo141["Esiti della valutazione<br/>180002f3-6752-5c1c-9bbe-91390cea7fd0<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo141 result
    nodo142["Esiti della valutazione<br/>5cf3f0d9-2df6-5f07-9f92-a9faec0b094b<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo142 result
    nodo143["Esiti della valutazione<br/>8947f3c5-cb85-563e-9f24-2adf1e539e4d<br/>technical_status: not_verifiable<br/>governance_status: none<br/>reason: completezza dell'inventario DataObject non nota<br/>confidence_level: insufficient"]
    class nodo143 result
    nodo144["Esiti della valutazione<br/>47b74015-300c-5fe0-ba2c-a279fe186052<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo144 result
    nodo145["Esiti della valutazione<br/>12de80fb-56ee-5042-b16a-3ac3a4c2e501<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo145 result
    nodo146["Esiti della valutazione<br/>9e07e507-09bc-5865-a19e-04a17fa16143<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo146 result
    nodo147["Esiti della valutazione<br/>8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo147 result
    nodo148["Esiti della valutazione<br/>b75d1458-c10f-5e12-b482-68e71f582bea<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': '{supported}', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandat…"]
    class nodo148 result
    nodo149["Esiti della valutazione<br/>103ed1f8-5443-5e33-b62a-32584c36f36c<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: medium<br/>evaluated_facts_json: [{'comparison': '{supported}', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandat…"]
    class nodo149 result
    nodo150["Esiti della valutazione<br/>2e43323b-e825-5f6d-bc1c-60e6cf55914e<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo150 result
    nodo151["Esiti della valutazione<br/>0a6e22d2-0365-5bd8-b8b8-40a101f8859e<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo151 result
    nodo152["Esiti della valutazione<br/>fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: low<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo152 result
    nodo153["Esiti della valutazione<br/>93c7e862-d222-58c6-b6c9-ddab1bea53f5<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo153 result
    nodo154["Esiti della valutazione<br/>aebf7a65-8ae9-53e8-99f0-6101ff923150<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo154 result
    nodo155["Esiti della valutazione<br/>6aa51b0f-b1d1-5df1-953c-c3cbf3d26265<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'project_baseline', 'mandato…"]
    class nodo155 result
    nodo156["Esiti della valutazione<br/>31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d<br/>technical_status: compliant<br/>governance_status: none<br/>reason: Le condizioni tecniche osservabili della regola risultano soddisfatte.<br/>confidence_level: high<br/>evaluated_facts_json: [{'comparison': 'true', 'comparison_result': true, 'condition_origin': 'regulatory', 'mandatory': t…"]
    class nodo156 result
    nodo157["Esiti della valutazione<br/>308648b9-4ca8-5874-ac7b-8ba5f5193384<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo157 result
    nodo158["Esiti della valutazione<br/>80be57b7-7ffd-514f-9195-128b6b9867bf<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo158 result
    nodo159["Esiti della valutazione<br/>86f1f877-dfdf-5c1f-94da-00a58a5f4fcb<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo159 result
    nodo160["Esiti della valutazione<br/>6c7bf986-038c-52c6-888b-8dbde7b6d114<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo160 result
    nodo161["Esiti della valutazione<br/>74252cb9-8928-5299-8c80-e125b8fb2698<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo161 result
    nodo162["Esiti della valutazione<br/>18a5096f-546c-523f-9da7-193cfcf4f4c5<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo162 result
    nodo163["Esiti della valutazione<br/>7408e456-1ed0-5575-8f88-4aa8576dfb70<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo163 result
    nodo164["Esiti della valutazione<br/>84b86738-75ad-5f6b-be05-2b0a84330424<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo164 result
    nodo165["Esiti della valutazione<br/>ecb880e6-f066-5db5-9e45-19c39f04593e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo165 result
    nodo166["Esiti della valutazione<br/>c5826f34-a2c0-5401-97ee-bf161da61273<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo166 result
    nodo167["Esiti della valutazione<br/>9d835f2b-2713-536c-a708-140ca344a36d<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo167 result
    nodo168["Esiti della valutazione<br/>3fb46f9b-7911-5eec-a7ba-f5141f99454c<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo168 result
    nodo169["Esiti della valutazione<br/>a11123ce-ca57-57dc-abe8-b8407cd3338e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo169 result
    nodo170["Esiti della valutazione<br/>fd96f19d-c801-5696-89e0-9dc5fb3c8534<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo170 result
    nodo171["Esiti della valutazione<br/>5debe74a-081c-5201-92f5-19e36adcd669<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo171 result
    nodo172["Esiti della valutazione<br/>3bb222b7-d9da-53e3-953d-d000c0050ee1<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo172 result
    nodo173["Esiti della valutazione<br/>a7413ab8-be2d-5bec-ac74-09168480a66a<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo173 result
    nodo174["Esiti della valutazione<br/>76985295-4f44-5b93-8e6c-40a64c0178a2<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo174 result
    nodo175["Esiti della valutazione<br/>ebcce0de-43e9-54c1-b55f-b7a1dcd403d6<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo175 result
    nodo176["Esiti della valutazione<br/>1e029768-3489-5291-81ab-447b96090e2b<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo176 result
    nodo177["Esiti della valutazione<br/>64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo177 result
    nodo178["Esiti della valutazione<br/>ed93df21-89bc-51b3-8194-173e3056ad3e<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo178 result
    nodo179["Esiti della valutazione<br/>444dffd7-95ac-5ba0-b4d2-6a2632b64e30<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo179 result
    nodo180["Esiti della valutazione<br/>4ad2712b-657b-5004-8c35-81b4b3308911<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo180 result
    nodo181["Esiti della valutazione<br/>b5dbc921-ee11-5c0a-b358-09c6c6df7d35<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
    class nodo181 result
    nodo182["Esiti della valutazione<br/>2add08be-48c6-51ad-8e32-b9a7fa46f276<br/>technical_status: not_applicable<br/>governance_status: none<br/>reason: asset con rilevanza NIS nota e negativa<br/>confidence_level: insufficient"]
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
| Dataset | Ambiente normalizzato - Aurora Salute (`dataset-aurora-normalized-2026`) | `description` | Output sintetico dei Moduli 1 e 2 per un'organizzazione essenziale con elevata maturità tecnica e raccolta evidenze completa. Organizzazione, persone e prodotti sono inventati; i riferimenti CVE sono reali e associati a dipendenze sintetiche esclusivamente a scopo dimostrativo. |
| Dataset | Ambiente normalizzato - Aurora Salute (`dataset-aurora-normalized-2026`) | `generated_at` | 2026-08-15T11:37:00+02:00 |
| Dataset | Ambiente normalizzato - Aurora Salute (`dataset-aurora-normalized-2026`) | `id` | dataset-aurora-normalized-2026 |
| Dataset | Ambiente normalizzato - Aurora Salute (`dataset-aurora-normalized-2026`) | `name` | Ambiente normalizzato - Aurora Salute |
| Dataset | Ambiente normalizzato - Aurora Salute (`dataset-aurora-normalized-2026`) | `source_systems` | CMDB, vulnerability-manager, IAM, backup-manager, network-manager, monitoring-platform, configuration-manager |
| Organizzazione | Aurora Salute S.p.A. (`org-aurora`) | `acn_specification` | Determinazione ACN 379907/2025 - specifiche di base vigenti |
| Organizzazione | Aurora Salute S.p.A. (`org-aurora`) | `id` | org-aurora |
| Organizzazione | Aurora Salute S.p.A. (`org-aurora`) | `name` | Aurora Salute S.p.A. |
| Organizzazione | Aurora Salute S.p.A. (`org-aurora`) | `nis_profile` | essential |
| Organizzazione | Aurora Salute S.p.A. (`org-aurora`) | `risk_assessment_reference` | RISK-AURORA-2026-02 |
| Responsabili | Responsabile Infrastrutture e Sicurezza (`owner-aurora-ops`) | `contact_reference` | role://aurora-system-owner |
| Responsabili | Responsabile Infrastrutture e Sicurezza (`owner-aurora-ops`) | `id` | owner-aurora-ops |
| Responsabili | Responsabile Infrastrutture e Sicurezza (`owner-aurora-ops`) | `name` | Responsabile Infrastrutture e Sicurezza |
| Responsabili | Responsabile Infrastrutture e Sicurezza (`owner-aurora-ops`) | `provenance_ids` | prov-governance |
| Responsabili | Responsabile Infrastrutture e Sicurezza (`owner-aurora-ops`) | `role` | system-owner |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `asset_ids` | asset-aurora-core |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `criticality` | critical |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `data_object_ids` | data-aurora-core |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `description` | Erogazione di servizi digitali critici a supporto dell'operatività sanitaria. |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `id` | proc-aurora-core |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `name` | Servizio clinico digitale |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `owner_id` | owner-aurora-ops |
| Processi | Servizio clinico digitale (`proc-aurora-core`) | `provenance_ids` | prov-governance |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `asset_ids` | asset-aurora-core |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `classification` | restricted |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `description` | Categoria sintetica; non contiene dati reali. |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_at_rest` | True |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_at_rest_observation_type` | direct |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_at_rest_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_at_rest_provenance_ids` | prov-config |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_at_rest_status` | known |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_in_transit` | True |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_in_transit_observation_type` | direct |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_in_transit_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_in_transit_provenance_ids` | prov-config |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encrypted_in_transit_status` | known |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encryption_configuration` | AES-256 managed keys |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encryption_configuration_observation_type` | direct |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encryption_configuration_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encryption_configuration_provenance_ids` | prov-config |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `encryption_configuration_status` | known |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `id` | data-aurora-core |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `name` | Dati operativi sanitari sintetici |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `provenance_ids` | prov-config |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media` | False |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media_encrypted_provenance_ids` | prov-config |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media_encrypted_status` | not_applicable |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media_observation_type` | direct |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media_observed_at` | 2026-08-14T07:00:00Z |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media_provenance_ids` | prov-config |
| Categorie di dati | Dati operativi sanitari sintetici (`data-aurora-core`) | `removable_media_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `admin_remote_access_logging` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `admin_remote_access_logging_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `admin_remote_access_logging_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `admin_remote_access_logging_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `admin_remote_access_logging_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `anomaly_thresholds_configured` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `anomaly_thresholds_configured_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `anomaly_thresholds_configured_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `anomaly_thresholds_configured_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `anomaly_thresholds_configured_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `asset_type` | server |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `critical_software_supplier_channels_monitored` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `critical_software_supplier_channels_monitored_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `critical_software_supplier_channels_monitored_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `critical_software_supplier_channels_monitored_provenance_ids` | prov-scan |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `critical_software_supplier_channels_monitored_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `criticality` | critical |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `data_object_ids` | data-aurora-core |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `description` | Gateway applicativo critico esposto tramite HTTPS. |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `environment` | production |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `evidence_ids` | ev-aurora-asset, ev-aurora-software, ev-aurora-flow, ev-aurora-provider, ev-aurora-scan, ev-aurora-treatment, ev-aurora-vulnmanagement, ev-aurora-accessreview, ev-aurora-accessconfig, ev-aurora-physical, ev-aurora-encryption, ev-aurora-backup, ev-aurora-restore, ev-aurora-system, ev-aurora-patch, ev-aurora-maintenance, ev-aurora-log, ev-aurora-network, ev-aurora-emergency, ev-aurora-monitoring, ev-aurora-endpoint |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `exposure_level` | high |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `extended_vulnerability_assessment_performed` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `extended_vulnerability_assessment_performed_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `extended_vulnerability_assessment_performed_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `extended_vulnerability_assessment_performed_provenance_ids` | prov-scan |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `extended_vulnerability_assessment_performed_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `firewall_enabled` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `firewall_enabled_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `firewall_enabled_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `firewall_enabled_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `firewall_enabled_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardening_baseline_applied` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardening_baseline_applied_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardening_baseline_applied_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardening_baseline_applied_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardening_baseline_applied_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardware_inventory_complete` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardware_inventory_complete_observation_type` | evidence_based |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardware_inventory_complete_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardware_inventory_complete_provenance_ids` | prov-inventory |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hardware_inventory_complete_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `hostname` | gateway.aurora.example.invalid |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `id` | asset-aurora-core |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `impact_level` | critical |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `internet_exposed` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `internet_exposed_observation_type` | evidence_based |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `internet_exposed_provenance_ids` | prov-inventory |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `internet_exposed_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `ip_addresses` | 192.0.2.31 |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `lifecycle_status` | active |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `log_retention_within_plan` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `log_retention_within_plan_observation_type` | declared |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `log_retention_within_plan_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `log_retention_within_plan_provenance_ids` | prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `log_retention_within_plan_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_centralized` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_centralized_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_centralized_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_centralized_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_centralized_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_protected` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_protected_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_protected_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_protected_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `logs_protected_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `mac_addresses` | nessuna |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `maintenance_logged` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `maintenance_logged_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `maintenance_logged_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `maintenance_logged_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `maintenance_logged_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `name` | Core Clinical Gateway |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `network_segment` | protected-core |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `network_segment_observation_type` | evidence_based |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `network_segment_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `network_segment_provenance_ids` | prov-inventory |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `network_segment_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `nis_relevant` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `nis_relevant_observation_type` | declared |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `nis_relevant_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `nis_relevant_provenance_ids` | prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `nis_relevant_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `operating_system` | ExampleLinux |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `operating_system_version` | 12.4 |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `owner_id` | owner-aurora-ops |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `physical_protection_documented` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `physical_protection_documented_observation_type` | declared |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `physical_protection_documented_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `physical_protection_documented_provenance_ids` | prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `physical_protection_documented_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `process_ids` | proc-aurora-core |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `provenance_ids` | prov-inventory, prov-config, prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `provider_services_inventory_complete` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `provider_services_inventory_complete_observation_type` | declared |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `provider_services_inventory_complete_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `provider_services_inventory_complete_provenance_ids` | prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `provider_services_inventory_complete_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_protected` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_protected_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_protected_observed_at` | 2026-08-14T07:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_protected_provenance_ids` | prov-config |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_protected_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_registry_complete` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_registry_complete_observation_type` | declared |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_registry_complete_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_registry_complete_provenance_ids` | prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `remote_access_registry_complete_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `risk_assessment_reference` | RISK-AURORA-2026-02 |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `secure_disposal_documented` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `secure_disposal_documented_observation_type` | declared |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `secure_disposal_documented_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `secure_disposal_documented_provenance_ids` | prov-governance |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `secure_disposal_documented_status` | known |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `service_ids` | svc-aurora-https |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `support_status` | supported |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `vulnerability_advisories_monitored` | True |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `vulnerability_advisories_monitored_observation_type` | direct |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `vulnerability_advisories_monitored_observed_at` | 2026-08-14T05:00:00Z |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `vulnerability_advisories_monitored_provenance_ids` | prov-scan |
| Asset | Core Clinical Gateway (`asset-aurora-core`) | `vulnerability_advisories_monitored_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `asset_type` | database |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `criticality` | medium |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `data_object_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `description` | Asset rilevato dal Modulo 1 ma escluso dal perimetro tecnico NIS. |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `environment` | production |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `evidence_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `exposure_level` | low |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `hostname` | aux-aurora.example.invalid |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `id` | asset-aurora-aux |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `impact_level` | medium |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `internet_exposed` | False |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `internet_exposed_observation_type` | evidence_based |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `internet_exposed_provenance_ids` | prov-inventory |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `internet_exposed_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `ip_addresses` | 192.0.2.32 |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `lifecycle_status` | active |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `mac_addresses` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `name` | Sistema ausiliario fuori perimetro NIS |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `network_segment` | auxiliary |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `network_segment_observation_type` | evidence_based |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `network_segment_observed_at` | 2026-08-14T06:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `network_segment_provenance_ids` | prov-inventory |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `network_segment_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `nis_relevant` | False |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `nis_relevant_observation_type` | declared |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `nis_relevant_observed_at` | 2026-08-10T09:00:00Z |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `nis_relevant_provenance_ids` | prov-governance |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `nis_relevant_status` | known |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `owner_id` | owner-aurora-ops |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `process_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `properties_json` | {} |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `provenance_ids` | prov-inventory, prov-governance |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `risk_assessment_reference` | RISK-AURORA-2026-02 |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `service_ids` | nessuna |
| Asset | Sistema ausiliario fuori perimetro NIS (`asset-aurora-aux`) | `support_status` | supported |
| Servizi | HTTPS (`svc-aurora-https`) | `application_protocol` | https |
| Servizi | HTTPS (`svc-aurora-https`) | `asset_id` | asset-aurora-core |
| Servizi | HTTPS (`svc-aurora-https`) | `authorized` | True |
| Servizi | HTTPS (`svc-aurora-https`) | `authorized_observation_type` | evidence_based |
| Servizi | HTTPS (`svc-aurora-https`) | `authorized_observed_at` | 2026-08-14T06:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `authorized_provenance_ids` | prov-inventory |
| Servizi | HTTPS (`svc-aurora-https`) | `authorized_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `certificate_expiration` | 2027-08-14T00:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `certificate_expiration_observation_type` | direct |
| Servizi | HTTPS (`svc-aurora-https`) | `certificate_expiration_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `certificate_expiration_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `certificate_expiration_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `cryptographic_baseline_id` | CRYPTO-BASELINE-2026.1 |
| Servizi | HTTPS (`svc-aurora-https`) | `encrypted` | True |
| Servizi | HTTPS (`svc-aurora-https`) | `encrypted_observation_type` | direct |
| Servizi | HTTPS (`svc-aurora-https`) | `encrypted_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `encrypted_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `encrypted_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `encryption_configuration` | TLSv1.3 |
| Servizi | HTTPS (`svc-aurora-https`) | `encryption_configuration_observation_type` | direct |
| Servizi | HTTPS (`svc-aurora-https`) | `encryption_configuration_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `encryption_configuration_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `encryption_configuration_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `evidence_ids` | ev-aurora-encryption |
| Servizi | HTTPS (`svc-aurora-https`) | `id` | svc-aurora-https |
| Servizi | HTTPS (`svc-aurora-https`) | `internet_exposed` | True |
| Servizi | HTTPS (`svc-aurora-https`) | `internet_exposed_observation_type` | evidence_based |
| Servizi | HTTPS (`svc-aurora-https`) | `internet_exposed_observed_at` | 2026-08-14T06:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `internet_exposed_provenance_ids` | prov-inventory |
| Servizi | HTTPS (`svc-aurora-https`) | `internet_exposed_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `name` | HTTPS |
| Servizi | HTTPS (`svc-aurora-https`) | `obsolete_protocol` | False |
| Servizi | HTTPS (`svc-aurora-https`) | `obsolete_protocol_observation_type` | direct |
| Servizi | HTTPS (`svc-aurora-https`) | `obsolete_protocol_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `obsolete_protocol_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `obsolete_protocol_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `port` | 443 |
| Servizi | HTTPS (`svc-aurora-https`) | `product` | AuroraGateway |
| Servizi | HTTPS (`svc-aurora-https`) | `protocol` | tcp |
| Servizi | HTTPS (`svc-aurora-https`) | `provenance_ids` | prov-inventory, prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_enabled` | True |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_enabled_observation_type` | direct |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_enabled_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_enabled_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_enabled_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_versions` | TLSv1.3 |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_versions_observation_type` | direct |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_versions_observed_at` | 2026-08-14T07:00:00Z |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_versions_provenance_ids` | prov-config |
| Servizi | HTTPS (`svc-aurora-https`) | `tls_versions_status` | known |
| Servizi | HTTPS (`svc-aurora-https`) | `transport_protocol` | tcp |
| Servizi | HTTPS (`svc-aurora-https`) | `version` | 8.4 |
| Componenti software | AuroraGateway (`software-aurora-core`) | `asset_id` | asset-aurora-core |
| Componenti software | AuroraGateway (`software-aurora-core`) | `authorized` | True |
| Componenti software | AuroraGateway (`software-aurora-core`) | `authorized_observation_type` | declared |
| Componenti software | AuroraGateway (`software-aurora-core`) | `authorized_observed_at` | 2026-08-10T09:00:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `authorized_provenance_ids` | prov-governance |
| Componenti software | AuroraGateway (`software-aurora-core`) | `authorized_status` | known |
| Componenti software | AuroraGateway (`software-aurora-core`) | `critical_update_tested` | True |
| Componenti software | AuroraGateway (`software-aurora-core`) | `critical_update_tested_observation_type` | evidence_based |
| Componenti software | AuroraGateway (`software-aurora-core`) | `critical_update_tested_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `critical_update_tested_provenance_ids` | prov-patch |
| Componenti software | AuroraGateway (`software-aurora-core`) | `critical_update_tested_status` | known |
| Componenti software | AuroraGateway (`software-aurora-core`) | `evidence_ids` | ev-aurora-software, ev-aurora-patch |
| Componenti software | AuroraGateway (`software-aurora-core`) | `id` | software-aurora-core |
| Componenti software | AuroraGateway (`software-aurora-core`) | `last_security_update_at` | 2026-08-10T01:00:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `last_security_update_at_observation_type` | evidence_based |
| Componenti software | AuroraGateway (`software-aurora-core`) | `last_security_update_at_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `last_security_update_at_provenance_ids` | prov-patch |
| Componenti software | AuroraGateway (`software-aurora-core`) | `last_security_update_at_status` | known |
| Componenti software | AuroraGateway (`software-aurora-core`) | `name` | AuroraGateway |
| Componenti software | AuroraGateway (`software-aurora-core`) | `provenance_ids` | prov-inventory, prov-patch |
| Componenti software | AuroraGateway (`software-aurora-core`) | `security_update_status` | within_risk_plan |
| Componenti software | AuroraGateway (`software-aurora-core`) | `security_update_status_observation_type` | evidence_based |
| Componenti software | AuroraGateway (`software-aurora-core`) | `security_update_status_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `security_update_status_provenance_ids` | prov-patch |
| Componenti software | AuroraGateway (`software-aurora-core`) | `security_update_status_status` | known |
| Componenti software | AuroraGateway (`software-aurora-core`) | `support_status` | supported |
| Componenti software | AuroraGateway (`software-aurora-core`) | `support_status_observation_type` | evidence_based |
| Componenti software | AuroraGateway (`software-aurora-core`) | `support_status_observed_at` | 2026-08-14T07:30:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `support_status_provenance_ids` | prov-patch |
| Componenti software | AuroraGateway (`software-aurora-core`) | `support_status_status` | known |
| Componenti software | AuroraGateway (`software-aurora-core`) | `version` | 8.4 |
| Componenti software | AuroraGateway (`software-aurora-core`) | `version_observation_type` | evidence_based |
| Componenti software | AuroraGateway (`software-aurora-core`) | `version_observed_at` | 2026-08-14T06:00:00Z |
| Componenti software | AuroraGateway (`software-aurora-core`) | `version_provenance_ids` | prov-inventory |
| Componenti software | AuroraGateway (`software-aurora-core`) | `version_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `account_type` | administrator |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `asset_id` | asset-aurora-core |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `authorized` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `authorized_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `authorized_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `authorized_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `authorized_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `credentials_managed` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `credentials_managed_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `credentials_managed_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `credentials_managed_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `credentials_managed_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `evidence_ids` | ev-aurora-accessreview, ev-aurora-accessconfig |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `id` | account-aurora-admin |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `individual` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `individual_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `individual_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `individual_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `individual_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `last_reviewed_at` | 2026-08-08T09:00:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `last_reviewed_at_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `last_reviewed_at_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `last_reviewed_at_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `last_reviewed_at_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `least_privilege` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `least_privilege_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `least_privilege_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `least_privilege_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `least_privilege_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `mfa_enabled` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `mfa_enabled_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `mfa_enabled_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `mfa_enabled_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `mfa_enabled_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `privileged` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `privileged_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `privileged_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `privileged_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `privileged_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `remote_access` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `remote_access_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `remote_access_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `remote_access_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `remote_access_status` | known |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `separate_admin_account` | True |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `separate_admin_account_observation_type` | evidence_based |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `separate_admin_account_observed_at` | 2026-08-14T07:45:00Z |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `separate_admin_account_provenance_ids` | prov-access |
| Utenze | account-aurora-admin (`account-aurora-admin`) | `separate_admin_account_status` | known |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `application_protocol` | https |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `asset_id` | asset-aurora-core |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `authorized` | True |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `authorized_observation_type` | evidence_based |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `authorized_observed_at` | 2026-08-14T06:30:00Z |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `authorized_provenance_ids` | prov-network |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `authorized_status` | known |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `destination` | asset-aurora-core |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `direction` | inbound |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `encrypted` | True |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `encrypted_observation_type` | evidence_based |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `encrypted_observed_at` | 2026-08-14T06:30:00Z |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `encrypted_provenance_ids` | prov-network |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `encrypted_status` | known |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `evidence_ids` | ev-aurora-flow |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `id` | flow-aurora-https |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `port` | 443 |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `provenance_ids` | prov-network |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `source` | internet |
| Flussi di rete | flow-aurora-https (`flow-aurora-https`) | `transport_protocol` | tcp |
| Backup | backup-aurora-core (`backup-aurora-core`) | `asset_id` | asset-aurora-core |
| Backup | backup-aurora-core (`backup-aurora-core`) | `evidence_ids` | ev-aurora-backup, ev-aurora-restore |
| Backup | backup-aurora-core (`backup-aurora-core`) | `frequency_within_plan` | True |
| Backup | backup-aurora-core (`backup-aurora-core`) | `frequency_within_plan_observation_type` | evidence_based |
| Backup | backup-aurora-core (`backup-aurora-core`) | `frequency_within_plan_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `frequency_within_plan_provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `frequency_within_plan_status` | known |
| Backup | backup-aurora-core (`backup-aurora-core`) | `id` | backup-aurora-core |
| Backup | backup-aurora-core (`backup-aurora-core`) | `last_success_at` | 2026-08-15T02:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `last_success_at_observation_type` | evidence_based |
| Backup | backup-aurora-core (`backup-aurora-core`) | `last_success_at_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `last_success_at_provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `last_success_at_status` | known |
| Backup | backup-aurora-core (`backup-aurora-core`) | `offline_copy` | True |
| Backup | backup-aurora-core (`backup-aurora-core`) | `offline_copy_observation_type` | evidence_based |
| Backup | backup-aurora-core (`backup-aurora-core`) | `offline_copy_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `offline_copy_provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `offline_copy_status` | known |
| Backup | backup-aurora-core (`backup-aurora-core`) | `plan_reference` | BACKUP-AURORA-2026 |
| Backup | backup-aurora-core (`backup-aurora-core`) | `protected_copy` | True |
| Backup | backup-aurora-core (`backup-aurora-core`) | `protected_copy_observation_type` | evidence_based |
| Backup | backup-aurora-core (`backup-aurora-core`) | `protected_copy_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `protected_copy_provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `protected_copy_status` | known |
| Backup | backup-aurora-core (`backup-aurora-core`) | `provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_at` | 2026-07-20T08:00:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_at_observation_type` | evidence_based |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_at_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_at_provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_at_status` | known |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_successful` | True |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_successful_observation_type` | evidence_based |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_successful_observed_at` | 2026-08-14T03:30:00Z |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_successful_provenance_ids` | prov-backup |
| Backup | backup-aurora-core (`backup-aurora-core`) | `restore_test_successful_status` | known |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `asset_id` | asset-aurora-core |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `capability_type` | emergency_communications |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `configuration_reference` | EMERGENCY-COMMS-AURORA-1 |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `configured` | True |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `configured_status` | known |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `enabled` | True |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `enabled_status` | known |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `evidence_ids` | ev-aurora-emergency |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `id` | cap-aurora-emergency |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `maintained` | True |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `maintained_status` | known |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `monitored` | True |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `monitored_status` | known |
| Capacità di sicurezza | cap-aurora-emergency (`cap-aurora-emergency`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `asset_id` | asset-aurora-core |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `capability_type` | intrusion_detection |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `configured` | True |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `configured_status` | known |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `enabled` | True |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `enabled_status` | known |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `evidence_ids` | ev-aurora-monitoring |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `id` | cap-aurora-ids |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `maintained` | True |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `maintained_status` | known |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `monitored` | True |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `monitored_status` | known |
| Capacità di sicurezza | cap-aurora-ids (`cap-aurora-ids`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `asset_id` | asset-aurora-core |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `capability_type` | traffic_filter |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `configured` | True |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `configured_status` | known |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `enabled` | True |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `enabled_status` | known |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `evidence_ids` | ev-aurora-monitoring |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `id` | cap-aurora-filter |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `maintained` | True |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `maintained_status` | known |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `monitored` | True |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `monitored_status` | known |
| Capacità di sicurezza | cap-aurora-filter (`cap-aurora-filter`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `asset_id` | asset-aurora-core |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `capability_type` | access_monitoring |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `configured` | True |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `configured_status` | known |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `enabled` | True |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `enabled_status` | known |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `evidence_ids` | ev-aurora-monitoring |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `id` | cap-aurora-access-monitor |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `maintained` | True |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `maintained_status` | known |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `monitored` | True |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `monitored_status` | known |
| Capacità di sicurezza | cap-aurora-access-monitor (`cap-aurora-access-monitor`) | `provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `asset_id` | asset-aurora-core |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `capability_type` | endpoint_protection |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `configured` | True |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `configured_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `configured_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `configured_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `configured_status` | known |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `enabled` | True |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `enabled_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `enabled_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `enabled_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `enabled_status` | known |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `evidence_ids` | ev-aurora-endpoint |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `id` | cap-aurora-endpoint |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `maintained` | True |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `maintained_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `maintained_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `maintained_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `maintained_status` | known |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `monitored` | True |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `monitored_observation_type` | direct |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `monitored_observed_at` | 2026-08-14T07:00:00Z |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `monitored_provenance_ids` | prov-config |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `monitored_status` | known |
| Capacità di sicurezza | cap-aurora-endpoint (`cap-aurora-endpoint`) | `provenance_ids` | prov-config |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `accepted_exception` | False |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `accepted_exception_observation_type` | declared |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `accepted_exception_observed_at` | 2026-08-10T09:00:00Z |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `accepted_exception_provenance_ids` | prov-governance |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `accepted_exception_status` | known |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `asset_id` | asset-aurora-core |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `component` | Stack HTTP/2 di AuroraGateway |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `cve` | CVE-2023-44487 |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `cvss_score` | 7.5 |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `description` | Riferimento CVE reale applicato, esclusivamente a scopo dimostrativo, allo stack HTTP/2 del prodotto sintetico AuroraGateway. |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `detected_at` | 2026-07-28T05:00:00Z |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `evidence_ids` | ev-aurora-scan, ev-aurora-treatment |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `id` | vuln-aurora-001 |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `patch_available` | True |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `patch_available_observation_type` | direct |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `patch_available_observed_at` | 2026-08-14T05:00:00Z |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `patch_available_provenance_ids` | prov-scan |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `patch_available_status` | known |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `provenance_ids` | prov-scan, prov-patch |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `remediation_due_date` | 2026-08-20T23:59:59Z |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `remediation_status` | remediated |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `remediation_status_observation_type` | evidence_based |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `remediation_status_observed_at` | 2026-08-14T07:30:00Z |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `remediation_status_provenance_ids` | prov-patch |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `remediation_status_status` | known |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `service_id` | svc-aurora-https |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `severity` | high |
| Vulnerabilità | Dipendenza HTTP/2 aggiornata dopo advisory (`vuln-aurora-001`) | `title` | Dipendenza HTTP/2 aggiornata dopo advisory |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `asset_ids` | asset-aurora-core |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `content_json` | {} |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `control_ids` | CTRL-ID-AM-01 |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `description` | Inventario asset acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `evidence_type` | asset_inventory |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `id` | ev-aurora-asset |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `provenance_ids` | prov-inventory |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `reliability` | high |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `service_ids` | nessuna |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `source` | CMDB |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `source_category` | asset_internal |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `title` | Inventario asset |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Inventario asset (`ev-aurora-asset`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario software (`ev-aurora-software`) | `asset_ids` | asset-aurora-core |
| Evidenze | Inventario software (`ev-aurora-software`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario software (`ev-aurora-software`) | `content_json` | {} |
| Evidenze | Inventario software (`ev-aurora-software`) | `control_ids` | CTRL-ID-AM-02, CTRL-PR-PS-02 |
| Evidenze | Inventario software (`ev-aurora-software`) | `description` | Inventario software acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario software (`ev-aurora-software`) | `evidence_type` | software_inventory |
| Evidenze | Inventario software (`ev-aurora-software`) | `id` | ev-aurora-software |
| Evidenze | Inventario software (`ev-aurora-software`) | `provenance_ids` | prov-inventory |
| Evidenze | Inventario software (`ev-aurora-software`) | `reliability` | high |
| Evidenze | Inventario software (`ev-aurora-software`) | `service_ids` | nessuna |
| Evidenze | Inventario software (`ev-aurora-software`) | `source` | CMDB |
| Evidenze | Inventario software (`ev-aurora-software`) | `source_category` | asset_internal |
| Evidenze | Inventario software (`ev-aurora-software`) | `title` | Inventario software |
| Evidenze | Inventario software (`ev-aurora-software`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario software (`ev-aurora-software`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `asset_ids` | asset-aurora-core |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `content_json` | {} |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `control_ids` | CTRL-ID-AM-03-E |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `description` | Inventario flussi di rete acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `evidence_type` | network_flow_inventory |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `id` | ev-aurora-flow |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `provenance_ids` | prov-network |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `reliability` | high |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `service_ids` | nessuna |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `source` | network-manager |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `source_category` | asset_internal |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `title` | Inventario flussi di rete |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario flussi di rete (`ev-aurora-flow`) | `vulnerability_ids` | nessuna |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `asset_ids` | asset-aurora-core |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `content_json` | {} |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `control_ids` | CTRL-ID-AM-04 |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `description` | Inventario servizi fornitori acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `evidence_type` | provider_service_inventory |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `id` | ev-aurora-provider |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `provenance_ids` | prov-governance |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `reliability` | medium |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `service_ids` | nessuna |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `source` | service-catalog |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `source_category` | declared |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `title` | Inventario servizi fornitori |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Inventario servizi fornitori (`ev-aurora-provider`) | `vulnerability_ids` | nessuna |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `asset_ids` | asset-aurora-core |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `content_json` | {"activity_description": "Vulnerability assessment autenticato e riesame manuale.", "cve": "CVE-2023-44487", "impact_levels": ["high"], "nvd_url": "https://nvd.nist.gov/vuln/detail/CVE-2023-44487", "outcomes": "Relazione strutturata approvata per lo scenario dimostrativo.", "synthetic_context": "Organizzazione e prodotto sono inventati; il CVE è reale e la sua associazione allo stack HTTP/2 di AuroraGateway è esclusivamente dimostrativa.", "vulnerabilities": ["vuln-aurora-001"]} |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `control_ids` | CTRL-ID-RA-01, CTRL-ID-RA-01-E, CTRL-ID-RA-08 |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `description` | Scansione vulnerabilità acquisita e normalizzata dai moduli 1 e 2; il prodotto e l'associazione alla dipendenza sono sintetici. |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `evidence_type` | vulnerability_scan |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `id` | ev-aurora-scan |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `provenance_ids` | prov-scan |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `reliability` | high |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `service_ids` | nessuna |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `source` | vulnerability-scanner |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `source_category` | asset_internal |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `title` | Scansione vulnerabilità |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Scansione vulnerabilità (`ev-aurora-scan`) | `vulnerability_ids` | vuln-aurora-001 |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `asset_ids` | asset-aurora-core |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `content_json` | {} |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `control_ids` | CTRL-ID-RA-08 |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `description` | Registro trattamento vulnerabilità acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `evidence_type` | vulnerability_treatment |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `id` | ev-aurora-treatment |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `provenance_ids` | prov-patch |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `reliability` | high |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `service_ids` | nessuna |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `source` | vulnerability-manager |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `source_category` | asset_internal |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `title` | Registro trattamento vulnerabilità |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro trattamento vulnerabilità (`ev-aurora-treatment`) | `vulnerability_ids` | vuln-aurora-001 |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `asset_ids` | asset-aurora-core |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `content_json` | {} |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `control_ids` | CTRL-ID-RA-01, CTRL-ID-RA-08, CTRL-ID-RA-08-E |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `description` | Monitoraggio advisory vulnerabilità acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `evidence_type` | vulnerability_management |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `id` | ev-aurora-vulnmanagement |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `provenance_ids` | prov-scan |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `reliability` | high |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `service_ids` | nessuna |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `source` | vulnerability-manager |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `source_category` | asset_internal |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `title` | Monitoraggio advisory vulnerabilità |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Monitoraggio advisory vulnerabilità (`ev-aurora-vulnmanagement`) | `vulnerability_ids` | nessuna |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `asset_ids` | asset-aurora-core |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `content_json` | {} |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `control_ids` | CTRL-PR-AA-01 |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `description` | Revisione identità e accessi acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `evidence_type` | access_review |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `id` | ev-aurora-accessreview |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `provenance_ids` | prov-access |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `reliability` | high |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `service_ids` | nessuna |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `source` | IAM |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `source_category` | asset_internal |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `title` | Revisione identità e accessi |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Revisione identità e accessi (`ev-aurora-accessreview`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `asset_ids` | asset-aurora-core |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `content_json` | {} |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `control_ids` | CTRL-PR-AA-03, CTRL-PR-AA-05 |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `description` | Configurazione MFA e privilegi acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `evidence_type` | access_configuration |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `id` | ev-aurora-accessconfig |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `provenance_ids` | prov-access |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `reliability` | high |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `service_ids` | nessuna |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `source` | IAM |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `source_category` | asset_internal |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `title` | Configurazione MFA e privilegi |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione MFA e privilegi (`ev-aurora-accessconfig`) | `vulnerability_ids` | nessuna |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `asset_ids` | asset-aurora-core |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `content_json` | {} |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `control_ids` | CTRL-PR-AA-06 |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `description` | Evidenza protezione fisica acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `evidence_type` | physical_security |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `id` | ev-aurora-physical |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `provenance_ids` | prov-governance |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `reliability` | medium |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `service_ids` | nessuna |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `source` | facilities |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `source_category` | declared |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `title` | Evidenza protezione fisica |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Evidenza protezione fisica (`ev-aurora-physical`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `asset_ids` | asset-aurora-core |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `content_json` | {"baseline_id": "CRYPTO-BASELINE-2026.1"} |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `control_ids` | CTRL-PR-DS-01, CTRL-PR-DS-02 |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `description` | Configurazione cifratura acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `evidence_type` | encryption_configuration |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `id` | ev-aurora-encryption |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `reliability` | high |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `service_ids` | svc-aurora-https |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `source` | configuration-manager |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `source_category` | asset_internal |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `title` | Configurazione cifratura |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `valid_until` | 2026-09-30T23:59:59Z |
| Evidenze | Configurazione cifratura (`ev-aurora-encryption`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro backup (`ev-aurora-backup`) | `asset_ids` | asset-aurora-core |
| Evidenze | Registro backup (`ev-aurora-backup`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro backup (`ev-aurora-backup`) | `content_json` | {"plan_reference": "BACKUP-AURORA-2026"} |
| Evidenze | Registro backup (`ev-aurora-backup`) | `control_ids` | CTRL-PR-DS-11, CTRL-PR-DS-11-E |
| Evidenze | Registro backup (`ev-aurora-backup`) | `description` | Registro backup acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro backup (`ev-aurora-backup`) | `evidence_type` | backup_record |
| Evidenze | Registro backup (`ev-aurora-backup`) | `id` | ev-aurora-backup |
| Evidenze | Registro backup (`ev-aurora-backup`) | `provenance_ids` | prov-backup |
| Evidenze | Registro backup (`ev-aurora-backup`) | `reliability` | high |
| Evidenze | Registro backup (`ev-aurora-backup`) | `service_ids` | nessuna |
| Evidenze | Registro backup (`ev-aurora-backup`) | `source` | backup-manager |
| Evidenze | Registro backup (`ev-aurora-backup`) | `source_category` | asset_internal |
| Evidenze | Registro backup (`ev-aurora-backup`) | `title` | Registro backup |
| Evidenze | Registro backup (`ev-aurora-backup`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro backup (`ev-aurora-backup`) | `vulnerability_ids` | nessuna |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `asset_ids` | asset-aurora-core |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `content_json` | {} |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `control_ids` | CTRL-PR-DS-11-E |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `description` | Test di ripristino acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `evidence_type` | restore_test |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `id` | ev-aurora-restore |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `provenance_ids` | prov-backup |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `reliability` | high |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `service_ids` | nessuna |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `source` | backup-manager |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `source_category` | asset_internal |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `title` | Test di ripristino |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Test di ripristino (`ev-aurora-restore`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `asset_ids` | asset-aurora-core |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `content_json` | {} |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `control_ids` | CTRL-PR-PS-01-E |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `description` | Configurazione e hardening acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `evidence_type` | system_configuration |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `id` | ev-aurora-system |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `reliability` | high |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `service_ids` | nessuna |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `source` | configuration-manager |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `source_category` | asset_internal |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `title` | Configurazione e hardening |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione e hardening (`ev-aurora-system`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro patching (`ev-aurora-patch`) | `asset_ids` | asset-aurora-core |
| Evidenze | Registro patching (`ev-aurora-patch`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro patching (`ev-aurora-patch`) | `content_json` | {} |
| Evidenze | Registro patching (`ev-aurora-patch`) | `control_ids` | CTRL-PR-PS-02, CTRL-PR-PS-02-E |
| Evidenze | Registro patching (`ev-aurora-patch`) | `description` | Registro patching acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro patching (`ev-aurora-patch`) | `evidence_type` | patch_record |
| Evidenze | Registro patching (`ev-aurora-patch`) | `id` | ev-aurora-patch |
| Evidenze | Registro patching (`ev-aurora-patch`) | `provenance_ids` | prov-patch |
| Evidenze | Registro patching (`ev-aurora-patch`) | `reliability` | high |
| Evidenze | Registro patching (`ev-aurora-patch`) | `service_ids` | nessuna |
| Evidenze | Registro patching (`ev-aurora-patch`) | `source` | patch-manager |
| Evidenze | Registro patching (`ev-aurora-patch`) | `source_category` | asset_internal |
| Evidenze | Registro patching (`ev-aurora-patch`) | `title` | Registro patching |
| Evidenze | Registro patching (`ev-aurora-patch`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro patching (`ev-aurora-patch`) | `vulnerability_ids` | nessuna |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `asset_ids` | asset-aurora-core |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `content_json` | {} |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `control_ids` | CTRL-PR-PS-03-E |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `description` | Registro manutenzione acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `evidence_type` | maintenance_record |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `id` | ev-aurora-maintenance |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `provenance_ids` | prov-config |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `reliability` | high |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `service_ids` | nessuna |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `source` | configuration-manager |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `source_category` | asset_internal |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `title` | Registro manutenzione |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Registro manutenzione (`ev-aurora-maintenance`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `asset_ids` | asset-aurora-core |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `content_json` | {} |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `control_ids` | CTRL-PR-PS-04 |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `description` | Configurazione logging acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `evidence_type` | log_configuration |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `id` | ev-aurora-log |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `reliability` | high |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `service_ids` | nessuna |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `source` | logging-platform |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `source_category` | asset_internal |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `title` | Configurazione logging |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione logging (`ev-aurora-log`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `asset_ids` | asset-aurora-core |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `content_json` | {} |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `control_ids` | CTRL-PR-IR-01 |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `description` | Configurazione accessi remoti e firewall acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `evidence_type` | network_security |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `id` | ev-aurora-network |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `provenance_ids` | prov-network |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `reliability` | high |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `service_ids` | nessuna |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `source` | network-manager |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `source_category` | asset_internal |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `title` | Configurazione accessi remoti e firewall |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione accessi remoti e firewall (`ev-aurora-network`) | `vulnerability_ids` | nessuna |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `asset_ids` | asset-aurora-core |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `content_json` | {} |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `control_ids` | CTRL-PR-IR-03-E |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `description` | Comunicazioni di emergenza acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `evidence_type` | emergency_communications |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `id` | ev-aurora-emergency |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `provenance_ids` | prov-config |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `reliability` | high |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `service_ids` | nessuna |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `source` | crisis-platform |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `source_category` | asset_internal |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `title` | Comunicazioni di emergenza |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Comunicazioni di emergenza (`ev-aurora-emergency`) | `vulnerability_ids` | nessuna |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `asset_ids` | asset-aurora-core |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `content_json` | {} |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `control_ids` | CTRL-DE-CM-01, CTRL-DE-CM-01-E |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `description` | Configurazione monitoraggio acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `evidence_type` | monitoring_configuration |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `id` | ev-aurora-monitoring |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `provenance_ids` | prov-config |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `reliability` | high |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `service_ids` | nessuna |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `source` | monitoring-platform |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `source_category` | asset_internal |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `title` | Configurazione monitoraggio |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Configurazione monitoraggio (`ev-aurora-monitoring`) | `vulnerability_ids` | nessuna |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `asset_ids` | asset-aurora-core |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `collected_at` | 2026-08-14T08:00:00Z |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `content_json` | {} |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `control_ids` | CTRL-DE-CM-09 |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `description` | Protezione endpoint acquisito e normalizzato dai moduli 1 e 2. |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `evidence_type` | endpoint_protection |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `id` | ev-aurora-endpoint |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `provenance_ids` | prov-config |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `reliability` | high |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `service_ids` | nessuna |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `source` | endpoint-platform |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `source_category` | asset_internal |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `title` | Protezione endpoint |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `valid_until` | 2027-12-31T23:59:59Z |
| Evidenze | Protezione endpoint (`ev-aurora-endpoint`) | `vulnerability_ids` | nessuna |
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
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `acn_point` | ID.AM-01 |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `confidence_level` | medium |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `control_id` | CTRL-ID-AM-01 |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `decision_policy` | all_required |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-asset"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "asset.hardware_inventory_complete", "provenance_ids": ["prov-inventory"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-asset.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `errors` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "asset.hardware_inventory_complete", "provenance_ids": ["prov-inventory"], "value_status": "known"}] |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `evidence_ids` | ev-aurora-asset |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `governance_status` | none |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `id` | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `information_actions` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `known_violations` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `missing_information` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `nis_profile` | essential |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `requirement_id` | REQ-ID-AM-01 |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `rule_id` | RULE-ID-AM-01 |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `technical_status` | compliant |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `thresholds_used_json` | {"evidence.ev-aurora-asset.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 8cdb8a9a-4f57-56d5-a48c-b79c9b01e297 (`8cdb8a9a-4f57-56d5-a48c-b79c9b01e297`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `acn_point` | ID.AM-02 |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `confidence_level` | low |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `control_id` | CTRL-ID-AM-02 |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `decision_policy` | all_required |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-software"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "identificato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "Core Clinical Gateway", "path": "Asset.asset-aurora-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "HTTPS", "path": "Service.svc-aurora-https.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "Service.svc-aurora-https.authorized", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "AuroraGateway", "path": "SoftwareComponent.software-aurora-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": "8.4", "path": "SoftwareComponent.software-aurora-core.version", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "SoftwareComponent.software-aurora-core.authorized", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `errors` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `evaluated_facts_json` | [{"comparison": "identificato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "Core Clinical Gateway", "path": "Asset.asset-aurora-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "HTTPS", "path": "Service.svc-aurora-https.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": true, "path": "Service.svc-aurora-https.authorized", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": null, "observed_at": null, "observed_value": "AuroraGateway", "path": "SoftwareComponent.software-aurora-core.name", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:00:00Z", "observed_value": "8.4", "path": "SoftwareComponent.software-aurora-core.version", "provenance_ids": ["prov-inventory"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "SoftwareComponent.software-aurora-core.authorized", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `evidence_ids` | ev-aurora-software |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `governance_status` | none |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `id` | 134c76f6-829c-54f4-8a20-bb2658caed81 |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `information_actions` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `known_violations` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `missing_information` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `nis_profile` | essential |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `requirement_id` | REQ-ID-AM-02 |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `rule_id` | RULE-ID-AM-02 |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `technical_status` | compliant |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `thresholds_used_json` | {"evidence.ev-aurora-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 134c76f6-829c-54f4-8a20-bb2658caed81 (`134c76f6-829c-54f4-8a20-bb2658caed81`) | `verification_mode` | direct_technical |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `acn_point` | ID.AM-03 |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `confidence_level` | medium |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `control_id` | CTRL-ID-AM-03-E |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `decision_policy` | all_required |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-flow"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "internet", "path": "NetworkFlow.flow-aurora-https.source", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "asset-aurora-core", "path": "NetworkFlow.flow-aurora-https.destination", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "tcp", "path": "NetworkFlow.flow-aurora-https.transport_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "https", "path": "NetworkFlow.flow-aurora-https.application_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:30:00Z", "observed_value": true, "path": "NetworkFlow.flow-aurora-https.authorized", "provenance_ids": ["prov-network"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-flow.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `errors` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `evaluated_facts_json` | [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "internet", "path": "NetworkFlow.flow-aurora-https.source", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "asset-aurora-core", "path": "NetworkFlow.flow-aurora-https.destination", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "tcp", "path": "NetworkFlow.flow-aurora-https.transport_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "https", "path": "NetworkFlow.flow-aurora-https.application_protocol", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T06:30:00Z", "observed_value": true, "path": "NetworkFlow.flow-aurora-https.authorized", "provenance_ids": ["prov-network"], "value_status": "known"}] |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `evidence_ids` | ev-aurora-flow |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `governance_status` | none |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `id` | b868dcad-1d71-59a7-bc03-919729465688 |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `information_actions` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `known_violations` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `missing_information` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `nis_profile` | essential |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `requirement_id` | REQ-ID-AM-03-E |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `rule_id` | RULE-ID-AM-03-E |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `technical_status` | compliant |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `thresholds_used_json` | {"evidence.ev-aurora-flow.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | b868dcad-1d71-59a7-bc03-919729465688 (`b868dcad-1d71-59a7-bc03-919729465688`) | `verification_mode` | direct_technical |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `acn_point` | ID.AM-04 |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `confidence_level` | low |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `control_id` | CTRL-ID-AM-04 |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `decision_policy` | all_required |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-provider"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.provider_services_inventory_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-provider.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `errors` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.provider_services_inventory_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `evidence_ids` | ev-aurora-provider |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `governance_status` | none |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `id` | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `information_actions` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `known_violations` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `missing_information` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `nis_profile` | essential |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `requirement_id` | REQ-ID-AM-04 |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `rule_id` | RULE-ID-AM-04 |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `technical_status` | compliant |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `thresholds_used_json` | {"evidence.ev-aurora-provider.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | b69beb1f-d755-507a-bf1e-cdc747b2f0b8 (`b69beb1f-d755-507a-bf1e-cdc747b2f0b8`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `confidence_level` | high |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `conflicting_information` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `control_id` | CTRL-ID-RA-01 |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `decision_policy` | all_required |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-vulnmanagement"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `errors` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}] |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `evidence_ids` | ev-aurora-vulnmanagement |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `governance_status` | none |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `id` | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `information_actions` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `known_violations` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `missing_information` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `nis_profile` | essential |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `requirement_id` | REQ-ID-RA-01 |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `rule_id` | RULE-ID-RA-01 |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `selector_decisions` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `technical_remediations` | nessuna |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `technical_status` | compliant |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `thresholds_used_json` | {"evidence.ev-aurora-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | ae8c53db-9242-5d62-a2b4-86acdf5a15a2 (`ae8c53db-9242-5d62-a2b4-86acdf5a15a2`) | `verification_mode` | direct_technical |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `confidence_level` | high |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `conflicting_information` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `control_id` | CTRL-ID-RA-01-E |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `decision_policy` | all_required |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-scan"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.extended_vulnerability_assessment_performed", "provenance_ids": ["prov-scan"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-scan.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `errors` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.extended_vulnerability_assessment_performed", "provenance_ids": ["prov-scan"], "value_status": "known"}] |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `evidence_ids` | ev-aurora-scan |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `governance_status` | none |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `id` | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `information_actions` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `known_violations` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `missing_information` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `nis_profile` | essential |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `requirement_id` | REQ-ID-RA-01-E |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `rule_id` | RULE-ID-RA-01-E |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `selector_decisions` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `technical_remediations` | nessuna |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `technical_status` | compliant |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `thresholds_used_json` | {"evidence.ev-aurora-scan.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc (`cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `confidence_level` | medium |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `control_id` | CTRL-ID-RA-08 |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `decision_policy` | all_required |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-treatment", "ev-aurora-vulnmanagement"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}, {"comparison": "remediated o mitigated", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "remediated", "path": "Vulnerability.vuln-aurora-001.remediation_status", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-treatment.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-aurora-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `errors` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.vulnerability_advisories_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}, {"comparison": "remediated o mitigated", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "remediated", "path": "Vulnerability.vuln-aurora-001.remediation_status", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `evidence_ids` | ev-aurora-treatment, ev-aurora-vulnmanagement |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `governance_status` | none |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `id` | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `information_actions` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `known_violations` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `missing_information` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `nis_profile` | essential |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `requirement_id` | REQ-ID-RA-08 |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `rule_id` | RULE-ID-RA-08 |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `technical_status` | compliant |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `thresholds_used_json` | {"evidence.ev-aurora-treatment.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-aurora-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | 9876425a-cf3f-5d29-b6ef-cc59cdeca1fa (`9876425a-cf3f-5d29-b6ef-cc59cdeca1fa`) | `verification_mode` | direct_technical |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `confidence_level` | high |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `conflicting_information` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `control_id` | CTRL-ID-RA-08-E |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `decision_policy` | all_required |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-vulnmanagement"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.critical_software_supplier_channels_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `errors` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T05:00:00Z", "observed_value": true, "path": "asset.critical_software_supplier_channels_monitored", "provenance_ids": ["prov-scan"], "value_status": "known"}] |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `evidence_ids` | ev-aurora-vulnmanagement |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `governance_status` | none |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `id` | e0506187-5d20-5d37-b92e-6878f7cac413 |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `information_actions` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `known_violations` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `missing_information` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `nis_profile` | essential |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `requirement_id` | REQ-ID-RA-08-E |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `rule_id` | RULE-ID-RA-08-E |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `selector_decisions` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `technical_remediations` | nessuna |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `technical_status` | compliant |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `thresholds_used_json` | {"evidence.ev-aurora-vulnmanagement.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | e0506187-5d20-5d37-b92e-6878f7cac413 (`e0506187-5d20-5d37-b92e-6878f7cac413`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `acn_point` | PR.AA-01 |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `confidence_level` | medium |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `control_id` | CTRL-PR-AA-01 |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `decision_policy` | all_required |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-accessreview"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "administrator", "path": "Account.account-aurora-admin.account_type", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.individual", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.authorized", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.credentials_managed", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": "2026-08-08T09:00:00Z", "path": "Account.account-aurora-admin.last_reviewed_at", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-accessreview.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `errors` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `evaluated_facts_json` | [{"comparison": "presente", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": null, "observed_at": null, "observed_value": "administrator", "path": "Account.account-aurora-admin.account_type", "provenance_ids": [], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.individual", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.authorized", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.credentials_managed", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "presente e autorizzato", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": "2026-08-08T09:00:00Z", "path": "Account.account-aurora-admin.last_reviewed_at", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `evidence_ids` | ev-aurora-accessreview |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `governance_status` | none |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `id` | a284ba8d-6d80-587f-acaa-eb0379ad632b |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `information_actions` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `known_violations` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `missing_information` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `nis_profile` | essential |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `requirement_id` | REQ-PR-AA-01 |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `rule_id` | RULE-PR-AA-01 |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `technical_status` | compliant |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `thresholds_used_json` | {"evidence.ev-aurora-accessreview.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}} |
| Esiti della valutazione | a284ba8d-6d80-587f-acaa-eb0379ad632b (`a284ba8d-6d80-587f-acaa-eb0379ad632b`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `acn_point` | PR.AA-03 |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `confidence_level` | medium |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `control_id` | CTRL-PR-AA-03 |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `decision_policy` | all_required |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-accessconfig"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.mfa_enabled", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": ["account-aurora-admin"], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-03", "rule_version": "2.1.0", "selector_decisions": [{"conflicting_information": [], "entity_id": "account-aurora-admin", "evaluated_fields": ["privileged", "remote_access"], "missing_information": [], "selector_type": "any", "status": "selected"}], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `errors` | nessuna |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.mfa_enabled", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `evidence_ids` | ev-aurora-accessconfig |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `governance_status` | none |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `id` | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `information_actions` | nessuna |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `known_violations` | nessuna |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `missing_information` | nessuna |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `nis_profile` | essential |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `requirement_id` | REQ-PR-AA-03 |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `rule_id` | RULE-PR-AA-03 |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `selector_decisions_json` | [{"conflicting_information": [], "entity_id": "account-aurora-admin", "evaluated_fields": ["privileged", "remote_access"], "missing_information": [], "selector_type": "any", "status": "selected"}] |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `technical_status` | compliant |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `thresholds_used_json` | {"evidence.ev-aurora-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50 (`3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `acn_point` | PR.AA-05 |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `confidence_level` | medium |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `control_id` | CTRL-PR-AA-05 |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `decision_policy` | all_required |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-accessconfig"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.least_privilege", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.separate_admin_account", "provenance_ids": ["prov-access"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": ["account-aurora-admin"], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-05", "rule_version": "2.1.0", "selector_decisions": [{"conflicting_information": [], "entity_id": "account-aurora-admin", "evaluated_fields": ["privileged"], "missing_information": [], "selector_type": "any", "status": "selected"}], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `errors` | nessuna |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.least_privilege", "provenance_ids": ["prov-access"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:45:00Z", "observed_value": true, "path": "Account.account-aurora-admin.separate_admin_account", "provenance_ids": ["prov-access"], "value_status": "known"}] |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `evidence_ids` | ev-aurora-accessconfig |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `governance_status` | none |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `id` | 180002f3-6752-5c1c-9bbe-91390cea7fd0 |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `information_actions` | nessuna |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `known_violations` | nessuna |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `missing_information` | nessuna |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `nis_profile` | essential |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `requirement_id` | REQ-PR-AA-05 |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `rule_id` | RULE-PR-AA-05 |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `selector_decisions_json` | [{"conflicting_information": [], "entity_id": "account-aurora-admin", "evaluated_fields": ["privileged"], "missing_information": [], "selector_type": "any", "status": "selected"}] |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `technical_status` | compliant |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `thresholds_used_json` | {"evidence.ev-aurora-accessconfig.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 180002f3-6752-5c1c-9bbe-91390cea7fd0 (`180002f3-6752-5c1c-9bbe-91390cea7fd0`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `acn_point` | PR.AA-06 |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `confidence_level` | low |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `control_id` | CTRL-PR-AA-06 |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `decision_policy` | all_required |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-physical"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.physical_protection_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-06", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-physical.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `errors` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.physical_protection_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `evidence_ids` | ev-aurora-physical |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `governance_status` | none |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `id` | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `information_actions` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `known_violations` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `missing_information` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `nis_profile` | essential |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `requirement_id` | REQ-PR-AA-06 |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `rule_id` | RULE-PR-AA-06 |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `technical_status` | compliant |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `thresholds_used_json` | {"evidence.ev-aurora-physical.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | 5cf3f0d9-2df6-5f07-9f92-a9faec0b094b (`5cf3f0d9-2df6-5f07-9f92-a9faec0b094b`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `acn_point` | PR.DS-01 |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `confidence_level` | insufficient |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `control_id` | CTRL-PR-DS-01 |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `decision_policy` | all_required |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-core", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_verifiable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `errors` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `governance_status` | none |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `id` | 8947f3c5-cb85-563e-9f24-2adf1e539e4d |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `information_actions` | Acquisire l'informazione mancante indicata nel risultato. |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `known_violations` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `missing_information` | DataObject.inventory_status |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `nis_profile` | essential |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `reason` | completezza dell'inventario DataObject non nota |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `recommendation` | Cifrare i supporti rimovibili secondo classificazione e baseline approvata. |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `requirement_id` | REQ-PR-DS-01 |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `rule_id` | RULE-PR-DS-01 |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `technical_status` | not_verifiable |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 8947f3c5-cb85-563e-9f24-2adf1e539e4d (`8947f3c5-cb85-563e-9f24-2adf1e539e4d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `acn_point` | PR.DS-02 |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `confidence_level` | high |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `control_id` | CTRL-PR-DS-02 |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `decision_policy` | all_required |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-encryption"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-aurora-https.encrypted", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-aurora-https.tls_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "baseline crittografica", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": ["TLSv1.3"], "path": "Service.svc-aurora-https.tls_versions", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "evidence.ev-aurora-encryption.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `errors` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-aurora-https.encrypted", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "Service.svc-aurora-https.tls_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "baseline crittografica", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": ["TLSv1.3"], "path": "Service.svc-aurora-https.tls_versions", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `evidence_ids` | ev-aurora-encryption |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `governance_status` | none |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `id` | 47b74015-300c-5fe0-ba2c-a279fe186052 |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `information_actions` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `known_violations` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `missing_information` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `nis_profile` | essential |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `requirement_id` | REQ-PR-DS-02 |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `rule_id` | RULE-PR-DS-02 |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `technical_status` | compliant |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `thresholds_used_json` | {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "evidence.ev-aurora-encryption.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2026-09-30T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}} |
| Esiti della valutazione | 47b74015-300c-5fe0-ba2c-a279fe186052 (`47b74015-300c-5fe0-ba2c-a279fe186052`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `confidence_level` | medium |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `control_id` | CTRL-PR-DS-11 |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `decision_policy` | all_required |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-backup"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.frequency_within_plan", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.offline_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `errors` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.frequency_within_plan", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.offline_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}] |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `evidence_ids` | ev-aurora-backup |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `governance_status` | none |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `id` | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `information_actions` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `known_violations` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `missing_information` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `nis_profile` | essential |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `requirement_id` | REQ-PR-DS-11 |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `rule_id` | RULE-PR-DS-11 |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `technical_status` | compliant |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `thresholds_used_json` | {"evidence.ev-aurora-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 12de80fb-56ee-5042-b16a-3ac3a4c2e501 (`12de80fb-56ee-5042-b16a-3ac3a4c2e501`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `confidence_level` | medium |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `control_id` | CTRL-PR-DS-11-E |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `decision_policy` | all_required |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-backup", "ev-aurora-restore"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.protected_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.restore_test_successful", "provenance_ids": ["prov-backup"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-aurora-restore.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `errors` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.protected_copy", "provenance_ids": ["prov-backup"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T03:30:00Z", "observed_value": true, "path": "BackupRecord.backup-aurora-core.restore_test_successful", "provenance_ids": ["prov-backup"], "value_status": "known"}] |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `evidence_ids` | ev-aurora-backup, ev-aurora-restore |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `governance_status` | none |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `id` | 9e07e507-09bc-5865-a19e-04a17fa16143 |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `information_actions` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `known_violations` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `missing_information` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `nis_profile` | essential |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `requirement_id` | REQ-PR-DS-11-E |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `rule_id` | RULE-PR-DS-11-E |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `technical_status` | compliant |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `thresholds_used_json` | {"evidence.ev-aurora-backup.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-aurora-restore.freshness": {"maximum_age_days": 90, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-11-12T08:00:00+00:00"}} |
| Esiti della valutazione | 9e07e507-09bc-5865-a19e-04a17fa16143 (`9e07e507-09bc-5865-a19e-04a17fa16143`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `acn_point` | PR.PS-01 |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `confidence_level` | high |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `control_id` | CTRL-PR-PS-01-E |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `decision_policy` | all_required |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-system"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.hardening_baseline_applied", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-system.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `errors` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.hardening_baseline_applied", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `evidence_ids` | ev-aurora-system |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `governance_status` | none |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `id` | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `information_actions` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `known_violations` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `missing_information` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `nis_profile` | essential |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `requirement_id` | REQ-PR-PS-01-E |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `rule_id` | RULE-PR-PS-01-E |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `technical_status` | compliant |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `thresholds_used_json` | {"evidence.ev-aurora-system.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d (`8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `confidence_level` | medium |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `control_id` | CTRL-PR-PS-02 |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `decision_policy` | all_required |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-patch", "ev-aurora-software"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "{supported}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "supported", "path": "SoftwareComponent.software-aurora-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "within_risk_plan", "path": "SoftwareComponent.software-aurora-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-aurora-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `errors` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `evaluated_facts_json` | [{"comparison": "{supported}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "supported", "path": "SoftwareComponent.software-aurora-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "within_risk_plan", "path": "SoftwareComponent.software-aurora-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `evidence_ids` | ev-aurora-patch, ev-aurora-software |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `governance_status` | none |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `id` | b75d1458-c10f-5e12-b482-68e71f582bea |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `information_actions` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `known_violations` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `missing_information` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `nis_profile` | essential |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `requirement_id` | REQ-PR-PS-02 |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `rule_id` | RULE-PR-PS-02 |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `technical_status` | compliant |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `thresholds_used_json` | {"evidence.ev-aurora-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}, "evidence.ev-aurora-software.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | b75d1458-c10f-5e12-b482-68e71f582bea (`b75d1458-c10f-5e12-b482-68e71f582bea`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `confidence_level` | medium |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `control_id` | CTRL-PR-PS-02-E |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `decision_policy` | all_required |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-patch"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "{supported}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "supported", "path": "SoftwareComponent.software-aurora-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "within_risk_plan", "path": "SoftwareComponent.software-aurora-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": true, "path": "SoftwareComponent.software-aurora-core.critical_update_tested", "provenance_ids": ["prov-patch"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `errors` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `evaluated_facts_json` | [{"comparison": "{supported}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "supported", "path": "SoftwareComponent.software-aurora-core.support_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "{current, within_risk_plan}", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": "within_risk_plan", "path": "SoftwareComponent.software-aurora-core.security_update_status", "provenance_ids": ["prov-patch"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "evidence_based", "observed_at": "2026-08-14T07:30:00Z", "observed_value": true, "path": "SoftwareComponent.software-aurora-core.critical_update_tested", "provenance_ids": ["prov-patch"], "value_status": "known"}] |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `evidence_ids` | ev-aurora-patch |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `governance_status` | none |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `id` | 103ed1f8-5443-5e33-b62a-32584c36f36c |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `information_actions` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `known_violations` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `missing_information` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `nis_profile` | essential |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `requirement_id` | REQ-PR-PS-02-E |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `rule_id` | RULE-PR-PS-02-E |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `technical_status` | compliant |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `thresholds_used_json` | {"evidence.ev-aurora-patch.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 103ed1f8-5443-5e33-b62a-32584c36f36c (`103ed1f8-5443-5e33-b62a-32584c36f36c`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `acn_point` | PR.PS-03 |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `confidence_level` | low |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `control_id` | CTRL-PR-PS-03-E |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `decision_policy` | all_required |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-maintenance"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.maintenance_logged", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.secure_disposal_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-maintenance.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `errors` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.maintenance_logged", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.secure_disposal_documented", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `evidence_ids` | ev-aurora-maintenance |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `governance_status` | none |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `id` | 2e43323b-e825-5f6d-bc1c-60e6cf55914e |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `information_actions` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `known_violations` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `missing_information` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `nis_profile` | essential |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `requirement_id` | REQ-PR-PS-03-E |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `rule_id` | RULE-PR-PS-03-E |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `technical_status` | compliant |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `thresholds_used_json` | {"evidence.ev-aurora-maintenance.freshness": {"maximum_age_days": 365, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2027-08-14T08:00:00+00:00"}} |
| Esiti della valutazione | 2e43323b-e825-5f6d-bc1c-60e6cf55914e (`2e43323b-e825-5f6d-bc1c-60e6cf55914e`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `acn_point` | PR.PS-04 |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `confidence_level` | low |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `control_id` | CTRL-PR-PS-04 |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `decision_policy` | all_required |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-log"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.admin_remote_access_logging", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.logs_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.logs_centralized", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.log_retention_within_plan", "provenance_ids": ["prov-governance"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-log.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `errors` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.admin_remote_access_logging", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.logs_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": false, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.logs_centralized", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.log_retention_within_plan", "provenance_ids": ["prov-governance"], "value_status": "known"}] |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `evidence_ids` | ev-aurora-log |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `governance_status` | none |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `id` | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `information_actions` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `known_violations` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `missing_information` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `nis_profile` | essential |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `requirement_id` | REQ-PR-PS-04 |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `rule_id` | RULE-PR-PS-04 |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `technical_status` | compliant |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `thresholds_used_json` | {"evidence.ev-aurora-log.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 0a6e22d2-0365-5bd8-b8b8-40a101f8859e (`0a6e22d2-0365-5bd8-b8b8-40a101f8859e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `acn_point` | PR.IR-01 |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `confidence_level` | low |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `conflicting_information` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `control_id` | CTRL-PR-IR-01 |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `decision_policy` | all_required |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-network"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.remote_access_registry_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.remote_access_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.firewall_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-network.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `errors` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "declared", "observed_at": "2026-08-10T09:00:00Z", "observed_value": true, "path": "asset.remote_access_registry_complete", "provenance_ids": ["prov-governance"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.remote_access_protected", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.firewall_enabled", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `evidence_ids` | ev-aurora-network |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `governance_status` | none |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `id` | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `information_actions` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `known_violations` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `missing_information` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `nis_profile` | essential |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `requirement_id` | REQ-PR-IR-01 |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `rule_id` | RULE-PR-IR-01 |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `selector_decisions` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `technical_remediations` | nessuna |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `technical_status` | compliant |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `thresholds_used_json` | {"evidence.ev-aurora-network.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16 (`fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `acn_point` | PR.IR-03 |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `confidence_level` | high |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `control_id` | CTRL-PR-IR-03-E |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `decision_policy` | all_required |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-emergency"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-emergency.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-emergency.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-emergency.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-emergency.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `errors` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-emergency.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-emergency.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-emergency.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `evidence_ids` | ev-aurora-emergency |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `governance_status` | none |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `id` | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `information_actions` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `known_violations` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `missing_information` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `nis_profile` | essential |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `requirement_id` | REQ-PR-IR-03-E |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `rule_id` | RULE-PR-IR-03-E |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `technical_status` | compliant |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `thresholds_used_json` | {"evidence.ev-aurora-emergency.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 93c7e862-d222-58c6-b6c9-ddab1bea53f5 (`93c7e862-d222-58c6-b6c9-ddab1bea53f5`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `confidence_level` | high |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `conflicting_information` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `control_id` | CTRL-DE-CM-01 |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `decision_policy` | all_required |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-monitoring"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-ids.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-ids.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-ids.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `errors` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-ids.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-ids.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-ids.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `evidence_ids` | ev-aurora-monitoring |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `governance_status` | none |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `id` | aebf7a65-8ae9-53e8-99f0-6101ff923150 |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `information_actions` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `known_violations` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `missing_information` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `nis_profile` | essential |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `requirement_id` | REQ-DE-CM-01 |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `rule_id` | RULE-DE-CM-01 |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `selector_decisions` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `technical_remediations` | nessuna |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `technical_status` | compliant |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `thresholds_used_json` | {"evidence.ev-aurora-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | aebf7a65-8ae9-53e8-99f0-6101ff923150 (`aebf7a65-8ae9-53e8-99f0-6101ff923150`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `confidence_level` | high |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `control_id` | CTRL-DE-CM-01-E |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `decision_policy` | all_required |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-monitoring"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.anomaly_thresholds_configured", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `errors` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "project_baseline", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "asset.anomaly_thresholds_configured", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `evidence_ids` | ev-aurora-monitoring |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `governance_status` | none |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `id` | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `information_actions` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `known_violations` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `missing_information` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `nis_profile` | essential |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `requirement_id` | REQ-DE-CM-01-E |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `rule_id` | RULE-DE-CM-01-E |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `technical_status` | compliant |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `thresholds_used_json` | {"evidence.ev-aurora-monitoring.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 6aa51b0f-b1d1-5df1-953c-c3cbf3d26265 (`6aa51b0f-b1d1-5df1-953c-c3cbf3d26265`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `acn_point` | DE.CM-09 |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `asset_id` | asset-aurora-core |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `confidence_level` | high |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `control_id` | CTRL-DE-CM-09 |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `decision_policy` | all_required |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `decision_trace_json` | {"admitted_evidence_ids": ["ev-aurora-endpoint"], "asset_id": "asset-aurora-core", "conditions": [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-09", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "compliant", "thresholds": {"evidence.ev-aurora-endpoint.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `errors` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `evaluated_facts_json` | [{"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.enabled", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.configured", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.maintained", "provenance_ids": ["prov-config"], "value_status": "known"}, {"comparison": "true", "comparison_result": true, "condition_origin": "regulatory", "mandatory": true, "observation_type": "direct", "observed_at": "2026-08-14T07:00:00Z", "observed_value": true, "path": "SecurityCapability.cap-aurora-endpoint.monitored", "provenance_ids": ["prov-config"], "value_status": "known"}] |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `evidence_ids` | ev-aurora-endpoint |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `governance_status` | none |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `id` | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `information_actions` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `known_violations` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `missing_information` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `nis_profile` | essential |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `reason` | Le condizioni tecniche osservabili della regola risultano soddisfatte. |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `requirement_id` | REQ-DE-CM-09 |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `rule_id` | RULE-DE-CM-09 |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `technical_status` | compliant |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `thresholds_used_json` | {"evidence.ev-aurora-endpoint.freshness": {"maximum_age_days": 30, "origin": "project_baseline", "policy": "evidence_freshness", "policy_version": "EVIDENCE-2026.1", "valid_until": "2027-12-31T23:59:59Z", "value": "2026-09-13T08:00:00+00:00"}} |
| Esiti della valutazione | 31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d (`31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `acn_point` | ID.AM-01 |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `confidence_level` | insufficient |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `control_id` | CTRL-ID-AM-01 |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `decision_policy` | all_required |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `errors` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `governance_status` | none |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `id` | 308648b9-4ca8-5874-ac7b-8ba5f5193384 |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `information_actions` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `known_violations` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `missing_information` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `nis_profile` | essential |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `requirement_id` | REQ-ID-AM-01 |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `risk_clause` | Completezza e granularità sono quelle definite dal perimetro di rischio. |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `rule_id` | RULE-ID-AM-01 |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `technical_status` | not_applicable |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 308648b9-4ca8-5874-ac7b-8ba5f5193384 (`308648b9-4ca8-5874-ac7b-8ba5f5193384`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `acn_point` | ID.AM-02 |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `confidence_level` | insufficient |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `control_id` | CTRL-ID-AM-02 |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `decision_policy` | all_required |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `errors` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `governance_status` | none |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `id` | 80be57b7-7ffd-514f-9195-128b6b9867bf |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `information_actions` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `known_violations` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `missing_information` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `nis_profile` | essential |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `requirement_id` | REQ-ID-AM-02 |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `risk_clause` | Il livello di dettaglio dipende dal rischio e dall'architettura. |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `rule_id` | RULE-ID-AM-02 |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `technical_status` | not_applicable |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 80be57b7-7ffd-514f-9195-128b6b9867bf (`80be57b7-7ffd-514f-9195-128b6b9867bf`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `acn_point` | ID.AM-03 |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `confidence_level` | insufficient |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `control_id` | CTRL-ID-AM-03-E |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `decision_policy` | all_required |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `errors` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `governance_status` | none |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `id` | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `information_actions` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `known_violations` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `missing_information` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `nis_profile` | essential |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `requirement_id` | REQ-ID-AM-03-E |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `risk_clause` | Il perimetro dei flussi deriva dalla valutazione del rischio. |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `rule_id` | RULE-ID-AM-03-E |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `technical_status` | not_applicable |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 86f1f877-dfdf-5c1f-94da-00a58a5f4fcb (`86f1f877-dfdf-5c1f-94da-00a58a5f4fcb`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `acn_point` | ID.AM-04 |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `confidence_level` | insufficient |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `control_id` | CTRL-ID-AM-04 |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `decision_policy` | all_required |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-AM-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `errors` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `governance_status` | none |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `id` | 6c7bf986-038c-52c6-888b-8dbde7b6d114 |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `information_actions` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `known_violations` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `missing_information` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `nis_profile` | essential |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `requirement_id` | REQ-ID-AM-04 |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `risk_clause` | Sono incluse le dipendenze pertinenti al rischio del sistema. |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `rule_id` | RULE-ID-AM-04 |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `technical_status` | not_applicable |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 6c7bf986-038c-52c6-888b-8dbde7b6d114 (`6c7bf986-038c-52c6-888b-8dbde7b6d114`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `confidence_level` | insufficient |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `control_id` | CTRL-ID-RA-01 |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `decision_policy` | all_required |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `errors` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `governance_status` | none |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `id` | 74252cb9-8928-5299-8c80-e125b8fb2698 |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `information_actions` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `known_violations` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `missing_information` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `nis_profile` | essential |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `requirement_id` | REQ-ID-RA-01 |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `risk_clause` | Le fonti monitorate sono selezionate rispetto alle tecnologie inventariate. |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `rule_id` | RULE-ID-RA-01 |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `technical_status` | not_applicable |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 74252cb9-8928-5299-8c80-e125b8fb2698 (`74252cb9-8928-5299-8c80-e125b8fb2698`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `acn_point` | ID.RA-01 |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `confidence_level` | insufficient |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `control_id` | CTRL-ID-RA-01-E |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `decision_policy` | all_required |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `errors` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `governance_status` | none |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `id` | 18a5096f-546c-523f-9da7-193cfcf4f4c5 |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `information_actions` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `known_violations` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `missing_information` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `nis_profile` | essential |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `requirement_id` | REQ-ID-RA-01-E |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `risk_clause` | Tecniche e profondità sono determinate dal rischio e dallo stato dell'arte. |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `rule_id` | RULE-ID-RA-01-E |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `technical_status` | not_applicable |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 18a5096f-546c-523f-9da7-193cfcf4f4c5 (`18a5096f-546c-523f-9da7-193cfcf4f4c5`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `confidence_level` | insufficient |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `control_id` | CTRL-ID-RA-08 |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `decision_policy` | all_required |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `errors` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `governance_status` | none |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `id` | 7408e456-1ed0-5575-8f88-4aa8576dfb70 |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `information_actions` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `known_violations` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `missing_information` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `nis_profile` | essential |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `requirement_id` | REQ-ID-RA-08 |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `risk_clause` | Priorità e termini sono quelli documentati nella valutazione del rischio. |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `rule_id` | RULE-ID-RA-08 |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `technical_status` | not_applicable |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 7408e456-1ed0-5575-8f88-4aa8576dfb70 (`7408e456-1ed0-5575-8f88-4aa8576dfb70`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `acn_point` | ID.RA-08 |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `confidence_level` | insufficient |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `control_id` | CTRL-ID-RA-08-E |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `decision_policy` | all_required |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-ID-RA-08-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `errors` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `governance_status` | none |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `id` | 84b86738-75ad-5f6b-be05-2b0a84330424 |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `information_actions` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `known_violations` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `missing_information` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `nis_profile` | essential |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `requirement_id` | REQ-ID-RA-08-E |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `risk_clause` | Il software critico è individuato dall'inventario e dalla valutazione del rischio. |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `rule_id` | RULE-ID-RA-08-E |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `technical_status` | not_applicable |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 84b86738-75ad-5f6b-be05-2b0a84330424 (`84b86738-75ad-5f6b-be05-2b0a84330424`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `acn_point` | PR.AA-01 |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `confidence_level` | insufficient |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `control_id` | CTRL-PR-AA-01 |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `decision_policy` | all_required |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `errors` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `governance_status` | none |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `id` | ecb880e6-f066-5db5-9e45-19c39f04593e |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `information_actions` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `known_violations` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `missing_information` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `nis_profile` | essential |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `requirement_id` | REQ-PR-AA-01 |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `risk_clause` | Frequenza delle revisioni e requisiti credenziali derivano da ruolo e rischio. |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `rule_id` | RULE-PR-AA-01 |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `technical_status` | not_applicable |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | ecb880e6-f066-5db5-9e45-19c39f04593e (`ecb880e6-f066-5db5-9e45-19c39f04593e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `acn_point` | PR.AA-03 |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `confidence_level` | insufficient |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `conflicting_information` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `control_id` | CTRL-PR-AA-03 |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `decision_policy` | all_required |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-03", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `errors` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `evidence_ids` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `governance_status` | none |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `id` | c5826f34-a2c0-5401-97ee-bf161da61273 |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `information_actions` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `known_violations` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `missing_information` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `nis_profile` | essential |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `requirement_id` | REQ-PR-AA-03 |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `risk_clause` | L'applicazione di MFA dipende dalla rilevanza del sistema e dal rischio degli accessi. |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `rule_id` | RULE-PR-AA-03 |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `selector_decisions` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `technical_remediations` | nessuna |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `technical_status` | not_applicable |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `thresholds_used_json` | {} |
| Esiti della valutazione | c5826f34-a2c0-5401-97ee-bf161da61273 (`c5826f34-a2c0-5401-97ee-bf161da61273`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `acn_point` | PR.AA-05 |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `confidence_level` | insufficient |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `control_id` | CTRL-PR-AA-05 |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `decision_policy` | all_required |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-05", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `errors` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `governance_status` | none |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `id` | 9d835f2b-2713-536c-a708-140ca344a36d |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `information_actions` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `known_violations` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `missing_information` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `nis_profile` | essential |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `requirement_id` | REQ-PR-AA-05 |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `risk_clause` | I privilegi ammessi dipendono dalle funzioni autorizzate. |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `rule_id` | RULE-PR-AA-05 |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `technical_status` | not_applicable |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 9d835f2b-2713-536c-a708-140ca344a36d (`9d835f2b-2713-536c-a708-140ca344a36d`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `acn_point` | PR.AA-06 |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `confidence_level` | insufficient |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `control_id` | CTRL-PR-AA-06 |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `decision_policy` | all_required |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-AA-06", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `errors` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `governance_status` | none |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `id` | 3fb46f9b-7911-5eec-a7ba-f5141f99454c |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `information_actions` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `known_violations` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `missing_information` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `nis_profile` | essential |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `requirement_id` | REQ-PR-AA-06 |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `risk_clause` | Le misure fisiche dipendono da ubicazione minacce e impatto. |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `rule_id` | RULE-PR-AA-06 |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `technical_status` | not_applicable |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 3fb46f9b-7911-5eec-a7ba-f5141f99454c (`3fb46f9b-7911-5eec-a7ba-f5141f99454c`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `acn_point` | PR.DS-01 |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `confidence_level` | insufficient |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `control_id` | CTRL-PR-DS-01 |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `decision_policy` | all_required |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `errors` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `governance_status` | none |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `id` | a11123ce-ca57-57dc-abe8-b8407cd3338e |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `information_actions` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `known_violations` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `missing_information` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `nis_profile` | essential |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `requirement_id` | REQ-PR-DS-01 |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `risk_clause` | Il sottoinsieme osservabile copre i supporti rimovibili; i dispositivi portatili restano fuori perimetro. |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `rule_id` | RULE-PR-DS-01 |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `technical_status` | not_applicable |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | a11123ce-ca57-57dc-abe8-b8407cd3338e (`a11123ce-ca57-57dc-abe8-b8407cd3338e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `acn_point` | PR.DS-02 |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `confidence_level` | insufficient |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `conflicting_information` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `control_id` | CTRL-PR-DS-02 |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `decision_policy` | all_required |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {"origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}}, "undetermined_entity_ids": []} |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `errors` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `evidence_ids` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `governance_status` | none |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `id` | fd96f19d-c801-5696-89e0-9dc5fb3c8534 |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `information_actions` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `known_violations` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `missing_information` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `nis_profile` | essential |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `requirement_id` | REQ-PR-DS-02 |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `risk_clause` | Gli algoritmi ammessi provengono dalla baseline tecnica CRYPTO-BASELINE-2026.1 e non direttamente dalla NIS2. |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `rule_id` | RULE-PR-DS-02 |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `selector_decisions` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `technical_remediations` | nessuna |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `technical_status` | not_applicable |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `thresholds_used_json` | {"origin": "project_baseline", "policy_version": "OPERATIONAL-2026.1", "reference": "tls_minimum", "value": {"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "baseline_id": "CRYPTO-BASELINE-2026.1", "requires_tls": true}} |
| Esiti della valutazione | fd96f19d-c801-5696-89e0-9dc5fb3c8534 (`fd96f19d-c801-5696-89e0-9dc5fb3c8534`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `confidence_level` | insufficient |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `control_id` | CTRL-PR-DS-11 |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `decision_policy` | all_required |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `errors` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `governance_status` | none |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `id` | 5debe74a-081c-5201-92f5-19e36adcd669 |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `information_actions` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `known_violations` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `missing_information` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `nis_profile` | essential |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `requirement_id` | REQ-PR-DS-11 |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `risk_clause` | La frequenza proviene dai piani di continuità e ripristino dichiarati. |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `rule_id` | RULE-PR-DS-11 |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `technical_status` | not_applicable |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 5debe74a-081c-5201-92f5-19e36adcd669 (`5debe74a-081c-5201-92f5-19e36adcd669`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `acn_point` | PR.DS-11 |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `confidence_level` | insufficient |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `control_id` | CTRL-PR-DS-11-E |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `decision_policy` | all_required |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-DS-11-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `errors` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `governance_status` | none |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `id` | 3bb222b7-d9da-53e3-953d-d000c0050ee1 |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `information_actions` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `known_violations` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `missing_information` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `nis_profile` | essential |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `requirement_id` | REQ-PR-DS-11-E |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `risk_clause` | Protezione e periodicità dei test derivano dagli scenari di perdita e compromissione. |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `rule_id` | RULE-PR-DS-11-E |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `technical_status` | not_applicable |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 3bb222b7-d9da-53e3-953d-d000c0050ee1 (`3bb222b7-d9da-53e3-953d-d000c0050ee1`) | `verification_mode` | direct_technical |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `acn_point` | PR.PS-01 |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `confidence_level` | insufficient |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `conflicting_information` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `control_id` | CTRL-PR-PS-01-E |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `decision_policy` | all_required |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `errors` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `evidence_ids` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `governance_status` | none |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `id` | a7413ab8-be2d-5bec-ac74-09168480a66a |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `information_actions` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `known_violations` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `missing_information` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `nis_profile` | essential |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `requirement_id` | REQ-PR-PS-01-E |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `risk_clause` | La baseline è scelta in funzione della tecnologia e dello stato dell'arte. |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `rule_id` | RULE-PR-PS-01-E |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `selector_decisions` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `technical_remediations` | nessuna |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `technical_status` | not_applicable |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `thresholds_used_json` | {} |
| Esiti della valutazione | a7413ab8-be2d-5bec-ac74-09168480a66a (`a7413ab8-be2d-5bec-ac74-09168480a66a`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `confidence_level` | insufficient |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `control_id` | CTRL-PR-PS-02 |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `decision_policy` | all_required |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `errors` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `governance_status` | none |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `id` | 76985295-4f44-5b93-8e6c-40a64c0178a2 |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `information_actions` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `known_violations` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `missing_information` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `nis_profile` | essential |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `requirement_id` | REQ-PR-PS-02 |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `risk_clause` | Le scadenze di patching provengono dal piano di rischio dichiarato. |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `rule_id` | RULE-PR-PS-02 |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `technical_status` | not_applicable |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 76985295-4f44-5b93-8e6c-40a64c0178a2 (`76985295-4f44-5b93-8e6c-40a64c0178a2`) | `verification_mode` | direct_technical |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `acn_point` | PR.PS-02 |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `confidence_level` | insufficient |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `conflicting_information` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `control_id` | CTRL-PR-PS-02-E |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `decision_policy` | all_required |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-02-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `errors` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `evidence_ids` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `governance_status` | none |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `id` | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `information_actions` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `known_violations` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `missing_information` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `nis_profile` | essential |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `requirement_id` | REQ-PR-PS-02-E |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `risk_clause` | Modalità e ambiente di test sono commisurati a rischio e compatibilità. |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `rule_id` | RULE-PR-PS-02-E |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `selector_decisions` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `technical_remediations` | nessuna |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `technical_status` | not_applicable |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `thresholds_used_json` | {} |
| Esiti della valutazione | ebcce0de-43e9-54c1-b55f-b7a1dcd403d6 (`ebcce0de-43e9-54c1-b55f-b7a1dcd403d6`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `acn_point` | PR.PS-03 |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `confidence_level` | insufficient |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `control_id` | CTRL-PR-PS-03-E |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `decision_policy` | all_required |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `errors` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `governance_status` | none |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `id` | 1e029768-3489-5291-81ab-447b96090e2b |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `information_actions` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `known_violations` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `missing_information` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `nis_profile` | essential |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `requirement_id` | REQ-PR-PS-03-E |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `risk_clause` | Le tecniche dipendono da supporto dati e rischio residuo. |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `rule_id` | RULE-PR-PS-03-E |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `technical_status` | not_applicable |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 1e029768-3489-5291-81ab-447b96090e2b (`1e029768-3489-5291-81ab-447b96090e2b`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `acn_point` | PR.PS-04 |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `confidence_level` | insufficient |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `control_id` | CTRL-PR-PS-04 |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `decision_policy` | all_required |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-PS-04", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `errors` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `governance_status` | none |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `id` | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `information_actions` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `known_violations` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `missing_information` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `nis_profile` | essential |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `requirement_id` | REQ-PR-PS-04 |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `risk_clause` | Eventi e durata di conservazione provengono dal piano di logging e dal rischio. |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `rule_id` | RULE-PR-PS-04 |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `technical_status` | not_applicable |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6 (`64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6`) | `verification_mode` | direct_technical |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `acn_point` | PR.IR-01 |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `confidence_level` | insufficient |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `conflicting_information` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `control_id` | CTRL-PR-IR-01 |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `decision_policy` | all_required |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `errors` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `evidence_ids` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `governance_status` | none |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `id` | ed93df21-89bc-51b3-8194-173e3056ad3e |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `information_actions` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `known_violations` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `missing_information` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `nis_profile` | essential |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `requirement_id` | REQ-PR-IR-01 |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `risk_clause` | Regole e canali sono commisurati a esposizione e rischio. |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `rule_id` | RULE-PR-IR-01 |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `selector_decisions` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `technical_remediations` | nessuna |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `technical_status` | not_applicable |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `thresholds_used_json` | {} |
| Esiti della valutazione | ed93df21-89bc-51b3-8194-173e3056ad3e (`ed93df21-89bc-51b3-8194-173e3056ad3e`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `acn_point` | PR.IR-03 |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `confidence_level` | insufficient |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `control_id` | CTRL-PR-IR-03-E |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `decision_policy` | all_required |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-PR-IR-03-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `errors` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `governance_status` | none |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `id` | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `information_actions` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `known_violations` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `missing_information` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `nis_profile` | essential |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `requirement_id` | REQ-PR-IR-03-E |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `risk_clause` | Canali e protezioni dipendono dagli scenari di crisi. |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `rule_id` | RULE-PR-IR-03-E |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `technical_status` | not_applicable |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 444dffd7-95ac-5ba0-b4d2-6a2632b64e30 (`444dffd7-95ac-5ba0-b4d2-6a2632b64e30`) | `verification_mode` | evidence_assisted |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `confidence_level` | insufficient |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `control_id` | CTRL-DE-CM-01 |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `decision_policy` | all_required |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `errors` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `governance_status` | none |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `id` | 4ad2712b-657b-5004-8c35-81b4b3308911 |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `information_actions` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `known_violations` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `missing_information` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `nis_profile` | essential |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `requirement_id` | REQ-DE-CM-01 |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `risk_clause` | La copertura della capacità di rilevamento è basata su architettura e rischio. |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `rule_id` | RULE-DE-CM-01 |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `technical_status` | not_applicable |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 4ad2712b-657b-5004-8c35-81b4b3308911 (`4ad2712b-657b-5004-8c35-81b4b3308911`) | `verification_mode` | direct_technical |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `acn_point` | DE.CM-01 |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `confidence_level` | insufficient |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `conflicting_information` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `control_id` | CTRL-DE-CM-01-E |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `decision_policy` | all_required |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-01-E", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `errors` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `evidence_ids` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `governance_status` | none |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `id` | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `information_actions` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `known_violations` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `missing_information` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `nis_profile` | essential |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `requirement_id` | REQ-DE-CM-01-E |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `risk_clause` | Le soglie sono calibrate sul comportamento atteso e non sono universali. |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `rule_id` | RULE-DE-CM-01-E |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `selector_decisions` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `technical_remediations` | nessuna |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `technical_status` | not_applicable |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `thresholds_used_json` | {} |
| Esiti della valutazione | b5dbc921-ee11-5c0a-b358-09c6c6df7d35 (`b5dbc921-ee11-5c0a-b358-09c6c6df7d35`) | `verification_mode` | direct_technical |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `acn_point` | DE.CM-09 |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `assessment_id` | scenario-aurora-essential-mature |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `asset_id` | asset-aurora-aux |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `confidence_level` | insufficient |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `conflicting_information` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `control_id` | CTRL-DE-CM-09 |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `decision_policy` | all_required |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `decision_trace_json` | {"admitted_evidence_ids": [], "asset_id": "asset-aurora-aux", "conditions": [], "decision_policy": {"allow_partial": false, "entity_aggregation": "all_must_pass", "threshold": null, "type": "all_required"}, "discarded_evidence": [], "evaluated_at": "2026-08-15T10:00:00+00:00", "evaluated_entity_ids": [], "governance_status": "none", "nis_profile": "essential", "rule_id": "RULE-DE-CM-09", "rule_version": "2.1.0", "selector_decisions": [], "technical_status": "not_applicable", "thresholds": {}, "undetermined_entity_ids": []} |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `errors` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `evaluated_at` | 2026-08-15T10:00:00Z |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `evaluated_facts` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `evidence_ids` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `governance_status` | none |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `id` | 2add08be-48c6-51ad-8e32-b9a7fa46f276 |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `information_actions` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `known_violations` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `missing_information` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `nis_profile` | essential |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `reason` | asset con rilevanza NIS nota e negativa |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `requirement_id` | REQ-DE-CM-09 |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `risk_clause` | La capacità è selezionata in base al tipo di endpoint e al rischio. |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `rule_id` | RULE-DE-CM-09 |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `rule_version` | 2.1.0 |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `selector_decisions` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `technical_remediations` | nessuna |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `technical_status` | not_applicable |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `thresholds_used_json` | {} |
| Esiti della valutazione | 2add08be-48c6-51ad-8e32-b9a7fa46f276 (`2add08be-48c6-51ad-8e32-b9a7fa46f276`) | `verification_mode` | direct_technical |

## Inventario completo delle relazioni

| Nodo di partenza | Relazione | Nodo di arrivo |
|---|---|---|
| `asset-aurora-core` | espone (`EXPOSES`) | `svc-aurora-https` |
| `asset-aurora-core` | tratta (`PROCESSES`) | `data-aurora-core` |
| `asset-aurora-core` | è gestito da (`MANAGED_BY`) | `owner-aurora-ops` |
| `vuln-aurora-001` | interessa (`AFFECTS`) | `asset-aurora-core` |
| `asset-aurora-core` | è protetto da (`PROTECTED_BY`) | `cap-aurora-endpoint` |
| `proc-aurora-core` | dipende da (`DEPENDS_ON`) | `asset-aurora-core` |
| `dataset-aurora-normalized-2026` | descrive (`DESCRIBES`) | `org-aurora` |
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
| `8cdb8a9a-4f57-56d5-a48c-b79c9b01e297` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `8cdb8a9a-4f57-56d5-a48c-b79c9b01e297` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-01` |
| `8cdb8a9a-4f57-56d5-a48c-b79c9b01e297` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-01` |
| `8cdb8a9a-4f57-56d5-a48c-b79c9b01e297` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-01` |
| `134c76f6-829c-54f4-8a20-bb2658caed81` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `134c76f6-829c-54f4-8a20-bb2658caed81` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-02` |
| `134c76f6-829c-54f4-8a20-bb2658caed81` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-02` |
| `134c76f6-829c-54f4-8a20-bb2658caed81` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-02` |
| `b868dcad-1d71-59a7-bc03-919729465688` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `b868dcad-1d71-59a7-bc03-919729465688` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-03-E` |
| `b868dcad-1d71-59a7-bc03-919729465688` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-03-E` |
| `b868dcad-1d71-59a7-bc03-919729465688` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-03-E` |
| `b69beb1f-d755-507a-bf1e-cdc747b2f0b8` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `b69beb1f-d755-507a-bf1e-cdc747b2f0b8` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-04` |
| `b69beb1f-d755-507a-bf1e-cdc747b2f0b8` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-04` |
| `b69beb1f-d755-507a-bf1e-cdc747b2f0b8` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-04` |
| `ae8c53db-9242-5d62-a2b4-86acdf5a15a2` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `ae8c53db-9242-5d62-a2b4-86acdf5a15a2` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01` |
| `ae8c53db-9242-5d62-a2b4-86acdf5a15a2` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01` |
| `ae8c53db-9242-5d62-a2b4-86acdf5a15a2` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01` |
| `cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01-E` |
| `cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01-E` |
| `cea56de2-d1c6-5c6b-ba75-5eaf2b1cf0bc` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01-E` |
| `9876425a-cf3f-5d29-b6ef-cc59cdeca1fa` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `9876425a-cf3f-5d29-b6ef-cc59cdeca1fa` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08` |
| `9876425a-cf3f-5d29-b6ef-cc59cdeca1fa` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08` |
| `9876425a-cf3f-5d29-b6ef-cc59cdeca1fa` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08` |
| `e0506187-5d20-5d37-b92e-6878f7cac413` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `e0506187-5d20-5d37-b92e-6878f7cac413` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08-E` |
| `e0506187-5d20-5d37-b92e-6878f7cac413` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08-E` |
| `e0506187-5d20-5d37-b92e-6878f7cac413` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08-E` |
| `a284ba8d-6d80-587f-acaa-eb0379ad632b` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `a284ba8d-6d80-587f-acaa-eb0379ad632b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-01` |
| `a284ba8d-6d80-587f-acaa-eb0379ad632b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-01` |
| `a284ba8d-6d80-587f-acaa-eb0379ad632b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-01` |
| `3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-03` |
| `3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-03` |
| `3a6911a6-b3d7-5ee3-a5c3-4c67853f1e50` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-03` |
| `180002f3-6752-5c1c-9bbe-91390cea7fd0` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `180002f3-6752-5c1c-9bbe-91390cea7fd0` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-05` |
| `180002f3-6752-5c1c-9bbe-91390cea7fd0` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-05` |
| `180002f3-6752-5c1c-9bbe-91390cea7fd0` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-05` |
| `5cf3f0d9-2df6-5f07-9f92-a9faec0b094b` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `5cf3f0d9-2df6-5f07-9f92-a9faec0b094b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-06` |
| `5cf3f0d9-2df6-5f07-9f92-a9faec0b094b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-06` |
| `5cf3f0d9-2df6-5f07-9f92-a9faec0b094b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-06` |
| `8947f3c5-cb85-563e-9f24-2adf1e539e4d` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `8947f3c5-cb85-563e-9f24-2adf1e539e4d` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-01` |
| `8947f3c5-cb85-563e-9f24-2adf1e539e4d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-01` |
| `8947f3c5-cb85-563e-9f24-2adf1e539e4d` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-01` |
| `47b74015-300c-5fe0-ba2c-a279fe186052` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `47b74015-300c-5fe0-ba2c-a279fe186052` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-02` |
| `47b74015-300c-5fe0-ba2c-a279fe186052` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-02` |
| `47b74015-300c-5fe0-ba2c-a279fe186052` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-02` |
| `12de80fb-56ee-5042-b16a-3ac3a4c2e501` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `12de80fb-56ee-5042-b16a-3ac3a4c2e501` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11` |
| `12de80fb-56ee-5042-b16a-3ac3a4c2e501` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11` |
| `12de80fb-56ee-5042-b16a-3ac3a4c2e501` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11` |
| `9e07e507-09bc-5865-a19e-04a17fa16143` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `9e07e507-09bc-5865-a19e-04a17fa16143` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11-E` |
| `9e07e507-09bc-5865-a19e-04a17fa16143` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11-E` |
| `9e07e507-09bc-5865-a19e-04a17fa16143` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11-E` |
| `8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-01-E` |
| `8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-01-E` |
| `8a0d7853-2685-5ed3-8fcd-5f50d8d4da4d` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-01-E` |
| `b75d1458-c10f-5e12-b482-68e71f582bea` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `b75d1458-c10f-5e12-b482-68e71f582bea` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02` |
| `b75d1458-c10f-5e12-b482-68e71f582bea` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02` |
| `b75d1458-c10f-5e12-b482-68e71f582bea` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02` |
| `103ed1f8-5443-5e33-b62a-32584c36f36c` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `103ed1f8-5443-5e33-b62a-32584c36f36c` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02-E` |
| `103ed1f8-5443-5e33-b62a-32584c36f36c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02-E` |
| `103ed1f8-5443-5e33-b62a-32584c36f36c` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02-E` |
| `2e43323b-e825-5f6d-bc1c-60e6cf55914e` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `2e43323b-e825-5f6d-bc1c-60e6cf55914e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-03-E` |
| `2e43323b-e825-5f6d-bc1c-60e6cf55914e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-03-E` |
| `2e43323b-e825-5f6d-bc1c-60e6cf55914e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-03-E` |
| `0a6e22d2-0365-5bd8-b8b8-40a101f8859e` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `0a6e22d2-0365-5bd8-b8b8-40a101f8859e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-04` |
| `0a6e22d2-0365-5bd8-b8b8-40a101f8859e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-04` |
| `0a6e22d2-0365-5bd8-b8b8-40a101f8859e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-04` |
| `fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-01` |
| `fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-01` |
| `fd7f0e11-06a2-5bb8-9b09-0716d8f9fb16` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-01` |
| `93c7e862-d222-58c6-b6c9-ddab1bea53f5` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `93c7e862-d222-58c6-b6c9-ddab1bea53f5` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-03-E` |
| `93c7e862-d222-58c6-b6c9-ddab1bea53f5` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-03-E` |
| `93c7e862-d222-58c6-b6c9-ddab1bea53f5` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-03-E` |
| `aebf7a65-8ae9-53e8-99f0-6101ff923150` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `aebf7a65-8ae9-53e8-99f0-6101ff923150` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01` |
| `aebf7a65-8ae9-53e8-99f0-6101ff923150` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01` |
| `aebf7a65-8ae9-53e8-99f0-6101ff923150` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01` |
| `6aa51b0f-b1d1-5df1-953c-c3cbf3d26265` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `6aa51b0f-b1d1-5df1-953c-c3cbf3d26265` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01-E` |
| `6aa51b0f-b1d1-5df1-953c-c3cbf3d26265` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01-E` |
| `6aa51b0f-b1d1-5df1-953c-c3cbf3d26265` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01-E` |
| `31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d` | valuta (`EVALUATES`) | `asset-aurora-core` |
| `31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-09` |
| `31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-09` |
| `31dfa6a7-6975-59bd-a0aa-4c30b99b5c4d` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-09` |
| `308648b9-4ca8-5874-ac7b-8ba5f5193384` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `308648b9-4ca8-5874-ac7b-8ba5f5193384` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-01` |
| `308648b9-4ca8-5874-ac7b-8ba5f5193384` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-01` |
| `308648b9-4ca8-5874-ac7b-8ba5f5193384` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-01` |
| `80be57b7-7ffd-514f-9195-128b6b9867bf` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `80be57b7-7ffd-514f-9195-128b6b9867bf` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-02` |
| `80be57b7-7ffd-514f-9195-128b6b9867bf` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-02` |
| `80be57b7-7ffd-514f-9195-128b6b9867bf` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-02` |
| `86f1f877-dfdf-5c1f-94da-00a58a5f4fcb` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `86f1f877-dfdf-5c1f-94da-00a58a5f4fcb` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-03-E` |
| `86f1f877-dfdf-5c1f-94da-00a58a5f4fcb` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-03-E` |
| `86f1f877-dfdf-5c1f-94da-00a58a5f4fcb` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-03-E` |
| `6c7bf986-038c-52c6-888b-8dbde7b6d114` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `6c7bf986-038c-52c6-888b-8dbde7b6d114` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-AM-04` |
| `6c7bf986-038c-52c6-888b-8dbde7b6d114` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-AM-04` |
| `6c7bf986-038c-52c6-888b-8dbde7b6d114` | applica la regola (`APPLIES_RULE`) | `RULE-ID-AM-04` |
| `74252cb9-8928-5299-8c80-e125b8fb2698` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `74252cb9-8928-5299-8c80-e125b8fb2698` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01` |
| `74252cb9-8928-5299-8c80-e125b8fb2698` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01` |
| `74252cb9-8928-5299-8c80-e125b8fb2698` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01` |
| `18a5096f-546c-523f-9da7-193cfcf4f4c5` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `18a5096f-546c-523f-9da7-193cfcf4f4c5` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-01-E` |
| `18a5096f-546c-523f-9da7-193cfcf4f4c5` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-01-E` |
| `18a5096f-546c-523f-9da7-193cfcf4f4c5` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-01-E` |
| `7408e456-1ed0-5575-8f88-4aa8576dfb70` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `7408e456-1ed0-5575-8f88-4aa8576dfb70` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08` |
| `7408e456-1ed0-5575-8f88-4aa8576dfb70` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08` |
| `7408e456-1ed0-5575-8f88-4aa8576dfb70` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08` |
| `84b86738-75ad-5f6b-be05-2b0a84330424` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `84b86738-75ad-5f6b-be05-2b0a84330424` | è esito del controllo (`RESULT_OF`) | `CTRL-ID-RA-08-E` |
| `84b86738-75ad-5f6b-be05-2b0a84330424` | è riconducibile al requisito (`TRACES_TO`) | `REQ-ID-RA-08-E` |
| `84b86738-75ad-5f6b-be05-2b0a84330424` | applica la regola (`APPLIES_RULE`) | `RULE-ID-RA-08-E` |
| `ecb880e6-f066-5db5-9e45-19c39f04593e` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `ecb880e6-f066-5db5-9e45-19c39f04593e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-01` |
| `ecb880e6-f066-5db5-9e45-19c39f04593e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-01` |
| `ecb880e6-f066-5db5-9e45-19c39f04593e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-01` |
| `c5826f34-a2c0-5401-97ee-bf161da61273` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `c5826f34-a2c0-5401-97ee-bf161da61273` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-03` |
| `c5826f34-a2c0-5401-97ee-bf161da61273` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-03` |
| `c5826f34-a2c0-5401-97ee-bf161da61273` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-03` |
| `9d835f2b-2713-536c-a708-140ca344a36d` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `9d835f2b-2713-536c-a708-140ca344a36d` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-05` |
| `9d835f2b-2713-536c-a708-140ca344a36d` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-05` |
| `9d835f2b-2713-536c-a708-140ca344a36d` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-05` |
| `3fb46f9b-7911-5eec-a7ba-f5141f99454c` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `3fb46f9b-7911-5eec-a7ba-f5141f99454c` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-AA-06` |
| `3fb46f9b-7911-5eec-a7ba-f5141f99454c` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-AA-06` |
| `3fb46f9b-7911-5eec-a7ba-f5141f99454c` | applica la regola (`APPLIES_RULE`) | `RULE-PR-AA-06` |
| `a11123ce-ca57-57dc-abe8-b8407cd3338e` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `a11123ce-ca57-57dc-abe8-b8407cd3338e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-01` |
| `a11123ce-ca57-57dc-abe8-b8407cd3338e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-01` |
| `a11123ce-ca57-57dc-abe8-b8407cd3338e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-01` |
| `fd96f19d-c801-5696-89e0-9dc5fb3c8534` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `fd96f19d-c801-5696-89e0-9dc5fb3c8534` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-02` |
| `fd96f19d-c801-5696-89e0-9dc5fb3c8534` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-02` |
| `fd96f19d-c801-5696-89e0-9dc5fb3c8534` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-02` |
| `5debe74a-081c-5201-92f5-19e36adcd669` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `5debe74a-081c-5201-92f5-19e36adcd669` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11` |
| `5debe74a-081c-5201-92f5-19e36adcd669` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11` |
| `5debe74a-081c-5201-92f5-19e36adcd669` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11` |
| `3bb222b7-d9da-53e3-953d-d000c0050ee1` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `3bb222b7-d9da-53e3-953d-d000c0050ee1` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-DS-11-E` |
| `3bb222b7-d9da-53e3-953d-d000c0050ee1` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-DS-11-E` |
| `3bb222b7-d9da-53e3-953d-d000c0050ee1` | applica la regola (`APPLIES_RULE`) | `RULE-PR-DS-11-E` |
| `a7413ab8-be2d-5bec-ac74-09168480a66a` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `a7413ab8-be2d-5bec-ac74-09168480a66a` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-01-E` |
| `a7413ab8-be2d-5bec-ac74-09168480a66a` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-01-E` |
| `a7413ab8-be2d-5bec-ac74-09168480a66a` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-01-E` |
| `76985295-4f44-5b93-8e6c-40a64c0178a2` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `76985295-4f44-5b93-8e6c-40a64c0178a2` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02` |
| `76985295-4f44-5b93-8e6c-40a64c0178a2` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02` |
| `76985295-4f44-5b93-8e6c-40a64c0178a2` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02` |
| `ebcce0de-43e9-54c1-b55f-b7a1dcd403d6` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `ebcce0de-43e9-54c1-b55f-b7a1dcd403d6` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-02-E` |
| `ebcce0de-43e9-54c1-b55f-b7a1dcd403d6` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-02-E` |
| `ebcce0de-43e9-54c1-b55f-b7a1dcd403d6` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-02-E` |
| `1e029768-3489-5291-81ab-447b96090e2b` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `1e029768-3489-5291-81ab-447b96090e2b` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-03-E` |
| `1e029768-3489-5291-81ab-447b96090e2b` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-03-E` |
| `1e029768-3489-5291-81ab-447b96090e2b` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-03-E` |
| `64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-PS-04` |
| `64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-PS-04` |
| `64a3818c-ae8d-5d4c-aa84-c8e14eb2bce6` | applica la regola (`APPLIES_RULE`) | `RULE-PR-PS-04` |
| `ed93df21-89bc-51b3-8194-173e3056ad3e` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `ed93df21-89bc-51b3-8194-173e3056ad3e` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-01` |
| `ed93df21-89bc-51b3-8194-173e3056ad3e` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-01` |
| `ed93df21-89bc-51b3-8194-173e3056ad3e` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-01` |
| `444dffd7-95ac-5ba0-b4d2-6a2632b64e30` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `444dffd7-95ac-5ba0-b4d2-6a2632b64e30` | è esito del controllo (`RESULT_OF`) | `CTRL-PR-IR-03-E` |
| `444dffd7-95ac-5ba0-b4d2-6a2632b64e30` | è riconducibile al requisito (`TRACES_TO`) | `REQ-PR-IR-03-E` |
| `444dffd7-95ac-5ba0-b4d2-6a2632b64e30` | applica la regola (`APPLIES_RULE`) | `RULE-PR-IR-03-E` |
| `4ad2712b-657b-5004-8c35-81b4b3308911` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `4ad2712b-657b-5004-8c35-81b4b3308911` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01` |
| `4ad2712b-657b-5004-8c35-81b4b3308911` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01` |
| `4ad2712b-657b-5004-8c35-81b4b3308911` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01` |
| `b5dbc921-ee11-5c0a-b358-09c6c6df7d35` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `b5dbc921-ee11-5c0a-b358-09c6c6df7d35` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-01-E` |
| `b5dbc921-ee11-5c0a-b358-09c6c6df7d35` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-01-E` |
| `b5dbc921-ee11-5c0a-b358-09c6c6df7d35` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-01-E` |
| `2add08be-48c6-51ad-8e32-b9a7fa46f276` | valuta (`EVALUATES`) | `asset-aurora-aux` |
| `2add08be-48c6-51ad-8e32-b9a7fa46f276` | è esito del controllo (`RESULT_OF`) | `CTRL-DE-CM-09` |
| `2add08be-48c6-51ad-8e32-b9a7fa46f276` | è riconducibile al requisito (`TRACES_TO`) | `REQ-DE-CM-09` |
| `2add08be-48c6-51ad-8e32-b9a7fa46f276` | applica la regola (`APPLIES_RULE`) | `RULE-DE-CM-09` |
