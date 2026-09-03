"""Modelli del dominio e contratto canonico dei dati normalizzati.

Le classi di questo file non conoscono YAML, filesystem, FastAPI o Neo4j:
descrivono soltanto entità, valori e risultati del problema applicativo.
"""

from __future__ import annotations

import re
from datetime import datetime
from ipaddress import ip_address
from typing import Any, Generic, Literal, TypeVar

from pydantic import (
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_core import InitErrorDetails, PydanticCustomError

from .enums import (
    ApplicabilityReasonCode,
    ApplicabilityStatus,
    AssetType,
    ComplianceStatus,
    ConditionOrigin,
    ConfidenceLevel,
    DecisionPolicyType,
    EmptyCollectionPolicy,
    EntityAggregationPolicy,
    EvidenceSourceCategory,
    GovernanceStatus,
    InventoryScope,
    InventoryStatus,
    KnowledgeValueStatus,
    NisProfile,
    ObservationType,
    SelectorStatus,
    Severity,
    UnknownCause,
    VerificationMode,
)

T = TypeVar("T")


class StrictModel(BaseModel):
    """Base Pydantic che rifiuta campi non previsti dal contratto."""

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def timezone_aware_datetimes(self) -> StrictModel:
        """Rifiuta timestamp senza fuso, anche dentro liste e KnowledgeValue."""

        def check(value: Any) -> None:
            if isinstance(value, datetime):
                if value.tzinfo is None or value.utcoffset() is None:
                    raise ValueError("le date devono includere il fuso orario")
                return
            if isinstance(value, BaseModel):
                for nested in value.__dict__.values():
                    check(nested)
                return
            if isinstance(value, dict):
                for nested in value.values():
                    check(nested)
                return
            if isinstance(value, (list, tuple, set)):
                for nested in value:
                    check(nested)

        for field_value in self.__dict__.values():
            check(field_value)
        return self


class KnowledgeValue(StrictModel, Generic[T]):
    """Valore accompagnato da stato di conoscenza e riferimenti alle fonti."""

    status: KnowledgeValueStatus
    value: T | None = None
    provenance_ids: list[str] = Field(default_factory=list)
    observation_type: ObservationType | None = None
    observed_at: datetime | None = None
    unknown_cause: UnknownCause | None = None

    @model_validator(mode="before")
    @classmethod
    def required_status_metadata(cls, data: Any) -> Any:
        """Richiede al produttore i metadati che il Modulo 3 non può inferire."""
        if not isinstance(data, dict):
            return data

        errors: list[InitErrorDetails] = []
        status = data.get("status")
        if status == KnowledgeValueStatus.KNOWN and data.get("observation_type") is None:
            errors.append(
                InitErrorDetails(
                    type=PydanticCustomError(
                        "missing_observation_type",
                        "observation_type è obbligatorio quando status='known'",
                    ),
                    loc=("observation_type",),
                    input=data,
                )
            )
        if status == KnowledgeValueStatus.UNKNOWN and data.get("unknown_cause") is None:
            errors.append(
                InitErrorDetails(
                    type=PydanticCustomError(
                        "missing_unknown_cause",
                        "unknown_cause è obbligatorio quando status='unknown'",
                    ),
                    loc=("unknown_cause",),
                    input=data,
                )
            )
        if status == KnowledgeValueStatus.CONFLICTING and data.get("unknown_cause") is None:
            errors.append(
                InitErrorDetails(
                    type=PydanticCustomError(
                        "missing_unknown_cause",
                        "unknown_cause è obbligatorio quando status='conflicting'",
                    ),
                    loc=("unknown_cause",),
                    input=data,
                )
            )
        if errors:
            raise ValidationError.from_exception_data(cls.__name__, errors)
        return data

    @model_validator(mode="after")
    def coherent(self) -> KnowledgeValue[T]:
        """Impedisce di confondere un valore falso con un valore sconosciuto."""
        if self.status == KnowledgeValueStatus.KNOWN and self.value is None:
            raise ValueError("known richiede un valore")
        if self.status != KnowledgeValueStatus.KNOWN and self.value is not None:
            raise ValueError("solo known può contenere un valore")
        if self.status == KnowledgeValueStatus.CONFLICTING and len(self.provenance_ids) < 2:
            raise ValueError("conflicting richiede almeno due fonti")
        if (
            self.status == KnowledgeValueStatus.CONFLICTING
            and self.unknown_cause != UnknownCause.CONFLICTING_SOURCES
        ):
            raise ValueError("conflicting richiede unknown_cause='conflicting_sources'")
        if self.status == KnowledgeValueStatus.KNOWN and self.unknown_cause is not None:
            raise ValueError("known non può dichiarare unknown_cause")
        return self


class InventoryState(StrictModel):
    """Completezza dichiarata di una collezione entro uno scope esplicito."""

    id: str
    entity_type: str
    scope: InventoryScope
    scope_id: str
    status: InventoryStatus
    unknown_cause: UnknownCause | None = None
    observed_at: datetime
    provenance_ids: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def coherent_inventory(self) -> InventoryState:
        if self.status in {InventoryStatus.UNKNOWN, InventoryStatus.INCOMPLETE} and self.unknown_cause is None:
            self.unknown_cause = UnknownCause.NOT_DECLARED
        if self.status == InventoryStatus.COMPLETE and self.unknown_cause is not None:
            raise ValueError("un inventario complete non può avere una causa di incompletezza")
        return self


class DatasetInfo(StrictModel):
    """Metadati che identificano la fotografia normalizzata dell'ambiente."""

    id: str
    name: str
    generated_at: datetime
    description: str
    source_systems: list[str]

class Organization(StrictModel):
    """Organizzazione fittizia o reale cui appartiene il dataset."""

    id: str
    name: str
    nis_profile: NisProfile
    risk_assessment_reference: str
    acn_specification: str


class ProvenanceRecord(StrictModel):
    """Descrive origine, metodo e affidabilità di un'informazione."""

    id: str
    source: str
    source_type: str
    source_category: EvidenceSourceCategory
    collected_at: datetime
    method: str
    reliability: str
    original_reference: str | None = None
    notes: str | None = None


class Asset(StrictModel):
    """Sistema, applicazione o componente valutato dai controlli tecnici."""

    id: str
    name: str
    asset_type: AssetType
    description: str = ""
    hostname: str | None = None
    ip_addresses: list[str] = Field(default_factory=list)
    mac_addresses: list[str] = Field(default_factory=list)
    environment: str
    network_segment: KnowledgeValue[str]
    internet_exposed: KnowledgeValue[bool]
    nis_relevant: KnowledgeValue[bool]
    criticality: Severity
    impact_level: Severity
    exposure_level: Severity
    risk_assessment_reference: str
    lifecycle_status: str
    operating_system: str | None = None
    operating_system_version: str | None = None
    support_status: str | None = None
    owner_id: str | None = None
    process_ids: list[str] = Field(default_factory=list)
    data_object_ids: list[str] = Field(default_factory=list)
    service_ids: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)
    properties: dict[str, KnowledgeValue[Any]] = Field(default_factory=dict)

    @field_validator("ip_addresses")
    @classmethod
    def ips(cls, values: list[str]) -> list[str]:
        """Convalida ogni indirizzo usando il parser standard IP."""
        for value in values:
            ip_address(value)
        return values


