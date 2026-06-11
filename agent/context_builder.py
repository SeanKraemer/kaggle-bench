from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agent.action_bank import build_agent_visible_action_bank
from agent.data_access import (
    TableLoadPlan,
    load_table_rows_for_summary,
    resolve_dataset_paths,
)
from agent.profiles.boolean_like import profile_boolean_like_columns
from agent.profiles.join import profile_join_key
from agent.profiles.missingness import profile_missingness
from agent.profiles.numeric import profile_numeric_columns
from agent.profiles.schema import profile_table_schema
from agent.profiles.target import profile_target_distribution
from agent.profile_cache import build_profile_cache_key, load_profile_cache, write_profile_cache
from agent.summaries import render_candidate_actions_json, render_context_summary, render_dataset_summary
from agent.task_bundle import TaskBundle, load_task_bundle


@dataclass(frozen=True)
class BenchmarkContext:
    bundle: TaskBundle
    dataset_paths: dict[str, list[Path]]
    context_summary: str
    visible_actions: list[dict]
    valid_action_ids: set[str]
    candidate_actions_json: str


@dataclass(frozen=True)
class MaterializedBenchmarkContext:
    benchmark: BenchmarkContext
    train_rows: list[dict[str, str]]
    lookup_rows: list[dict[str, str]]
    table_profiles: list[dict]
    primary_train_profile: dict
    join_profile: dict
    target_profile: dict
    dataset_summary: str


@dataclass(frozen=True)
class JoinSpec:
    lookup_path: Path
    left_on: str | list[str]
    right_on: str | list[str]


def build_benchmark_context(
    *,
    task_dir: str | Path,
    testcase_id: str,
    data_root: str | Path,
) -> BenchmarkContext:
    bundle = load_task_bundle(task_dir, testcase_id)
    dataset_paths = resolve_dataset_paths(data_root, bundle.task)
    context_summary = render_context_summary(testcase=bundle.testcase)
    visible_actions = build_agent_visible_action_bank(bundle, stage_scope=None)
    valid_action_ids = {action["action_id"] for action in visible_actions}
    candidate_actions_json = render_candidate_actions_json(visible_actions)
    return BenchmarkContext(
        bundle=bundle,
        dataset_paths=dataset_paths,
        context_summary=context_summary,
        visible_actions=visible_actions,
        valid_action_ids=valid_action_ids,
        candidate_actions_json=candidate_actions_json,
    )


def _empty_join_profile(*, train_rows: list[dict[str, str]]) -> dict:
    return {
        "left_key_columns": [],
        "right_key_columns": [],
        "left_row_count": len(train_rows),
        "right_row_count": 0,
        "left_distinct_key_count": 0,
        "right_distinct_key_count": 0,
        "overlap_key_count": 0,
        "left_key_coverage_rate": 0.0,
        "right_key_coverage_rate": 0.0,
    }


def _matches_table_id(path: Path, table_id: str | None) -> bool:
    if not table_id:
        return False
    return path.stem.lower() == table_id.lower()


def _has_empty_join_columns(value: str | list[str] | None) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value == ""
    if isinstance(value, list):
        return not value or any(not isinstance(item, str) or item == "" for item in value)
    return True


def _infer_join_spec(
    benchmark: BenchmarkContext,
    *,
    train_files: list[Path],
    lookup_files: list[Path],
) -> JoinSpec | None:
    if not train_files:
        return None

    primary_train = train_files[0]
    available_lookup_paths = [*lookup_files, *train_files[1:]]
    if not available_lookup_paths:
        return None
    for action in benchmark.visible_actions:
        if action.get("action_type") != "JOIN_LOOKUP":
            continue
        params = action.get("canonical_params", {})
        left_on = params.get("left_on")
        right_on = params.get("right_on")
        if _has_empty_join_columns(left_on) or _has_empty_join_columns(right_on):
            continue
        left_table_id = params.get("left_table_id")
        if left_table_id and not _matches_table_id(primary_train, left_table_id):
            continue
        right_table_id = params.get("right_table_id")
        lookup_path = next((path for path in available_lookup_paths if _matches_table_id(path, right_table_id)), None)
        if lookup_path is None:
            continue
        return JoinSpec(
            lookup_path=lookup_path,
            left_on=left_on,
            right_on=right_on,
        )
    dataset_primary_key = benchmark.bundle.task.get("dataset", {}).get("primary_key")
    if not dataset_primary_key or not lookup_files:
        return None
    return JoinSpec(
        lookup_path=lookup_files[0],
        left_on=dataset_primary_key,
        right_on=dataset_primary_key,
    )


def _build_table_profile(
    *,
    table_name: str,
    table_role: str,
    rows: list[dict[str, str]],
    load_plan: TableLoadPlan,
) -> dict:
    return {
        "table_name": table_name,
        "table_role": table_role,
        "sampling": {
            "mode": load_plan.mode,
            "source_row_count": load_plan.source_row_count,
            "source_column_count": load_plan.source_column_count,
            "loaded_row_count": len(rows),
            "file_size_bytes": load_plan.file_size_bytes,
            "estimated_cells": load_plan.estimated_cells,
            "sample_row_count": load_plan.sample_row_count,
        },
        "schema_profile": profile_table_schema(rows),
        "missingness_profile": profile_missingness(rows),
        "numeric_profile": profile_numeric_columns(rows),
        "boolean_like_profile": profile_boolean_like_columns(rows),
    }


def _resolve_target_profile_rows(
    current_target_rows: list[dict[str, str]] | None,
    rows: list[dict[str, str]],
    target_column: str,
) -> list[dict[str, str]]:
    if current_target_rows is not None:
        return current_target_rows
    if rows and target_column in rows[0]:
        return rows
    return current_target_rows


