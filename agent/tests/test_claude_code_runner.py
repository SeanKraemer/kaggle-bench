from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "agent" / "claude_code" / "runner.py"
WORKSPACE_PATH = ROOT / "agent" / "claude_code" / "workspace.py"


def load_runner_module():
    spec = importlib.util.spec_from_file_location("agent_claude_code_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load claude_code runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_workspace_module():
    spec = importlib.util.spec_from_file_location("agent_claude_code_workspace", WORKSPACE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load claude_code workspace helpers")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def assert_file_ends_with_newline(testcase: unittest.TestCase, path: Path) -> None:
    payload = path.read_bytes()
    testcase.assertTrue(payload, f"{path} should not be empty")
    testcase.assertEqual(payload[-1:], b"\n", f"{path} should end with a newline")


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
                }
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
        "parcelid,logerror,transactiondate\n1,0.1,2016-10-01\n",
    )
    write_text(
        data_root / "properties_2016.csv",
        "parcelid,feature_num\n1,10\n",
    )
    return data_root


class ClaudeCodeRunnerTests(unittest.TestCase):
    def test_prepare_claude_workspace_writes_prompt_and_dataset_symlink(self) -> None:
        workspace = load_workspace_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dataset_root = root / "dataset-root"
            dataset_root.mkdir(parents=True, exist_ok=True)

            workdir = workspace.prepare_claude_workspace(
                task_goal="Solve the benchmark instance.",
                testcase={"testcase_id": "tc1"},
                visible_actions=[{"action_id": "CA-1", "action_type": "JOIN_LOOKUP", "canonical_params": {}}],
                prompt="[TASK]\n...",
                dataset_root=dataset_root,
            )
            try:
                self.assertEqual(workdir, workdir.resolve())
                self.assertTrue((workdir / ".claude-home").is_dir())
                self.assertTrue((workdir / "dataset").is_symlink())
                self.assertEqual((workdir / "dataset").resolve(), dataset_root.resolve())
                self.assertEqual((workdir / "TASK.md").read_text(encoding="utf-8"), "Solve the benchmark instance.")
                self.assertIn("tc1", (workdir / "testcase.json").read_text(encoding="utf-8"))
                self.assertIn("CA-1", (workdir / "candidate_actions_visible.json").read_text(encoding="utf-8"))
                self.assertEqual((workdir / "PROMPT.md").read_text(encoding="utf-8"), "[TASK]\n...")
                self.assertFalse((workdir / "dataset_summary.json").exists())
            finally:
                if workdir.exists():
                    import shutil

                    shutil.rmtree(workdir)

    def test_run_claude_code_packages_workspace_and_writes_artifact(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            captured = {}

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                captured["workdir"] = workdir
                captured["command"] = command
                captured["env"] = env
                captured["prompt_exists"] = (workdir / "PROMPT.md").exists()
                captured["task_exists"] = (workdir / "TASK.md").exists()
                captured["dataset_symlink_exists"] = (workdir / "dataset").is_symlink()
                captured["dataset_symlink_target"] = (workdir / "dataset").resolve()
                captured["candidate_actions_payload"] = json.loads(
                    (workdir / "candidate_actions_visible.json").read_text(encoding="utf-8")
                )
                prediction_path = workdir / "prediction.json"
                prediction_path.write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                        }
                    ),
                    encoding="utf-8",
                )
                return {
                    "returncode": 0,
                    "stdout": json.dumps(
                        {
                            "type": "result",
                            "total_cost_usd": 0.0123,
                            "usage": {
                                "input_tokens": 111,
                                "output_tokens": 22,
                                "cache_creation_input_tokens": 33,
                                "cache_read_input_tokens": 44,
                            },
                        }
                    ),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            result = runner.run_claude_code(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
                executor=fake_executor,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))
            prompt_text = result["prompt_path"].read_text(encoding="utf-8")
            prompt_exists = result["prompt_path"].exists()

        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(
            output_payload["token_usage"],
            {"input_tokens": 111, "output_tokens": 22, "total_tokens": 133},
        )
        self.assertEqual(metadata_payload["status"], "success")
        self.assertEqual(metadata_payload["cost_usd"], 0.0123)
        self.assertIn("claude", " ".join(captured["command"]).lower())
        self.assertIn("--verbose", captured["command"])
        self.assertIn("--permission-mode", captured["command"])
        self.assertIn("bypassPermissions", captured["command"])
        self.assertIn(f"--add-dir={captured['workdir']}", captured["command"])
        self.assertIn(f"--add-dir={data_root.resolve()}", captured["command"])
        self.assertNotIn("--add-dir", captured["command"])
        self.assertTrue(captured["command"][-1].startswith("[TASK]"))
        self.assertIn("HOME", captured["env"])
        self.assertNotIn("ANTHROPIC_API_KEY", captured["env"])
        self.assertNotEqual(captured["env"]["HOME"], str(captured["workdir"] / ".claude-home"))
        self.assertTrue(captured["prompt_exists"])
        self.assertTrue(captured["task_exists"])
        self.assertTrue(captured["dataset_symlink_exists"])
        self.assertEqual(captured["dataset_symlink_target"], data_root.resolve())
        self.assertTrue(prompt_exists)
        self.assertIn("prediction.json", prompt_text)
        self.assertIn("`dataset`", prompt_text)
        self.assertIn("No precomputed dataset summary is provided", prompt_text)
        self.assertEqual(output_payload["artifact_refs"][2]["kind"], "prompt")
        self.assertEqual(
            captured["candidate_actions_payload"],
            [{"action_id": "CA-1", "action_type": "JOIN_LOOKUP", "canonical_params": {"how": "left", "right_table_id": "properties_2016"}}],
        )

    def test_run_claude_code_persists_failure_provenance_for_invalid_prediction_text(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            captured = {}

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                captured["workdir"] = workdir
                return {
                    "returncode": 0,
                    "stdout": json.dumps(
                        {
                            "type": "result",
                            "result": "done, but not json",
                            "total_cost_usd": 0.01,
                            "usage": {
                                "input_tokens": 10,
                                "output_tokens": 5,
                            },
                        }
                    ),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            with self.assertRaises(json.JSONDecodeError):
                runner.run_claude_code(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="try1",
                    data_root=data_root,
                    executor=fake_executor,
                )

            provenance_dir = task_dir / "outputs" / "provenance"
            metadata_payload = json.loads(
                (provenance_dir / "tc1_claude_code_try1.meta.json").read_text(encoding="utf-8")
            )
            metadata_path = provenance_dir / "tc1_claude_code_try1.meta.json"
            trace_path = provenance_dir / "tc1_claude_code_try1.trace.md"
            prompt_path = provenance_dir / "tc1_claude_code_try1.prompt.md"
            stream_path = provenance_dir / "tc1_claude_code_try1.stream.jsonl"
            raw_prediction_path = provenance_dir / "tc1_claude_code_try1.raw_prediction.txt"
            trace_text = trace_path.read_text(encoding="utf-8")
            prompt_text = prompt_path.read_text(encoding="utf-8")
            stream_text = stream_path.read_text(encoding="utf-8")
            raw_prediction_text = raw_prediction_path.read_text(encoding="utf-8")
            output_exists = (task_dir / "outputs" / "tc1_claude_code_try1.json").exists()
            workdir_exists = captured["workdir"].exists()
            for path in [metadata_path, trace_path, prompt_path, stream_path, raw_prediction_path]:
                assert_file_ends_with_newline(self, path)

        self.assertEqual(metadata_payload["status"], "failed")
        self.assertIn("Expecting value", metadata_payload["error_message"])
        self.assertIn("## Failure", trace_text)
        self.assertIn("## Raw Prediction Text", trace_text)
        self.assertIn("done, but not json", raw_prediction_text)
        self.assertIn("prediction.json", prompt_text)
        self.assertIn('"result": "done, but not json"', stream_text)
        self.assertFalse(output_exists)
        self.assertTrue(workdir_exists)

    def test_run_claude_code_rejects_api_key_auth_mode_without_explicit_override(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            with self.assertRaises(PermissionError) as context:
                runner.run_claude_code(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="api_try1",
                    data_root=data_root,
                    auth_mode="api_key",
                    api_key_path=api_key_path,
                    executor=lambda **_: None,
                )

        self.assertIn("subscription auth by default", str(context.exception))
        self.assertIn("allow_api_key_override=True", str(context.exception))
        self.assertIn("CLAUDE_CODE_ALLOW_API_KEY=1", str(context.exception))

    def test_run_claude_code_rejects_api_key_auth_mode_without_env_flag(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")

            with patch.dict(os.environ, {}, clear=False):
                os.environ.pop("CLAUDE_CODE_ALLOW_API_KEY", None)
                with self.assertRaises(PermissionError) as context:
                    runner.run_claude_code(
                        task_dir=task_dir,
                        testcase_id="tc1_from_scratch",
                        run_id="api_try1",
                        data_root=data_root,
                        auth_mode="api_key",
                        allow_api_key_override=True,
                        api_key_path=api_key_path,
                        executor=lambda **_: None,
                    )

        self.assertIn("CLAUDE_CODE_ALLOW_API_KEY=1", str(context.exception))

    def test_run_claude_code_supports_explicit_api_key_auth_mode(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            captured = {}

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                captured["workdir"] = workdir
                captured["env"] = env
                (workdir / "prediction.json").write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                        }
                    ),
                    encoding="utf-8",
                )
                return {
                    "returncode": 0,
                    "stdout": json.dumps({"type": "result", "usage": {"input_tokens": 1, "output_tokens": 1}}),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            with patch.dict(os.environ, {"CLAUDE_CODE_ALLOW_API_KEY": "1"}, clear=False):
                runner.run_claude_code(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="api_try1",
                    data_root=data_root,
                    auth_mode="api_key",
                    allow_api_key_override=True,
                    api_key_path=api_key_path,
                    executor=fake_executor,
                )

        self.assertEqual(captured["env"]["ANTHROPIC_API_KEY"], "test-anthropic-key")
        self.assertEqual(captured["env"]["HOME"], str(captured["workdir"] / ".claude-home"))

    def test_run_claude_code_rejects_unknown_auth_mode(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)

            with self.assertRaises(ValueError) as context:
                runner.run_claude_code(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="bad_auth_try1",
                    data_root=data_root,
                    auth_mode="bogus",
                    executor=lambda **_: None,
                )

        self.assertIn("Unsupported Claude Code auth_mode", str(context.exception))

    def test_run_claude_code_requires_api_key_when_api_auth_is_selected(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            missing_key_path = root / "missing_api_key.txt"

            with patch.dict(os.environ, {"CLAUDE_CODE_ALLOW_API_KEY": "1"}, clear=False):
                with self.assertRaises(FileNotFoundError):
                    runner.run_claude_code(
                        task_dir=task_dir,
                        testcase_id="tc1_from_scratch",
                        run_id="missing_key_try1",
                        data_root=data_root,
                        auth_mode="api_key",
                        allow_api_key_override=True,
                        api_key_path=missing_key_path,
                        executor=lambda **_: None,
                    )

    def test_run_claude_code_persists_stream_events_and_trace_summary(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            captured = {}

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                captured["command"] = command
                prediction_path = workdir / "prediction.json"
                prediction_path.write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                        }
                    ),
                    encoding="utf-8",
                )
                stream_lines = [
                    json.dumps(
                        {
                            "type": "system",
                            "subtype": "init",
                            "tools": ["Read", "Write"],
                            "model": "claude-sonnet-4-6",
                        }
                    ),
                    json.dumps(
                        {
                            "type": "stream_event",
                            "event": {
                                "type": "content_block_start",
                                "index": 0,
                                "content_block": {
                                    "type": "thinking",
                                    "thinking": "Inspect files",
                                },
                            },
                        }
                    ),
                    json.dumps(
                        {
                            "type": "stream_event",
                            "event": {
                                "type": "content_block_delta",
                                "index": 0,
                                "delta": {
                                    "type": "thinking_delta",
                                    "thinking": " then write output",
                                },
                            },
                        }
                    ),
                    json.dumps(
                        {
                            "type": "assistant",
                            "message": {
                                "role": "assistant",
                                "content": [
                                    {
                                        "type": "tool_use",
                                        "id": "toolu_123",
                                        "name": "Bash",
                                        "input": {
                                            "command": "python analyze.py --limit 1000",
                                            "description": "Analyze dataset sample",
                                        },
                                    }
                                ],
                            },
                        }
                    ),
                    json.dumps(
                        {
                            "type": "user",
                            "message": {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "tool_result",
                                        "tool_use_id": "toolu_123",
                                        "content": "rows=1000\nmissing_rate=0.42",
                                        "is_error": False,
                                    }
                                ],
                            },
                        }
                    ),
                    json.dumps(
                        {
                            "type": "assistant",
                            "message": {
                                "role": "assistant",
                                "content": [{"type": "text", "text": "Prepared prediction.json"}],
                            },
                        }
                    ),
                    json.dumps(
                        {
                            "type": "result",
                            "subtype": "success",
                            "is_error": False,
                            "num_turns": 3,
                            "result": "Prepared prediction.json",
                            "total_cost_usd": 0.045,
                            "usage": {
                                "input_tokens": 10,
                                "output_tokens": 20,
                                "cache_creation_input_tokens": 30,
                                "cache_read_input_tokens": 40,
                            },
                            "modelUsage": {
                                "claude-sonnet-4-6": {
                                    "inputTokens": 10,
                                    "outputTokens": 20,
                                }
                            },
                            "permission_denials": [
                                {"tool_name": "Bash", "tool_use_id": "toolu_denied"}
                            ],
                        }
                    ),
                ]
                return {
                    "returncode": 0,
                    "stdout": "\n".join(stream_lines) + "\n",
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            result = runner.run_claude_code(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try2",
                data_root=data_root,
                executor=fake_executor,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")
            stream_text = result["stream_path"].read_text(encoding="utf-8")

        self.assertIn("stream-json", captured["command"])
        self.assertIn("--verbose", captured["command"])
        self.assertIn("--include-partial-messages", captured["command"])
        self.assertEqual(output_payload["artifact_refs"][3]["kind"], "stream")
        self.assertEqual(metadata_payload["tool_call_count"], 1)
        self.assertEqual(metadata_payload["cost_usd"], 0.045)
        self.assertEqual(
            metadata_payload["usage_detail"],
            {
                "input_tokens": 10,
                "output_tokens": 20,
                "cache_creation_input_tokens": 30,
                "cache_read_input_tokens": 40,
            },
        )
        self.assertEqual(
            metadata_payload["permission_denials"],
            [{"tool_name": "Bash", "tool_use_id": "toolu_denied"}],
        )
        self.assertIn("## Tool Calls", trace_text)
        self.assertIn("Bash", trace_text)
        self.assertIn("python analyze.py --limit 1000", trace_text)
        self.assertIn("rows=1000", trace_text)
        self.assertIn("## Thinking", trace_text)
        self.assertIn("Inspect files then write output", trace_text)
        self.assertIn("## Raw Event Counts", trace_text)
        self.assertIn('"type": "result"', stream_text)

    def test_run_claude_code_validates_prediction_payload(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                (workdir / "prediction.json").write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1", "CA-1", "CA-999"],
                            "predicted_remove_action_ids": ["CA-1"],
                        }
                    ),
                    encoding="utf-8",
                )
                return {
                    "returncode": 0,
                    "stdout": json.dumps({"type": "result", "usage": {"input_tokens": 1, "output_tokens": 1}}),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            result = runner.run_claude_code(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="validated_try1",
                data_root=data_root,
                executor=fake_executor,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")

        self.assertEqual(output_payload["predicted_add_action_ids"], [])
        self.assertEqual(output_payload["predicted_remove_action_ids"], [])
        self.assertIn("Validation warnings", trace_text)
        self.assertIn("unknown_add_action_ids=['CA-999']", trace_text)

    def test_run_claude_code_raises_on_non_zero_exit_even_if_prediction_exists(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                (workdir / "prediction.json").write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                        }
                    ),
                    encoding="utf-8",
                )
                return {
                    "returncode": 1,
                    "stdout": json.dumps({"type": "result", "usage": {"input_tokens": 1, "output_tokens": 1}}),
                    "stderr": "permission denied",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            with self.assertRaises(RuntimeError) as context:
                runner.run_claude_code(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="failed_try1",
                    data_root=data_root,
                    executor=fake_executor,
                )

        self.assertIn("Claude Code exited with code 1", str(context.exception))

    def test_run_claude_code_falls_back_to_final_result_when_prediction_file_is_missing(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                fallback_result = (
                    "Unable to write the file directly. Here is the final prediction:\n"
                    "```json\n"
                    "{\n"
                    '  "predicted_add_action_ids": ["CA-1"],\n'
                    '  "predicted_remove_action_ids": []\n'
                    "}\n"
                    "```"
                )
                return {
                    "returncode": 0,
                    "stdout": json.dumps(
                        {
                            "type": "result",
                            "result": fallback_result,
                            "usage": {"input_tokens": 1, "output_tokens": 1},
                        }
                    ),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            result = runner.run_claude_code(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="fallback_try1",
                data_root=data_root,
                executor=fake_executor,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))

        self.assertEqual(output_payload["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(output_payload["predicted_remove_action_ids"], [])

    def test_run_claude_code_adds_max_thinking_tokens_when_requested(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            captured = {}

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                captured["command"] = command
                captured["env"] = env
                (workdir / "prediction.json").write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                        }
                    ),
                    encoding="utf-8",
                )
                return {
                    "returncode": 0,
                    "stdout": json.dumps({"type": "result", "usage": {"input_tokens": 1, "output_tokens": 1}}),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            runner.run_claude_code(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="thinking_try1",
                data_root=data_root,
                max_thinking_tokens=4096,
                executor=fake_executor,
            )

        self.assertIn("--max-thinking-tokens", captured["command"])
        self.assertIn("4096", captured["command"])

    def test_run_claude_code_defaults_to_sonnet_4_6_adaptive_thinking(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            captured = {}

            def fake_executor(*, workdir: Path, command: list[str], env: dict[str, str]):
                captured["command"] = command
                captured["env"] = env
                (workdir / "prediction.json").write_text(
                    json.dumps(
                        {
                            "predicted_add_action_ids": ["CA-1"],
                            "predicted_remove_action_ids": [],
                        }
                    ),
                    encoding="utf-8",
                )
                return {
                    "returncode": 0,
                    "stdout": json.dumps({"type": "result", "usage": {"input_tokens": 1, "output_tokens": 1}}),
                    "stderr": "",
                    "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                    "cost_usd": None,
                }

            runner.run_claude_code(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="default_adaptive_try1",
                data_root=data_root,
                executor=fake_executor,
            )

        self.assertIn("--model", captured["command"])
        self.assertIn("claude-sonnet-4-6", captured["command"])
        self.assertNotIn("--max-thinking-tokens", captured["command"])
        self.assertEqual(captured["env"]["CLAUDE_CODE_EFFORT_LEVEL"], "auto")
        self.assertNotIn("ANTHROPIC_API_KEY", captured["env"])
        self.assertNotIn("MAX_THINKING_TOKENS", captured["env"])
        self.assertNotIn("CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING", captured["env"])

    def test_run_claude_code_raises_clear_error_when_dataset_is_missing(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            api_key_path = root / "api_key.txt"
            api_key_path.write_text("test-anthropic-key\n", encoding="utf-8")
            missing_data_root = root / "missing-dataset"

            with self.assertRaises(FileNotFoundError) as context:
                runner.run_claude_code(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="missing_dataset_try1",
                    data_root=missing_data_root,
                    api_key_path=api_key_path,
                    executor=lambda **_: None,
                )

        self.assertIn("Please provide the real dataset files and rerun", str(context.exception))
        self.assertIn(str(missing_data_root.resolve()), str(context.exception))
