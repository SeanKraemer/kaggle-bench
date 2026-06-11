#!/usr/bin/env python3
"""Evaluate one or more output artifacts against a single testcase."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_div(numerator: float, denominator: float, default: float = 0.0) -> float:
    if denominator == 0:
        return default
    return numerator / denominator


def round_metric(value: float) -> float:
    return round(value, 6)


def mean_nullable(values: list[int | float | None]) -> float | None:
    concrete = [value for value in values if value is not None]
    if not concrete:
        return None
    return round_metric(sum(concrete) / len(concrete))


def variance(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    mean_value = sum(values) / len(values)
    return round_metric(sum((value - mean_value) ** 2 for value in values) / len(values))


def load_output_metadata(input_path: Path, output_artifact: dict[str, Any]) -> dict[str, Any] | None:
    metadata_ref = next(
        (ref for ref in output_artifact.get("artifact_refs", []) if ref.get("kind") == "metadata"), None
    )
    if metadata_ref is None:
        return None

    metadata_path = (input_path.parent / metadata_ref["path"]).resolve()
    if not metadata_path.exists():
        return None

    return load_json(metadata_path)


def is_active_scope(action: dict[str, Any], stage_scope: str) -> bool:
    return stage_scope == "all" or action["eval_stage"] == "core_preprocessing"


def unit_key(kind: str, unit_id: str) -> str:
    return f"{kind}:{unit_id}"


def sort_units(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(units, key=lambda unit: (unit["kind"], unit["id"]))


def build_candidate_catalog(candidate_bundle: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {action["action_id"]: action for action in candidate_bundle["actions"]}


def analyze_selected_action_set(
    selected_action_ids: set[str],
    action_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    edges: dict[str, set[str]] = {action_id: set() for action_id in selected_action_ids}
    indegree: dict[str, int] = {action_id: 0 for action_id in selected_action_ids}
    conflict_pairs: set[tuple[str, str]] = set()

    for action_id in sorted(selected_action_ids):
        row = action_by_id[action_id]

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

    frontier = deque(sorted(action_id for action_id, degree in indegree.items() if degree == 0))
    visited: set[str] = set()
    remaining_indegree = dict(indegree)
    while frontier:
        action_id = frontier.popleft()
        visited.add(action_id)
        for next_action_id in sorted(edges[action_id]):
            remaining_indegree[next_action_id] -= 1
            if remaining_indegree[next_action_id] == 0:
                frontier.append(next_action_id)

    cycle_action_ids = sorted(action_id for action_id in selected_action_ids if action_id not in visited)
    return {
        "is_valid": not conflict_pairs and not cycle_action_ids,
        "conflict_pairs": [
            {"left_action_id": left, "right_action_id": right} for left, right in sorted(conflict_pairs)
        ],
        "cycle_action_ids": cycle_action_ids,
    }


def derive_expected_add_units(
    action_by_id: dict[str, dict[str, Any]],
    context_action_ids: set[str],
    stage_scope: str,
) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    satisfied_groups: set[str] = set()
    expected_units: dict[str, dict[str, Any]] = {}
    predicted_action_to_unit_key: dict[str, str] = {}
    candidate_group_members: dict[str, list[str]] = defaultdict(list)

    for action_id in context_action_ids:
        action = action_by_id[action_id]
        if action["role"] != "good" or not is_active_scope(action, stage_scope):
            continue
        group = action.get("equivalence_group")
        if isinstance(group, str) and group:
            satisfied_groups.add(group)

    for action_id, action in action_by_id.items():
        if action_id in context_action_ids or action["role"] != "good" or not is_active_scope(action, stage_scope):
            continue

        group = action.get("equivalence_group")
        if isinstance(group, str) and group:
            predicted_action_to_unit_key[action_id] = unit_key("equivalence_group", group)
            if group not in satisfied_groups:
                candidate_group_members[group].append(action_id)
            continue

        action_unit_key = unit_key("action", action_id)
        predicted_action_to_unit_key[action_id] = action_unit_key
        expected_units[action_unit_key] = {
            "kind": "action",
            "id": action_id,
        }

    for group, member_ids in sorted(candidate_group_members.items()):
        expected_units[unit_key("equivalence_group", group)] = {
            "kind": "equivalence_group",
            "id": group,
            "members": sorted(member_ids),
        }

    return expected_units, predicted_action_to_unit_key


def derive_expected_remove_action_ids(
    action_by_id: dict[str, dict[str, Any]],
    context_action_ids: set[str],
    stage_scope: str,
) -> set[str]:
    return {
        action_id
        for action_id in context_action_ids
        if action_by_id[action_id]["role"] == "bad" and is_active_scope(action_by_id[action_id], stage_scope)
    }


def classify_predictions(
    predicted_action_ids: list[Any],
    *,
    side: str,
    context_action_ids: set[str],
    action_by_id: dict[str, dict[str, Any]],
    stage_scope: str,
) -> tuple[list[str], list[dict[str, Any]], list[dict[str, Any]]]:
    unique_active_action_ids: list[str] = []
    invalid_predictions: list[dict[str, Any]] = []
    stage_filtered_predictions: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    for index, raw_action_id in enumerate(predicted_action_ids):
        if not isinstance(raw_action_id, str):
            invalid_predictions.append(
                {
                    "output_index": index,
                    "action_id": raw_action_id,
                    "reason": "non_string_action_id",
                }
            )
            continue

        if raw_action_id in seen_ids:
            invalid_predictions.append(
                {
                    "output_index": index,
                    "action_id": raw_action_id,
                    "reason": "duplicate_prediction",
                }
            )
            continue
        seen_ids.add(raw_action_id)

        action = action_by_id.get(raw_action_id)
        if action is None:
            invalid_predictions.append(
                {
                    "output_index": index,
                    "action_id": raw_action_id,
                    "reason": "unknown_action_id",
                }
            )
            continue

        if side == "add" and raw_action_id in context_action_ids:
            invalid_predictions.append(
                {
                    "output_index": index,
                    "action_id": raw_action_id,
                    "reason": "action_already_in_context",
                }
            )
            continue

        if side == "remove" and raw_action_id not in context_action_ids:
            invalid_predictions.append(
                {
                    "output_index": index,
                    "action_id": raw_action_id,
                    "reason": "action_not_in_context",
                }
            )
            continue

        if not is_active_scope(action, stage_scope):
            stage_filtered_predictions.append(
                {
                    "output_index": index,
                    "action_id": raw_action_id,
                    "eval_stage": action["eval_stage"],
                }
            )
            continue

        unique_active_action_ids.append(raw_action_id)

    return unique_active_action_ids, invalid_predictions, stage_filtered_predictions


def build_invalid_add_details(
    predicted_add_action_ids: list[str],
    final_state_analysis: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    conflicts_by_action_id: dict[str, list[str]] = defaultdict(list)
    for pair in final_state_analysis["conflict_pairs"]:
        left_action_id = pair["left_action_id"]
        right_action_id = pair["right_action_id"]
        conflicts_by_action_id[left_action_id].append(right_action_id)
        conflicts_by_action_id[right_action_id].append(left_action_id)

    cycle_action_ids = set(final_state_analysis["cycle_action_ids"])
    details: dict[str, dict[str, Any]] = {}
    for action_id in predicted_add_action_ids:
        conflicts_with = sorted(conflicts_by_action_id.get(action_id, []))
        in_cycle = action_id in cycle_action_ids
        if not conflicts_with and not in_cycle:
            continue
        details[action_id] = {
            "reason": "invalid_final_action_state",
            "conflicts_with_action_ids": conflicts_with,
            "cycle_member": in_cycle,
        }
    return details


def compute_side_metrics(
    expected_count: int, true_positive_count: int, false_positive_count: int
) -> dict[str, float | int]:
    false_negative_count = expected_count - true_positive_count
    predicted_count = true_positive_count + false_positive_count

    if expected_count == 0 and predicted_count == 0:
        precision = 1.0
        recall = 1.0
        f1 = 1.0
    elif expected_count == 0 and predicted_count > 0:
        precision = 0.0
        recall = 1.0
        f1 = 0.0
    else:
        precision = safe_div(true_positive_count, predicted_count, default=0.0)
        recall = safe_div(true_positive_count, expected_count, default=0.0)
        f1 = 0.0
        if precision > 0 or recall > 0:
            f1 = safe_div(2 * precision * recall, precision + recall, default=0.0)

    return {
        "expected_count": expected_count,
        "predicted_count": predicted_count,
        "true_positive_count": true_positive_count,
        "false_positive_count": false_positive_count,
        "false_negative_count": false_negative_count,
        "precision": round_metric(precision),
        "recall": round_metric(recall),
        "f1": round_metric(f1),
    }


def evaluate_add_side(
    action_by_id: dict[str, dict[str, Any]],
    context_action_ids: set[str],
    predicted_add_action_ids: list[Any],
    stage_scope: str,
    final_state_analysis: dict[str, Any],
) -> dict[str, Any]:
    expected_units, predicted_action_to_unit_key = derive_expected_add_units(
        action_by_id, context_action_ids, stage_scope
    )
    expected_unit_keys = set(expected_units)

    active_predicted_add_action_ids, invalid_predictions, stage_filtered_predictions = classify_predictions(
        predicted_add_action_ids,
        side="add",
        context_action_ids=context_action_ids,
        action_by_id=action_by_id,
        stage_scope=stage_scope,
    )

    invalid_add_details = build_invalid_add_details(active_predicted_add_action_ids, final_state_analysis)
    matched_units: list[dict[str, Any]] = []
    satisfied_unit_keys: set[str] = set()
    true_positive_count = 0
    false_positive_count = len(invalid_predictions)

    for output_index, action_id in enumerate(active_predicted_add_action_ids):
        invalid_detail = invalid_add_details.get(action_id)
        if invalid_detail is not None:
            invalid_predictions.append(
                {
                    "output_index": output_index,
                    "action_id": action_id,
                    **invalid_detail,
                }
            )
            false_positive_count += 1
            continue

        matched_unit_key = predicted_action_to_unit_key.get(action_id)
        if matched_unit_key is None:
            invalid_predictions.append(
                {
                    "output_index": output_index,
                    "action_id": action_id,
                    "reason": "action_is_not_a_good_add_target",
                }
            )
            false_positive_count += 1
            continue

        if matched_unit_key in expected_unit_keys and matched_unit_key not in satisfied_unit_keys:
            true_positive_count += 1
            satisfied_unit_keys.add(matched_unit_key)
            matched_units.append(
                {
                    "output_index": output_index,
                    "predicted_action_id": action_id,
                    "unit": expected_units[matched_unit_key],
                }
            )
            continue

        invalid_predictions.append(
            {
                "output_index": output_index,
                "action_id": action_id,
                "reason": "extra_prediction_or_duplicate_equivalence_member",
            }
        )
        false_positive_count += 1

    metrics = compute_side_metrics(len(expected_units), true_positive_count, false_positive_count)
    missed_units = sort_units(
        [unit for unit_key_value, unit in expected_units.items() if unit_key_value not in satisfied_unit_keys]
    )

    return {
        "stage_scope": stage_scope,
        "expected_unit_count": metrics["expected_count"],
        "predicted_action_count": metrics["predicted_count"],
        "true_positive_count": metrics["true_positive_count"],
        "false_positive_count": metrics["false_positive_count"],
        "false_negative_count": metrics["false_negative_count"],
        "add_precision": metrics["precision"],
        "add_recall": metrics["recall"],
        "add_f1": metrics["f1"],
        "precision": metrics["precision"],
        "recall": metrics["recall"],
        "f1": metrics["f1"],
        "matched_units": matched_units,
        "missed_units": missed_units,
        "invalid_predictions": invalid_predictions,
        "stage_filtered_predictions": stage_filtered_predictions,
    }


def evaluate_remove_side(
    action_by_id: dict[str, dict[str, Any]],
    context_action_ids: set[str],
    predicted_remove_action_ids: list[Any],
    stage_scope: str,
) -> dict[str, Any]:
    expected_remove_action_ids = derive_expected_remove_action_ids(action_by_id, context_action_ids, stage_scope)

    active_predicted_remove_action_ids, invalid_predictions, stage_filtered_predictions = classify_predictions(
        predicted_remove_action_ids,
        side="remove",
        context_action_ids=context_action_ids,
        action_by_id=action_by_id,
        stage_scope=stage_scope,
    )

    matched_remove_action_ids: list[str] = []
    true_positive_count = 0
    false_positive_count = len(invalid_predictions)
    expected_remove_action_id_set = set(expected_remove_action_ids)

    for output_index, action_id in enumerate(active_predicted_remove_action_ids):
        if action_id in expected_remove_action_id_set:
            true_positive_count += 1
            matched_remove_action_ids.append(action_id)
            continue

        invalid_predictions.append(
            {
                "output_index": output_index,
                "action_id": action_id,
                "reason": "remove_prediction_not_expected",
            }
        )
        false_positive_count += 1

    metrics = compute_side_metrics(len(expected_remove_action_ids), true_positive_count, false_positive_count)
    matched_remove_action_id_set = set(matched_remove_action_ids)
    missed_remove_action_ids = sorted(expected_remove_action_id_set - matched_remove_action_id_set)

    return {
        "stage_scope": stage_scope,
        "expected_action_count": metrics["expected_count"],
        "predicted_action_count": metrics["predicted_count"],
        "true_positive_count": metrics["true_positive_count"],
        "false_positive_count": metrics["false_positive_count"],
        "false_negative_count": metrics["false_negative_count"],
        "remove_precision": metrics["precision"],
        "remove_recall": metrics["recall"],
        "remove_f1": metrics["f1"],
        "rollback_accuracy": metrics["recall"],
        "precision": metrics["precision"],
        "recall": metrics["recall"],
        "f1": metrics["f1"],
        "matched_action_ids": sorted(matched_remove_action_id_set),
        "missed_action_ids": missed_remove_action_ids,
        "invalid_predictions": invalid_predictions,
        "stage_filtered_predictions": stage_filtered_predictions,
    }


def build_summary(
    add_result: dict[str, Any], remove_result: dict[str, Any], success_threshold: float
) -> dict[str, Any]:
    task_completion_score = 0.5 * add_result["add_f1"] + 0.5 * remove_result["remove_recall"]
    strict_task_completion_score = 0.5 * add_result["add_f1"] + 0.5 * remove_result["remove_f1"]
    return {
        "task_completion_score": round_metric(task_completion_score),
        "strict_task_completion_score": round_metric(strict_task_completion_score),
        "success_threshold": round_metric(success_threshold),
        "task_success": task_completion_score >= success_threshold,
    }


def evaluate(
    testcase_path: Path,
    input_path: Path,
    stage_scope: str,
    success_threshold: float,
) -> dict[str, Any]:
    testcase = load_json(testcase_path)
    output_artifact = load_json(input_path)
    task_dir = testcase_path.parent.parent
    candidate_bundle = load_json(task_dir / "candidate_actions.json")
    action_by_id = build_candidate_catalog(candidate_bundle)

    if testcase["competition_slug"] != output_artifact["competition_slug"]:
        raise SystemExit("competition_slug mismatch between testcase and input")
    if testcase["testcase_id"] != output_artifact["testcase_id"]:
        raise SystemExit("testcase_id mismatch between testcase and input")

    raw_context_action_ids = testcase["input"]["context_action_ids"]
    unknown_context_action_ids = sorted(
        action_id for action_id in raw_context_action_ids if action_id not in action_by_id
    )
    if unknown_context_action_ids:
        raise SystemExit(f"unknown context_action_ids in testcase: {', '.join(unknown_context_action_ids)}")
    context_action_ids = set(raw_context_action_ids)

    active_predicted_add_action_ids, _, _ = classify_predictions(
        output_artifact["predicted_add_action_ids"],
        side="add",
        context_action_ids=context_action_ids,
        action_by_id=action_by_id,
        stage_scope=stage_scope,
    )
    active_predicted_remove_action_ids, _, _ = classify_predictions(
        output_artifact["predicted_remove_action_ids"],
        side="remove",
        context_action_ids=context_action_ids,
        action_by_id=action_by_id,
        stage_scope=stage_scope,
    )
    final_state_action_ids = (context_action_ids - set(active_predicted_remove_action_ids)) | set(
        active_predicted_add_action_ids
    )
    final_state_analysis = analyze_selected_action_set(final_state_action_ids, action_by_id)

    add_result = evaluate_add_side(
        action_by_id=action_by_id,
        context_action_ids=context_action_ids,
        predicted_add_action_ids=output_artifact["predicted_add_action_ids"],
        stage_scope=stage_scope,
        final_state_analysis=final_state_analysis,
    )
    remove_result = evaluate_remove_side(
        action_by_id=action_by_id,
        context_action_ids=context_action_ids,
        predicted_remove_action_ids=output_artifact["predicted_remove_action_ids"],
        stage_scope=stage_scope,
    )
    summary = build_summary(add_result, remove_result, success_threshold)
    metadata = load_output_metadata(input_path, output_artifact)

    return {
        "competition_slug": testcase["competition_slug"],
        "testcase_id": testcase["testcase_id"],
        "input_path": str(input_path),
        "testcase_path": str(testcase_path),
        "agent_name": output_artifact["agent_name"],
        "run_id": output_artifact["run_id"],
        "stage_scope": stage_scope,
        "gt_source": "derived_from_candidate_bank",
        "ordered_actions": False,
        "context_action_ids": sorted(context_action_ids),
        "final_state": {
            "action_ids": sorted(final_state_action_ids),
            **final_state_analysis,
        },
        "add": add_result,
        "remove": remove_result,
        "summary": summary,
        "efficiency": {
            "time_spent_seconds": output_artifact["time_spent_seconds"],
            "token_usage": output_artifact["token_usage"],
            "api_call_count": None if metadata is None else metadata.get("api_call_count"),
            "tool_call_count": None if metadata is None else metadata.get("tool_call_count"),
            "cost_usd": None if metadata is None else metadata.get("cost_usd"),
        },
    }


def evaluate_many(
    testcase_path: Path,
    input_paths: list[Path],
    stage_scope: str,
    success_threshold: float,
) -> dict[str, Any]:
    runs = [
        evaluate(
            testcase_path=testcase_path,
            input_path=input_path.resolve(),
            stage_scope=stage_scope,
            success_threshold=success_threshold,
        )
        for input_path in input_paths
    ]
    if not runs:
        raise SystemExit("at least one input file is required")

    first = runs[0]
    if any(
        run["competition_slug"] != first["competition_slug"] or run["testcase_id"] != first["testcase_id"]
        for run in runs
    ):
        raise SystemExit("all inputs must belong to the same competition_slug and testcase_id")
    if any(run["agent_name"] != first["agent_name"] for run in runs):
        raise SystemExit("pass@k aggregation requires all inputs to come from the same agent_name")

    success_flags = [run["summary"]["task_success"] for run in runs]
    task_completion_scores = [run["summary"]["task_completion_score"] for run in runs]
    strict_task_completion_scores = [run["summary"]["strict_task_completion_score"] for run in runs]
    add_f1_scores = [run["add"]["add_f1"] for run in runs]
    remove_f1_scores = [run["remove"]["remove_f1"] for run in runs]
    remove_recalls = [run["remove"]["remove_recall"] for run in runs]

    aggregate = {
        "k": len(runs),
        "pass_at_k": any(success_flags),
        "success_count": sum(1 for flag in success_flags if flag),
        "run_success_rate": round_metric(sum(1 for flag in success_flags if flag) / len(runs)),
        "task_completion_score_mean": round_metric(sum(task_completion_scores) / len(task_completion_scores)),
        "task_completion_score_variance": variance(task_completion_scores),
        "strict_task_completion_score_mean": round_metric(
            sum(strict_task_completion_scores) / len(strict_task_completion_scores)
        ),
        "add_f1_mean": round_metric(sum(add_f1_scores) / len(add_f1_scores)),
        "remove_f1_mean": round_metric(sum(remove_f1_scores) / len(remove_f1_scores)),
        "rollback_accuracy_mean": round_metric(sum(remove_recalls) / len(remove_recalls)),
        "mean_time_spent_seconds": mean_nullable([run["efficiency"]["time_spent_seconds"] for run in runs]),
        "mean_total_tokens": mean_nullable([run["efficiency"]["token_usage"]["total_tokens"] for run in runs]),
        "mean_api_call_count": mean_nullable([run["efficiency"]["api_call_count"] for run in runs]),
        "mean_tool_call_count": mean_nullable([run["efficiency"]["tool_call_count"] for run in runs]),
        "mean_cost_usd": mean_nullable([run["efficiency"]["cost_usd"] for run in runs]),
        "success_threshold": round_metric(success_threshold),
    }

    return {
        "competition_slug": first["competition_slug"],
        "testcase_id": first["testcase_id"],
        "agent_name": first["agent_name"],
        "stage_scope": stage_scope,
        "runs": runs,
        "aggregate": aggregate,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--testcase", required=True, type=Path, help="Path to the testcase JSON artifact")
    parser.add_argument("--input", required=True, nargs="+", type=Path, help="Path(s) to output artifact JSON files")
    parser.add_argument("--stage-scope", choices=("primary", "all"), default="primary")
    parser.add_argument("--success-threshold", type=float, default=0.5)
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if len(args.input) == 1:
        result = evaluate(
            testcase_path=args.testcase.resolve(),
            input_path=args.input[0].resolve(),
            stage_scope=args.stage_scope,
            success_threshold=args.success_threshold,
        )
    else:
        result = evaluate_many(
            testcase_path=args.testcase.resolve(),
            input_paths=[path.resolve() for path in args.input],
            stage_scope=args.stage_scope,
            success_threshold=args.success_threshold,
        )

    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, sort_keys=bool(indent)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
