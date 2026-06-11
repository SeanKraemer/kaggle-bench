from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from agent.generic_agent.runner import run_generic_agent


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_temp_task_bundle(root: Path, *, context_action_ids: list[str] | None = None) -> Path:
    task_dir = root / "data" / "tasks" / "zillow-prize-1"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "zillow-prize-1",
            "dataset": {
                "train_files": ["train.csv"],
                "lookup_files": ["lookup.csv"],
                "target_column": "target",
                "primary_key": "id",
            },
            "goal": "Suggest preprocessing actions.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {"how": "left"},
                    "role": "good",
                },
                {
                    "action_id": "CA-2",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["target"]},
                    "role": "bad",
                },
            ]
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "zillow-prize-1",
            "input": {
                "scenario": "from_scratch",
                "context_action_ids": context_action_ids or [],
            },
        },
    )
    return task_dir


def build_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(data_root / "train.csv", "id,target\n1,0\n")
    write_text(data_root / "lookup.csv", "id,x\n1,2\n")
    return data_root


class GenericAgentRunnerTests(unittest.TestCase):
    def test_run_generic_agent_writes_success_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_data_root(root)
            captured = {}

            def fake_llm(**kwargs):
                captured.update(kwargs)
                return {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 10,
                    "output_tokens": 5,
                }

            result = run_generic_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                llm_call=fake_llm,
                reasoning_enabled=False,
                time_fn=lambda: 1.0,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")
            prompt_text = result["prompt_path"].read_text(encoding="utf-8")
            scratchpad_text = result["scratchpad_path"].read_text(encoding="utf-8")
            tool_calls_text = result["tool_calls_path"].read_text(encoding="utf-8")

        self.assertEqual(output_payload["agent_name"], "generic_agent")
        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(metadata_payload["tool_allowlist"], ["bash", "python", "scratchpad_read", "scratchpad_write"])
        self.assertEqual(metadata_payload["api_call_count"], 1)
        self.assertEqual(metadata_payload["tool_call_count"], 0)
        self.assertEqual(metadata_payload["time_spent_seconds"], output_payload["time_spent_seconds"])
        self.assertEqual(metadata_payload["token_usage"], output_payload["token_usage"])
        self.assertEqual(
            metadata_payload["token_usage"],
            {"input_tokens": 10, "output_tokens": 5, "total_tokens": 15},
        )
        self.assertIn("Generic Agent Trace", trace_text)
        self.assertIn("generic tools", prompt_text.lower())
        self.assertIn('"entries": []', scratchpad_text)
        self.assertEqual(tool_calls_text, "")
        self.assertEqual(
            [tool["name"] for tool in captured["tools"]], ["bash", "python", "scratchpad_read", "scratchpad_write"]
        )
        self.assertNotIn("api_calls_path", result)

    def test_run_generic_agent_writes_api_call_artifact_when_enabled(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_data_root(root)

            result = run_generic_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                llm_call=lambda **_: {
                    "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                    "input_tokens": 10,
                    "output_tokens": 5,
                    "stop_reason": "end_turn",
                },
                reasoning_enabled=False,
                capture_llm_calls=True,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            api_calls_text = result["api_calls_path"].read_text(encoding="utf-8")
            api_call_records = [json.loads(line) for line in api_calls_text.splitlines() if line.strip()]

        self.assertIn("api_calls_path", result)
        self.assertTrue(any(ref["kind"] == "api_calls" for ref in output_payload["artifact_refs"]))
        self.assertEqual(len(api_call_records), 1)
        self.assertEqual(api_call_records[0]["turn_index"], 1)
        self.assertEqual(api_call_records[0]["request"]["model"], "claude-sonnet-4-6")
        self.assertEqual(api_call_records[0]["response"]["stop_reason"], "end_turn")
        self.assertIn("predicted_add_action_ids", api_call_records[0]["response"]["raw_text"])
        self.assertNotIn("api_key", json.dumps(api_call_records[0]).lower())

    def test_run_generic_agent_tool_sequence_can_write_prediction_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_data_root(root)
            calls = []

            def fake_llm(**kwargs):
                calls.append(kwargs)
                if len(calls) == 1:
                    return {
                        "raw_text": "",
                        "tool_calls": [
                            {
                                "id": "toolu_py",
                                "name": "python",
                                "input": {
                                    "code": (
                                        "from pathlib import Path\n"
                                        "Path('prediction.json').write_text('{\"predicted_add_action_ids\":[\"CA-1\"],\"predicted_remove_action_ids\":[]}', encoding='utf-8')\n"
                                        "print('wrote prediction')\n"
                                    )
                                },
                            }
                        ],
                        "input_tokens": 1,
                        "output_tokens": 1,
                    }
                return {"raw_text": "prediction written", "input_tokens": 1, "output_tokens": 1}

            result = run_generic_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="tool_try",
                data_root=data_root,
                llm_call=fake_llm,
                reasoning_enabled=False,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            tool_calls_text = result["tool_calls_path"].read_text(encoding="utf-8")

        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertIn('"name": "python"', tool_calls_text)
        self.assertEqual(calls[1]["messages"][-1]["content"][0]["type"], "tool_result")

    def test_run_generic_agent_validation_normalizes_ids_and_restricts_removes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root, context_action_ids=["CA-2"])
            data_root = build_data_root(root)

            result = run_generic_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="validated_try",
                data_root=data_root,
                llm_call=lambda **_: {
                    "raw_text": json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1", "CA-1", "CA-999"],
                            "predicted_remove_action_ids": ["CA-1", "CA-2"],
                        }
                    ),
                    "input_tokens": 1,
                    "output_tokens": 1,
                },
                reasoning_enabled=False,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")

        self.assertEqual(output_payload["predicted_add_action_ids"], [])
        self.assertEqual(output_payload["predicted_remove_action_ids"], ["CA-2"])
        self.assertIn("unknown_add_action_ids=['CA-999']", trace_text)
        self.assertIn("removed_conflicting_action_ids=['CA-1']", trace_text)

    def test_run_generic_agent_preserves_workspace_on_missing_prediction(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_data_root(root)

            with self.assertRaises(ValueError) as raised:
                run_generic_agent(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="failed_try",
                    data_root=data_root,
                    llm_call=lambda **_: {"raw_text": "not json", "input_tokens": 1, "output_tokens": 1},
                    max_validation_retries=0,
                    reasoning_enabled=False,
                    capture_llm_calls=True,
                )

            match = re.search(r"Workspace preserved at (.*?)\. Failed provenance", str(raised.exception))
            self.assertIsNotNone(match)
            preserved = Path(match.group(1).strip())
            provenance_dir = task_dir / "outputs" / "provenance"
            failed_metadata = provenance_dir / "tc1_generic_agent_failed_try.failed.meta.json"
            failed_trace = provenance_dir / "tc1_generic_agent_failed_try.failed.trace.md"
            failed_prompt = provenance_dir / "tc1_generic_agent_failed_try.failed.prompt.md"
            failed_scratchpad = provenance_dir / "tc1_generic_agent_failed_try.failed.scratchpad.json"
            failed_tool_calls = provenance_dir / "tc1_generic_agent_failed_try.failed.tool_calls.jsonl"
            failed_api_calls = provenance_dir / "tc1_generic_agent_failed_try.failed.api_calls.jsonl"
            try:
                self.assertTrue(preserved.exists())
                self.assertTrue((preserved / "PROMPT.md").exists())
                self.assertFalse((task_dir / "outputs" / "tc1_generic_agent_failed_try.json").exists())
                self.assertTrue(failed_metadata.exists())
                self.assertTrue(failed_trace.exists())
                self.assertTrue(failed_prompt.exists())
                self.assertTrue(failed_scratchpad.exists())
                self.assertTrue(failed_tool_calls.exists())
                self.assertTrue(failed_api_calls.exists())
                metadata = json.loads(failed_metadata.read_text(encoding="utf-8"))
                self.assertEqual(metadata["status"], "failed")
                self.assertTrue(metadata["workspace_preserved"])
                self.assertEqual(metadata["workspace_path"], str(preserved))
                self.assertEqual(metadata["api_call_count"], 1)
                self.assertTrue(any(ref["kind"] == "api_calls" for ref in metadata["artifact_refs"]))
                api_records = [
                    json.loads(line)
                    for line in failed_api_calls.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                self.assertEqual(len(api_records), 1)
                self.assertIn("not json", api_records[0]["response"]["raw_text"])
            finally:
                if preserved.exists():
                    import shutil

                    shutil.rmtree(preserved)


if __name__ == "__main__":
    unittest.main()
