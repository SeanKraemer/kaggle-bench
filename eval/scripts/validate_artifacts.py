#!/usr/bin/env python3

import json
from collections import Counter, defaultdict, deque
from itertools import product
from pathlib import Path
from typing import Any, cast

from jsonschema import Draft202012Validator


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def format_error_location(error_path: list[object]) -> str:
    return "/".join(str(item) for item in error_path) or "<root>"


def load_validator(path: Path) -> Draft202012Validator:
    if not path.exists():
        raise SystemExit(f"Schema not found: {path}")
    schema_payload = load_json(path)
    if not isinstance(schema_payload, dict):
        raise SystemExit(f"Schema at {path} must be a top-level object")
    return Draft202012Validator(cast(dict[str, Any], schema_payload))


def validate_json_file(path: Path, validator: Draft202012Validator) -> tuple[Any | None, list[str]]:
    try:
        payload = load_json(path)
    except json.JSONDecodeError as exc:
        return None, [f"<root>: invalid JSON ({exc})"]

    errors = sorted(validator.iter_errors(payload), key=lambda err: list(err.path))
    messages = [f"{format_error_location(list(err.path))}: {err.message}" for err in errors]
    return payload, messages


def effective_primary_good_unit_count(candidate_catalog: dict[str, dict[str, object]]) -> int:
    equivalence_groups: set[str] = set()
    ungrouped_units = 0

    for row in candidate_catalog.values():
        if row.get("role") != "good" or row.get("eval_stage") != "core_preprocessing":
            continue
        group = row.get("equivalence_group")
        if isinstance(group, str) and group:
            equivalence_groups.add(group)
        else:
            ungrouped_units += 1

    return ungrouped_units + len(equivalence_groups)


def validate_selected_action_set_order(
    owner_label: str,
    selected_action_ids: set[str],
    candidate_catalog: dict[str, dict[str, object]],
) -> list[str]:
    if not selected_action_ids:
        return []

    edges: dict[str, set[str]] = {action_id: set() for action_id in selected_action_ids}
    indegree: dict[str, int] = {action_id: 0 for action_id in selected_action_ids}
    conflict_pairs: set[tuple[str, str]] = set()

    for action_id in sorted(selected_action_ids):
        row = candidate_catalog.get(action_id, {})

        for field_name in ("must_follow_action_ids", "invalidates_action_ids"):
            refs = row.get(field_name, [])
            if not isinstance(refs, list):
                continue
            for ref_id in refs:
                if ref_id not in selected_action_ids or ref_id == action_id:
                    continue
                if action_id not in edges[ref_id]:
                    edges[ref_id].add(action_id)
                    indegree[action_id] += 1

        conflict_refs = row.get("conflicts_with_action_ids", [])
        if not isinstance(conflict_refs, list):
            continue
        for ref_id in conflict_refs:
            if ref_id in selected_action_ids and ref_id != action_id:
                left_action_id, right_action_id = sorted((action_id, ref_id))
                conflict_pairs.add((left_action_id, right_action_id))

    errors = [
        f"{owner_label}: selected action set has an unsatisfiable conflict pair `{left}` and `{right}`"
        for left, right in sorted(conflict_pairs)
    ]
    if errors:
        return errors

    frontier = deque(sorted(action_id for action_id, degree in indegree.items() if degree == 0))
    visited = 0
    while frontier:
        action_id = frontier.popleft()
        visited += 1
        for next_action_id in sorted(edges[action_id]):
            indegree[next_action_id] -= 1
            if indegree[next_action_id] == 0:
                frontier.append(next_action_id)

    if visited != len(selected_action_ids):
        errors.append(f"{owner_label}: selected action set has no valid execution order")

    return errors


