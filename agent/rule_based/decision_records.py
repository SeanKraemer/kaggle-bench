from __future__ import annotations


def build_decision_record(
    *,
    action: dict,
    candidate_side: str,
    decision: str,
    triggered_rule: str | None,
    details: list[str],
) -> dict:
    return {
        "action_id": action["action_id"],
        "action_type": action["action_type"],
        "candidate_side": candidate_side,
        "decision": decision,
        "triggered_rule": triggered_rule,
        "details": details,
    }