class Service(StrictModel):
    """Servizio di rete esposto o utilizzato da un asset."""

    id: str
    asset_id: str
    name: str
    port: int = Field(ge=1, le=65535)
    protocol: str
    transport_protocol: str
    application_protocol: str
    product: str | None = None
    version: str | None = None
    authorized: KnowledgeValue[bool]
    internet_exposed: KnowledgeValue[bool]
    encrypted: KnowledgeValue[bool]
    tls_enabled: KnowledgeValue[bool]
    tls_versions: KnowledgeValue[list[str]]
    certificate_expiration: KnowledgeValue[datetime]
    obsolete_protocol: KnowledgeValue[bool]
    encryption_configuration: KnowledgeValue[str]
    cryptographic_baseline_id: str | None = None
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class Vulnerability(StrictModel):
    """Vulnerabilità nota associata a un asset e, facoltativamente, servizio."""

    id: str
    asset_id: str
    service_id: str | None = None
    cve: str | None = None
    title: str
    description: str = ""
    severity: Severity
    cvss_score: float = Field(ge=0, le=10)
    component: str
    detected_at: datetime
    patch_available: KnowledgeValue[bool]
    remediation_status: KnowledgeValue[str]
    remediation_due_date: datetime | None = None
    accepted_exception: KnowledgeValue[bool]
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)

    @field_validator("cve")
    @classmethod
    def valid_cve(cls, value: str | None) -> str | None:
        """Controlla la forma dell'identificativo CVE quando presente."""
        if value and not re.fullmatch(r"CVE-\d{4}-\d{4,}", value):
            raise ValueError("formato CVE non valido")
        return value


