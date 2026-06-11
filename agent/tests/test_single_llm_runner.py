from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "agent" / "single_llm" / "runner.py"


def load_runner_module():
    spec = importlib.util.spec_from_file_location("agent_single_llm_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load single_llm runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def assert_text_ends_with_newline(testcase: unittest.TestCase, text: str) -> None:
    testcase.assertTrue(text.endswith("\n"))


def build_temp_task_bundle(root: Path) -> Path:
    task_dir = root / "data" / "tasks" / "zillow-prize-1"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "zillow-prize-1",
            "dataset": {
                "train_files": ["train_2016_v2.csv"],
                "lookup_files": ["properties_2016.csv"],
                "target_column": "logerror",
                "primary_key": "parcelid",
            },
            "goal": "Suggest preprocessing actions for logerror prediction.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "zillow-prize-1",
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {"how": "left", "right_table_id": "properties_2016"},
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                    "difficulty": "easy",
                    "reasoning": "hint",
                },
                {
                    "action_id": "CA-2",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["parcelid"]},
                    "eval_stage": "core_preprocessing",
                    "role": "bad",
                    "equivalence_group": "hidden",
                    "provenance_type": "synthetic",
                },
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "zillow-prize-1",
            "task_ref": "../task.json",
            "input": {
                "scenario": "from_scratch",
                "context_action_ids": [],
            },
        },
    )
    (task_dir / "outputs" / "provenance").mkdir(parents=True, exist_ok=True)
    return task_dir


def build_temp_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train_2016_v2.csv",
        "parcelid,logerror,transactiondate\n1,0.1,2016-10-01\n2,0.2,2016-10-02\n",
    )
    write_text(
        data_root / "properties_2016.csv",
        "parcelid,feature_num\n1,10\n2,\n",
    )
    return data_root


