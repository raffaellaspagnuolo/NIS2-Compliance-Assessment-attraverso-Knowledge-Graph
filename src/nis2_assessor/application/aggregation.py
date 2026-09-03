"""Aggregazione descrittiva e priorità operativa non normativa."""

from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from typing import Any

from nis2_assessor.application.policies import bundled_catalog_path, load_operational_policy
from nis2_assessor.domain.enums import ComplianceStatus, GovernanceStatus
from nis2_assessor.domain.models import AssessmentResult, Asset, Control
from nis2_assessor.domain.report_types import PriorityRecord

DETERMINED = {
    ComplianceStatus.COMPLIANT,
    ComplianceStatus.PARTIALLY_COMPLIANT,
    ComplianceStatus.NON_COMPLIANT,
}


def aggregate(
    results: list[AssessmentResult],
    assets: Sequence[Asset | Mapping[str, Any]],
    controls: Sequence[Control | Mapping[str, Any]],
    operational_policy: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Produce conteggi, copertura informativa e priorità su scala 0–100."""
    active_policy = operational_policy or load_operational_policy(
        bundled_catalog_path("operational_policy.example.yaml")
    )
    priority_policy = active_policy["priority"]
    weights = priority_policy["weights"]
    status_scores = priority_policy["status_scores"]
    level_scores = priority_policy["level_scores"]
    scale = float(priority_policy.get("scale", 100))
    asset_map = {str(_value(asset, "id")): asset for asset in assets}
    control_map = {str(_value(control, "id")): control for control in controls}
    counts = Counter(result.technical_status for result in results)
    applicable = [
        result
        for result in results
        if result.technical_status != ComplianceStatus.NOT_APPLICABLE
    ]
    determined = [
        result
        for result in applicable
        if result.technical_status in DETERMINED
        and (bool(result.evaluated_facts) or bool(result.evidence_ids))
    ]
    coverage = len(determined) / len(applicable) if applicable else None
    by_asset: dict[str, Counter[str]] = defaultdict(Counter)
    by_area: dict[str, Counter[str]] = defaultdict(Counter)
    priorities: list[PriorityRecord] = []

    for result in results:
        status = result.technical_status
        if status == ComplianceStatus.NOT_APPLICABLE:
            continue
        by_asset[result.asset_id][status.value] += 1
        technical_area = str(_value(control_map[result.control_id], "technical_area"))
        by_area[technical_area][status.value] += 1
        if status == ComplianceStatus.COMPLIANT:
            continue
        asset = asset_map[result.asset_id]
        components = {
            "technical_status": float(status_scores.get(status.value, 0.0)),
            "criticality": float(level_scores[str(_value(asset, "criticality"))]),
            "impact": float(level_scores[str(_value(asset, "impact_level"))]),
            "exposure": float(level_scores[str(_value(asset, "exposure_level"))]),
        }
        score = scale * sum(
            float(weights[name]) * value for name, value in components.items()
        )
        formula = f"{scale:g}*(" + "+".join(
            f"{float(weights[name]):g}*{name}" for name in components
        ) + ")"
        priorities.append(
            {
                "result_id": result.id,
                "asset_id": result.asset_id,
                "control_id": result.control_id,
                "score": round(score, 2),
                "formula": formula,
                "non_normative": True,
                "policy_version": str(active_policy["policy_version"]),
                "components": components,
            }
        )
    priorities.sort(
        key=lambda item: (-float(item["score"]), item["asset_id"], item["control_id"])
    )
    return {
        "assets_observed": len(assets),
        "assets_analyzed": sum(
            _known_bool(_value(asset, "nis_relevant")) is True for asset in assets
        ),
        "applicable_controls": len(applicable),
        "not_applicable_controls": counts[ComplianceStatus.NOT_APPLICABLE],
        "technically_determined_controls": len(determined),
        "verifiable_controls": len(determined),
        "not_verifiable_controls": counts[ComplianceStatus.NOT_VERIFIABLE],
        "manual_review_required": sum(
            result.governance_status == GovernanceStatus.MANUAL_REVIEW_REQUIRED
            for result in results
        ),
        "compliant": counts[ComplianceStatus.COMPLIANT],
        "partially_compliant": counts[ComplianceStatus.PARTIALLY_COMPLIANT],
        "non_compliant": counts[ComplianceStatus.NON_COMPLIANT],
        "information_coverage": round(coverage, 4) if coverage is not None else None,
        "information_coverage_numerator": len(determined),
        "information_coverage_denominator": len(applicable),
        "coverage_warning": coverage is None or coverage < 0.6,
        "results_by_asset": {key: dict(value) for key, value in by_asset.items()},
        "results_by_area": {key: dict(value) for key, value in by_area.items()},
        "priorities": priorities,
        "priority_policy_version": str(active_policy["policy_version"]),
        "priority_note": (
            "Priorità operativa configurabile e non normativa su scala 0–100; "
            "l'esposizione nulla non annulla le altre componenti."
        ),
    }


def _value(entity: object, name: str) -> Any:
    if isinstance(entity, Mapping):
        return entity.get(name)
    return getattr(entity, name)


def _known_bool(value: Any) -> bool | None:
    if hasattr(value, "status"):
        return value.value if str(value.status) == "known" else None
    if isinstance(value, Mapping) and value.get("status") == "known":
        return bool(value.get("value"))
    return value if isinstance(value, bool) else None
