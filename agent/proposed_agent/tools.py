from __future__ import annotations

from pathlib import Path
from typing import Any

from agent.agentic_core.scratchpad import DEFAULT_SCRATCHPAD_MAX_CHARS, JsonScratchpad
from agent.agentic_core.scratchpad_tools import build_scratchpad_tool_specs
from agent.agentic_core.types import AgenticToolSpec
from agent.context_builder import MaterializedBenchmarkContext
from agent.data_access import load_csv_rows, load_table_rows_for_summary
from agent.profiles.categorical import profile_categorical_columns
from agent.profiles.datetime import profile_datetime_columns
from agent.profiles.join import profile_join_key as build_join_profile


PROPOSED_TOOL_NAMES = [
    "lookup_actions",
    "summarize_context_actions",
    "inspect_dataset_tables",
    "inspect_columns",
    "profile_join_key",
    "profile_target_distribution",
    "preview_rows",
    "scratchpad_read",
    "scratchpad_write",
]
DEFAULT_TOOL_OUTPUT_MAX_CHARS = 4000
DEFAULT_PREVIEW_ROW_LIMIT = 20
DEFAULT_ACTION_LOOKUP_LIMIT = 50


def build_proposed_tool_specs(
    *,
    materialized: MaterializedBenchmarkContext,
    scratchpad: JsonScratchpad,
    preview_row_limit: int = DEFAULT_PREVIEW_ROW_LIMIT,
    action_lookup_limit: int = DEFAULT_ACTION_LOOKUP_LIMIT,
) -> list[AgenticToolSpec]:
    visible_actions = materialized.benchmark.visible_actions
    actions_by_id = {action["action_id"]: action for action in visible_actions}
    active_ids = set(_context_action_ids(materialized))
    table_paths = _table_paths(materialized)

    def lookup_actions_handler(payload: dict[str, Any]) -> dict[str, Any]:
        action_type = _optional_str(payload.get("action_type"))
        action_id = _optional_str(payload.get("action_id"))
        column = _optional_str(payload.get("column"))
        active_state = _optional_str(payload.get("active_state")) or "all"
        limit = _clamp_int(payload.get("limit"), default=action_lookup_limit, minimum=1, maximum=200)
        if active_state not in {"active", "inactive", "all"}:
            raise ValueError("active_state must be one of: active, inactive, all")

        matches = []
        for action in visible_actions:
            current_id = action["action_id"]
            if action_id is not None and current_id != action_id:
                continue
            if action_type is not None and action.get("action_type") != action_type:
                continue
            if column is not None and not _action_mentions_column(action, column):
                continue
            if active_state == "active" and current_id not in active_ids:
                continue
            if active_state == "inactive" and current_id in active_ids:
                continue
            matches.append(action)

        limited = matches[:limit]
        return {
            "filters": {
                "action_type": action_type,
                "action_id": action_id,
                "column": column,
                "active_state": active_state,
                "limit": limit,
            },
            "match_count": len(matches),
            "truncated": len(matches) > len(limited),
            "actions": limited,
        }

    def summarize_context_actions_handler(_: dict[str, Any]) -> dict[str, Any]:
        missing_ids = [action_id for action_id in active_ids if action_id not in actions_by_id]
        return {
            "context_action_ids": _context_action_ids(materialized),
            "missing_from_visible_bank": sorted(missing_ids),
            "actions": [
                actions_by_id[action_id]
                for action_id in _context_action_ids(materialized)
                if action_id in actions_by_id
            ],
        }

    def inspect_dataset_tables_handler(_: dict[str, Any]) -> dict[str, Any]:
        tables = []
        for profile in materialized.table_profiles:
            sampling = profile.get("sampling", {})
            schema_columns = profile.get("schema_profile", {}).get("columns", {})
            tables.append(
                {
                    "table_name": profile.get("table_name"),
                    "table_role": profile.get("table_role"),
                    "sampling": sampling,
                    "column_count": len(schema_columns),
                    "columns": sorted(schema_columns),
                }
            )
        return {"tables": tables}

    def inspect_columns_handler(payload: dict[str, Any]) -> dict[str, Any]:
        columns = _required_string_list(payload.get("columns"), "columns", limit=30)
        table_name = _optional_str(payload.get("table_name"))
        matching_profiles = _matching_table_profiles(materialized, table_name=table_name)
        results = []
        for table_profile in matching_profiles:
            selected = {}
            for column in columns:
                column_payload = _column_profile_payload(table_profile, column)
                if column_payload["present"]:
                    selected[column] = column_payload
            if selected:
                row_profiles = _optional_row_backed_column_profiles(
                    table_paths=table_paths,
                    table_name=str(table_profile.get("table_name", "")),
                    columns=columns,
                )
                for column, extra in row_profiles.items():
                    selected.setdefault(column, {"present": True}).update(extra)
                results.append(
                    {
                        "table_name": table_profile.get("table_name"),
                        "table_role": table_profile.get("table_role"),
                        "columns": selected,
                    }
                )
        return {"requested_columns": columns, "tables": results}

    def profile_join_key_handler(payload: dict[str, Any]) -> dict[str, Any]:
        join_request = _resolve_join_request(payload, actions_by_id=actions_by_id, table_paths=table_paths)
        left_rows, left_plan = load_table_rows_for_summary(join_request["left_path"])
        right_rows, right_plan = load_table_rows_for_summary(join_request["right_path"])
        profile = build_join_profile(
            left_rows,
            right_rows,
            left_key=join_request["left_on"],
            right_key=join_request["right_on"],
        )
        profile["sampling"] = {
            "left_mode": left_plan.mode,
            "left_source_row_count": left_plan.source_row_count,
            "left_loaded_row_count": len(left_rows),
            "right_mode": right_plan.mode,
            "right_source_row_count": right_plan.source_row_count,
            "right_loaded_row_count": len(right_rows),
        }
        profile["tables"] = {
            "left_table": Path(join_request["left_path"]).name,
            "right_table": Path(join_request["right_path"]).name,
        }
        return profile

    def profile_target_distribution_handler(_: dict[str, Any]) -> dict[str, Any]:
        return {
            "target_column": materialized.benchmark.bundle.task.get("dataset", {}).get(
                "target_column"
            ),
            "profile": materialized.target_profile,
        }

    def preview_rows_handler(payload: dict[str, Any]) -> dict[str, Any]:
        table_name = _required_str(payload.get("table_name"), "table_name")
        columns = _optional_string_list(payload.get("columns"), limit=30)
        limit = _clamp_int(payload.get("limit"), default=preview_row_limit, minimum=1, maximum=preview_row_limit)
        table_path = _resolve_table_path(table_paths, table_name)
        rows = load_csv_rows(table_path, limit=limit)
        if columns:
            rows = [{column: row.get(column, "") for column in columns} for row in rows]
        return {
            "table_name": Path(table_path).name,
            "columns": columns or (list(rows[0]) if rows else []),
            "row_count": len(rows),
            "rows": rows,
        }

    tools = [
        AgenticToolSpec(
            name="lookup_actions",
            description="Look up visible candidate actions by action type, column, action ID, and active state.",
            input_schema={
                "type": "object",
                "properties": {
                    "action_type": {"type": "string"},
                    "column": {"type": "string"},
                    "action_id": {"type": "string"},
                    "active_state": {"type": "string", "enum": ["active", "inactive", "all"]},
                    "limit": {"type": "integer", "minimum": 1, "maximum": 200},
                },
            },
            handler=lookup_actions_handler,
        ),
        AgenticToolSpec(
            name="summarize_context_actions",
            description="Return visible details for the currently active context actions.",
            input_schema={"type": "object", "properties": {}},
            handler=summarize_context_actions_handler,
        ),
        AgenticToolSpec(
            name="inspect_dataset_tables",
            description="Return compact table names, roles, sampling, and column lists.",
            input_schema={"type": "object", "properties": {}},
            handler=inspect_dataset_tables_handler,
        ),
        AgenticToolSpec(
            name="inspect_columns",
            description="Return compact schema/missingness/numeric/boolean/categorical/datetime evidence for selected columns.",
            input_schema={
                "type": "object",
                "properties": {
                    "columns": {"type": "array", "items": {"type": "string"}},
                    "table_name": {"type": "string"},
                },
                "required": ["columns"],
            },
            handler=inspect_columns_handler,
        ),
        AgenticToolSpec(
            name="profile_join_key",
            description="Profile join-key overlap for a visible JOIN_LOOKUP action or explicit table/key pair.",
            input_schema={
                "type": "object",
                "properties": {
                    "action_id": {"type": "string"},
                    "left_table": {"type": "string"},
                    "right_table": {"type": "string"},
                    "left_on": {},
                    "right_on": {},
                },
            },
            handler=profile_join_key_handler,
        ),
        AgenticToolSpec(
            name="profile_target_distribution",
            description="Return the compact target-column distribution profile.",
            input_schema={"type": "object", "properties": {}},
            handler=profile_target_distribution_handler,
        ),
        AgenticToolSpec(
            name="preview_rows",
            description="Preview a small bounded number of rows from a resolved dataset table.",
            input_schema={
                "type": "object",
                "properties": {
                    "table_name": {"type": "string"},
                    "columns": {"type": "array", "items": {"type": "string"}},
                    "limit": {"type": "integer", "minimum": 1, "maximum": preview_row_limit},
                },
                "required": ["table_name"],
            },
            handler=preview_rows_handler,
        ),
    ]
    tools.extend(
        build_scratchpad_tool_specs(
            scratchpad=scratchpad,
            read_description="Read the run-local scratchpad shared across proposed-agent phases.",
            write_description="Append an entry to the run-local scratchpad shared across proposed-agent phases.",
        )
    )
    return tools


