from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
AGGREGATE_PATH = ROOT / "eval" / "aggregate.py"


def load_aggregate_module():
    spec = importlib.util.spec_from_file_location("aggregate_module", AGGREGATE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load new aggregate module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AGGREGATE = load_aggregate_module()


def write_json(path: Path, payload: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def task_output(
    path: Path,
    *,
    competition_slug: str,
    testcase_id: str,
    agent_name: str,
    run_id: str,
    predicted_add_action_ids: list[str],
    predicted_remove_action_ids: list[str],
) -> Path:
    return write_json(
        path,
        {
            "competition_slug": competition_slug,
            "testcase_id": testcase_id,
            "agent_name": agent_name,
            "run_by": "test",
            "run_id": run_id,
            "artifact_refs": [],
            "predicted_add_action_ids": predicted_add_action_ids,
            "predicted_remove_action_ids": predicted_remove_action_ids,
            "time_spent_seconds": 1,
            "token_usage": {
                "input_tokens": None,
                "output_tokens": None,
                "total_tokens": None,
            },
            "notes": "aggregate test artifact",
        },
    )


def build_temp_task(task_dir: Path) -> None:
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "tiny-task",
            "dataset": {
                "provider": "kaggle",
                "competition": "tiny-task",
                "train_files": ["train.csv"],
                "test_files": [],
                "lookup_files": [],
                "sample_submission_files": [],
                "data_dictionary_files": [],
                "target_column": "target",
                "primary_key": "id",
            },
            "goal": "test task",
            "metric": {"name": "TinyMetric"},
            "task_characteristics": {
                "ml_domain": "tabular",
                "problem_type": "classification",
                "table_structure": "single_table",
                "dataset_size_bucket": "small",
                "dataset_size_raw": 100,
                "feature_dimensionality_bucket": "low",
                "feature_dimensionality_raw": 10,
                "preprocessing_complexity_bucket": "low",
                "preprocessing_complexity_raw": 2,
                "analysis_notes": "test",
            },
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "tiny-task",
            "generated_at": "2026-03-30",
            "actions": [
                {
                    "action_id": "CA-000001",
                    "action_type": "PARSE_DATETIME",
                    "canonical_params": {"columns": ["transactiondate"]},
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "observed_notebook",
                    "notebook_refs": ["nb"],
                    "source_profile": "winner_style",
                    "context_notes": "test",
                    "evidence_snippets": ["test"],
                    "rareness": "common",
                    "confidence": 1.0,
                }
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1.json",
        {
            "testcase_id": "tc1",
            "competition_slug": "tiny-task",
            "task_ref": "../task.json",
            "input": {
                "scenario": "from_scratch",
                "context_action_ids": [],
            },
        },
    )


class AggregateTests(unittest.TestCase):
    def test_discover_task_dirs_filters_to_evaluable_tasks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tasks_dir = Path(tmp)
            (tasks_dir / "alpha").mkdir()
            (tasks_dir / "beta").mkdir()
            write_json(tasks_dir / "alpha" / "task.json", {"competition_slug": "alpha"})

            with mock.patch.object(AGGREGATE, "TASKS_DIR", tasks_dir):
                discovered = AGGREGATE.discover_task_dirs([])

        self.assertEqual([path.name for path in discovered], ["alpha"])

    def test_discover_task_dirs_raises_for_missing_requested_task(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tasks_dir = Path(tmp)
            (tasks_dir / "alpha").mkdir()
            write_json(tasks_dir / "alpha" / "task.json", {"competition_slug": "alpha"})

            with mock.patch.object(AGGREGATE, "TASKS_DIR", tasks_dir):
                with self.assertRaises(SystemExit) as ctx:
                    AGGREGATE.discover_task_dirs(["missing-task"])

        self.assertIn("missing-task", str(ctx.exception))

    def test_discover_output_groups_includes_outputs_adapted_and_human_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = Path(tmp) / "tiny-task"
            build_temp_task(task_dir)
            task_output(
                task_dir / "outputs" / "tc1_agent_try1.json",
                competition_slug="tiny-task",
                testcase_id="tc1",
                agent_name="agent",
                run_id="try1",
                predicted_add_action_ids=[],
                predicted_remove_action_ids=[],
            )
            task_output(
                task_dir / "adapted_outputs" / "tc1_agent_try2.json",
                competition_slug="tiny-task",
                testcase_id="tc1",
                agent_name="agent",
                run_id="try2",
                predicted_add_action_ids=["CA-000001"],
                predicted_remove_action_ids=[],
            )
            task_output(
                task_dir / "human_baseline" / "tc1_human.json",
                competition_slug="tiny-task",
                testcase_id="tc1",
                agent_name="human",
                run_id="draft_human",
                predicted_add_action_ids=["CA-000001"],
                predicted_remove_action_ids=[],
            )

            groups = AGGREGATE.discover_output_groups(task_dir)

        self.assertEqual(sorted(groups), [("tc1", "agent"), ("tc1", "human")])
        self.assertEqual(len(groups[("tc1", "agent")]), 2)
        self.assertEqual(len(groups[("tc1", "human")]), 1)

    def test_main_writes_json_report_with_pass_at_k_aggregate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tasks_dir = root / "data" / "tasks"
            task_dir = tasks_dir / "tiny-task"
            build_temp_task(task_dir)

            task_output(
                task_dir / "outputs" / "tc1_agent_try1.json",
                competition_slug="tiny-task",
                testcase_id="tc1",
                agent_name="agent",
                run_id="try1",
                predicted_add_action_ids=[],
                predicted_remove_action_ids=[],
            )
            task_output(
                task_dir / "outputs" / "tc1_agent_try2.json",
                competition_slug="tiny-task",
                testcase_id="tc1",
                agent_name="agent",
                run_id="try2",
                predicted_add_action_ids=["CA-000001"],
                predicted_remove_action_ids=[],
            )
            output_path = root / "aggregate.json"

            args = argparse.Namespace(
                task=["tiny-task"],
                stage_scope="primary",
                success_threshold=0.75,
                format="json",
                output=output_path,
            )

            with (
                mock.patch.object(AGGREGATE, "TASKS_DIR", tasks_dir),
                mock.patch.object(AGGREGATE, "parse_args", return_value=args),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                exit_code = AGGREGATE.main()

            report = json.loads(output_path.read_text(encoding="utf-8"))

        self.assertEqual(exit_code, 0)
        self.assertEqual(report["tasks"], ["tiny-task"])
        self.assertEqual(report["single_run_count"], 2)
        self.assertEqual(report["group_count"], 1)
        self.assertEqual(report["groups"][0]["k"], 2)
        self.assertTrue(report["groups"][0]["pass_at_k"])
        self.assertEqual(report["groups"][0]["run_success_rate"], 0.5)
        self.assertEqual(report["groups"][0]["add_precision"], 0.5)
        self.assertEqual(report["agent_summary"][0]["task_success_rate"], 1.0)
        self.assertEqual(report["agent_summary"][0]["mean_run_success_rate"], 0.5)

    def test_format_markdown_renders_expected_sections(self) -> None:
        markdown = AGGREGATE.format_markdown(
            {
                "tasks": ["tiny-task"],
                "stage_scope": "primary",
                "success_threshold": 0.5,
                "format": "markdown",
                "output_path": "eval/results/benchmarks/tiny-task-primary.md",
                "single_run_count": 1,
                "group_count": 1,
                "overall_summary": {
                    "group_count": 1,
                    "agent_count": 1,
                    "task_count": 1,
                    "task_success_rate": 1.0,
                    "mean_k": 1.0,
                    "mean_run_success_rate": 1.0,
                    "mean_add_precision": 1.0,
                    "mean_add_recall": 1.0,
                    "mean_add_f1": 1.0,
                    "mean_remove_precision": 1.0,
                    "mean_remove_recall": 1.0,
                    "mean_remove_f1": 1.0,
                    "mean_rollback_accuracy": 1.0,
                    "mean_task_completion_score": 1.0,
                    "mean_strict_task_completion_score": 1.0,
                    "mean_task_completion_variance": 0.0,
                    "mean_time_spent_seconds": 1.0,
                    "mean_total_tokens": 10.0,
                    "mean_api_call_count": 1.0,
                    "mean_tool_call_count": 0.0,
                    "mean_cost_usd": 0.01,
                },
                "single_runs": [
                    {
                        "task_slug": "tiny-task",
                        "testcase_id": "tc1",
                        "agent_name": "agent",
                        "run_id": "try1",
                        "add_precision": 1.0,
                        "add_recall": 1.0,
                        "add_f1": 1.0,
                        "remove_precision": 1.0,
                        "remove_recall": 1.0,
                        "remove_f1": 1.0,
                        "rollback_accuracy": 1.0,
                        "task_completion_score": 1.0,
                        "strict_task_completion_score": 1.0,
                        "task_success": True,
                        "time_spent_seconds": 1.0,
                        "total_tokens": 10.0,
                        "api_call_count": 1.0,
                        "tool_call_count": 0.0,
                        "cost_usd": 0.01,
                    }
                ],
                "groups": [
                    {
                        "task_slug": "tiny-task",
                        "testcase_id": "tc1",
                        "agent_name": "agent",
                        "k": 1,
                        "pass_at_k": True,
                        "run_success_rate": 1.0,
                        "add_precision": 1.0,
                        "add_recall": 1.0,
                        "add_f1": 1.0,
                        "remove_precision": 1.0,
                        "remove_recall": 1.0,
                        "remove_f1": 1.0,
                        "rollback_accuracy": 1.0,
                        "task_completion_score": 1.0,
                        "strict_task_completion_score": 1.0,
                        "task_completion_variance": 0.0,
                        "time_spent_seconds": 1.0,
                        "total_tokens": 10.0,
                        "api_call_count": 1.0,
                        "tool_call_count": 0.0,
                        "cost_usd": 0.01,
                    }
                ],
                "task_summary": [
                    {
                        "task_slug": "tiny-task",
                        "metric_name": "TinyMetric",
                        "ml_domain": "tabular",
                        "problem_type": "classification",
                        "table_structure": "single_table",
                        "dataset_size_bucket": "small",
                        "dataset_size_raw": 100,
                        "feature_dimensionality_bucket": "low",
                        "feature_dimensionality_raw": 10,
                        "preprocessing_complexity_bucket": "low",
                        "preprocessing_complexity_raw": 2,
                        "group_count": 1,
                        "agent_count": 1,
                        "task_success_rate": 1.0,
                        "mean_k": 1.0,
                        "mean_run_success_rate": 1.0,
                        "mean_add_precision": 1.0,
                        "mean_add_recall": 1.0,
                        "mean_add_f1": 1.0,
                        "mean_remove_precision": 1.0,
                        "mean_remove_recall": 1.0,
                        "mean_remove_f1": 1.0,
                        "mean_rollback_accuracy": 1.0,
                        "mean_task_completion_score": 1.0,
                        "mean_strict_task_completion_score": 1.0,
                        "mean_task_completion_variance": 0.0,
                        "mean_time_spent_seconds": 1.0,
                        "mean_total_tokens": 10.0,
                        "mean_api_call_count": 1.0,
                        "mean_tool_call_count": 0.0,
                        "mean_cost_usd": 0.01,
                    }
                ],
                "agent_summary": [
                    {
                        "agent_name": "agent",
                        "group_count": 1,
                        "task_success_rate": 1.0,
                        "mean_k": 1.0,
                        "mean_run_success_rate": 1.0,
                        "mean_add_precision": 1.0,
                        "mean_add_recall": 1.0,
                        "mean_add_f1": 1.0,
                        "mean_remove_precision": 1.0,
                        "mean_remove_recall": 1.0,
                        "mean_remove_f1": 1.0,
                        "mean_rollback_accuracy": 1.0,
                        "mean_task_completion_score": 1.0,
                        "mean_strict_task_completion_score": 1.0,
                        "mean_task_completion_variance": 0.0,
                        "mean_time_spent_seconds": 1.0,
                        "mean_total_tokens": 10.0,
                        "mean_api_call_count": 1.0,
                        "mean_tool_call_count": 0.0,
                        "mean_cost_usd": 0.01,
                    }
                ],
            }
        )

        self.assertIn("# Benchmark Aggregate Report", markdown)
        self.assertIn("## Task Characteristics", markdown)
        self.assertIn("## Reproducible Commands", markdown)
        self.assertIn("## Agent Summary", markdown)
        self.assertIn("Mean Remove Recall", markdown)
        self.assertNotIn("Mean Rollback", markdown)
        self.assertIn("tiny-task", markdown)


if __name__ == "__main__":
    unittest.main()
