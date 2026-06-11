from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
EVAL_PATH = ROOT / "eval" / "eval.py"
ZILLOW_TESTCASE = ROOT / "data" / "tasks" / "zillow-prize-1" / "testcases" / "tc1_from_scratch.json"
ZILLOW_HUMAN = ROOT / "data" / "tasks" / "zillow-prize-1" / "human_baseline" / "tc1_human.json"


def load_eval_module():
    spec = importlib.util.spec_from_file_location("eval_module", EVAL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load eval module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EVAL = load_eval_module()


def write_json(path: Path, payload: Any) -> Path:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def temp_output(
    directory: Path,
    *,
    competition_slug: str,
    testcase_id: str,
    predicted_add_action_ids: list[str],
    predicted_remove_action_ids: list[str],
) -> Path:
    return write_json(
        directory / f"{testcase_id}_output.json",
        {
            "competition_slug": competition_slug,
            "testcase_id": testcase_id,
            "agent_name": "test-agent",
            "run_by": "test",
            "run_id": "run-1",
            "artifact_refs": [],
            "predicted_add_action_ids": predicted_add_action_ids,
            "predicted_remove_action_ids": predicted_remove_action_ids,
            "time_spent_seconds": 1,
            "token_usage": {
                "input_tokens": None,
                "output_tokens": None,
                "total_tokens": None,
            },
            "notes": "test artifact",
        },
    )


def temp_task_bundle(
    directory: Path,
    *,
    testcase_id: str,
    testcase: Any,
    actions: list[Any],
) -> Path:
    task_dir = directory / "task"
    testcase_dir = task_dir / "testcases"
    testcase_dir.mkdir(parents=True, exist_ok=True)
    write_json(
        task_dir / "candidate_actions.json",
        {"competition_slug": "temp-task", "generated_at": "2026-03-30", "actions": actions},
    )
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "temp-task",
            "dataset": {
                "provider": "kaggle",
                "competition": "temp-task",
                "train_files": ["train.csv"],
                "test_files": [],
                "lookup_files": [],
                "sample_submission_files": [],
                "data_dictionary_files": [],
                "target_column": "target",
                "primary_key": "id",
            },
            "goal": "test task",
            "task_characteristics": {
                "ml_domain": "tabular",
                "problem_type": "regression",
                "table_structure": "single_table",
                "dataset_size_bucket": "small",
                "dataset_size_raw": 1,
                "feature_dimensionality_bucket": "low",
                "feature_dimensionality_raw": 1,
                "preprocessing_complexity_bucket": "low",
                "preprocessing_complexity_raw": 1,
                "analysis_notes": "test",
            },
        },
    )
    testcase_path = testcase_dir / f"{testcase_id}.json"
    write_json(testcase_path, testcase)
    return testcase_path