def _context_action_ids(materialized: MaterializedBenchmarkContext) -> list[str]:
    values = materialized.benchmark.bundle.testcase.get("input", {}).get("context_action_ids", [])
    return [value for value in values if isinstance(value, str)] if isinstance(values, list) else []


def _table_paths(materialized: MaterializedBenchmarkContext) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in [
        *materialized.benchmark.dataset_paths.get("train_files", []),
        *materialized.benchmark.dataset_paths.get("lookup_files", []),
    ]:
        paths[path.name] = path
        paths[path.stem] = path
        if path.stem.endswith(".csv"):
            paths[path.stem[:-4]] = path
    return paths


def _optional_str(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None


def _required_str(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field_name} must be a non-empty string")
    return value


def _optional_string_list(value: Any, *, limit: int) -> list[str]:
    if value is None:
        return []
    return _required_string_list(value, "columns", limit=limit)


def _required_string_list(value: Any, field_name: str, *, limit: int) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field_name} must be a non-empty list of strings")
    values = []
    for item in value:
        if not isinstance(item, str) or not item:
            raise ValueError(f"{field_name} must contain only non-empty strings")
        if item not in values:
            values.append(item)
    return values[:limit]


def _clamp_int(value: Any, *, default: int, minimum: int, maximum: int) -> int:
    if not isinstance(value, int):
        return default
    return max(minimum, min(value, maximum))


