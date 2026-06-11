from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agent.agentic_core.scratchpad import JsonScratchpad
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.types import AgenticToolCall
from agent.context_builder import build_benchmark_context, materialize_benchmark_context
from agent.proposed_agent.tools import build_proposed_tool_specs
from agent.tests.agentic_agent_fixtures import build_proposed_tool_task


def build_runtime(root: Path) -> AgenticToolRuntime:
    task_dir, data_root = build_proposed_tool_task(root)
    benchmark = build_benchmark_context(
        task_dir=task_dir,
        testcase_id="tc1_from_scratch",
        data_root=data_root,
    )
    materialized = materialize_benchmark_context(benchmark)
    scratchpad = JsonScratchpad(root / "scratchpad.json")
    return AgenticToolRuntime(build_proposed_tool_specs(materialized=materialized, scratchpad=scratchpad))


class ProposedAgentToolTests(unittest.TestCase):
    def test_tool_allowlist_excludes_generic_tools(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime = build_runtime(Path(tmp))

            names = runtime.list_tool_names()

        self.assertNotIn("bash", names)
        self.assertNotIn("python", names)
        self.assertIn("lookup_actions", names)
        self.assertIn("inspect_columns", names)
        self.assertIn("scratchpad_write", names)

    def test_lookup_actions_filters_and_hides_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime = build_runtime(Path(tmp))

            result = runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_lookup",
                    name="lookup_actions",
                    input={
                        "action_type": "IMPUTE_MISSING",
                        "column": "feature_num",
                        "active_state": "inactive",
                    },
                )
            )

        self.assertFalse(result.is_error)
        self.assertEqual(result.output["match_count"], 1)
        self.assertEqual(result.output["actions"][0]["action_id"], "CA-2")
        self.assertEqual(
            sorted(result.output["actions"][0]),
            ["action_id", "action_type", "canonical_params"],
        )
        self.assertNotIn("hidden", json.dumps(result.output))

    def test_context_summary_exposes_visible_fields_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime = build_runtime(Path(tmp))

            result = runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_context",
                    name="summarize_context_actions",
                    input={},
                )
            )

        self.assertEqual(result.output["context_action_ids"], ["CA-3"])
        self.assertEqual(result.output["actions"][0]["action_id"], "CA-3")
        self.assertNotIn("role", result.output["actions"][0])
        self.assertNotIn("hidden-bad", json.dumps(result.output))

    def test_dataset_profile_tools_return_bounded_structured_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime = build_runtime(Path(tmp))

            tables = runtime.call(AgenticToolCall("toolu_tables", "inspect_dataset_tables", {})).output
            columns = runtime.call(
                AgenticToolCall(
                    "toolu_columns",
                    "inspect_columns",
                    {"columns": ["feature_num", "date", "cat"]},
                )
            ).output
            preview = runtime.call(
                AgenticToolCall(
                    "toolu_preview",
                    "preview_rows",
                    {"table_name": "train.csv", "columns": ["id", "cat"], "limit": 1},
                )
            ).output
            target = runtime.call(AgenticToolCall("toolu_target", "profile_target_distribution", {})).output
            join = runtime.call(AgenticToolCall("toolu_join", "profile_join_key", {"action_id": "CA-1"})).output

        self.assertEqual(len(tables["tables"]), 2)
        self.assertIn("feature_num", columns["tables"][0]["columns"])
        self.assertIn("datetime", columns["tables"][0]["columns"]["date"])
        self.assertEqual(preview["rows"], [{"id": "1", "cat": "a"}])
        self.assertEqual(target["target_column"], "target")
        self.assertEqual(join["left_key_columns"], ["id"])

    def test_scratchpad_tools_share_state(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime = build_runtime(Path(tmp))

            runtime.call(
                AgenticToolCall(
                    "toolu_write",
                    "scratchpad_write",
                    {"entry": {"phase": "add", "note": "check imputation"}},
                )
            )
            result = runtime.call(AgenticToolCall("toolu_read", "scratchpad_read", {}))

        self.assertEqual(
            result.output["entries"],
            [{"phase": "add", "note": "check imputation"}],
        )


if __name__ == "__main__":
    unittest.main()