def validate_good_selection_coherence(
    candidate_path: Path,
    candidate_catalog: dict[str, dict[str, object]],
    scope: str,
) -> list[str]:
    fixed_actions: set[str] = set()
    grouped_actions: dict[str, list[str]] = defaultdict(list)

    for action_id, row in candidate_catalog.items():
        if row.get("role") != "good":
            continue
        if scope == "primary" and row.get("eval_stage") != "core_preprocessing":
            continue
        group = row.get("equivalence_group")
        if isinstance(group, str) and group:
            grouped_actions[group].append(action_id)
        else:
            fixed_actions.add(action_id)

    group_items = sorted((group, sorted(action_ids)) for group, action_ids in grouped_actions.items())
    combination_count = 1
    for _, action_ids in group_items:
        combination_count *= len(action_ids)

    if combination_count > 512:
        return [
            f"{candidate_path}: representative `{scope}` good-selection search space is too large ({combination_count} combinations)"
        ]

    option_lists = [action_ids for _, action_ids in group_items]
    representative_choices = product(*option_lists) if option_lists else [()]

    for choice in representative_choices:
        representative_selection = set(fixed_actions)
        representative_selection.update(choice)
        if not validate_selected_action_set_order(
            f"{candidate_path}: representative `{scope}` good selection",
            representative_selection,
            candidate_catalog,
        ):
            return []

    return [f"{candidate_path}: no valid execution order exists for representative `{scope}` good selections"]


def infer_three_bucket(metric_value: int, thresholds: dict[str, object]) -> str | None:
    low_max = thresholds.get("low_max")
    medium_max = thresholds.get("medium_max")
    if not isinstance(low_max, int) or not isinstance(medium_max, int):
        return None
    if low_max > medium_max:
        return None
    if metric_value <= low_max:
        return "low"
    if metric_value <= medium_max:
        return "medium"
    return "high"


def infer_four_bucket(metric_value: int, thresholds: dict[str, object]) -> str | None:
    small_max = thresholds.get("small_max")
    medium_max = thresholds.get("medium_max")
    large_max = thresholds.get("large_max")
    if not isinstance(small_max, int) or not isinstance(medium_max, int) or not isinstance(large_max, int):
        return None
    if not (small_max <= medium_max <= large_max):
        return None
    if metric_value <= small_max:
        return "small"
    if metric_value <= medium_max:
        return "medium"
    if metric_value <= large_max:
        return "large"
    return "xlarge"


def validate_task_bucket_criteria(
    task_payload: dict[str, object],
    shared_criteria: dict[str, object],
) -> list[str]:
    task_characteristics = task_payload.get("task_characteristics")
    if not isinstance(task_characteristics, dict):
        return []

    errors: list[str] = []

    dataset_size_criteria = shared_criteria.get("dataset_size")
    if isinstance(dataset_size_criteria, dict):
        metric_value = task_characteristics.get("dataset_size_raw")
        thresholds = dataset_size_criteria.get("thresholds")
        if isinstance(metric_value, int) and isinstance(thresholds, dict):
            inferred = infer_four_bucket(metric_value, thresholds)
            if inferred is None:
                errors.append("shared bucket criteria `dataset_size` has invalid threshold ordering")
            elif task_characteristics.get("dataset_size_bucket") != inferred:
                errors.append(
                    "task_characteristics/dataset_size_bucket: "
                    f"expected `{inferred}` from shared criteria, found `{task_characteristics.get('dataset_size_bucket')}`"
                )

    for criteria_key, raw_field, bucket_field in (
        ("feature_dimensionality", "feature_dimensionality_raw", "feature_dimensionality_bucket"),
        ("preprocessing_complexity", "preprocessing_complexity_raw", "preprocessing_complexity_bucket"),
    ):
        bucket_criteria = shared_criteria.get(criteria_key)
        if not isinstance(bucket_criteria, dict):
            continue
        metric_value = task_characteristics.get(raw_field)
        thresholds = bucket_criteria.get("thresholds")
        if isinstance(metric_value, int) and isinstance(thresholds, dict):
            inferred = infer_three_bucket(metric_value, thresholds)
            if inferred is None:
                errors.append(f"shared bucket criteria `{criteria_key}` has invalid threshold ordering")
            elif task_characteristics.get(bucket_field) != inferred:
                errors.append(
                    f"task_characteristics/{bucket_field}: "
                    f"expected `{inferred}` from shared criteria, found `{task_characteristics.get(bucket_field)}`"
                )

    return errors