class ResponsibleParty(StrictModel):
    """Responsabile rappresentato tramite riferimento non sensibile."""

    id: str
    name: str
    role: str
    contact_reference: str
    provenance_ids: list[str] = Field(default_factory=list)


class Process(StrictModel):
    """Processo utile a contestualizzare criticità e dipendenze degli asset."""

    id: str
    name: str
    description: str
    criticality: str
    asset_ids: list[str]
    data_object_ids: list[str]
    owner_id: str
    provenance_ids: list[str] = Field(default_factory=list)


class DataObject(StrictModel):
    """Categoria di dati trattata dagli asset, senza contenuti personali reali."""

    id: str
    name: str
    classification: str
    description: str
    encrypted_at_rest: KnowledgeValue[bool]
    encrypted_in_transit: KnowledgeValue[bool]
    removable_media: KnowledgeValue[bool]
    removable_media_encrypted: KnowledgeValue[bool]
    encryption_configuration: KnowledgeValue[str]
    asset_ids: list[str]
    provenance_ids: list[str] = Field(default_factory=list)


class Evidence(StrictModel):
    """Evidenza tecnica o documentale già raccolta e normalizzata."""

    id: str
    evidence_type: str
    title: str
    description: str
    source: str
    source_category: EvidenceSourceCategory
    collected_at: datetime
    valid_until: datetime | None = None
    reliability: str
    content: dict[str, Any] = Field(default_factory=dict)
    file_reference: str | None = None
    asset_ids: list[str] = Field(default_factory=list)
    service_ids: list[str] = Field(default_factory=list)
    vulnerability_ids: list[str] = Field(default_factory=list)
    control_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class SoftwareComponent(StrictModel):
    """Componente software inventariato e osservato su uno specifico asset."""

    id: str
    asset_id: str
    name: str
    version: KnowledgeValue[str]
    authorized: KnowledgeValue[bool]
    support_status: KnowledgeValue[str]
    security_update_status: KnowledgeValue[str]
    last_security_update_at: KnowledgeValue[datetime]
    critical_update_tested: KnowledgeValue[bool]
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class Account(StrictModel):
    """Utenza normalizzata usata dai controlli ACN di identità e accesso."""

    id: str
    asset_id: str
    account_type: str
    individual: KnowledgeValue[bool]
    authorized: KnowledgeValue[bool]
    privileged: KnowledgeValue[bool]
    remote_access: KnowledgeValue[bool]
    mfa_enabled: KnowledgeValue[bool]
    credentials_managed: KnowledgeValue[bool]
    least_privilege: KnowledgeValue[bool]
    separate_admin_account: KnowledgeValue[bool]
    last_reviewed_at: KnowledgeValue[datetime]
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class NetworkFlow(StrictModel):
    """Flusso di rete autorizzato o osservato associato a un sistema."""

    id: str
    asset_id: str
    source: str
    destination: str
    direction: str
    transport_protocol: str
    application_protocol: str
    port: int | None = Field(default=None, ge=1, le=65535)
    authorized: KnowledgeValue[bool]
    encrypted: KnowledgeValue[bool]
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class NetworkInterface(StrictModel):
    """Interfaccia di rete censita separatamente dagli indirizzi dell'asset."""

    id: str
    asset_id: str
    name: str
    interface_type: str
    enabled: KnowledgeValue[bool]
    authorized: KnowledgeValue[bool]
    ip_addresses: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class BackupRecord(StrictModel):
    """Stato del piano di backup, delle copie e delle prove di ripristino."""

    id: str
    asset_id: str
    plan_reference: str
    last_success_at: KnowledgeValue[datetime]
    frequency_within_plan: KnowledgeValue[bool]
    offline_copy: KnowledgeValue[bool]
    protected_copy: KnowledgeValue[bool]
    restore_test_at: KnowledgeValue[datetime]
    restore_test_successful: KnowledgeValue[bool]
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class SecurityCapability(StrictModel):
    """Capacità tecnica installata o configurata a protezione di un asset."""

    id: str
    asset_id: str
    capability_type: str
    enabled: KnowledgeValue[bool]
    configured: KnowledgeValue[bool]
    maintained: KnowledgeValue[bool]
    monitored: KnowledgeValue[bool]
    configuration_reference: str | None = None
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class TechnicalException(StrictModel):
    """Deroga tecnica che richiede sempre una decisione umana esplicita."""

    id: str
    asset_id: str
    control_id: str
    rationale: str
    compensating_measure: str
    residual_risk: Severity
    approval_reference: str
    valid_until: datetime | None = None
    evidence_ids: list[str] = Field(default_factory=list)
    provenance_ids: list[str] = Field(default_factory=list)


