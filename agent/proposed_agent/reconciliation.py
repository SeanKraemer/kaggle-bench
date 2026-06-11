from __future__ import annotations

import json
import re
from typing import Any

from agent.prediction_validation import (
    normalize_action_id_list,
    normalize_action_rationales,
    parse_and_validate_prediction_text,
    parse_prediction_text,
)


_INPUT_COLUMN_PARAM_KEYS = {
    "column",
    "columns",
    "source_column",
    "source_columns",
    "input_column",
    "input_columns",
    "group_by_column",
    "group_by_columns",
    "target_column",
    "target_columns",
    "key",
    "keys",
    "join_key",
    "join_keys",
    "left_on",
    "right_on",
}
_OUTPUT_COLUMN_PARAM_KEYS = {
    "output_column",
    "output_columns",
    "new_column",
    "new_columns",
    "derived_column",
    "derived_columns",
}
_HIGH_CONFIDENCE_BLOCKING_DROP_MARKERS = (
    "before_feature",
    "before feature",
    "before_extraction",
    "before extraction",
    "before_group",
    "before group",
    "before_join",
    "before join",
    "before_encoding",
    "before encoding",
    "pre_feature",
    "pre-feature",
    "pre_extraction",
    "pre-extraction",
    "premature",
)


def parse_and_validate_add_phase_text(
    raw_text: str,
    *,
    valid_action_ids: set[str],
    active_action_ids: set[str],
) -> tuple[dict[str, Any], list[str]]:
    return validate_add_phase(
        parse_prediction_text(raw_text),
        valid_action_ids=valid_action_ids,
        active_action_ids=active_action_ids,
    )


def parse_and_validate_remove_phase_text(
    raw_text: str,
    *,
    valid_action_ids: set[str],
    active_action_ids: set[str],
) -> tuple[dict[str, Any], list[str]]:
    return validate_remove_phase(
        parse_prediction_text(raw_text),
        valid_action_ids=valid_action_ids,
        active_action_ids=active_action_ids,
    )


def validate_add_phase(
    payload: dict[str, Any],
    *,
    valid_action_ids: set[str],
    active_action_ids: set[str],
) -> tuple[dict[str, Any], list[str]]:
    if not isinstance(payload, dict):
        raise ValueError("add phase payload must be an object")
    if payload.get("phase") != "add":
        raise ValueError("add phase payload must include phase='add'")
    if "predicted_add_action_ids" not in payload or "predicted_remove_action_ids" not in payload:
        raise ValueError("add phase payload must include add and remove prediction fields")
    if payload.get("predicted_remove_action_ids") != []:
        raise ValueError("add phase must not include remove decisions")

    add_ids, warnings = normalize_action_id_list(
        payload.get("predicted_add_action_ids"),
        field_name="add_action_ids",
        valid_action_ids=valid_action_ids,
    )
    active_add_ids = [action_id for action_id in add_ids if action_id in active_action_ids]
    if active_add_ids:
        warnings.append(f"dropped_active_add_action_ids={active_add_ids}")
        add_ids = [action_id for action_id in add_ids if action_id not in active_action_ids]
    rationales, rationale_warnings = normalize_action_rationales(
        payload.get("action_rationales"),
        valid_action_ids=valid_action_ids,
    )
    warnings.extend(rationale_warnings)
    return (
        {
            "phase": "add",
            "predicted_add_action_ids": add_ids,
            "predicted_remove_action_ids": [],
            "notes": payload.get("notes") if isinstance(payload.get("notes"), str) else None,
            "action_rationales": rationales,
        },
        warnings,
    )