class NewEvalTests(unittest.TestCase):
    def test_build_summary_uses_remove_recall_for_task_completion(self) -> None:
        summary = EVAL.build_summary(
            add_result={"add_f1": 0.4},
            remove_result={
                "remove_recall": 0.8,
                "rollback_accuracy": 0.1,
                "remove_f1": 0.6,
            },
            success_threshold=0.5,
        )

        self.assertEqual(summary["task_completion_score"], 0.6)
        self.assertEqual(summary["strict_task_completion_score"], 0.5)
        self.assertTrue(summary["task_success"])

    def test_equivalence_group_already_satisfied_by_context_makes_extra_member_false_positive(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            actions = [
                {
                    "action_id": "CA-G1",
                    "action_type": "GOOD_EQUIV",
                    "canonical_params": {},
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
                    "equivalence_group": "g",
                },
                {
                    "action_id": "CA-G2",
                    "action_type": "GOOD_EQUIV",
                    "canonical_params": {},
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
                    "equivalence_group": "g",
                },
                {
                    "action_id": "CA-G3",
                    "action_type": "GOOD_ACTION",
                    "canonical_params": {},
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
                },
                {
                    "action_id": "CA-B1",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-G3"],
                    "derivation_reasoning": "test",
                },
            ]
            testcase = {
                "testcase_id": "equiv_case",
                "competition_slug": "temp-task",
                "task_ref": "../task.json",
                "input": {
                    "scenario": "mixed",
                    "context_action_ids": ["CA-G1", "CA-B1"],
                },
            }
            testcase_path = temp_task_bundle(temp_dir, testcase_id="equiv_case", testcase=testcase, actions=actions)
            output_path = temp_output(
                temp_dir,
                competition_slug="temp-task",
                testcase_id="equiv_case",
                predicted_add_action_ids=["CA-G2", "CA-G3"],
                predicted_remove_action_ids=["CA-B1"],
            )

            result = EVAL.evaluate(
                testcase_path=testcase_path,
                input_path=output_path,
                stage_scope="primary",
                success_threshold=0.5,
            )

        self.assertEqual(result["add"]["expected_unit_count"], 1)
        self.assertEqual(result["add"]["true_positive_count"], 1)
        self.assertEqual(result["add"]["false_positive_count"], 1)
        self.assertEqual(result["add"]["false_negative_count"], 0)
        self.assertEqual(result["remove"]["true_positive_count"], 1)
        self.assertEqual(result["remove"]["false_positive_count"], 0)

    def test_primary_scope_ignores_non_core_predictions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            actions = [
                {
                    "action_id": "CA-CORE",
                    "action_type": "GOOD_CORE",
                    "canonical_params": {},
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
                },
                {
                    "action_id": "CA-VAL",
                    "action_type": "GOOD_VAL",
                    "canonical_params": {},
                    "eval_stage": "validation_protocol",
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
                },
                {
                    "action_id": "CA-B1",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-CORE"],
                    "derivation_reasoning": "test",
                },
                {
                    "action_id": "CA-B2",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-CORE"],
                    "derivation_reasoning": "test",
                },
                {
                    "action_id": "CA-B3",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-CORE"],
                    "derivation_reasoning": "test",
                },
            ]
            testcase = {
                "testcase_id": "scope_case",
                "competition_slug": "temp-task",
                "task_ref": "../task.json",
                "input": {
                    "scenario": "from_scratch",
                    "context_action_ids": [],
                },
            }
            testcase_path = temp_task_bundle(temp_dir, testcase_id="scope_case", testcase=testcase, actions=actions)
            output_path = temp_output(
                temp_dir,
                competition_slug="temp-task",
                testcase_id="scope_case",
                predicted_add_action_ids=["CA-VAL"],
                predicted_remove_action_ids=[],
            )

            result = EVAL.evaluate(
                testcase_path=testcase_path,
                input_path=output_path,
                stage_scope="primary",
                success_threshold=0.5,
            )

        self.assertEqual(result["add"]["false_positive_count"], 0)
        self.assertEqual(len(result["add"]["stage_filtered_predictions"]), 1)
        self.assertEqual(result["add"]["add_recall"], 0.0)
        self.assertEqual(result["remove"]["remove_f1"], 1.0)

    def test_conflicting_add_does_not_satisfy_recall(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            actions = [
                {
                    "action_id": "CA-GOOD",
                    "action_type": "GOOD_ACTION",
                    "canonical_params": {},
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
                },
                {
                    "action_id": "CA-BAD",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-GOOD"],
                    "derivation_reasoning": "test",
                    "conflicts_with_action_ids": ["CA-GOOD"],
                },
                {
                    "action_id": "CA-B2",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-GOOD"],
                    "derivation_reasoning": "test",
                },
                {
                    "action_id": "CA-B3",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-GOOD"],
                    "derivation_reasoning": "test",
                },
            ]
            testcase = {
                "testcase_id": "conflict_case",
                "competition_slug": "temp-task",
                "task_ref": "../task.json",
                "input": {
                    "scenario": "fault_injected",
                    "context_action_ids": ["CA-BAD"],
                },
            }
            testcase_path = temp_task_bundle(temp_dir, testcase_id="conflict_case", testcase=testcase, actions=actions)
            output_path = temp_output(
                temp_dir,
                competition_slug="temp-task",
                testcase_id="conflict_case",
                predicted_add_action_ids=["CA-GOOD"],
                predicted_remove_action_ids=[],
            )

            result = EVAL.evaluate(
                testcase_path=testcase_path,
                input_path=output_path,
                stage_scope="primary",
                success_threshold=0.5,
            )

        self.assertEqual(result["add"]["true_positive_count"], 0)
        self.assertEqual(result["add"]["false_positive_count"], 1)
        self.assertEqual(result["add"]["false_negative_count"], 1)
        self.assertFalse(result["final_state"]["is_valid"])

    def test_empty_side_convention_preserves_headline_score_but_not_strict_score(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            actions = [
                {
                    "action_id": "CA-GOOD",
                    "action_type": "GOOD_ACTION",
                    "canonical_params": {},
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
                },
                {
                    "action_id": "CA-B1",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-GOOD"],
                    "derivation_reasoning": "test",
                },
                {
                    "action_id": "CA-B2",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-GOOD"],
                    "derivation_reasoning": "test",
                },
                {
                    "action_id": "CA-B3",
                    "action_type": "BAD_ACTION",
                    "canonical_params": {},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "difficulty": "easy",
                    "reasoning": "test",
                    "provenance_type": "synthetic",
                    "derived_from_action_ids": ["CA-GOOD"],
                    "derivation_reasoning": "test",
                },
            ]
            testcase = {
                "testcase_id": "empty_case",
                "competition_slug": "temp-task",
                "task_ref": "../task.json",
                "input": {
                    "scenario": "partial_good",
                    "context_action_ids": ["CA-GOOD"],
                },
            }
            testcase_path = temp_task_bundle(temp_dir, testcase_id="empty_case", testcase=testcase, actions=actions)
            output_path = temp_output(
                temp_dir,
                competition_slug="temp-task",
                testcase_id="empty_case",
                predicted_add_action_ids=[],
                predicted_remove_action_ids=["CA-GOOD"],
            )

            result = EVAL.evaluate(
                testcase_path=testcase_path,
                input_path=output_path,
                stage_scope="primary",
                success_threshold=0.5,
            )

        self.assertEqual(result["add"]["add_f1"], 1.0)
        self.assertEqual(result["remove"]["remove_precision"], 0.0)
        self.assertEqual(result["remove"]["remove_recall"], 1.0)
        self.assertEqual(result["remove"]["remove_f1"], 0.0)
        self.assertEqual(result["summary"]["task_completion_score"], 1.0)
        self.assertEqual(result["summary"]["strict_task_completion_score"], 0.5)

    def test_zillow_human_baseline_smoke(self) -> None:
        result = EVAL.evaluate(
            testcase_path=ZILLOW_TESTCASE,
            input_path=ZILLOW_HUMAN,
            stage_scope="primary",
            success_threshold=0.5,
        )

        self.assertEqual(result["competition_slug"], "zillow-prize-1")
        self.assertEqual(result["testcase_id"], "tc1_from_scratch")
        self.assertEqual(result["stage_scope"], "primary")
        self.assertIn("task_completion_score", result["summary"])


if __name__ == "__main__":
    unittest.main()
