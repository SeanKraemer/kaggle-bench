from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from agent.generic_agent.request_context import build_generic_agent_request_context
from agent.generic_agent.workspace import prepare_generic_workspace


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_temp_task_bundle(root: Path) -> Path:
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
                    "role": "hidden",
                    "reasoning": "hidden",
                }
            ]
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "zillow-prize-1",
            "input": {"scenario": "from_scratch", "context_action_ids": []},
        },
    )
    return task_dir


def build_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(data_root / "train.csv", "id,target\n1,0\n")
    write_text(data_root / "lookup.csv", "id,x\n1,2\n")
    return data_root


class GenericAgentWorkspaceTests(unittest.TestCase):
    def test_prepare_generic_workspace_writes_expected_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dataset_root = build_data_root(root)
            workspace = prepare_generic_workspace(
                task_goal="Solve task.",
                testcase={"testcase_id": "tc1"},
                visible_actions=[
                    {"action_id": "CA-1", "action_type": "JOIN_LOOKUP", "canonical_params": {}}
                ],
                prompt="prompt",
                dataset_root=dataset_root,
            )
            try:
                self.assertTrue(workspace.dataset_path.is_symlink())
                self.assertEqual(workspace.dataset_path.resolve(), dataset_root.resolve())
                self.assertTrue((workspace.workdir / "TASK.md").exists())
                self.assertTrue((workspace.workdir / "testcase.json").exists())
                self.assertTrue((workspace.workdir / "candidate_actions_visible.json").exists())
                self.assertTrue((workspace.workdir / "output_schema.json").exists())
                self.assertTrue((workspace.workdir / "PROMPT.md").exists())
                self.assertTrue(workspace.scratchpad_path.exists())
                self.assertEqual(workspace.prediction_path.name, "prediction.json")
                self.assertFalse((workspace.workdir / "agent").exists())
            finally:
                shutil.rmtree(workspace.workdir)

    def test_request_context_visible_actions_exclude_hidden_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_data_root(root)

            context = build_generic_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

        self.assertEqual(
            context.benchmark.visible_actions,
            [{"action_id": "CA-1", "action_type": "JOIN_LOOKUP", "canonical_params": {"how": "left"}}],
        )
        self.assertNotIn("role", context.benchmark.candidate_actions_json)
        self.assertNotIn("reasoning", context.benchmark.candidate_actions_json)

    def test_request_context_prompt_uses_full_visible_action_bank(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            action_bank_path = task_dir / "candidate_actions.json"
            payload = json.loads(action_bank_path.read_text(encoding="utf-8"))
            long_expression = "very_long_expression_payload_" * 200
            payload["actions"][0]["canonical_params"]["expression"] = long_expression
            write_json(action_bank_path, payload)
            data_root = build_data_root(root)

            context = build_generic_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

        self.assertIn(long_expression, context.benchmark.candidate_actions_json)
        self.assertIn(long_expression, context.prompt)
        self.assertIn(long_expression, context.system_blocks[0]["text"])
        self.assertIn('"canonical_params"', context.prompt)
        self.assertNotIn('"candidate_action_count"', context.prompt)
        self.assertNotIn('"canonical_param_keys"', context.prompt)
        self.assertNotIn("role", context.prompt)
        self.assertNotIn("reasoning", context.prompt)


if __name__ == "__main__":
    unittest.main()
