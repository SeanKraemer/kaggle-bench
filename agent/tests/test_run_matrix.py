from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_MATRIX_PATH = ROOT / "agent" / "run_matrix.py"


def load_run_matrix_module():
    spec = importlib.util.spec_from_file_location("agent_run_matrix", RUN_MATRIX_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load run_matrix module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RunMatrixTests(unittest.TestCase):
    def test_build_run_plan_expands_agents_testcases_and_tries(self) -> None:
        run_matrix = load_run_matrix_module()

        plan = run_matrix.build_run_plan(
            agent_names=["rule_based", "single_llm"],
            testcase_ids=["tc1_from_scratch", "tc2_partial_good"],
            run_ids=["try1", "try2"],
        )

        self.assertEqual(len(plan), 8)
        self.assertEqual(plan[0]["agent_name"], "rule_based")
        self.assertEqual(plan[-1]["run_id"], "try2")

    def test_execute_run_plan_dispatches_to_matching_runner(self) -> None:
        run_matrix = load_run_matrix_module()
        calls = []

        def fake_runner(**kwargs):
            calls.append(kwargs)
            return {"status": "ok"}

        results = run_matrix.execute_run_plan(
            run_plan=[
                {"agent_name": "rule_based", "testcase_id": "tc1_from_scratch", "run_id": "try1"},
                {"agent_name": "single_llm", "testcase_id": "tc1_from_scratch", "run_id": "try1"},
            ],
            runner_by_agent={
                "rule_based": fake_runner,
                "single_llm": fake_runner,
            },
            shared_kwargs={"task_dir": Path("/tmp/task"), "data_root": Path("/tmp/data")},
        )

        self.assertEqual(len(calls), 2)
        self.assertEqual(results[0]["agent_name"], "rule_based")
        self.assertEqual(results[1]["result"]["status"], "ok")
