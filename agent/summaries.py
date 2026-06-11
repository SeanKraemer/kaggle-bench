from __future__ import annotations

import json
import re
from pathlib import Path


def _format_summary_line(label: str, value: str | None) -> str:
    if value is None or value == "":
        return f"{label}:"
    return f"{label}: {value}"


def _join_dataset_file_names(paths: list[Path]) -> str:
    return ", ".join(path.name for path in paths)


def render_dataset_summary(
    *,
    task: dict,
    dataset_paths: dict,
    table_profiles: list[dict] | None = None,
    primary_train_profile: dict,
    join_profile: dict,
    target_profile: dict,
) -> str:
    lines = [
        _format_summary_line("Goal", task.get("goal")),
        _format_summary_line(
            "Train files",
            _join_dataset_file_names(dataset_paths.get("train_files", [])),
        ),
        _format_summary_line(
            "Lookup files",
            _join_dataset_file_names(dataset_paths.get("lookup_files", [])),
        ),
        _format_summary_line("Target column", task.get("dataset", {}).get("target_column")),
        _format_summary_line("Primary key", task.get("dataset", {}).get("primary_key")),
    ]
    lines.extend(
        [
            "Primary train profile:",
            f"Sampling: {json.dumps(primary_train_profile.get('sampling', {}), indent=2)}",
            f"Schema profile: {json.dumps(primary_train_profile.get('schema_profile', {}), indent=2)}",
            f"Missingness profile: {json.dumps(primary_train_profile.get('missingness_profile', {}), indent=2)}",
            f"Numeric profile: {json.dumps(primary_train_profile.get('numeric_profile', {}), indent=2)}",
            f"Boolean-like profile: {json.dumps(primary_train_profile.get('boolean_like_profile', {}), indent=2)}",
            "Table profiles:",
        ]
    )
    for table_profile in table_profiles or []:
        lines.extend(
            [
                f"Table: {table_profile.get('table_name', '')}",
                f"Role: {table_profile.get('table_role', '')}",
                f"Sampling: {json.dumps(table_profile.get('sampling', {}), indent=2)}",
                f"Schema profile: {json.dumps(table_profile.get('schema_profile', {}), indent=2)}",
                f"Missingness profile: {json.dumps(table_profile.get('missingness_profile', {}), indent=2)}",
                f"Numeric profile: {json.dumps(table_profile.get('numeric_profile', {}), indent=2)}",
                f"Boolean-like profile: {json.dumps(table_profile.get('boolean_like_profile', {}), indent=2)}",
            ]
        )
    lines.extend(
        [
            f"Join profile: {json.dumps(join_profile, indent=2)}",
            f"Target profile: {json.dumps(target_profile, indent=2)}",
        ]
    )
    return "\n".join(lines)


_COLUMN_PARAM_KEYS = {
    "column",
    "columns",
    "date_column",
    "date_columns",
    "group_by_column",
    "group_by_columns",
    "key_column",
    "key_columns",
    "left_on",
    "order_by_column",
    "order_by_columns",
    "right_on",
    "sort_column",
    "sort_columns",
    "target_column",
    "target_columns",
}


def _collect_available_columns(table_profiles: list[dict] | None) -> set[str]:
    available_columns: set[str] = set()
    for table_profile in table_profiles or []:
        available_columns.update(table_profile.get("schema_profile", {}).get("columns", {}).keys())
    return available_columns


def _match_expression_columns(expression: str, available_columns: set[str]) -> set[str]:
    matches: set[str] = set()
    for column in sorted(available_columns, key=len, reverse=True):
        if re.search(rf"(?<![A-Za-z0-9_]){re.escape(column)}(?![A-Za-z0-9_])", expression):
            matches.add(column)
    return matches


def collect_action_referenced_columns(*, visible_actions: list[dict], table_profiles: list[dict] | None) -> set[str]:
    available_columns = _collect_available_columns(table_profiles)
    referenced_columns: set[str] = set()
    for action in visible_actions:
        canonical_params = action.get("canonical_params", {}) or {}
        for key, value in canonical_params.items():
            if key in _COLUMN_PARAM_KEYS or key.endswith("_column") or key.endswith("_columns"):
                values = value if isinstance(value, list) else [value]
                for item in values:
                    if isinstance(item, str) and item in available_columns:
                        referenced_columns.add(item)
        expression = canonical_params.get("expression")
        if isinstance(expression, str):
            referenced_columns.update(_match_expression_columns(expression, available_columns))
    return referenced_columns


def _filter_profile_columns(profile: dict, referenced_columns: set[str]) -> dict:
    columns = profile.get("columns", {})
    filtered_profile = {key: value for key, value in profile.items() if key != "columns"}
    filtered_profile["columns"] = {
        column: columns[column]
        for column in sorted(columns)
        if column in referenced_columns
    }
    return filtered_profile


def _build_schema_profile_view(schema_profile: dict, referenced_columns: set[str]) -> dict:
    filtered_columns = _filter_profile_columns(schema_profile, referenced_columns)["columns"]
    return {
        "row_count": schema_profile.get("row_count", 0),
        "column_count": schema_profile.get("column_count", 0),
        "referenced_column_count": len(filtered_columns),
        "columns": filtered_columns,
    }