def validate_remove_phase(
    payload: dict[str, Any],
    *,
    valid_action_ids: set[str],
    active_action_ids: set[str],
) -> tuple[dict[str, Any], list[str]]:
    if not isinstance(payload, dict):
        raise ValueError("remove phase payload must be an object")
    if payload.get("phase") != "remove":
        raise ValueError("remove phase payload must include phase='remove'")
    if "predicted_add_action_ids" not in payload or "predicted_remove_action_ids" not in payload:
        raise ValueError("remove phase payload must include add and remove prediction fields")
    if payload.get("predicted_add_action_ids") != []:
        raise ValueError("remove phase must not include add decisions")

    remove_ids, warnings = normalize_action_id_list(
        payload.get("predicted_remove_action_ids"),
        field_name="remove_action_ids",
        valid_action_ids=valid_action_ids,
    )
    inactive_remove_ids = [action_id for action_id in remove_ids if action_id not in active_action_ids]
    if inactive_remove_ids:
        warnings.append(f"dropped_inactive_remove_action_ids={inactive_remove_ids}")
        remove_ids = [action_id for action_id in remove_ids if action_id in active_action_ids]
    rationales, rationale_warnings = normalize_action_rationales(
        payload.get("action_rationales"),
        valid_action_ids=valid_action_ids,
    )
    warnings.extend(rationale_warnings)
    return (
        {
            "phase": "remove",
            "predicted_add_action_ids": [],
            "predicted_remove_action_ids": remove_ids,
            "notes": payload.get("notes") if isinstance(payload.get("notes"), str) else None,
            "action_rationales": rationales,
        },
        warnings,
    )


def reconcile_phase_outputs(
    *,
    add_prediction: dict[str, Any],
    remove_prediction: dict[str, Any],
    valid_action_ids: set[str],
    active_action_ids: set[str],
    visible_actions: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], list[str]]:
    warnings: list[str] = []
    add_ids = _dedupe_strings(add_prediction.get("predicted_add_action_ids", []))
    remove_ids = _dedupe_strings(remove_prediction.get("predicted_remove_action_ids", []))

    conflicts = sorted(set(add_ids) & set(remove_ids))
    if conflicts:
        warnings.append(f"reconciliation_kept_remove_and_dropped_add_conflicts={conflicts}")
        add_ids = [action_id for action_id in add_ids if action_id not in conflicts]

    active_add_ids = [action_id for action_id in add_ids if action_id in active_action_ids]
    if active_add_ids:
        warnings.append(f"reconciliation_dropped_active_add_action_ids={active_add_ids}")
        add_ids = [action_id for action_id in add_ids if action_id not in active_action_ids]

    inactive_remove_ids = [action_id for action_id in remove_ids if action_id not in active_action_ids]
    if inactive_remove_ids:
        warnings.append(f"reconciliation_dropped_inactive_remove_action_ids={inactive_remove_ids}")
        remove_ids = [action_id for action_id in remove_ids if action_id in active_action_ids]

    if visible_actions:
        blocker_remove_ids, blocker_details = _find_raw_column_blockers(
            add_ids=add_ids,
            remove_ids=remove_ids,
            active_action_ids=active_action_ids,
            visible_actions=visible_actions,
        )
        if blocker_remove_ids:
            remove_ids = _dedupe_strings([*remove_ids, *blocker_remove_ids])
            warnings.append(f"auto_added_remove_raw_column_blockers={blocker_details}")

    final_payload = {
        "predicted_add_action_ids": add_ids,
        "predicted_remove_action_ids": remove_ids,
    }
    final_prediction, validation_warnings = parse_and_validate_prediction_text(
        json.dumps(final_payload),
        valid_action_ids=valid_action_ids,
        allowed_remove_action_ids=active_action_ids,
    )
    warnings.extend(validation_warnings)
    return final_prediction, warnings


