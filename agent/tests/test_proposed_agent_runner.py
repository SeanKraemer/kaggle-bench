from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agent.proposed_agent.runner import run_proposed_agent
from agent.tests.agentic_agent_fixtures import build_proposed_tool_task


class ProposedAgentRunnerTests(unittest.TestCase):
    def test_run_proposed_agent_accepts_profile_cache_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root, context_action_ids=["CA-3"])
            cache_dir = root / "profile-cache"
            responses = iter(
                [
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "add",
                                "predicted_add_action_ids": ["CA-2"],
                                "predicted_remove_action_ids": [],
                            }
                        ),
                        "input_tokens": 10,
                        "output_tokens": 5,
                        "stop_reason": "end_turn",
                    },
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "remove",
                                "predicted_add_action_ids": [],
                                "predicted_remove_action_ids": ["CA-3"],
                            }
                        ),
                        "input_tokens": 8,
                        "output_tokens": 4,
                        "stop_reason": "end_turn",
                    },
                ]
            )

            run_proposed_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="cache_dir",
                data_root=data_root,
                profile_cache_dir=cache_dir,
                llm_call=lambda **_: next(responses),
                reasoning_enabled=False,
            )

            cache_files_exist = any(cache_dir.iterdir())

        self.assertTrue(cache_files_exist)

    def test_run_proposed_agent_writes_success_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root, context_action_ids=["CA-3"])
            responses = iter(
                [
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "add",
                                "predicted_add_action_ids": ["CA-2"],
                                "predicted_remove_action_ids": [],
                            }
                        ),
                        "input_tokens": 10,
                        "output_tokens": 5,
                        "stop_reason": "end_turn",
                    },
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "remove",
                                "predicted_add_action_ids": [],
                                "predicted_remove_action_ids": ["CA-3"],
                            }
                        ),
                        "input_tokens": 8,
                        "output_tokens": 4,
                        "stop_reason": "end_turn",
                    },
                ]
            )

            result = run_proposed_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                llm_call=lambda **_: next(responses),
                reasoning_enabled=False,
                capture_llm_calls=True,
                time_fn=lambda: 1.0,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")

        artifact_kinds = [ref["kind"] for ref in output_payload["artifact_refs"]]
        self.assertEqual(output_payload["agent_name"], "proposed_agent")
        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-2"])
        self.assertEqual(output_payload["predicted_remove_action_ids"], ["CA-3"])
        self.assertEqual(metadata_payload["phase_statuses"], {"add": "success", "remove": "success"})
        self.assertEqual(metadata_payload["api_call_count"], 2)
        self.assertEqual(metadata_payload["token_usage"], output_payload["token_usage"])
        self.assertNotIn("bash", metadata_payload["tool_allowlist"])
        self.assertNotIn("python", metadata_payload["tool_allowlist"])
        self.assertIn("prompt", artifact_kinds)
        self.assertEqual(artifact_kinds.count("prompt"), 1)
        self.assertIn("scratchpad", artifact_kinds)
        self.assertIn("tool_calls", artifact_kinds)
        self.assertIn("api_calls", artifact_kinds)
        self.assertNotIn("notes", artifact_kinds)
        artifact_paths = [ref["path"] for ref in output_payload["artifact_refs"]]
        self.assertFalse(any("add_prompt" in path for path in artifact_paths))
        self.assertFalse(any("remove_prompt" in path for path in artifact_paths))
        self.assertFalse(any("reconciliation" in path for path in artifact_paths))
        self.assertIn("Reconciliation", trace_text)

    def test_run_proposed_agent_retries_malformed_phase_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root)
            responses = iter(
                [
                    {"raw_text": "not json", "input_tokens": 1, "output_tokens": 1},
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "add",
                                "predicted_add_action_ids": ["CA-2"],
                                "predicted_remove_action_ids": [],
                            }
                        ),
                        "input_tokens": 1,
                        "output_tokens": 1,
                    },
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "remove",
                                "predicted_add_action_ids": [],
                                "predicted_remove_action_ids": ["CA-3"],
                            }
                        ),
                        "input_tokens": 1,
                        "output_tokens": 1,
                    },
                ]
            )

            result = run_proposed_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="retry",
                data_root=data_root,
                llm_call=lambda **_: next(responses),
                reasoning_enabled=False,
                max_validation_retries=1,
            )

            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))

        self.assertEqual(metadata_payload["api_call_count"], 3)
        self.assertEqual(metadata_payload["status"], "success")

    def test_run_proposed_agent_default_tool_budget_allows_realistic_exploration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root)
            add_tool_responses = [
                {
                    "raw_text": "",
                    "tool_calls": [
                        {
                            "id": f"toolu_note_{turn}_{index}",
                            "name": "scratchpad_write",
                            "input": {"entry": {"turn": turn, "index": index}},
                        }
                        for index in range(2)
                    ],
                    "input_tokens": 1,
                    "output_tokens": 1,
                }
                for turn in range(4)
            ]
            responses = iter(
                [
                    *add_tool_responses,
                    {
                        "raw_text": "",
                        "tool_calls": [
                            {
                                "id": "toolu_note_final",
                                "name": "scratchpad_write",
                                "input": {"entry": {"turn": 4, "index": 0}},
                            }
                        ],
                        "input_tokens": 1,
                        "output_tokens": 1,
                    },
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "add",
                                "predicted_add_action_ids": ["CA-2"],
                                "predicted_remove_action_ids": [],
                            }
                        ),
                        "input_tokens": 1,
                        "output_tokens": 1,
                    },
                    {
                        "raw_text": json.dumps(
                            {
                                "phase": "remove",
                                "predicted_add_action_ids": [],
                                "predicted_remove_action_ids": ["CA-3"],
                            }
                        ),
                        "input_tokens": 1,
                        "output_tokens": 1,
                    },
                ]
            )

            result = run_proposed_agent(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="tool_budget",
                data_root=data_root,
                llm_call=lambda **_: next(responses),
                reasoning_enabled=False,
            )

            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))

        self.assertEqual(metadata_payload["status"], "success")
        self.assertEqual(metadata_payload["tool_call_count"], 9)

    def test_run_proposed_agent_failed_phase_writes_failed_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root)

            with self.assertRaises(ValueError):
                run_proposed_agent(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="failed",
                    data_root=data_root,
                    llm_call=lambda **_: {"raw_text": "not json", "input_tokens": 1, "output_tokens": 1},
                    reasoning_enabled=False,
                    max_validation_retries=0,
                    capture_llm_calls=True,
                )

            output_path = task_dir / "outputs" / "tc1_proposed_agent_failed.json"
            failed_metadata = task_dir / "outputs" / "provenance" / "tc1_proposed_agent_failed.failed.meta.json"
            metadata_payload = json.loads(failed_metadata.read_text(encoding="utf-8"))

        self.assertFalse(output_path.exists())
        self.assertEqual(metadata_payload["status"], "failed")
        self.assertEqual(metadata_payload["phase_statuses"]["add"], "failed")
        self.assertTrue(any(ref["kind"] == "api_calls" for ref in metadata_payload["artifact_refs"]))


if __name__ == "__main__":
    unittest.main()
