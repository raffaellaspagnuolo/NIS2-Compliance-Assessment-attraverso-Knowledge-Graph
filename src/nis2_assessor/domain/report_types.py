"""Tipi strutturali dei record interni usati nei report.

Questi TypedDict sostituiscono gradualmente dizionari completamente generici,
senza imporre una migrazione immediata dell'intero formato JSON pubblico.
"""

from typing import NotRequired, TypedDict


class EvidenceRejection(TypedDict):
    """Motivo per cui un'evidenza non è stata ammessa alla valutazione."""

    evidence_id: str
    reason: str


class PriorityRecord(TypedDict):
    """Voce ordinabile della lista delle priorità tecniche."""

    result_id: str
    asset_id: str
    control_id: str
    score: float
    formula: str
    non_normative: bool
    policy_version: str
    components: NotRequired[dict[str, float]]