def resolve_artifact_path(owner_path: Path, raw_path: str) -> Path:
    artifact_path = Path(raw_path)
    if not artifact_path.is_absolute():
        artifact_path = (owner_path.parent / artifact_path).resolve()
    return artifact_path


def validate_artifact_refs(owner_path: Path, artifact_refs: object) -> tuple[list[str], list[Path]]:
    if not isinstance(artifact_refs, list):
        return [], []

    errors: list[str] = []
    resolved_paths: list[Path] = []
    for idx, artifact_ref in enumerate(artifact_refs):
        if not isinstance(artifact_ref, dict):
            continue
        raw_path = artifact_ref.get("path")
        if not isinstance(raw_path, str) or not raw_path:
            continue
        artifact_path = resolve_artifact_path(owner_path, raw_path)
        resolved_paths.append(artifact_path)
        if not artifact_path.exists():
            errors.append(f"artifact_refs/{idx}/path: referenced artifact does not exist at `{raw_path}`")
    return errors, resolved_paths


def load_candidate_catalog(path: Path) -> tuple[dict[str, dict[str, object]], list[str]]:
    try:
        payload = load_json(path)
    except FileNotFoundError:
        return {}, [f"{path}: missing file"]
    except json.JSONDecodeError as exc:
        return {}, [f"{path}: invalid JSON ({exc})"]

    if not isinstance(payload, dict):
        return {}, [f"{path}: expected top-level object"]

    rows = payload.get("actions")
    if not isinstance(rows, list):
        return {}, [f"{path}: expected `actions` to be an array"]

    seen_ids: set[str] = set()
    catalog: dict[str, dict[str, object]] = {}
    errors: list[str] = []
    role_counts: Counter[str] = Counter()
    equivalence_group_stages: dict[str, set[str]] = defaultdict(set)

    for idx, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"{path}: actions/{idx}: expected object")
            continue

        action_id = row.get("action_id")
        if not isinstance(action_id, str) or not action_id:
            errors.append(f"{path}: actions/{idx}/action_id: expected non-empty string")
            continue
        if action_id in seen_ids:
            errors.append(f"{path}: actions/{idx}/action_id: duplicate id `{action_id}`")
            continue
        seen_ids.add(action_id)
        catalog[action_id] = row

        role = row.get("role")
        if isinstance(role, str):
            role_counts[role] += 1

        group = row.get("equivalence_group")
        if group is not None and row.get("role") != "good":
            errors.append(f"{path}: actions/{idx}/equivalence_group: only `good` actions may define equivalence groups")
        elif isinstance(group, str) and group:
            stage = row.get("eval_stage")
            if isinstance(stage, str):
                equivalence_group_stages[group].add(stage)

    if role_counts.get("good", 0) == 0:
        errors.append(f"{path}: bank must contain at least one `good` action")
    if role_counts.get("bad", 0) == 0:
        errors.append(f"{path}: bank must contain at least one `bad` action")

    primary_good_units = effective_primary_good_unit_count(catalog)
    if primary_good_units == 0:
        errors.append(f"{path}: bank must contain at least one primary-scope effective good unit")
    elif role_counts.get("bad", 0) < 3 * primary_good_units:
        errors.append(
            f"{path}: bank must satisfy `bad >= 3 * primary_effective_good_units`; "
            f"found bad={role_counts.get('bad', 0)} primary_effective_good_units={primary_good_units}"
        )

    for group, stages in sorted(equivalence_group_stages.items()):
        if len(stages) > 1:
            errors.append(
                f"{path}: equivalence_group `{group}` spans multiple eval_stage values: {', '.join(sorted(stages))}"
            )

    for action_id, row in catalog.items():
        for field_name in ("must_follow_action_ids", "invalidates_action_ids", "conflicts_with_action_ids"):
            refs = row.get(field_name, [])
            if not isinstance(refs, list):
                continue
            for ref_idx, ref_id in enumerate(refs):
                if ref_id == action_id:
                    errors.append(f"{path}: action `{action_id}` {field_name}/{ref_idx}: self-reference is not allowed")
                elif ref_id not in catalog:
                    errors.append(f"{path}: action `{action_id}` {field_name}/{ref_idx}: unknown action id `{ref_id}`")

    errors.extend(validate_good_selection_coherence(path, catalog, "primary"))
    errors.extend(validate_good_selection_coherence(path, catalog, "all"))

    return catalog, errors


