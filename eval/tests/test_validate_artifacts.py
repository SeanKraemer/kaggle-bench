from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "eval" / "scripts" / "validate_artifacts.py"


def load_validator_module():
    spec = importlib.util.spec_from_file_location("validator_module", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load validator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator_module()


def write_json(path: Path, payload: dict) -> Path:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


class ValidatorHelperTests(unittest.TestCase):
    def test_output_schema_accepts_prompt_and_stream_artifact_kinds(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            output_path = write_json(
                temp_dir / "output.json",
                {
                    "competition_slug": "temp-task",
                    "testcase_id": "tc",
                    "agent_name": "test-agent",
                    "run_by": "test",
                    "run_id": "run-1",
                    "artifact_refs": [
                        {"kind": "metadata", "path": "provenance/meta.json"},
                        {"kind": "prompt", "path": "provenance/prompt.md"},
                        {"kind": "stream", "path": "provenance/stream.jsonl"},
                    ],
                    "predicted_add_action_ids": [],
                    "predicted_remove_action_ids": [],
                    "time_spent_seconds": 1,
                    "token_usage": {
                        "input_tokens": None,
                        "output_tokens": None,
                        "total_tokens": None,
                    },
                    "notes": "test artifact",
                },
            )

            output_validator = VALIDATOR.load_validator(ROOT / "data" / "schema" / "output.schema.json")
            _, errors = VALIDATOR.validate_json_file(output_path, output_validator)

        self.assertEqual(errors, [])

    def test_load_candidate_catalog_rejects_insufficient_bad_ratio(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            candidate_path = write_json(
                temp_dir / "candidate_actions.json",
                {
                    "competition_slug": "temp-task",
                    "generated_at": "2026-03-30",
                    "actions": [
                        {"action_id": "CA-G1", "role": "good", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-G2", "role": "good", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B1", "role": "bad", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B2", "role": "bad", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B3", "role": "bad", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B4", "role": "bad", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B5", "role": "bad", "eval_stage": "core_preprocessing"},
                    ],
                },
            )

            _, errors = VALIDATOR.load_candidate_catalog(candidate_path)

        self.assertTrue(any("bad >= 3 * primary_effective_good_units" in message for message in errors))

    def test_load_candidate_catalog_rejects_cross_stage_equivalence_group(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            candidate_path = write_json(
                temp_dir / "candidate_actions.json",
                {
                    "competition_slug": "temp-task",
                    "generated_at": "2026-03-30",
                    "actions": [
                        {
                            "action_id": "CA-G1",
                            "role": "good",
                            "eval_stage": "core_preprocessing",
                            "equivalence_group": "g",
                        },
                        {
                            "action_id": "CA-G2",
                            "role": "good",
                            "eval_stage": "validation_protocol",
                            "equivalence_group": "g",
                        },
                        {"action_id": "CA-B1", "role": "bad", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B2", "role": "bad", "eval_stage": "core_preprocessing"},
                        {"action_id": "CA-B3", "role": "bad", "eval_stage": "core_preprocessing"},
                    ],
                },
            )

            _, errors = VALIDATOR.load_candidate_catalog(candidate_path)

        self.assertTrue(any("spans multiple eval_stage values" in message for message in errors))

    def test_validate_testcase_payload_tolerates_non_object_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            testcase_path = temp_dir / "testcases" / "tc.json"
            testcase_path.parent.mkdir(parents=True, exist_ok=True)
            task_path = temp_dir / "task.json"
            task_path.write_text("{}", encoding="utf-8")

            errors = VALIDATOR.validate_testcase_payload(
                testcase_path=testcase_path,
                testcase_payload={
                    "testcase_id": "tc",
                    "competition_slug": "temp-task",
                    "task_ref": "../task.json",
                    "input": "oops",
                },
                expected_slug="temp-task",
                task_path=task_path,
                candidate_catalog={},
                candidate_ids=set(),
                seen_testcase_ids={},
            )

        self.assertIsInstance(errors, list)

    def test_validate_output_payload_allows_invalid_final_state_for_eval_scoring(self) -> None:
        candidate_catalog = {
            "CA-GOOD": {
                "action_id": "CA-GOOD",
                "role": "good",
                "eval_stage": "core_preprocessing",
            },
            "CA-BAD": {
                "action_id": "CA-BAD",
                "role": "bad",
                "eval_stage": "core_preprocessing",
                "conflicts_with_action_ids": ["CA-GOOD"],
            },
        }

        errors = VALIDATOR.validate_output_payload(
            output_path=Path("/tmp/output.json"),
            output_payload={
                "competition_slug": "temp-task",
                "testcase_id": "tc",
                "artifact_refs": [],
                "predicted_add_action_ids": ["CA-GOOD"],
                "predicted_remove_action_ids": [],
            },
            expected_slug="temp-task",
            testcase_contexts={"tc": {"CA-BAD"}},
            candidate_catalog=candidate_catalog,
            candidate_ids=set(candidate_catalog),
        )

        self.assertEqual(errors, [])

    def test_validate_output_payload_still_rejects_basic_contract_errors(self) -> None:
        candidate_catalog = {
            "CA-A": {
                "action_id": "CA-A",
                "role": "good",
                "eval_stage": "core_preprocessing",
            },
            "CA-B": {
                "action_id": "CA-B",
                "role": "good",
                "eval_stage": "core_preprocessing",
            },
        }

        errors = VALIDATOR.validate_output_payload(
            output_path=Path("/tmp/output.json"),
            output_payload={
                "competition_slug": "temp-task",
                "testcase_id": "tc",
                "artifact_refs": [],
                "predicted_add_action_ids": ["CA-A", "CA-UNKNOWN"],
                "predicted_remove_action_ids": ["CA-B", "CA-UNKNOWN"],
            },
            expected_slug="temp-task",
            testcase_contexts={"tc": {"CA-A"}},
            candidate_catalog=candidate_catalog,
            candidate_ids=set(candidate_catalog),
        )

        self.assertTrue(any("already in testcase context" in message for message in errors))
        self.assertTrue(any("unknown candidate action `CA-UNKNOWN`" in message for message in errors))
        self.assertTrue(any("action `CA-B` is not in testcase context" in message for message in errors))


if __name__ == "__main__":
    unittest.main()