class Requirement(StrictModel):
    """Requisito di riferimento cui sono collegati uno o più controlli."""

    id: str
    framework: str
    title: str
    description: str
    source_reference: str
    source_document: str
    source_version: str
    source_url: str
    acn_measure: str
    acn_point: str
    article_24_element: str
    applicable_profiles: list[NisProfile]
    verification_mode: VerificationMode
    risk_clause: str
    scope_note: str
    control_ids: list[str]
    manual_only_reason: str | None = None


class Control(StrictModel):
    """Controllo tecnico applicabile a determinate categorie di asset."""

    id: str
    requirement_id: str
    title: str
    description: str
    technical_area: str
    applicable_asset_types: list[AssetType]
    required_properties: list[str]
    required_evidence_types: list[str]
    applicable_profiles: list[NisProfile]
    relevant_system_required: bool = True
    verification_mode: VerificationMode
    rule_ids: list[str]


class Relationship(StrictModel):
    """Arco esplicito soggetto-predicato-oggetto del Knowledge Graph."""

    id: str
    subject_id: str
    predicate: str
    object_id: str
    provenance_ids: list[str] = Field(default_factory=list)


class NormalizedEnvironment(StrictModel):
    """Documento radice che costituisce l'unico ingresso della pipeline."""

    schema_version: str
    dataset: DatasetInfo
    organization: Organization
    responsible_parties: list[ResponsibleParty]
    processes: list[Process]
    data_objects: list[DataObject]
    assets: list[Asset]
    services: list[Service]
    software_components: list[SoftwareComponent]
    accounts: list[Account]
    network_interfaces: list[NetworkInterface] = Field(default_factory=list)
    network_flows: list[NetworkFlow]
    backups: list[BackupRecord]
    security_capabilities: list[SecurityCapability]
    technical_exceptions: list[TechnicalException]
    vulnerabilities: list[Vulnerability]
    evidences: list[Evidence]
    requirements: list[Requirement]
    controls: list[Control]
    relationships: list[Relationship]
    provenance_records: list[ProvenanceRecord]
    inventory_states: list[InventoryState] = Field(default_factory=list)


