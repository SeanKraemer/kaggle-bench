from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLES_PATH = ROOT / "agent" / "build_paper_tables.py"


def load_tables_module():
    spec = importlib.util.spec_from_file_location("agent_build_paper_tables", TABLES_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load build_paper_tables module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PaperTablesTests(unittest.TestCase):
    def test_build_overall_table_rows_aggregates_agent_metrics(self) -> None:
        tables = load_tables_module()

        rows = tables.build_overall_table_rows(
            [
                {
                    "agent_name": "rule_based",
                    "k": 5,
                    "add_f1": 0.7,
                    "remove_recall": 0.8,
                    "task_completion_score": 0.75,
                    "pass_at_k": True,
                    "cost_usd": 0.0,
                },
                {
                    "agent_name": "rule_based",
                    "k": 5,
                    "add_f1": 0.9,
                    "remove_recall": 0.6,
                    "task_completion_score": 0.75,
                    "pass_at_k": True,
                    "cost_usd": 0.0,
                },
                {
                    "agent_name": "single_llm",
                    "k": 5,
                    "add_f1": 0.95,
                    "remove_recall": 0.9,
                    "task_completion_score": 0.925,
                    "pass_at_k": True,
                    "cost_usd": 0.01,
                },
            ]
        )

        self.assertEqual(rows[0]["agent_name"], "rule_based")
        self.assertAlmostEqual(rows[0]["add_f1"], 0.8, places=6)
        self.assertAlmostEqual(rows[1]["avg_cost_per_run"], 0.01, places=6)

    def test_build_scenario_breakdown_rows_pivots_by_testcase(self) -> None:
        tables = load_tables_module()

        rows = tables.build_scenario_breakdown_rows(
            [
                {"testcase_id": "tc1_from_scratch", "agent_name": "rule_based", "task_completion_score": 0.8},
                {"testcase_id": "tc1_from_scratch", "agent_name": "single_llm", "task_completion_score": 0.95},
                {"testcase_id": "tc2_partial_good", "agent_name": "rule_based", "task_completion_score": 0.7},
            ],
            agent_order=["rule_based", "single_llm"],
        )

        self.assertEqual(rows[0]["testcase_id"], "tc1_from_scratch")
        self.assertEqual(rows[0]["rule_based"], 0.8)
        self.assertEqual(rows[0]["single_llm"], 0.95)