def _dedupe_strings(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    result = []
    seen = set()
    for value in values:
        if isinstance(value, str) and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _find_raw_column_blockers(
    *,
    add_ids: list[str],
    remove_ids: list[str],
    active_action_ids: set[str],
    visible_actions: list[dict[str, Any]],
) -> tuple[list[str], list[dict[str, Any]]]:
    action_by_id = {
        action["action_id"]: action
        for action in visible_actions
        if isinstance(action.get("action_id"), str)
    }
    column_lexicon = _build_column_lexicon(visible_actions)
    required_columns_by_add_id = {
        action_id: _required_raw_columns_for_action(action_by_id[action_id], column_lexicon)
        for action_id in add_ids
        if action_id in action_by_id
    }
    required_columns_by_add_id = {
        action_id: columns
        for action_id, columns in required_columns_by_add_id.items()
        if columns
    }
    if not required_columns_by_add_id:
        return [], []

    already_removed = set(remove_ids)
    blocker_ids: list[str] = []
    blocker_details: list[dict[str, Any]] = []
    for action_id in sorted(active_action_ids):
        if action_id in already_removed:
            continue
        action = action_by_id.get(action_id)
        if action is None or action.get("action_type") != "DROP_COLUMNS":
            continue
        if not _is_high_confidence_blocking_drop(action):
            continue
        dropped_columns = set(_param_strings(action.get("canonical_params", {}).get("columns")))
        if not dropped_columns:
            continue
        blocked_add_ids = sorted(
            add_id
            for add_id, required_columns in required_columns_by_add_id.items()
            if dropped_columns & required_columns
        )
        if not blocked_add_ids:
            continue
        blocker_ids.append(action_id)
        blocker_details.append(
            {
                "drop_action_id": action_id,
                "dropped_columns": sorted(dropped_columns),
                "blocked_add_action_ids": blocked_add_ids,
            }
        )
    return blocker_ids, blocker_details


def _required_raw_columns_for_action(action: dict[str, Any], column_lexicon: set[str]) -> set[str]:
    if action.get("action_type") == "DROP_COLUMNS":
        return set()
    params = action.get("canonical_params", {})
    if not isinstance(params, dict):
        return set()

    output_columns = set()
    required_columns = set()
    for key, value in params.items():
        normalized_key = _normalize_param_key(key)
        if normalized_key in _OUTPUT_COLUMN_PARAM_KEYS:
            output_columns.update(_param_strings(value))
            continue
        if _is_input_column_param_key(normalized_key):
            required_columns.update(_param_strings(value))

    expression = params.get("expression")
    if isinstance(expression, str):
        required_columns.update(_columns_mentioned_in_text(expression, column_lexicon))

    return {
        column
        for column in required_columns
        if column and column not in output_columns
    }


def _build_column_lexicon(actions: list[dict[str, Any]]) -> set[str]:
    columns: set[str] = set()
    for action in actions:
        params = action.get("canonical_params", {})
        if not isinstance(params, dict):
            continue
        for key, value in params.items():
            normalized_key = _normalize_param_key(key)
            if normalized_key in _OUTPUT_COLUMN_PARAM_KEYS:
                continue
            if _is_input_column_param_key(normalized_key):
                columns.update(_param_strings(value))
    return columns


def _is_input_column_param_key(key: str) -> bool:
    return key in _INPUT_COLUMN_PARAM_KEYS or (
        key.endswith("_columns") and key not in _OUTPUT_COLUMN_PARAM_KEYS
    )


def _is_high_confidence_blocking_drop(action: dict[str, Any]) -> bool:
    params = action.get("canonical_params", {})
    if not isinstance(params, dict):
        return False
    reason = params.get("reason")
    if not isinstance(reason, str):
        return False
    normalized_reason = reason.replace("-", "_").lower()
    return any(marker in normalized_reason for marker in _HIGH_CONFIDENCE_BLOCKING_DROP_MARKERS)


def _columns_mentioned_in_text(text: str, column_lexicon: set[str]) -> set[str]:
    mentioned: set[str] = set()
    for column in column_lexicon:
        pattern = rf"(?<![A-Za-z0-9_]){re.escape(column)}(?![A-Za-z0-9_])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            mentioned.add(column)
    return mentioned


def _param_strings(value: Any) -> set[str]:
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        values: set[str] = set()
        for item in value:
            values.update(_param_strings(item))
        return values
    if isinstance(value, dict):
        values: set[str] = set()
        for item in value.values():
            values.update(_param_strings(item))
        return values
    return set()


def _normalize_param_key(value: Any) -> str:
    return value.lower() if isinstance(value, str) else ""