class RuleCondition(StrictModel):
    """Condizione dichiarata nel catalogo e valutabile in modo auditabile."""

    id: str
    path: str
    mandatory: bool = True
    origin: ConditionOrigin = ConditionOrigin.REGULATORY
    selector: dict[str, Any] = Field(default_factory=dict)
    remediation: str | None = None


class DecisionPolicy(StrictModel):
    """Policy esplicita che sostituisce euristiche basate sul conteggio dei true."""

    type: DecisionPolicyType = DecisionPolicyType.ALL_REQUIRED
    entity_aggregation: EntityAggregationPolicy = EntityAggregationPolicy.ALL_MUST_PASS
    allow_partial: bool = False
    threshold: float | None = None

    @model_validator(mode="after")
    def coherent_threshold(self) -> DecisionPolicy:
        threshold_required = (
            self.type == DecisionPolicyType.THRESHOLD
            or self.entity_aggregation == EntityAggregationPolicy.THRESHOLD
        )
        if threshold_required and self.threshold is None:
            raise ValueError("threshold è obbligatoria per la policy threshold")
        if self.threshold is not None and not 0 < self.threshold <= 1:
            raise ValueError("threshold deve essere compresa nell'intervallo (0, 1]")
        return self


class Rule(StrictModel):
    """Configurazione versionata che seleziona un evaluator consentito."""

    id: str
    version: str
    control_id: str
    requirement_id: str
    title: str
    description: str
    evaluator: str
    applicability: dict[
        Literal["has_removable_media", "has_internet_exposed_services"], bool
    ] = Field(default_factory=dict)
    required_properties: list[str]
    required_evidence_types: list[str]
    parameters: dict[str, Any] = Field(default_factory=dict)
    applicable_profiles: list[NisProfile]
    relevant_system_required: bool = True
    verification_mode: VerificationMode
    risk_clause: str
    messages: dict[str, str]
    recommendation: str | None = None
    conditions: list[RuleCondition] = Field(default_factory=list)
    decision_policy: DecisionPolicy = Field(default_factory=DecisionPolicy)
    empty_collection_policy: EmptyCollectionPolicy = EmptyCollectionPolicy.NOT_VERIFIABLE
    allowed_outcomes: list[ComplianceStatus] = Field(
        default_factory=lambda: [
            ComplianceStatus.COMPLIANT,
            ComplianceStatus.NON_COMPLIANT,
            ComplianceStatus.NOT_VERIFIABLE,
            ComplianceStatus.NOT_APPLICABLE,
        ]
    )
    information_actions: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def explicit_policy_defaults(self) -> Rule:
        """Materializza policy complete anche per cataloghi 2.0 legacy."""
        if not self.conditions:
            paths = self.required_properties or [
                f"asset.{value}" for value in self.parameters.get("properties", [])
            ]
            self.conditions = [
                RuleCondition(
                    id=f"{self.id}:{path}",
                    path=path,
                    mandatory=True,
                    origin=(
                        ConditionOrigin.PROJECT_BASELINE
                        if any(token in path for token in ("tls", "retention", "threshold"))
                        else ConditionOrigin.REGULATORY
                    ),
                    remediation=self.recommendation,
                )
                for path in paths
            ]
        if self.decision_policy.allow_partial or (
            ComplianceStatus.PARTIALLY_COMPLIANT in self.allowed_outcomes
        ):
            raise ValueError(
                "partially_compliant non è prodotto dal motore decisionale corrente"
            )
        if not self.information_actions:
            self.information_actions = {
                "not_declared": "Acquisire e dichiarare il dato mancante.",
                "stale_information": "Aggiornare l'evidenza o il dato scaduto.",
                "collection_failed": "Correggere il collector e ripetere l'acquisizione.",
                "source_unavailable": "Ripristinare o sostituire la fonte informativa.",
            }
        return self