class SingleLLMRunnerTests(unittest.TestCase):
    def test_parse_prediction_text_extracts_wrapped_json(self) -> None:
        from agent.single_llm.parsing import parse_prediction_text

        parsed = parse_prediction_text('prefix {"predicted_add_action_ids": ["CA-1"], "predicted_remove_action_ids": []} suffix')

        self.assertEqual(parsed["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(parsed["predicted_remove_action_ids"], [])

    def test_parse_prediction_text_extracts_prediction_shaped_object_when_unrelated_json_follows(self) -> None:
        from agent.single_llm.parsing import parse_prediction_text

        parsed = parse_prediction_text(
            '\n'.join(
                [
                    "Here is the prediction:",
                    '{"predicted_add_action_ids": ["CA-1"], "predicted_remove_action_ids": []}',
                    "Debug note:",
                    '{"irrelevant": true}',
                ]
            )
        )

        self.assertEqual(parsed["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(parsed["predicted_remove_action_ids"], [])

    def test_parse_prediction_text_prefers_last_prediction_shaped_object(self) -> None:
        from agent.single_llm.parsing import parse_prediction_text

        parsed = parse_prediction_text(
            '\n'.join(
                [
                    "Template:",
                    '{"predicted_add_action_ids": [], "predicted_remove_action_ids": []}',
                    "Final answer:",
                    '{"predicted_add_action_ids": ["CA-2"], "predicted_remove_action_ids": ["CA-3"]}',
                ]
            )
        )

        self.assertEqual(parsed["predicted_add_action_ids"], ["CA-2"])
        self.assertEqual(parsed["predicted_remove_action_ids"], ["CA-3"])

    def test_parse_prediction_text_rejects_dicts_without_prediction_keys(self) -> None:
        from agent.single_llm.parsing import parse_prediction_text

        with self.assertRaisesRegex(
            ValueError,
            "prediction payload must include predicted_add_action_ids and predicted_remove_action_ids",
        ):
            parse_prediction_text(
                '\n'.join(
                    [
                        "Debug note:",
                        '{"irrelevant": true}',
                        "Another object:",
                        '{"notes": "still not the prediction"}',
                    ]
                )
            )

    def test_validate_prediction_payload_normalizes_action_ids_and_rationales(self) -> None:
        from agent.single_llm.parsing import validate_prediction_payload

        payload = {
            "predicted_add_action_ids": ["CA-1", "CA-1", "CA-999", 7],
            "predicted_remove_action_ids": ["CA-1", "CA-2", "CA-2"],
            "notes": 123,
            "action_rationales": [
                {
                    "action_id": "CA-1",
                    "decision": "add",
                    "reason": "needed",
                },
                {
                    "action_id": "CA-999",
                    "decision": "add",
                    "reason": "unknown",
                },
            ],
        }

        normalized, warnings = validate_prediction_payload(payload, valid_action_ids={"CA-1", "CA-2"})

        self.assertEqual(normalized["predicted_add_action_ids"], [])
        self.assertEqual(normalized["predicted_remove_action_ids"], ["CA-2"])
        self.assertIsNone(normalized["notes"])
        self.assertEqual(
            normalized["action_rationales"],
            [
                {
                    "action_id": "CA-1",
                    "decision": "add",
                    "reason": "needed",
                }
            ],
        )
        self.assertIn("unknown_add_action_ids=['CA-999']", warnings)
        self.assertIn("dropped_non_string_add_action_ids=[7]", warnings)
        self.assertIn("deduplicated_add_action_ids=['CA-1']", warnings)
        self.assertIn("removed_conflicting_action_ids=['CA-1']", warnings)
        self.assertIn("ignored_notes=not_a_string", warnings)
        self.assertIn("ignored_rationales_for_unknown_action_ids=['CA-999']", warnings)

    def test_run_single_llm_writes_success_artifacts(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")
            captured = {}

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **kwargs: (
                    captured.update(kwargs)
                    or {
                        "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                        "input_tokens": 100,
                        "output_tokens": 20,
                        "total_tokens": 120,
                    }
                ),
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))
            prompt_text = captured["prompt_text"]
            stored_prompt_text = result["prompt_path"].read_text(encoding="utf-8")
            prompt_exists = result["prompt_path"].exists()

        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(metadata_payload["status"], "success")
        self.assertEqual(metadata_payload["api_call_count"], 1)
        self.assertIn('"action_id": "CA-1"', prompt_text)
        self.assertNotIn('"role"', prompt_text)
        self.assertNotIn('"eval_stage"', prompt_text)
        self.assertNotIn('"reasoning"', prompt_text)
        self.assertNotIn('"difficulty"', prompt_text)
        self.assertNotIn('"provenance_type"', prompt_text)
        self.assertIn("Numeric profile:", prompt_text)
        self.assertIn("Boolean-like profile:", prompt_text)
        self.assertIn("Target column: logerror", prompt_text)
        self.assertIn("Primary key: parcelid", prompt_text)
        self.assertTrue(prompt_exists)
        self.assertEqual(stored_prompt_text.rstrip("\n"), prompt_text.rstrip("\n"))
        assert_text_ends_with_newline(self, stored_prompt_text)
        self.assertEqual(output_payload["artifact_refs"][2]["kind"], "prompt")
        self.assertEqual(captured["thinking"]["type"], "adaptive")
        self.assertEqual(captured["thinking"]["display"], "summarized")
        self.assertEqual(captured["output_config"]["effort"], "medium")
        self.assertEqual(captured["temperature"], 1.0)
        self.assertEqual(captured["system_blocks"][0]["cache_control"]["type"], "ephemeral")
        self.assertIn("Current context (testcase)", captured["message_content_blocks"][0]["text"])

    def test_run_single_llm_records_elapsed_time(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")
            clock_values = iter([10.0, 13.4])

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 100,
                    "output_tokens": 20,
                    "total_tokens": 120,
                },
                time_fn=lambda: next(clock_values),
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))

        self.assertEqual(output_payload["time_spent_seconds"], 3.4)

    def test_run_single_llm_prompt_uses_action_referenced_columns_only(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")
            captured = {}

            runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **kwargs: (
                    captured.update(kwargs)
                    or {
                        "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                        "input_tokens": 100,
                        "output_tokens": 20,
                        "total_tokens": 120,
                    }
                ),
            )

            prompt_text = captured["prompt_text"]

        self.assertIn("Referenced dataset columns in visible actions: 1 / 3", prompt_text)
        self.assertIn('"parcelid"', prompt_text)
        self.assertNotIn('"transactiondate"', prompt_text)
        self.assertNotIn('"feature_num"', prompt_text)

    def test_run_single_llm_trace_includes_prediction_summary_and_rationales(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: {
                    "raw_text": json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                            "notes": "Join is needed before feature cleanup.",
                            "action_rationales": [
                                {
                                    "action_id": "CA-1",
                                    "decision": "add",
                                    "reason": "The lookup join is needed to expose feature columns.",
                                }
                            ],
                        }
                    ),
                    "input_tokens": 100,
                    "output_tokens": 20,
                    "total_tokens": 120,
                },
            )

            trace_text = result["trace_path"].read_text(encoding="utf-8")

        self.assertIn("### Prediction Summary", trace_text)
        self.assertIn("Parsed add ids", trace_text)
        self.assertIn("CA-1", trace_text)
        self.assertIn("### Model Notes", trace_text)
        self.assertIn("Join is needed before feature cleanup.", trace_text)
        self.assertIn("### Action Rationales", trace_text)
        self.assertIn("The lookup join is needed to expose feature columns.", trace_text)

    def test_run_single_llm_accepts_bound_llm_caller_contract(self) -> None:
        runner = load_runner_module()
        from agent.llm.client import build_llm_caller

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")
            captured = {}

            def fake_send(**kwargs):
                captured.update(kwargs)
                return {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 5,
                    "output_tokens": 6,
                    "total_tokens": 11,
                }

            llm_caller = build_llm_caller(
                provider="anthropic",
                api_key="bound-key",
                send_fn=fake_send,
            )
            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try_bound",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=llm_caller,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))

        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(captured["api_key"], "bound-key")

    def test_run_single_llm_retries_after_parse_failure(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")
            responses = [
                {
                    "raw_text": "not valid json",
                    "input_tokens": 10,
                    "output_tokens": 5,
                    "total_tokens": 15,
                },
                {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 20,
                    "output_tokens": 10,
                    "total_tokens": 30,
                },
            ]

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: responses.pop(0),
                max_attempts=2,
            )

            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))

        self.assertEqual(metadata_payload["status"], "success")
        self.assertEqual(metadata_payload["api_call_count"], 2)

    def test_run_single_llm_retries_after_non_prediction_json(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")
            responses = [
                {
                    "raw_text": 'Debug note: {"irrelevant": true}',
                    "input_tokens": 10,
                    "output_tokens": 5,
                    "total_tokens": 15,
                },
                {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 20,
                    "output_tokens": 10,
                    "total_tokens": 30,
                },
            ]

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: responses.pop(0),
                max_attempts=2,
            )

            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))

        self.assertEqual(metadata_payload["status"], "success")
        self.assertEqual(metadata_payload["api_call_count"], 2)

    def test_run_single_llm_filters_invalid_and_duplicate_action_ids(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: {
                    "raw_text": json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1", "CA-1", "CA-999", 7],
                            "predicted_remove_action_ids": ["CA-1", "CA-2", "CA-2"],
                        }
                    ),
                    "input_tokens": 100,
                    "output_tokens": 20,
                    "total_tokens": 120,
                },
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")

        self.assertEqual(output_payload["predicted_add_action_ids"], [])
        self.assertEqual(output_payload["predicted_remove_action_ids"], ["CA-2"])
        self.assertIn("### Validation Warnings", trace_text)
        self.assertIn("unknown_add_action_ids=['CA-999']", trace_text)
        self.assertIn("dropped_non_string_add_action_ids=[7]", trace_text)
        self.assertIn("deduplicated_add_action_ids=['CA-1']", trace_text)
        self.assertIn("removed_conflicting_action_ids=['CA-1']", trace_text)

    def test_run_single_llm_trace_includes_thinking_and_cache_usage(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 100,
                    "output_tokens": 20,
                    "total_tokens": 120,
                    "thinking_summaries": ["Reasoning summary"],
                    "cache_creation_input_tokens": 500,
                    "cache_read_input_tokens": 1000,
                    "cache_creation": {"ephemeral_5m_input_tokens": 500},
                },
            )

            trace_text = result["trace_path"].read_text(encoding="utf-8")
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))

        self.assertIn("### Thinking Summary", trace_text)
        self.assertIn("Reasoning summary", trace_text)
        self.assertIn("### Cache Usage", trace_text)
        self.assertIn("cache_read_input_tokens", trace_text)
        self.assertEqual(metadata_payload["cache_usage"]["cache_read_input_tokens"], 1000)

    def test_run_single_llm_persists_partial_result_when_cost_cap_exceeded(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-key", encoding="utf-8")

            result = runner.run_single_llm(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                api_key_path=api_key_path,
                llm_call=lambda **_: {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 500000,
                    "output_tokens": 500000,
                    "total_tokens": 1000000,
                },
                cost_cap_usd=1.0,
            )

            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))

        self.assertEqual(metadata_payload["status"], "partial_success")
        self.assertIn("cost cap", metadata_payload["error_message"].lower())
