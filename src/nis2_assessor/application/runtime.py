"""Dipendenze runtime sostituibili usate per tempo e identificativi.

Separare il clock da ``datetime.now`` permette di fissare l'istante
dell'assessment e rende completamente riproducibili timestamp e validità.
"""

from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4


class SystemClock:
    """Clock di produzione che restituisce l'ora UTC corrente."""

    def now(self) -> datetime:
        """Restituisce sempre un datetime consapevole del fuso orario."""
        return datetime.now(UTC)


@dataclass(frozen=True)
class FixedClock:
    """Clock deterministico utile nelle validazioni e nelle riproduzioni forensi."""

    instant: datetime

    def now(self) -> datetime:
        """Restituisce sempre l'istante configurato dal chiamante."""
        if self.instant.tzinfo is None:
            raise ValueError("FixedClock richiede un datetime con fuso orario")
        return self.instant


def random_assessment_id() -> str:
    """Genera l'identificativo predefinito quando il chiamante non lo fornisce."""
    return f"assessment-{uuid4().hex[:12]}"