def _build_cached_materialized_context(benchmark: BenchmarkContext, cached_payload: dict) -> MaterializedBenchmarkContext:
    table_profiles = cached_payload["table_profiles"]
    primary_train_profile = cached_payload["primary_train_profile"]
    join_profile = cached_payload["join_profile"]
    target_profile = cached_payload["target_profile"]
    dataset_summary = render_dataset_summary(
        task=benchmark.bundle.task,
        dataset_paths=benchmark.dataset_paths,
        table_profiles=table_profiles,
        primary_train_profile=primary_train_profile,
        join_profile=join_profile,
        target_profile=target_profile,
    )
    return MaterializedBenchmarkContext(
        benchmark=benchmark,
        train_rows=[],
        lookup_rows=[],
        table_profiles=table_profiles,
        primary_train_profile=primary_train_profile,
        join_profile=join_profile,
        target_profile=target_profile,
        dataset_summary=dataset_summary,
    )


def materialize_benchmark_context(
    benchmark: BenchmarkContext,
    *,
    profile_cache_dir: str | Path | None = None,
) -> MaterializedBenchmarkContext:
    cache_key = build_profile_cache_key(benchmark)
    cached_payload = load_profile_cache(cache_dir=profile_cache_dir, cache_key=cache_key)
    if cached_payload is not None:
        return _build_cached_materialized_context(benchmark, cached_payload)

    dataset_paths = benchmark.dataset_paths
    train_files = dataset_paths.get("train_files", [])
    lookup_files = dataset_paths.get("lookup_files", [])
    if not train_files:
        raise ValueError("Materialized benchmark context requires at least one train file.")

    train_path = train_files[0]
    train_rows, train_load_plan = load_table_rows_for_summary(train_path)
    lookup_rows: list[dict[str, str]] = []
    join_profile = _empty_join_profile(train_rows=train_rows)
    join_spec = _infer_join_spec(
        benchmark,
        train_files=train_files,
        lookup_files=lookup_files,
    )
    target_column = benchmark.bundle.task["dataset"]["target_column"]
    target_profile_rows = _resolve_target_profile_rows(None, train_rows, target_column)
    table_profiles = [
        _build_table_profile(
            table_name=train_path.name,
            table_role="train",
            rows=train_rows,
            load_plan=train_load_plan,
        )
    ]
    primary_train_profile = table_profiles[0]

    for path in train_files[1:]:
        rows, load_plan = load_table_rows_for_summary(path)
        target_profile_rows = _resolve_target_profile_rows(target_profile_rows, rows, target_column)
        if join_spec is not None and path == join_spec.lookup_path:
            lookup_rows = rows
            join_profile = profile_join_key(
                train_rows,
                lookup_rows,
                left_key=join_spec.left_on,
                right_key=join_spec.right_on,
            )
            join_profile["sampling"] = {
                "left_mode": train_load_plan.mode,
                "left_source_row_count": train_load_plan.source_row_count,
                "left_loaded_row_count": len(train_rows),
                "right_mode": load_plan.mode,
                "right_source_row_count": load_plan.source_row_count,
                "right_loaded_row_count": len(lookup_rows),
            }
        table_profiles.append(
            _build_table_profile(
                table_name=path.name,
                table_role="train",
                rows=rows,
                load_plan=load_plan,
            )
        )

    for path in lookup_files:
        if join_spec is not None and path == join_spec.lookup_path and lookup_rows:
            rows = lookup_rows
            load_plan = load_table_rows_for_summary(path)[1]
        else:
            rows, load_plan = load_table_rows_for_summary(path)
        if join_spec is not None and path == join_spec.lookup_path and not lookup_rows:
            lookup_rows = rows
            join_profile = profile_join_key(
                train_rows,
                lookup_rows,
                left_key=join_spec.left_on,
                right_key=join_spec.right_on,
            )
            join_profile["sampling"] = {
                "left_mode": train_load_plan.mode,
                "left_source_row_count": train_load_plan.source_row_count,
                "left_loaded_row_count": len(train_rows),
                "right_mode": load_plan.mode,
                "right_source_row_count": load_plan.source_row_count,
                "right_loaded_row_count": len(lookup_rows),
            }
        table_profiles.append(
            _build_table_profile(
                table_name=path.name,
                table_role="lookup",
                rows=rows,
                load_plan=load_plan,
            )
        )

    if "sampling" not in join_profile:
        join_profile["sampling"] = {
            "left_mode": train_load_plan.mode,
            "left_source_row_count": train_load_plan.source_row_count,
            "left_loaded_row_count": len(train_rows),
            "right_mode": "none" if not lookup_rows else "full",
            "right_source_row_count": len(lookup_rows),
            "right_loaded_row_count": len(lookup_rows),
        }

    target_profile_rows = target_profile_rows or train_rows
    target_profile = profile_target_distribution(
        target_profile_rows,
        target_column,
    )
    dataset_summary = render_dataset_summary(
        task=benchmark.bundle.task,
        dataset_paths=dataset_paths,
        table_profiles=table_profiles,
        primary_train_profile=primary_train_profile,
        join_profile=join_profile,
        target_profile=target_profile,
    )
    write_profile_cache(
        cache_dir=profile_cache_dir,
        cache_key=cache_key,
        payload={
            "table_profiles": table_profiles,
            "primary_train_profile": primary_train_profile,
            "join_profile": join_profile,
            "target_profile": target_profile,
        },
    )
    return MaterializedBenchmarkContext(
        benchmark=benchmark,
        train_rows=train_rows,
        lookup_rows=lookup_rows,
        table_profiles=table_profiles,
        primary_train_profile=primary_train_profile,
        join_profile=join_profile,
        target_profile=target_profile,
        dataset_summary=dataset_summary,
    )
