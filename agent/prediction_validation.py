from __future__ import annotations

import json

_PREDICTION_REQUIRED_KEYS = frozenset({"predicted_add_action_ids", "predicted_remove_action_ids"})


def _is_prediction_payload(payload: object) -> bool:
    return isinstance(payload, dict) and _PREDICTION_REQUIRED_KEYS.issubset(payload)


def parse_prediction_text(raw_text: str) -> dict:
    decoded_payload: object | None = None
    try:
        decoded_payload = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        decode_error = exc
    else:
        if _is_prediction_payload(decoded_payload):
            return decoded_payload
        decode_error = None

    decoder = json.JSONDecoder()
    saw_any_dict = isinstance(decoded_payload, dict)
    last_prediction_payload: dict | None = None
    for start in (idx for idx, char in enumerate(raw_text) if char == "{"):
        try:
            payload, _ = decoder.raw_decode(raw_text, start)
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, dict):
            continue
        saw_any_dict = True
        if _is_prediction_payload(payload):
            last_prediction_payload = payload

    if last_prediction_payload is not None:
        return last_prediction_payload
    if saw_any_dict:
        raise ValueError("prediction payload must include predicted_add_action_ids and predicted_remove_action_ids")
    if decode_error is not None:
        raise decode_error
    raise ValueError("prediction payload must be an object")


def normalize_action_id_list(
    values: object,
    *,
    field_name: str,
    valid_action_ids: set[str],
) -> tuple[list[str], list[str]]:
    if not isinstance(values, list):
        raise ValueError(f"{field_name} must be a list")

    normalized: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()
    deduplicated: list[str] = []
    unknown: list[str] = []
    dropped_non_string: list[object] = []

    for item in values:
        if not isinstance(item, str):
            dropped_non_string.append(item)
            continue
        if item not in valid_action_ids:
            unknown.append(item)
            continue
        if item in seen:
            deduplicated.append(item)
            continue
        seen.add(item)
        normalized.append(item)

    if unknown:
        warnings.append(f"unknown_{field_name}={unknown}")
    if dropped_non_string:
        warnings.append(f"dropped_non_string_{field_name}={dropped_non_string}")
    if deduplicated:
        warnings.append(f"deduplicated_{field_name}={deduplicated}")
    return normalized, warnings


def normalize_action_rationales(
    values: object,
    *,
    valid_action_ids: set[str],
) -> tuple[list[dict[str, str]], list[str]]:
    if values is None:
        return [], []
    if not isinstance(values, list):
        return [], ["ignored_action_rationales=not_a_list"]

    normalized: list[dict[str, str]] = []
    warnings: list[str] = []
    invalid_entries = 0
    skipped_unknown_ids: list[str] = []

    for entry in values:
        if not isinstance(entry, dict):
            invalid_entries += 1
            continue
        action_id = entry.get("action_id")
        decision = entry.get("decision")
        reason = entry.get("reason")
        if not isinstance(action_id, str) or action_id not in valid_action_ids:
            if isinstance(action_id, str):
                skipped_unknown_ids.append(action_id)
            else:
                invalid_entries += 1
            continue
        if not isinstance(decision, str) or not isinstance(reason, str):
            invalid_entries += 1
            continue
        normalized.append({"action_id": action_id, "decision": decision, "reason": reason})

    if skipped_unknown_ids:
        warnings.append(f"ignored_rationales_for_unknown_action_ids={skipped_unknown_ids}")
    if invalid_entries:
        warnings.append(f"ignored_invalid_action_rationale_entries={invalid_entries}")
    return normalized, warnings


def validate_prediction_payload(
    payload: dict,
    *,
    valid_action_ids: set[str],
    allowed_remove_action_ids: set[str] | None = None,
) -> tuple[dict, list[str]]:
    if not isinstance(payload, dict):
        raise ValueError("prediction payload must be an object")
    if "predicted_add_action_ids" not in payload or "predicted_remove_action_ids" not in payload:
        raise ValueError("prediction payload must include predicted_add_action_ids and predicted_remove_action_ids")

    predicted_add_action_ids, warnings = normalize_action_id_list(
        payload.get("predicted_add_action_ids"),
        field_name="add_action_ids",
        valid_action_ids=valid_action_ids,
    )
    predicted_remove_action_ids, remove_warnings = normalize_action_id_list(
        payload.get("predicted_remove_action_ids"),
        field_name="remove_action_ids",
        valid_action_ids=valid_action_ids,
    )
    warnings.extend(remove_warnings)

    conflicting_action_ids = sorted(set(predicted_add_action_ids) & set(predicted_remove_action_ids))
    if conflicting_action_ids:
        warnings.append(f"removed_conflicting_action_ids={conflicting_action_ids}")
        predicted_add_action_ids = [
            action_id for action_id in predicted_add_action_ids if action_id not in conflicting_action_ids
        ]
        predicted_remove_action_ids = [
            action_id for action_id in predicted_remove_action_ids if action_id not in conflicting_action_ids
        ]

    if allowed_remove_action_ids is not None:
        out_of_scope_remove_action_ids = [
            action_id for action_id in predicted_remove_action_ids if action_id not in allowed_remove_action_ids
        ]
        if out_of_scope_remove_action_ids:
            warnings.append(f"removed_out_of_scope_remove_action_ids={out_of_scope_remove_action_ids}")
            predicted_remove_action_ids = [
                action_id for action_id in predicted_remove_action_ids if action_id in allowed_remove_action_ids
            ]

    notes = payload.get("notes")
    if notes is not None and not isinstance(notes, str):
        warnings.append("ignored_notes=not_a_string")
        notes = None

    action_rationales, rationale_warnings = normalize_action_rationales(
        payload.get("action_rationales"),
        valid_action_ids=valid_action_ids,
    )
    warnings.extend(rationale_warnings)

    return (
        {
            "predicted_add_action_ids": predicted_add_action_ids,
            "predicted_remove_action_ids": predicted_remove_action_ids,
            "notes": notes,
            "action_rationales": action_rationales,
        },
        warnings,
    )


def parse_and_validate_prediction_text(
    raw_text: str,
    *,
    valid_action_ids: set[str],
    allowed_remove_action_ids: set[str] | None = None,
) -> tuple[dict, list[str]]:
    payload = parse_prediction_text(raw_text)
    return validate_prediction_payload(
        payload,
        valid_action_ids=valid_action_ids,
        allowed_remove_action_ids=allowed_remove_action_ids,
    )