class ApplicabilityResult(StrictModel):
    """Decisione motivata che precede sempre la valutazione del controllo."""

    status: ApplicabilityStatus
    reason_code: ApplicabilityReasonCode
    reasons: list[str]
    evaluated_conditions: list[str]
    missing_information: list[str] = Field(default_factory=list)
    selector_decisions: list[SelectorDecision] = Field(default_factory=list)
    selected_entity_ids: list[str] = Field(default_factory=list)
    undetermined_entity_ids: list[str] = Field(default_factory=list)

    @property
    def applicable(self) -> bool:
        """Compatibilità di lettura: vero soltanto per lo stato applicabile."""
        return self.status == ApplicabilityStatus.APPLICABLE


class EvaluatedFact(StrictModel):
    """Singolo fatto consultato e confronto effettuato dall'evaluator."""

    path: str
    observed_value: Any = None
    value_status: str
    comparison: str
    comparison_result: bool | None
    provenance_ids: list[str] = Field(default_factory=list)
    mandatory: bool = True
    condition_origin: ConditionOrigin = ConditionOrigin.REGULATORY
    observation_type: ObservationType | None = None
    observed_at: datetime | None = None


class SelectorDecision(StrictModel):
    entity_id: str
    status: SelectorStatus
    selector_type: str
    evaluated_fields: list[str]
    missing_information: list[str] = Field(default_factory=list)
    conflicting_information: list[ConflictRecord] = Field(default_factory=list)


class ViolationRecord(StrictModel):
    path: str
    observed_value: Any = None
    comparison: str
    remediation: str | None = None


class ConflictRecord(StrictModel):
    path: str
    provenance_ids: list[str] = Field(default_factory=list)
    reason: str = "conflicting_sources"


class AssessmentResult(StrictModel):
    """Esito tracciabile per una coppia valutata o esclusa esplicitamente."""

    id: str
    assessment_id: str
    asset_id: str
    control_id: str
    requirement_id: str
    rule_id: str
    rule_version: str
    technical_status: ComplianceStatus = Field(
        validation_alias=AliasChoices("technical_status", "status")
    )
    governance_status: GovernanceStatus = GovernanceStatus.NONE
    reason: str
    evaluated_facts: list[EvaluatedFact]
    evidence_ids: list[str]
    missing_information: list[str]
    recommendation: str | None
    nis_profile: NisProfile
    acn_point: str
    verification_mode: VerificationMode
    risk_clause: str
    technical_exception_id: str | None = None
    evaluated_at: datetime
    confidence_level: ConfidenceLevel = ConfidenceLevel.INSUFFICIENT
    known_violations: list[ViolationRecord] = Field(default_factory=list)
    conflicting_information: list[ConflictRecord] = Field(default_factory=list)
    selector_decisions: list[SelectorDecision] = Field(default_factory=list)
    thresholds_used: dict[str, Any] = Field(default_factory=dict)
    decision_policy: str = "all_required"
    decision_trace: dict[str, Any] = Field(default_factory=dict)
    technical_remediations: list[str] = Field(default_factory=list)
    information_actions: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)

    @property
    def status(self) -> ComplianceStatus:
        """Alias v2 temporaneo per i chiamanti che leggono ancora ``status``."""
        return self.technical_status


class Finding(StrictModel):
    """Scostamento tecnico derivato da un risultato, non giudizio legale globale."""

    id: str
    assessment_result_id: str
    asset_id: str
    control_id: str
    title: str
    description: str
    severity: Severity
    evidence_ids: list[str] = Field(default_factory=list)
    recommendation: str | None = None
