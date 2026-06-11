from __future__ import annotations

from agent.rule_based.scorers import evaluate_add_action, evaluate_remove_action


def predict_actions(
    *,
    actions: list[dict],
    context_action_ids: list[str],
    dataset_insights: dict,
) -> dict[str, list[str]]:
    context_ids = set(context_action_ids)
    predicted_add_action_ids: list[str] = []
    predicted_remove_action_ids: list[str] = []
    decision_log: list[dict] = []

    for action in actions:
        action_id = action["action_id"]
        if action_id not in context_ids:
            record = evaluate_add_action(dataset_insights, action)
            decision_log.append(record)
            if record["decision"] == "selected_add":
                predicted_add_action_ids.append(action_id)
                continue
        elif action_id in context_ids:
            record = evaluate_remove_action(dataset_insights, action)
            decision_log.append(record)
            if record["decision"] == "selected_remove":
                predicted_remove_action_ids.append(action_id)

    return {
        "predicted_add_action_ids": predicted_add_action_ids,
        "predicted_remove_action_ids": predicted_remove_action_ids,
        "decision_log": decision_log,
    }