def render_single_llm_dataset_summary(
    *,
    task: dict,
    dataset_paths: dict,
    visible_actions: list[dict],
    table_profiles: list[dict] | None = None,
    primary_train_profile: dict,
    join_profile: dict,
    target_profile: dict,
) -> str:
    referenced_columns = collect_action_referenced_columns(
        visible_actions=visible_actions,
        table_profiles=table_profiles,
    )
    primary_schema = primary_train_profile.get("schema_profile", {})
    primary_table_name = primary_train_profile.get("table_name")
    primary_table_role = primary_train_profile.get("table_role")
    lines = [
        _format_summary_line("Goal", task.get("goal")),
        _format_summary_line(
            "Train files",
            _join_dataset_file_names(dataset_paths.get("train_files", [])),
        ),
        _format_summary_line(
            "Lookup files",
            _join_dataset_file_names(dataset_paths.get("lookup_files", [])),
        ),
        _format_summary_line("Target column", task.get("dataset", {}).get("target_column")),
        _format_summary_line("Primary key", task.get("dataset", {}).get("primary_key")),
        (
            "Referenced dataset columns in visible actions: "
            f"{len(referenced_columns)} / {primary_schema.get('column_count', 0)}"
        ),
        f"Referenced columns: {json.dumps(sorted(referenced_columns))}",
        "Primary train profile (referenced columns only):",
        f"Sampling: {json.dumps(primary_train_profile.get('sampling', {}), indent=2)}",
        f"Schema profile: {json.dumps(_build_schema_profile_view(primary_schema, referenced_columns), indent=2)}",
        f"Missingness profile: {json.dumps(_filter_profile_columns(primary_train_profile.get('missingness_profile', {}), referenced_columns), indent=2)}",
        f"Numeric profile: {json.dumps(_filter_profile_columns(primary_train_profile.get('numeric_profile', {}), referenced_columns), indent=2)}",
        f"Boolean-like profile: {json.dumps(_filter_profile_columns(primary_train_profile.get('boolean_like_profile', {}), referenced_columns), indent=2)}",
        "Secondary table profiles (referenced columns only):",
    ]
    for table_profile in table_profiles or []:
        if (
            table_profile.get("table_name") == primary_table_name
            and table_profile.get("table_role") == primary_table_role
        ):
            continue
        table_schema = table_profile.get("schema_profile", {})
        table_columns = set(table_schema.get("columns", {}))
        table_referenced_columns = table_columns & referenced_columns
        if not table_referenced_columns:
            continue
        lines.extend(
            [
                f"Table: {table_profile.get('table_name', '')}",
                f"Role: {table_profile.get('table_role', '')}",
                f"Sampling: {json.dumps(table_profile.get('sampling', {}), indent=2)}",
                f"Referenced columns: {json.dumps(sorted(table_referenced_columns))}",
                f"Schema profile: {json.dumps(_build_schema_profile_view(table_schema, table_referenced_columns), indent=2)}",
                f"Missingness profile: {json.dumps(_filter_profile_columns(table_profile.get('missingness_profile', {}), table_referenced_columns), indent=2)}",
                f"Numeric profile: {json.dumps(_filter_profile_columns(table_profile.get('numeric_profile', {}), table_referenced_columns), indent=2)}",
                f"Boolean-like profile: {json.dumps(_filter_profile_columns(table_profile.get('boolean_like_profile', {}), table_referenced_columns), indent=2)}",
            ]
        )
    lines.extend(
        [
            f"Join profile: {json.dumps(join_profile, indent=2)}",
            f"Target profile: {json.dumps(target_profile, indent=2)}",
        ]
    )
    return "\n".join(lines)


def render_context_summary(*, testcase: dict) -> str:
    testcase_id = testcase.get("testcase_id", "")
    scenario = testcase.get("input", {}).get("scenario", "")
    context_action_ids = testcase.get("input", {}).get("context_action_ids", [])
    return "\n".join(
        [
            _format_summary_line("Testcase", testcase_id),
            _format_summary_line("Scenario", scenario),
            _format_summary_line(
                "Current context_action_ids",
                json.dumps(context_action_ids),
            ),
        ]
    )


def render_candidate_actions_json(actions: list[dict]) -> str:
    return json.dumps(actions, indent=2)


def _count_action_types(actions: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for action in actions:
        action_type = action.get("action_type")
        key = action_type if isinstance(action_type, str) and action_type else "UNKNOWN"
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def _render_action_preview(action: dict) -> dict:
    params = action.get("canonical_params")
    param_keys = sorted(params) if isinstance(params, dict) else []
    return {
        "action_id": action.get("action_id"),
        "action_type": action.get("action_type"),
        "canonical_param_keys": param_keys,
        "canonical_param_count": len(param_keys),
    }


def render_candidate_actions_preview(
    actions: list[dict],
    *,
    context_action_ids: list[str] | None = None,
    candidate_actions_filename: str = "candidate_actions_visible.json",
    sample_per_action_type: int = 2,
) -> str:
    action_type_samples: dict[str, list[dict]] = {}
    for action in actions:
        action_type = action.get("action_type")
        key = action_type if isinstance(action_type, str) and action_type else "UNKNOWN"
        samples = action_type_samples.setdefault(key, [])
        if len(samples) < sample_per_action_type:
            samples.append(_render_action_preview(action))

    actions_by_id = {action.get("action_id"): action for action in actions}
    context_previews = [
        _render_action_preview(actions_by_id[action_id])
        if action_id in actions_by_id
        else {"action_id": action_id, "missing_from_visible_bank": True}
        for action_id in (context_action_ids or [])
    ]
    preview = {
        "candidate_actions_file": candidate_actions_filename,
        "candidate_action_count": len(actions),
        "instructions": (
            "This is only a compact preview. Inspect the full visible candidate-action "
            f"bank in `{candidate_actions_filename}` before returning final action IDs."
        ),
        "action_type_counts": _count_action_types(actions),
        "context_action_ids": context_action_ids or [],
        "context_action_previews": context_previews,
        "sample_actions_by_type": dict(sorted(action_type_samples.items())),
    }
    return json.dumps(preview, indent=2, sort_keys=True)
