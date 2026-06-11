from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AGGREGATE_PATH = ROOT / "eval" / "aggregate.py"


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def build_overall_table_rows(group_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in group_rows:
        grouped[row["agent_name"]].append(row)

    overall_rows = []
    for agent_name, rows in sorted(grouped.items()):
        overall_rows.append(
            {
                "agent_name": agent_name,
                "runs": max(int(row.get("k", 1)) for row in rows),
                "add_f1": mean([row["add_f1"] for row in rows]),
                "remove_recall": mean([row["remove_recall"] for row in rows]),
                "task_completion": mean([row["task_completion_score"] for row in rows]),
                "success_rate": mean([1.0 if row.get("pass_at_k") else 0.0 for row in rows]),
                "avg_cost_per_run": mean([float(row.get("cost_usd") or 0.0) for row in rows]),
            }
        )
    return overall_rows


def build_scenario_breakdown_rows(
    group_rows: list[dict[str, Any]],
    *,
    agent_order: list[str],
) -> list[dict[str, Any]]:
    by_testcase: dict[str, dict[str, Any]] = {}
    for row in group_rows:
        testcase_id = row["testcase_id"]
        if testcase_id not in by_testcase:
            by_testcase[testcase_id] = {"testcase_id": testcase_id}
        by_testcase[testcase_id][row["agent_name"]] = row["task_completion_score"]

    rows = []
    for testcase_id in sorted(by_testcase):
        row = by_testcase[testcase_id]
        for agent_name in agent_order:
            row.setdefault(agent_name, None)
        rows.append(row)
    return rows


def load_aggregate_module():
    spec = importlib.util.spec_from_file_location("aggregate_module", AGGREGATE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load aggregate module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def collect_group_rows(*, task_slug: str, stage_scope: str, success_threshold: float) -> list[dict[str, Any]]:
    aggregate = load_aggregate_module()
    task_dir = aggregate.TASKS_DIR / task_slug
    groups = aggregate.discover_output_groups(task_dir)
    rows = []
    for (testcase_id, _agent_name), paths in sorted(groups.items()):
        result = aggregate.evaluate_group(
            testcase_path=(task_dir / "testcases" / f"{testcase_id}.json"),
            input_paths=paths,
            stage_scope=stage_scope,
            success_threshold=success_threshold,
        )
        rows.append(aggregate.summarize_group_result(result, task_slug))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Build paper-friendly Zillow result tables.")
    parser.add_argument("--task", default="zillow-prize-1")
    parser.add_argument("--stage-scope", default="primary")
    parser.add_argument("--success-threshold", type=float, default=0.5)
    parser.add_argument("--json-output", type=Path, default=None)
    args = parser.parse_args()

    group_rows = collect_group_rows(
        task_slug=args.task,
        stage_scope=args.stage_scope,
        success_threshold=args.success_threshold,
    )
    agent_order = sorted({row["agent_name"] for row in group_rows})
    payload = {
        "overall_rows": build_overall_table_rows(group_rows),
        "scenario_rows": build_scenario_breakdown_rows(group_rows, agent_order=agent_order),
    }
    if args.json_output is not None:
        args.json_output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
