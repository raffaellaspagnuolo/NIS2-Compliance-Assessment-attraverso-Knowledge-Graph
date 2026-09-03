"""Facciata pubblica del dominio.

Riesporta i tipi usati più spesso, così i chiamanti non devono conoscere il
file interno in cui ciascuna classe è definita.
"""

from .enums import ComplianceStatus, EvidenceSourceCategory, KnowledgeValueStatus
from .models import AssessmentResult, Finding, KnowledgeValue, NormalizedEnvironment

# __all__ documenta e limita i simboli considerati parte dell'API pubblica.
__all__ = [
    "AssessmentResult",
    "ComplianceStatus",
    "EvidenceSourceCategory",
    "Finding",
    "KnowledgeValue",
    "KnowledgeValueStatus",
    "NormalizedEnvironment",
]
