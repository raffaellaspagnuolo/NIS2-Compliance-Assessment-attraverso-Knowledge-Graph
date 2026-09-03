"""Enumerazioni condivise dal dominio.

Questo file raccoglie i valori chiusi usati dal contratto dati e dal motore di
valutazione. Centralizzarli evita stringhe incoerenti nei vari moduli.
"""

from enum import StrEnum


class KnowledgeValueStatus(StrEnum):
    """Descrive quanto conosciamo di una proprietà, separatamente dal valore."""

    KNOWN = "known"
    UNKNOWN = "unknown"
    NOT_APPLICABLE = "not_applicable"
    CONFLICTING = "conflicting"


class ObservationType(StrEnum):
    """Modalità con cui un valore è stato ottenuto."""

    DIRECT = "direct"
    DERIVED = "derived"
    DECLARED = "declared"
    EVIDENCE_BASED = "evidence_based"


class UnknownCause(StrEnum):
    """Causa operativa di una conoscenza insufficiente."""

    NOT_COLLECTED = "not_collected"
    COLLECTION_FAILED = "collection_failed"
    SOURCE_UNAVAILABLE = "source_unavailable"
    CONFLICTING_SOURCES = "conflicting_sources"
    NOT_DECLARED = "not_declared"
    STALE_INFORMATION = "stale_information"


class InventoryStatus(StrEnum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    UNKNOWN = "unknown"


class InventoryScope(StrEnum):
    DATASET = "dataset"
    ASSET = "asset"


class SelectorStatus(StrEnum):
    SELECTED = "selected"
    NOT_SELECTED = "not_selected"
    UNDETERMINED = "undetermined"


class ConfidenceLevel(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INSUFFICIENT = "insufficient"


class GovernanceStatus(StrEnum):
    NONE = "none"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"


class ConditionOrigin(StrEnum):
    REGULATORY = "regulatory"
    PROJECT_BASELINE = "project_baseline"


class DecisionPolicyType(StrEnum):
    ALL_REQUIRED = "all_required"
    AT_LEAST_ONE = "at_least_one"
    THRESHOLD = "threshold"
    MANDATORY_PLUS_OPTIONAL = "mandatory_plus_optional"
    PER_ENTITY = "per_entity"


class EntityAggregationPolicy(StrEnum):
    ALL_MUST_PASS = "all_must_pass"
    ANY_FAILURE_FAILS = "any_failure_fails"
    THRESHOLD = "threshold"
    BEST_EFFORT = "best_effort"


class EmptyCollectionPolicy(StrEnum):
    NOT_APPLICABLE = "not_applicable"
    NON_COMPLIANT = "non_compliant"
    NOT_VERIFIABLE = "not_verifiable"
    CONTINUE = "continue"


class ComplianceStatus(StrEnum):
    """Esiti tecnici e di workflow supportati dal motore estendibile."""

    COMPLIANT = "compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_VERIFIABLE = "not_verifiable"
    NOT_APPLICABLE = "not_applicable"
    NOT_ASSESSED = "not_assessed"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"
    ERROR = "error"


class ApplicabilityStatus(StrEnum):
    """Esito distinto e tri-state della decisione di applicabilità."""

    APPLICABLE = "applicable"
    NOT_APPLICABLE = "not_applicable"
    UNDETERMINED = "undetermined"


class ApplicabilityReasonCode(StrEnum):
    """Codici stabili usati per spiegare e raggruppare le esclusioni."""

    CONDITIONS_SATISFIED = "conditions_satisfied"
    MISSING_GRAPH_ENTITY = "missing_graph_entity"
    PROFILE_EXCLUDED = "profile_excluded"
    NIS_RELEVANCE_EXCLUDED = "nis_relevance_excluded"
    NIS_RELEVANCE_UNDETERMINED = "nis_relevance_undetermined"
    ASSET_TYPE_EXCLUDED = "asset_type_excluded"
    SERVICES_ABSENT = "services_absent"
    SERVICE_EXPOSURE_EXCLUDED = "service_exposure_excluded"
    SERVICE_EXPOSURE_UNDETERMINED = "service_exposure_undetermined"
    REMOVABLE_MEDIA_EXCLUDED = "removable_media_excluded"
    REMOVABLE_MEDIA_UNDETERMINED = "removable_media_undetermined"


class EvidenceSourceCategory(StrEnum):
    """Le quattro categorie informative definite dal perimetro di tesi."""

    DECLARED = "declared"
    EXTERNALLY_OBSERVED = "externally_observed"
    ASSET_INTERNAL = "asset_internal"
    PUBLIC = "public"


class NisProfile(StrEnum):
    """Profili delle specifiche di base ACN supportati dal catalogo 2.0."""

    IMPORTANT = "important"
    ESSENTIAL = "essential"


class VerificationMode(StrEnum):
    """Modalità con cui un requisito tecnico può essere trattato dal checker."""

    DIRECT_TECHNICAL = "direct_technical"
    # Alias Python per le integrazioni esistenti; la serializzazione è canonica.
    AUTOMATIC = "direct_technical"
    EVIDENCE_ASSISTED = "evidence_assisted"
    MANUAL_ONLY = "manual_only"

    @classmethod
    def _missing_(cls, value: object) -> "VerificationMode | None":
        if value == "automatic":
            return cls.DIRECT_TECHNICAL
        return None


class AssetType(StrEnum):
    """Tipologie di asset supportate dalla versione iniziale dello schema."""

    SERVER = "server"
    WORKSTATION = "workstation"
    NETWORK_DEVICE = "network_device"
    APPLICATION = "application"
    DATABASE = "database"
    CLOUD_SERVICE = "cloud_service"
    STORAGE = "storage"
    VIRTUAL_MACHINE = "virtual_machine"
    CONTAINER_HOST = "container_host"
    SECURITY_DEVICE = "security_device"
    OTHER = "other"


class Severity(StrEnum):
    """Scala unica di severità usata da asset, regole e vulnerabilità."""

    NONE = "none"
    UNKNOWN = "unknown"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
