from __future__ import annotations

ALLOWED_AGENT_ACTION_FIELDS = (
    "action_id",
    "action_type",
    "canonical_params",
)


def build_agent_visible_actions(actions: list[dict]) -> list[dict]:
    visible_actions: list[dict] = []
    for action in actions:
        visible_actions.append({field_name: action.get(field_name) for field_name in ALLOWED_AGENT_ACTION_FIELDS})
    return visible_actions


def build_agent_visible_action_bank(task_bundle, stage_scope: str | None = None) -> list[dict]:
    del stage_scope
    return build_agent_visible_actions(task_bundle.actions)


def resolve_action_ids(
    actions: list[dict],
    *,
    action_type: str | None = None,
    canonical_param_filters: dict | None = None,
) -> list[str]:
    filters = canonical_param_filters or {}
    matches: list[str] = []
    for action in actions:
        if action_type is not None and action.get("action_type") != action_type:
            continue
        params = action.get("canonical_params", {})
        if any(params.get(key) != value for key, value in filters.items()):
            continue
        matches.append(action["action_id"])
    return matches