def validate_testcase_payload(
    testcase_path: Path,
    testcase_payload: dict[str, object],
    expected_slug: str,
    task_path: Path,
    candidate_catalog: dict[str, dict[str, object]],
    candidate_ids: set[str],
    seen_testcase_ids: dict[str, Path],
) -> list[str]:
    errors: list[str] = []

    if testcase_payload.get("competition_slug") != expected_slug:
        errors.append(
            f"competition_slug mismatch: expected `{expected_slug}`, found `{testcase_payload.get('competition_slug')}`"
        )

    resolved_task_ref = (testcase_path.parent / str(testcase_payload.get("task_ref"))).resolve()
    if resolved_task_ref != task_path.resolve():
        errors.append(f"task_ref must resolve to {task_path}")

    testcase_id = testcase_payload.get("testcase_id")
    if isinstance(testcase_id, str) and testcase_id:
        prior_owner = seen_testcase_ids.get(testcase_id)
        if prior_owner is not None:
            errors.append(f"testcase_id `{testcase_id}` is duplicated; first defined in `{prior_owner}`")
        else:
            seen_testcase_ids[testcase_id] = testcase_path

    input_payload = testcase_payload.get("input")
    context_action_ids = input_payload.get("context_action_ids", []) if isinstance(input_payload, dict) else []
    if isinstance(context_action_ids, list):
        known_context_action_ids: set[str] = set()
        for idx, action_id in enumerate(context_action_ids):
            if action_id not in candidate_ids:
                errors.append(f"input/context_action_ids/{idx}: unknown candidate action `{action_id}`")
            elif isinstance(action_id, str):
                known_context_action_ids.add(action_id)

        errors.extend(
            validate_selected_action_set_order(
                f"{testcase_path}: input.context_action_ids",
                known_context_action_ids,
                candidate_catalog,
            )
        )

    return errors


