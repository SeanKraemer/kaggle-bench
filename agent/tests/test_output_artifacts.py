from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_ARTIFACTS_PATH = ROOT / "agent" / "output_artifacts.py"


def load_output_artifacts_module():
    spec = importlib.util.spec_from_file_location("agent_output_artifacts", OUTPUT_ARTIFACTS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load output_artifacts module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_file_ends_with_newline(testcase: unittest.TestCase, path: Path) -> None:
    payload = path.read_bytes()
    testcase.assertTrue(payload, f"{path} should not be empty")
    testcase.assertEqual(payload[-1:], b"\n", f"{path} should end with a newline")


class OutputArtifactsTests(unittest.TestCase):
    def test_write_output_bundle_creates_output_trace_and_metadata(self) -> None:
        output_artifacts = load_output_artifacts_module()

        with tempfile.TemporaryDirectory() as tmp:
            task_dir = Path(tmp)
            (task_dir / "outputs" / "provenance").mkdir(parents=True, exist_ok=True)

            paths = output_artifacts.write_output_bundle(
                task_dir=task_dir,
                competition_slug="zillow-prize-1",
                testcase_id="tc1_from_scratch",
                agent_name="single_llm",
                run_by="agent_runner",
                run_id="try1",
                predicted_add_action_ids=["CA-1"],
                predicted_remove_action_ids=[],
                notes="test run",
                time_spent_seconds=12,
                token_usage={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150},
                trace_text="# trace",
                metadata={
                    "artifact_type": "output_run_metadata",
                    "status": "success",
                    "model_name": "claude-sonnet-4-6",
                    "api_provider": "anthropic",
                    "api_call_count": 1,
                    "tool_call_count": 0,
                    "cost_usd": 0.01,
                    "error_message": None,
                    "notes": "metadata",
                },
            )

            output_payload = json.loads(paths["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(paths["metadata_path"].read_text(encoding="utf-8"))
            trace_exists = paths["trace_path"].exists()
            for path in [paths["output_path"], paths["metadata_path"], paths["trace_path"]]:
                assert_file_ends_with_newline(self, path)

        self.assertEqual(output_payload["agent_name"], "single_llm")
        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(metadata_payload["status"], "success")
        self.assertTrue(trace_exists)

    def test_write_output_bundle_persists_extra_provenance_artifacts(self) -> None:
        output_artifacts = load_output_artifacts_module()

        with tempfile.TemporaryDirectory() as tmp:
            task_dir = Path(tmp)
            (task_dir / "outputs" / "provenance").mkdir(parents=True, exist_ok=True)

            paths = output_artifacts.write_output_bundle(
                task_dir=task_dir,
                competition_slug="zillow-prize-1",
                testcase_id="tc1_from_scratch",
                agent_name="single_llm",
                run_by="agent_runner",
                run_id="try1",
                predicted_add_action_ids=["CA-1"],
                predicted_remove_action_ids=[],
                notes="test run",
                time_spent_seconds=12,
                token_usage={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150},
                trace_text="# trace",
                metadata={
                    "artifact_type": "output_run_metadata",
                    "status": "success",
                    "model_name": "claude-sonnet-4-6",
                    "api_provider": "anthropic",
                    "api_call_count": 1,
                    "tool_call_count": 0,
                    "cost_usd": 0.01,
                    "error_message": None,
                    "notes": "metadata",
                },
                extra_artifacts=[
                    {
                        "kind": "prompt",
                        "filename": "tc1_single_llm_try1.prompt.md",
                        "description": "Prompt text for this run.",
                        "content": "# prompt   ",
                    },
                    {
                        "kind": "stream",
                        "filename": "tc1_single_llm_try1.stream.jsonl",
                        "description": "Stream text for this run.",
                        "content": '{"type":"result"}   ',
                    },
                ],
            )

            output_payload = json.loads(paths["output_path"].read_text(encoding="utf-8"))
            prompt_path = task_dir / "outputs" / output_payload["artifact_refs"][2]["path"]
            stream_path = task_dir / "outputs" / output_payload["artifact_refs"][3]["path"]
            prompt_exists = prompt_path.exists()
            prompt_text = prompt_path.read_text(encoding="utf-8")
            stream_text = stream_path.read_text(encoding="utf-8")

        self.assertEqual(output_payload["artifact_refs"][2]["kind"], "prompt")
        self.assertEqual(output_payload["artifact_refs"][3]["kind"], "stream")
        self.assertTrue(prompt_exists)
        self.assertEqual(prompt_text, "# prompt\n")
        self.assertEqual(stream_text, '{"type":"result"}\n')

    def test_write_failed_provenance_bundle_adds_trailing_newlines(self) -> None:
        output_artifacts = load_output_artifacts_module()

        with tempfile.TemporaryDirectory() as tmp:
            task_dir = Path(tmp)

            paths = output_artifacts.write_failed_provenance_bundle(
                task_dir=task_dir,
                competition_slug="zillow-prize-1",
                testcase_id="tc1_from_scratch",
                agent_name="proposed_agent",
                run_by="agent_runner",
                run_id="try1",
                trace_text="# failed trace",
                metadata={
                    "artifact_type": "failed_output_run_metadata",
                    "status": "failed",
                    "error_message": "failed",
                },
                extra_artifacts=[
                    {
                        "kind": "prompt",
                        "filename": "tc1_proposed_agent_try1.failed.prompt.md",
                        "description": "Prompt text for this failed run.",
                        "content": "# failed prompt",
                    }
                ],
            )

            prompt_path = paths["prompt_path"]
            for path in [paths["metadata_path"], paths["trace_path"], prompt_path]:
                assert_file_ends_with_newline(self, path)