def _iter_param_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _iter_param_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from _iter_param_strings(item)


def _action_mentions_column(action: dict[str, Any], column: str) -> bool:
    params = action.get("canonical_params", {})
    return any(value == column for value in _iter_param_strings(params))


def _matching_table_profiles(
    materialized: MaterializedBenchmarkContext,
    *,
    table_name: str | None,
) -> list[dict[str, Any]]:
    if table_name is None:
        return materialized.table_profiles
    return [
        profile
        for profile in materialized.table_profiles
        if _table_name_matches(str(profile.get("table_name", "")), table_name)
    ]


def _column_profile_payload(table_profile: dict[str, Any], column: str) -> dict[str, Any]:
    schema = table_profile.get("schema_profile", {}).get("columns", {})
    missingness = table_profile.get("missingness_profile", {}).get("columns", {})
    numeric = table_profile.get("numeric_profile", {}).get("columns", {})
    boolean_like = table_profile.get("boolean_like_profile", {}).get("columns", {})
    return {
        "present": column in schema,
        "schema": schema.get(column),
        "missingness": missingness.get(column),
        "numeric": numeric.get(column),
        "boolean_like": boolean_like.get(column),
    }


def _optional_row_backed_column_profiles(
    *,
    table_paths: dict[str, Path],
    table_name: str,
    columns: list[str],
) -> dict[str, Any]:
    if not table_name:
        return {}
    try:
        path = _resolve_table_path(table_paths, table_name)
        rows, _ = load_table_rows_for_summary(path)
    except Exception:
        return {}
    categorical = profile_categorical_columns(rows).get("columns", {})
    datetime = profile_datetime_columns(rows).get("columns", {})
    return {
        column: {
            "categorical": categorical.get(column),
            "datetime": datetime.get(column),
        }
        for column in columns
        if column in categorical or column in datetime
    }


def _resolve_join_request(
    payload: dict[str, Any],
    *,
    actions_by_id: dict[str, dict[str, Any]],
    table_paths: dict[str, Path],
) -> dict[str, Any]:
    action_id = _optional_str(payload.get("action_id"))
    if action_id is not None:
        action = actions_by_id.get(action_id)
        if action is None:
            raise ValueError(f"unknown action_id: {action_id}")
        if action.get("action_type") != "JOIN_LOOKUP":
            raise ValueError(f"action_id is not a JOIN_LOOKUP action: {action_id}")
        params = action.get("canonical_params", {})
        left_on = params.get("left_on")
        right_on = params.get("right_on")
        right_table = params.get("right_table_id")
        left_table = params.get("left_table_id")
        if not left_on or not right_on or not right_table:
            raise ValueError("JOIN_LOOKUP action must define left_on, right_on, and right_table_id")
        return {
            "left_path": _resolve_table_path(table_paths, left_table) if left_table else _first_train_path(table_paths),
            "right_path": _resolve_table_path(table_paths, right_table),
            "left_on": left_on,
            "right_on": right_on,
        }

    left_table = _required_str(payload.get("left_table"), "left_table")
    right_table = _required_str(payload.get("right_table"), "right_table")
    left_on = payload.get("left_on")
    right_on = payload.get("right_on")
    if not left_on or not right_on:
        raise ValueError("profile_join_key requires left_on and right_on")
    return {
        "left_path": _resolve_table_path(table_paths, left_table),
        "right_path": _resolve_table_path(table_paths, right_table),
        "left_on": left_on,
        "right_on": right_on,
    }


def _resolve_table_path(table_paths: dict[str, Path], table_name: str | None) -> Path:
    if not table_name:
        raise ValueError("table name is required")
    if table_name in table_paths:
        return table_paths[table_name]
    for key, path in table_paths.items():
        if _table_name_matches(key, table_name):
            return path
    raise ValueError(f"unknown dataset table: {table_name}")


def _first_train_path(table_paths: dict[str, Path]) -> Path:
    for key, path in table_paths.items():
        if path.name.startswith("train"):
            return path
    if table_paths:
        return next(iter(table_paths.values()))
    raise ValueError("no dataset tables are available")


def _table_name_matches(candidate: str, requested: str) -> bool:
    return candidate == requested or Path(candidate).stem == requested