def validate_output_payload(
    output_path: Path,
    output_payload: dict[str, object],
    expected_slug: str,
    testcase_contexts: dict[str, set[str]],
    candidate_catalog: dict[str, dict[str, object]],
    candidate_ids: set[str],
) -> list[str]:
    errors: list[str] = []

    if output_payload.get("competition_slug") != expected_slug:
        errors.append(
            f"competition_slug mismatch: expected `{expected_slug}`, found `{output_payload.get('competition_slug')}`"
        )

    testcase_id = output_payload.get("testcase_id")
    if not isinstance(testcase_id, str) or testcase_id not in testcase_contexts:
        errors.append(f"unknown testcase_id `{testcase_id}`")
        context_action_ids: set[str] = set()
    else:
        context_action_ids = testcase_contexts[testcase_id]

    artifact_errors, _ = validate_artifact_refs(output_path, output_payload.get("artifact_refs"))
    errors.extend(artifact_errors)

    predicted_add = output_payload.get("predicted_add_action_ids", [])
    predicted_remove = output_payload.get("predicted_remove_action_ids", [])

    if isinstance(predicted_add, list):
        valid_predicted_add: set[str] = set()
        for idx, action_id in enumerate(predicted_add):
            if action_id not in candidate_ids:
                errors.append(f"predicted_add_action_ids/{idx}: unknown candidate action `{action_id}`")
            elif action_id in context_action_ids:
                errors.append(f"predicted_add_action_ids/{idx}: action `{action_id}` is already in testcase context")
            elif isinstance(action_id, str):
                valid_predicted_add.add(action_id)
    else:
        valid_predicted_add = set()

    if isinstance(predicted_remove, list):
        valid_predicted_remove: set[str] = set()
        for idx, action_id in enumerate(predicted_remove):
            if action_id not in candidate_ids:
                errors.append(f"predicted_remove_action_ids/{idx}: unknown candidate action `{action_id}`")
            elif action_id not in context_action_ids:
                errors.append(f"predicted_remove_action_ids/{idx}: action `{action_id}` is not in testcase context")
            elif isinstance(action_id, str):
                valid_predicted_remove.add(action_id)
    else:
        valid_predicted_remove = set()

    if isinstance(predicted_add, list) and isinstance(predicted_remove, list):
        overlap = sorted(set(predicted_add) & set(predicted_remove))
        for action_id in overlap:
            errors.append(
                f"action `{action_id}` cannot appear in both predicted_add_action_ids and predicted_remove_action_ids"
            )

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    data_dir = repo_root / "data"
    tasks_dir = data_dir / "tasks"
    schema_dir = data_dir / "schema"
    shared_schema_dir = data_dir / "schema"

    task_validator = load_validator(shared_schema_dir / "task.schema.json")
    task_bucket_criteria_validator = load_validator(
        shared_schema_dir / "task_characteristic_bucket_criteria.schema.json"
    )
    candidate_validator = load_validator(schema_dir / "candidate_actions.schema.json")
    testcase_validator = load_validator(schema_dir / "testcase.schema.json")
    output_validator = load_validator(schema_dir / "output.schema.json")

    task_bucket_criteria_path = shared_schema_dir / "task_characteristic_bucket_criteria.json"
    task_bucket_criteria_payload, task_bucket_criteria_errors = validate_json_file(
        task_bucket_criteria_path,
        task_bucket_criteria_validator,
    )

    validated_files = 1
    if task_bucket_criteria_errors:
        print(f"[FAIL] {task_bucket_criteria_path}")
        for message in task_bucket_criteria_errors:
            print(f"  - {message}")
        raise SystemExit(f"Schema validation failed with {len(task_bucket_criteria_errors)} error(s).")
    print(f"[PASS] {task_bucket_criteria_path}")

    if not isinstance(task_bucket_criteria_payload, dict):
        raise SystemExit(f"Schema validation failed: expected object in {task_bucket_criteria_path}")

    total_errors = 0
    task_dirs = sorted(
        path for path in tasks_dir.iterdir() if path.is_dir() and (path / "candidate_actions.json").exists()
    )

    for task_dir in task_dirs:
        task_path = task_dir / "task.json"
        candidate_path = task_dir / "candidate_actions.json"
        testcase_paths = sorted((task_dir / "testcases").glob("*.json")) if (task_dir / "testcases").exists() else []
        output_paths = sorted((task_dir / "outputs").glob("*.json")) if (task_dir / "outputs").exists() else []
        adapted_output_paths = (
            sorted((task_dir / "adapted_outputs").glob("*.json")) if (task_dir / "adapted_outputs").exists() else []
        )
        human_output_paths = (
            sorted((task_dir / "human_baseline").glob("*.json")) if (task_dir / "human_baseline").exists() else []
        )

        expected_slug = task_dir.name
        seen_testcase_ids: dict[str, Path] = {}
        testcase_contexts: dict[str, set[str]] = {}
        candidate_catalog: dict[str, dict[str, object]] = {}

        if task_path.exists():
            task_payload, task_errors = validate_json_file(task_path, task_validator)
            validated_files += 1
            task_extra_errors: list[str] = []
            if isinstance(task_payload, dict):
                if task_payload.get("competition_slug") != expected_slug:
                    task_extra_errors.append(
                        f"competition_slug mismatch: expected `{expected_slug}`, found `{task_payload.get('competition_slug')}`"
                    )
                task_extra_errors.extend(validate_task_bucket_criteria(task_payload, task_bucket_criteria_payload))
            all_errors = task_errors + task_extra_errors
            if all_errors:
                print(f"[FAIL] {task_path}")
                for message in all_errors:
                    print(f"  - {message}")
                total_errors += len(all_errors)
            else:
                print(f"[PASS] {task_path}")
        else:
            print(f"[FAIL] {task_dir}")
            print("  - missing task.json")
            total_errors += 1
            continue

        if candidate_path.exists():
            candidate_payload, candidate_errors = validate_json_file(candidate_path, candidate_validator)
            validated_files += 1
            candidate_extra_errors: list[str] = []
            if isinstance(candidate_payload, dict):
                if candidate_payload.get("competition_slug") != expected_slug:
                    candidate_extra_errors.append(
                        f"competition_slug mismatch: expected `{expected_slug}`, found `{candidate_payload.get('competition_slug')}`"
                    )
                candidate_catalog, catalog_errors = load_candidate_catalog(candidate_path)
                candidate_extra_errors.extend(catalog_errors)
            all_errors = candidate_errors + candidate_extra_errors
            if all_errors:
                print(f"[FAIL] {candidate_path}")
                for message in all_errors:
                    print(f"  - {message}")
                total_errors += len(all_errors)
            else:
                print(f"[PASS] {candidate_path}")
        else:
            print(f"[FAIL] {task_dir}")
            print("  - missing candidate_actions.json")
            total_errors += 1
            continue

        candidate_ids = set(candidate_catalog)

        for testcase_path in testcase_paths:
            testcase_payload, testcase_errors = validate_json_file(testcase_path, testcase_validator)
            validated_files += 1
            testcase_extra_errors: list[str] = []
            if isinstance(testcase_payload, dict):
                testcase_extra_errors.extend(
                    validate_testcase_payload(
                        testcase_path,
                        testcase_payload,
                        expected_slug,
                        task_path,
                        candidate_catalog,
                        candidate_ids,
                        seen_testcase_ids,
                    )
                )
                testcase_id = testcase_payload.get("testcase_id")
                input_payload = testcase_payload.get("input")
                context_ids = input_payload.get("context_action_ids", []) if isinstance(input_payload, dict) else []
                if isinstance(testcase_id, str) and isinstance(context_ids, list):
                    testcase_contexts[testcase_id] = set(context_ids)
            all_errors = testcase_errors + testcase_extra_errors
            if all_errors:
                print(f"[FAIL] {testcase_path}")
                for message in all_errors:
                    print(f"  - {message}")
                total_errors += len(all_errors)
            else:
                print(f"[PASS] {testcase_path}")

        for output_path in output_paths + adapted_output_paths + human_output_paths:
            output_payload, output_errors = validate_json_file(output_path, output_validator)
            validated_files += 1
            output_extra_errors: list[str] = []
            if isinstance(output_payload, dict):
                output_extra_errors.extend(
                    validate_output_payload(
                        output_path,
                        output_payload,
                        expected_slug,
                        testcase_contexts,
                        candidate_catalog,
                        candidate_ids,
                    )
                )
            all_errors = output_errors + output_extra_errors
            if all_errors:
                print(f"[FAIL] {output_path}")
                for message in all_errors:
                    print(f"  - {message}")
                total_errors += len(all_errors)
            else:
                print(f"[PASS] {output_path}")

    print(f"Validated files: {validated_files}")
    if total_errors:
        raise SystemExit(f"Schema validation failed with {total_errors} error(s).")

    print("All eval task artifacts are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
