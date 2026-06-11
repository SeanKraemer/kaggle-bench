#!/usr/bin/env python3
"""Aggregate action-bank benchmark results across one or more tasks."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = REPO_ROOT / "data" / "tasks"
EVAL_PATH = REPO_ROOT / "eval" / "eval.py"


def load_eval_module():
    spec = importlib.util.spec_from_file_location("eval_module", EVAL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load eval module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TASK_EVAL = load_eval_module()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def discover_task_dirs(task_filters: list[str]) -> list[Path]:
    selected = set(task_filters)
    task_dirs: list[Path] = []

    for candidate in sorted(TASKS_DIR.iterdir()):
        if not candidate.is_dir():
            continue
        if selected and candidate.name not in selected:
            continue
        if not (candidate / "task.json").exists():
            continue
        task_dirs.append(candidate)

    missing = sorted(selected - {task_dir.name for task_dir in task_dirs})
    if missing:
        raise SystemExit(f"no evaluable task.json found for: {', '.join(missing)}")

    return task_dirs


def discover_output_groups(task_dir: Path) -> dict[tuple[str, str], list[Path]]:
    groups: dict[tuple[str, str], list[Path]] = defaultdict(list)

    for directory_name in ("outputs", "adapted_outputs", "human_baseline"):
        artifact_dir = task_dir / directory_name
        if not artifact_dir.exists():
            continue
        for path in sorted(artifact_dir.glob("*.json")):
            artifact = load_json(path)
            key = (artifact["testcase_id"], artifact["agent_name"])
            groups[key].append(path)

    return groups


def load_task_profile(task_dir: Path) -> dict[str, Any]:
    task = load_json(task_dir / "task.json")
    characteristics = task.get("task_characteristics", {})
    metric = task.get("metric", {})
    return {
        "task_slug": task_dir.name,
        "metric_name": metric.get("name"),
        "ml_domain": characteristics.get("ml_domain"),
        "problem_type": characteristics.get("problem_type"),
        "table_structure": characteristics.get("table_structure"),
        "dataset_size_bucket": characteristics.get("dataset_size_bucket"),
        "dataset_size_raw": characteristics.get("dataset_size_raw"),
        "feature_dimensionality_bucket": characteristics.get("feature_dimensionality_bucket"),
        "feature_dimensionality_raw": characteristics.get("feature_dimensionality_raw"),
        "preprocessing_complexity_bucket": characteristics.get("preprocessing_complexity_bucket"),
        "preprocessing_complexity_raw": characteristics.get("preprocessing_complexity_raw"),
    }


def evaluate_group(
    testcase_path: Path,
    input_paths: list[Path],
    stage_scope: str,
    success_threshold: float,
) -> dict[str, Any]:
    resolved_paths = [path.resolve() for path in input_paths]
    if len(resolved_paths) == 1:
        return TASK_EVAL.evaluate(
            testcase_path=testcase_path.resolve(),
            input_path=resolved_paths[0],
            stage_scope=stage_scope,
            success_threshold=success_threshold,
        )
    return TASK_EVAL.evaluate_many(
        testcase_path=testcase_path.resolve(),
        input_paths=resolved_paths,
        stage_scope=stage_scope,
        success_threshold=success_threshold,
    )


def mean(values: list[float]) -> float:
    return TASK_EVAL.round_metric(sum(values) / len(values))


def mean_nullable(values: list[int | float | None]) -> float | None:
    return TASK_EVAL.mean_nullable(values)


def summarize_run(run: dict[str, Any], task_slug: str) -> dict[str, Any]:
    return {
        "task_slug": task_slug,
        "testcase_id": run["testcase_id"],
        "agent_name": run["agent_name"],
        "run_id": run["run_id"],
        "add_precision": run["add"]["add_precision"],
        "add_recall": run["add"]["add_recall"],
        "add_f1": run["add"]["add_f1"],
        "remove_precision": run["remove"]["remove_precision"],
        "remove_recall": run["remove"]["remove_recall"],
        "remove_f1": run["remove"]["remove_f1"],
        "rollback_accuracy": run["remove"]["rollback_accuracy"],
        "task_completion_score": run["summary"]["task_completion_score"],
        "strict_task_completion_score": run["summary"]["strict_task_completion_score"],
        "task_success": run["summary"]["task_success"],
        "time_spent_seconds": run["efficiency"]["time_spent_seconds"],
        "total_tokens": run["efficiency"]["token_usage"]["total_tokens"],
        "api_call_count": run["efficiency"]["api_call_count"],
        "tool_call_count": run["efficiency"]["tool_call_count"],
        "cost_usd": run["efficiency"]["cost_usd"],
    }


def summarize_group_result(result: dict[str, Any], task_slug: str) -> dict[str, Any]:
    if "runs" not in result:
        single = summarize_run(result, task_slug)
        return {
            "task_slug": task_slug,
            "testcase_id": single["testcase_id"],
            "agent_name": single["agent_name"],
            "k": 1,
            "pass_at_k": single["task_success"],
            "run_success_rate": 1.0 if single["task_success"] else 0.0,
            "add_precision": single["add_precision"],
            "add_recall": single["add_recall"],
            "add_f1": single["add_f1"],
            "remove_precision": single["remove_precision"],
            "remove_recall": single["remove_recall"],
            "remove_f1": single["remove_f1"],
            "rollback_accuracy": single["rollback_accuracy"],
            "task_completion_score": single["task_completion_score"],
            "strict_task_completion_score": single["strict_task_completion_score"],
            "task_completion_variance": 0.0,
            "time_spent_seconds": single["time_spent_seconds"],
            "total_tokens": single["total_tokens"],
            "api_call_count": single["api_call_count"],
            "tool_call_count": single["tool_call_count"],
            "cost_usd": single["cost_usd"],
        }

    runs = [summarize_run(run, task_slug) for run in result["runs"]]
    aggregate = result["aggregate"]
    return {
        "task_slug": task_slug,
        "testcase_id": result["testcase_id"],
        "agent_name": result["agent_name"],
        "k": aggregate["k"],
        "pass_at_k": aggregate["pass_at_k"],
        "run_success_rate": aggregate["run_success_rate"],
        "add_precision": mean([run["add_precision"] for run in runs]),
        "add_recall": mean([run["add_recall"] for run in runs]),
        "add_f1": aggregate["add_f1_mean"],
        "remove_precision": mean([run["remove_precision"] for run in runs]),
        "remove_recall": mean([run["remove_recall"] for run in runs]),
        "remove_f1": aggregate["remove_f1_mean"],
        "rollback_accuracy": aggregate["rollback_accuracy_mean"],
        "task_completion_score": aggregate["task_completion_score_mean"],
        "strict_task_completion_score": aggregate["strict_task_completion_score_mean"],
        "task_completion_variance": aggregate["task_completion_score_variance"],
        "time_spent_seconds": aggregate["mean_time_spent_seconds"],
        "total_tokens": aggregate["mean_total_tokens"],
        "api_call_count": aggregate["mean_api_call_count"],
        "tool_call_count": aggregate["mean_tool_call_count"],
        "cost_usd": aggregate["mean_cost_usd"],
    }


def build_agent_summary(group_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_agent: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in group_rows:
        by_agent[row["agent_name"]].append(row)

    summaries: list[dict[str, Any]] = []
    for agent_name, rows in sorted(by_agent.items()):
        summaries.append(
            {
                "agent_name": agent_name,
                "group_count": len(rows),
                "task_success_rate": TASK_EVAL.round_metric(sum(1 for row in rows if row["pass_at_k"]) / len(rows)),
                "mean_k": mean([float(row["k"]) for row in rows]),
                "mean_run_success_rate": mean([row["run_success_rate"] for row in rows]),
                "mean_add_precision": mean([row["add_precision"] for row in rows]),
                "mean_add_recall": mean([row["add_recall"] for row in rows]),
                "mean_add_f1": mean([row["add_f1"] for row in rows]),
                "mean_remove_precision": mean([row["remove_precision"] for row in rows]),
                "mean_remove_recall": mean([row["remove_recall"] for row in rows]),
                "mean_remove_f1": mean([row["remove_f1"] for row in rows]),
                "mean_rollback_accuracy": mean([row["rollback_accuracy"] for row in rows]),
                "mean_task_completion_score": mean([row["task_completion_score"] for row in rows]),
                "mean_strict_task_completion_score": mean([row["strict_task_completion_score"] for row in rows]),
                "mean_task_completion_variance": mean([row["task_completion_variance"] for row in rows]),
                "mean_time_spent_seconds": mean_nullable([row["time_spent_seconds"] for row in rows]),
                "mean_total_tokens": mean_nullable([row["total_tokens"] for row in rows]),
                "mean_api_call_count": mean_nullable([row["api_call_count"] for row in rows]),
                "mean_tool_call_count": mean_nullable([row["tool_call_count"] for row in rows]),
                "mean_cost_usd": mean_nullable([row["cost_usd"] for row in rows]),
            }
        )
    return summaries


def build_task_summary(
    task_profiles: dict[str, dict[str, Any]], group_rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    by_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in group_rows:
        by_task[row["task_slug"]].append(row)

    summaries: list[dict[str, Any]] = []
    for task_slug, rows in sorted(by_task.items()):
        profile = task_profiles[task_slug]
        summaries.append(
            {
                **profile,
                "group_count": len(rows),
                "agent_count": len({row["agent_name"] for row in rows}),
                "task_success_rate": TASK_EVAL.round_metric(sum(1 for row in rows if row["pass_at_k"]) / len(rows)),
                "mean_k": mean([float(row["k"]) for row in rows]),
                "mean_run_success_rate": mean([row["run_success_rate"] for row in rows]),
                "mean_add_precision": mean([row["add_precision"] for row in rows]),
                "mean_add_recall": mean([row["add_recall"] for row in rows]),
                "mean_add_f1": mean([row["add_f1"] for row in rows]),
                "mean_remove_precision": mean([row["remove_precision"] for row in rows]),
                "mean_remove_recall": mean([row["remove_recall"] for row in rows]),
                "mean_remove_f1": mean([row["remove_f1"] for row in rows]),
                "mean_rollback_accuracy": mean([row["rollback_accuracy"] for row in rows]),
                "mean_task_completion_score": mean([row["task_completion_score"] for row in rows]),
                "mean_strict_task_completion_score": mean([row["strict_task_completion_score"] for row in rows]),
                "mean_task_completion_variance": mean([row["task_completion_variance"] for row in rows]),
                "mean_time_spent_seconds": mean_nullable([row["time_spent_seconds"] for row in rows]),
                "mean_total_tokens": mean_nullable([row["total_tokens"] for row in rows]),
                "mean_api_call_count": mean_nullable([row["api_call_count"] for row in rows]),
                "mean_tool_call_count": mean_nullable([row["tool_call_count"] for row in rows]),
                "mean_cost_usd": mean_nullable([row["cost_usd"] for row in rows]),
            }
        )
    return summaries


def build_overall_summary(group_rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not group_rows:
        return {
            "group_count": 0,
            "agent_count": 0,
            "task_count": 0,
            "task_success_rate": None,
            "mean_k": None,
            "mean_run_success_rate": None,
            "mean_add_precision": None,
            "mean_add_recall": None,
            "mean_add_f1": None,
            "mean_remove_precision": None,
            "mean_remove_recall": None,
            "mean_remove_f1": None,
            "mean_rollback_accuracy": None,
            "mean_task_completion_score": None,
            "mean_strict_task_completion_score": None,
            "mean_task_completion_variance": None,
            "mean_time_spent_seconds": None,
            "mean_total_tokens": None,
            "mean_api_call_count": None,
            "mean_tool_call_count": None,
            "mean_cost_usd": None,
        }

    return {
        "group_count": len(group_rows),
        "agent_count": len({row["agent_name"] for row in group_rows}),
        "task_count": len({row["task_slug"] for row in group_rows}),
        "task_success_rate": TASK_EVAL.round_metric(sum(1 for row in group_rows if row["pass_at_k"]) / len(group_rows)),
        "mean_k": mean([float(row["k"]) for row in group_rows]),
        "mean_run_success_rate": mean([row["run_success_rate"] for row in group_rows]),
        "mean_add_precision": mean([row["add_precision"] for row in group_rows]),
        "mean_add_recall": mean([row["add_recall"] for row in group_rows]),
        "mean_add_f1": mean([row["add_f1"] for row in group_rows]),
        "mean_remove_precision": mean([row["remove_precision"] for row in group_rows]),
        "mean_remove_recall": mean([row["remove_recall"] for row in group_rows]),
        "mean_remove_f1": mean([row["remove_f1"] for row in group_rows]),
        "mean_rollback_accuracy": mean([row["rollback_accuracy"] for row in group_rows]),
        "mean_task_completion_score": mean([row["task_completion_score"] for row in group_rows]),
        "mean_strict_task_completion_score": mean([row["strict_task_completion_score"] for row in group_rows]),
        "mean_task_completion_variance": mean([row["task_completion_variance"] for row in group_rows]),
        "mean_time_spent_seconds": mean_nullable([row["time_spent_seconds"] for row in group_rows]),
        "mean_total_tokens": mean_nullable([row["total_tokens"] for row in group_rows]),
        "mean_api_call_count": mean_nullable([row["api_call_count"] for row in group_rows]),
        "mean_tool_call_count": mean_nullable([row["tool_call_count"] for row in group_rows]),
        "mean_cost_usd": mean_nullable([row["cost_usd"] for row in group_rows]),
    }


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    header_row = "| " + " | ".join(headers) + " |"
    divider_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_rows = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_row, divider_row, *body_rows])


def format_number(value: float | int | None) -> str:
    if value is None:
        return "`null`"
    if isinstance(value, int):
        return str(value)
    return f"{value:.6f}"


def format_bucket(bucket: str | None, raw: int | float | None) -> str:
    bucket_label = bucket or "unknown"
    if raw is None:
        return bucket_label
    return f"{bucket_label} ({raw})"


def build_generation_command(report: dict[str, Any]) -> str:
    parts = ["uv", "run", "python", "eval/aggregate.py"]
    for task in report["tasks"]:
        parts.extend(["--task", task])
    parts.extend(["--stage-scope", report["stage_scope"]])
    parts.extend(["--format", report["format"]])
    parts.extend(["--success-threshold", str(report["success_threshold"])])
    if report.get("output_path"):
        parts.extend(["--output", report["output_path"]])
    return " ".join(parts)


def format_markdown(report: dict[str, Any]) -> str:
    overall = report["overall_summary"]
    lines = [
        "# Benchmark Aggregate Report",
        "",
        "## Configuration",
        "",
        f"- Stage scope: `{report['stage_scope']}`",
        f"- Success threshold: `{report['success_threshold']}`",
        f"- Tasks included: {', '.join(f'`{task}`' for task in report['tasks'])}",
        f"- Evaluated run artifacts: `{report['single_run_count']}`",
        f"- Evaluated grouped agent/testcase units: `{report['group_count']}`",
        "",
        "## Benchmark Overview",
        "",
        f"- Task Success Rate: `{format_number(overall['task_success_rate'])}`",
        f"- Mean Add Precision: `{format_number(overall['mean_add_precision'])}`",
        f"- Mean Add Recall: `{format_number(overall['mean_add_recall'])}`",
        f"- Mean Add F1: `{format_number(overall['mean_add_f1'])}`",
        f"- Mean Remove Precision: `{format_number(overall['mean_remove_precision'])}`",
        f"- Mean Remove Recall: `{format_number(overall['mean_remove_recall'])}`",
        f"- Mean Remove F1: `{format_number(overall['mean_remove_f1'])}`",
        f"- Mean Task Completion Score: `{format_number(overall['mean_task_completion_score'])}`",
        f"- Mean Strict Task Completion Score: `{format_number(overall['mean_strict_task_completion_score'])}`",
        f"- Mean Task Completion Variance: `{format_number(overall['mean_task_completion_variance'])}`",
        f"- Mean Runtime (s): `{format_number(overall['mean_time_spent_seconds'])}`",
        f"- Mean Total Tokens: `{format_number(overall['mean_total_tokens'])}`",
        f"- Mean API Calls: `{format_number(overall['mean_api_call_count'])}`",
        f"- Mean Tool Calls: `{format_number(overall['mean_tool_call_count'])}`",
        f"- Mean Cost (USD): `{format_number(overall['mean_cost_usd'])}`",
        "",
        "## Task Characteristics",
        "",
        markdown_table(
            [
                "Task",
                "Metric",
                "Domain",
                "Problem",
                "Table Structure",
                "Dataset Size",
                "Feature Dimensionality",
                "Preprocessing Complexity",
            ],
            [
                [
                    row["task_slug"],
                    row["metric_name"] or "`null`",
                    row["ml_domain"] or "`null`",
                    row["problem_type"] or "`null`",
                    row["table_structure"] or "`null`",
                    format_bucket(row["dataset_size_bucket"], row["dataset_size_raw"]),
                    format_bucket(row["feature_dimensionality_bucket"], row["feature_dimensionality_raw"]),
                    format_bucket(row["preprocessing_complexity_bucket"], row["preprocessing_complexity_raw"]),
                ]
                for row in report["task_summary"]
            ],
        ),
        "",
        "## Task Summary",
        "",
        markdown_table(
            [
                "Task",
                "Groups",
                "Agents",
                "Task Success Rate",
                "Mean k",
                "Mean Add P",
                "Mean Add R",
                "Mean Add F1",
                "Mean Remove P",
                "Mean Remove R",
                "Mean Remove F1",
                "Mean Task Completion",
                "Mean Strict Completion",
                "Mean Variance",
                "Mean Time (s)",
                "Mean Tokens",
                "Mean API Calls",
                "Mean Tool Calls",
                "Mean Cost (USD)",
            ],
            [
                [
                    row["task_slug"],
                    str(row["group_count"]),
                    str(row["agent_count"]),
                    format_number(row["task_success_rate"]),
                    format_number(row["mean_k"]),
                    format_number(row["mean_add_precision"]),
                    format_number(row["mean_add_recall"]),
                    format_number(row["mean_add_f1"]),
                    format_number(row["mean_remove_precision"]),
                    format_number(row["mean_remove_recall"]),
                    format_number(row["mean_remove_f1"]),
                    format_number(row["mean_task_completion_score"]),
                    format_number(row["mean_strict_task_completion_score"]),
                    format_number(row["mean_task_completion_variance"]),
                    format_number(row["mean_time_spent_seconds"]),
                    format_number(row["mean_total_tokens"]),
                    format_number(row["mean_api_call_count"]),
                    format_number(row["mean_tool_call_count"]),
                    format_number(row["mean_cost_usd"]),
                ]
                for row in report["task_summary"]
            ],
        ),
        "",
        "## Single-Run Artifacts",
        "",
        markdown_table(
            [
                "Task",
                "Testcase",
                "Agent",
                "Run",
                "Add P",
                "Add R",
                "Add F1",
                "Remove P",
                "Remove R",
                "Remove F1",
                "Task Completion",
                "Strict Completion",
                "Success",
                "Time (s)",
                "Tokens",
                "API Calls",
                "Tool Calls",
                "Cost (USD)",
            ],
            [
                [
                    row["task_slug"],
                    row["testcase_id"],
                    row["agent_name"],
                    row["run_id"],
                    format_number(row["add_precision"]),
                    format_number(row["add_recall"]),
                    format_number(row["add_f1"]),
                    format_number(row["remove_precision"]),
                    format_number(row["remove_recall"]),
                    format_number(row["remove_f1"]),
                    format_number(row["task_completion_score"]),
                    format_number(row["strict_task_completion_score"]),
                    "`true`" if row["task_success"] else "`false`",
                    format_number(row["time_spent_seconds"]),
                    format_number(row["total_tokens"]),
                    format_number(row["api_call_count"]),
                    format_number(row["tool_call_count"]),
                    format_number(row["cost_usd"]),
                ]
                for row in report["single_runs"]
            ],
        ),
        "",
        "## Grouped Agent/Testcase Results",
        "",
        markdown_table(
            [
                "Task",
                "Testcase",
                "Agent",
                "k",
                "Pass@k",
                "Run Success Rate",
                "Mean Add P",
                "Mean Add R",
                "Mean Add F1",
                "Mean Remove P",
                "Mean Remove R",
                "Mean Remove F1",
                "Mean Task Completion",
                "Mean Strict Completion",
                "Mean Variance",
                "Mean Time (s)",
                "Mean Tokens",
                "Mean API Calls",
                "Mean Tool Calls",
                "Mean Cost (USD)",
            ],
            [
                [
                    row["task_slug"],
                    row["testcase_id"],
                    row["agent_name"],
                    str(row["k"]),
                    "`true`" if row["pass_at_k"] else "`false`",
                    format_number(row["run_success_rate"]),
                    format_number(row["add_precision"]),
                    format_number(row["add_recall"]),
                    format_number(row["add_f1"]),
                    format_number(row["remove_precision"]),
                    format_number(row["remove_recall"]),
                    format_number(row["remove_f1"]),
                    format_number(row["task_completion_score"]),
                    format_number(row["strict_task_completion_score"]),
                    format_number(row["task_completion_variance"]),
                    format_number(row["time_spent_seconds"]),
                    format_number(row["total_tokens"]),
                    format_number(row["api_call_count"]),
                    format_number(row["tool_call_count"]),
                    format_number(row["cost_usd"]),
                ]
                for row in report["groups"]
            ],
        ),
        "",
        "## Agent Summary",
        "",
        markdown_table(
            [
                "Agent",
                "Groups",
                "Task Success Rate",
                "Mean k",
                "Mean Run Success Rate",
                "Mean Add P",
                "Mean Add R",
                "Mean Add F1",
                "Mean Remove P",
                "Mean Remove R",
                "Mean Remove F1",
                "Mean Task Completion",
                "Mean Strict Completion",
                "Mean Variance",
                "Mean Time (s)",
                "Mean Tokens",
                "Mean API Calls",
                "Mean Tool Calls",
                "Mean Cost (USD)",
            ],
            [
                [
                    row["agent_name"],
                    str(row["group_count"]),
                    format_number(row["task_success_rate"]),
                    format_number(row["mean_k"]),
                    format_number(row["mean_run_success_rate"]),
                    format_number(row["mean_add_precision"]),
                    format_number(row["mean_add_recall"]),
                    format_number(row["mean_add_f1"]),
                    format_number(row["mean_remove_precision"]),
                    format_number(row["mean_remove_recall"]),
                    format_number(row["mean_remove_f1"]),
                    format_number(row["mean_task_completion_score"]),
                    format_number(row["mean_strict_task_completion_score"]),
                    format_number(row["mean_task_completion_variance"]),
                    format_number(row["mean_time_spent_seconds"]),
                    format_number(row["mean_total_tokens"]),
                    format_number(row["mean_api_call_count"]),
                    format_number(row["mean_tool_call_count"]),
                    format_number(row["mean_cost_usd"]),
                ]
                for row in report["agent_summary"]
            ],
        ),
        "",
        "## Reproducible Commands",
        "",
        "```bash",
        "uv run python eval/scripts/validate_artifacts.py",
        "uv run python -m unittest discover -s eval/tests -p 'test_*.py'",
        build_generation_command(report),
        "```",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate benchmark results across one or more tasks.")
    parser.add_argument(
        "--task",
        action="append",
        default=[],
        help="Task slug to include. Repeat to include multiple tasks. If omitted, all evaluable new tasks are included.",
    )
    parser.add_argument(
        "--stage-scope",
        choices=("all", "primary"),
        default="primary",
        help="Scoring scope passed through to eval/eval.py logic.",
    )
    parser.add_argument(
        "--success-threshold",
        type=float,
        default=0.5,
        help="Threshold for binary task_success and Pass@k.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the rendered report.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    task_dirs = discover_task_dirs(args.task)
    task_profiles = {task_dir.name: load_task_profile(task_dir) for task_dir in task_dirs}

    single_runs: list[dict[str, Any]] = []
    grouped_rows: list[dict[str, Any]] = []

    for task_dir in task_dirs:
        groups = discover_output_groups(task_dir)
        for (testcase_id, _agent_name), input_paths in sorted(groups.items()):
            testcase_path = task_dir / "testcases" / f"{testcase_id}.json"
            if not testcase_path.exists():
                raise SystemExit(f"missing testcase file for {task_dir.name}/{testcase_id}")

            group_result = evaluate_group(
                testcase_path=testcase_path,
                input_paths=input_paths,
                stage_scope=args.stage_scope,
                success_threshold=args.success_threshold,
            )

            if "runs" in group_result:
                for run in group_result["runs"]:
                    single_runs.append(summarize_run(run, task_dir.name))
            else:
                single_runs.append(summarize_run(group_result, task_dir.name))

            grouped_rows.append(summarize_group_result(group_result, task_dir.name))

    report = {
        "tasks": [task_dir.name for task_dir in task_dirs],
        "stage_scope": args.stage_scope,
        "success_threshold": TASK_EVAL.round_metric(args.success_threshold),
        "format": args.format,
        "output_path": None if args.output is None else str(args.output),
        "single_run_count": len(single_runs),
        "group_count": len(grouped_rows),
        "single_runs": sorted(
            single_runs, key=lambda row: (row["task_slug"], row["testcase_id"], row["agent_name"], row["run_id"])
        ),
        "groups": sorted(grouped_rows, key=lambda row: (row["task_slug"], row["testcase_id"], row["agent_name"])),
        "overall_summary": build_overall_summary(grouped_rows),
        "task_summary": build_task_summary(task_profiles, grouped_rows),
        "agent_summary": build_agent_summary(grouped_rows),
    }

    rendered = json.dumps(report, indent=2) if args.format == "json" else format_markdown(report)
    if args.output is not None:
        output_path = args.output.resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + ("" if rendered.endswith("\n") else "\n"), encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
