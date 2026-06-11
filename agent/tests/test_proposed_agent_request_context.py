from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agent.proposed_agent.request_context import build_proposed_agent_request_context
from agent.tests.agentic_agent_fixtures import build_proposed_tool_task


class ProposedAgentRequestContextTests(unittest.TestCase):
    def test_request_context_accepts_profile_cache_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root)
            cache_dir = root / "profile-cache"

            context = build_proposed_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                profile_cache_dir=cache_dir,
                reasoning_enabled=False,
            )

            cache_files_exist = any(cache_dir.iterdir())

        self.assertTrue(cache_files_exist)
        self.assertIn("Primary train profile", context.prompt)

    def test_request_context_uses_single_llm_style_dataset_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            task_dir, data_root = build_proposed_tool_task(Path(tmp))

            context = build_proposed_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                reasoning_enabled=False,
            )

        self.assertIn("Referenced dataset columns in visible actions", context.prompt)
        self.assertIn("Secondary table profiles (referenced columns only):", context.prompt)
        self.assertNotIn("Table profiles:", context.prompt)

    def test_request_context_contains_compact_evidence_and_tool_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            task_dir, data_root = build_proposed_tool_task(Path(tmp))

            context = build_proposed_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                reasoning_enabled=False,
            )

        self.assertIn("Primary train profile", context.prompt)
        self.assertIn("feature_num", context.prompt)
        self.assertIn("lookup_actions", context.prompt)
        self.assertIn("inspect_columns", context.prompt)
        self.assertIn("Do not use bash", context.prompt)
        self.assertIn('"action_id": "CA-1"', context.prompt)
        self.assertIn('"canonical_params"', context.prompt)
        self.assertIn('"left_on": "id"', context.prompt)
        self.assertNotIn("candidate_action_count", context.prompt)
        self.assertNotIn("canonical_param_keys", context.prompt)
        self.assertNotIn("hidden-good", context.prompt)
        self.assertNotIn("hidden-bad", context.prompt)
        self.assertIsNone(context.thinking)
        self.assertIsNone(context.output_config)

    def test_request_context_uses_cacheable_static_system_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            task_dir, data_root = build_proposed_tool_task(Path(tmp))

            context = build_proposed_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                cache_enabled=True,
            )

        self.assertEqual(context.system_blocks[0]["cache_control"]["type"], "ephemeral")
        self.assertIn("[Current context (testcase)]", context.message_content_blocks[0]["text"])
        self.assertNotIn("[Current context (testcase)]", context.system_blocks[0]["text"])
        self.assertEqual(
            sorted(context.benchmark.visible_actions[0]),
            ["action_id", "action_type", "canonical_params"],
        )
        self.assertNotIn("hidden", json.dumps(context.benchmark.visible_actions))


if __name__ == "__main__":
    unittest.main()
