from __future__ import annotations

from itertools import product
from pathlib import Path
from typing import Any, Callable


def build_run_plan(
    *,
    agent_names: list[str],
    testcase_ids: list[str],
    run_ids: list[str],
) -> list[dict[str, str]]:
    return [
        {
            "agent_name": agent_name,
            "testcase_id": testcase_id,
            "run_id": run_id,
        }
        for agent_name, testcase_id, run_id in product(agent_names, testcase_ids, run_ids)
    ]


def execute_run_plan(
    *,
    run_plan: list[dict[str, str]],
    runner_by_agent: dict[str, Callable[..., Any]],
    shared_kwargs: dict[str, Any],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for item in run_plan:
        runner = runner_by_agent[item["agent_name"]]
        result = runner(
            testcase_id=item["testcase_id"],
            run_id=item["run_id"],
            **shared_kwargs,
        )
        results.append({**item, "result": result})
    return results
