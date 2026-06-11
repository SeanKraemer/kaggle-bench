from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agent.agentic_core.scratchpad import JsonScratchpad
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.types import AgenticRunBudget
from agent.llm.config import (
    DEFAULT_CACHE_READ_COST_PER_MILLION,
    DEFAULT_CACHE_WRITE_1H_COST_PER_MILLION,
    DEFAULT_CACHE_WRITE_5M_COST_PER_MILLION,
    DEFAULT_INPUT_COST_PER_MILLION,
    DEFAULT_OUTPUT_COST_PER_MILLION,
)
from agent.proposed_agent.controller import run_proposed_agent_controller
from agent.proposed_agent.request_context import build_proposed_agent_request_context
from agent.proposed_agent.tools import build_proposed_tool_specs
from agent.tests.agentic_agent_fixtures import build_proposed_tool_task


class ProposedAgentControllerTests(unittest.TestCase):
    def test_controller_runs_add_then_remove_with_shared_scratchpad(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir, data_root = build_proposed_tool_task(root, context_action_ids=["CA-3"])
            context = build_proposed_agent_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                reasoning_enabled=False,
            )
            scratchpad = JsonScratchpad(root / "scratchpad.json")
            runtime = AgenticToolRuntime(
                build_proposed_tool_specs(
                    materialized=context.materialized,
                    scratchpad=scratchpad,
                )
            )
            calls = []

            def fake_llm(**kwargs):
                calls.append(kwargs)
                if len(calls) == 1:
                    return {
                        "raw_text": "",
                        "tool_calls": [
                            {
                                "id": "toolu_write",
                                "name": "scratchpad_write",
                                "input": {"entry": {"phase": "add", "note": "CA-2 looks useful"}},
                            }
                        ],
                        "input_tokens": 1,
                        "output_tokens": 1,
                    }
                if len(calls) == 2:
                    return {
                        "raw_text": json.dumps(
                            {
                                "phase": "add",
                                "predicted_add_action_ids": ["CA-2"],
                                "predicted_remove_action_ids": [],
                            }
                        ),
                        "input_tokens": 1,
                        "output_tokens": 1,
                    }
                return {
                    "raw_text": json.dumps(
                        {
                            "phase": "remove",
                            "predicted_add_action_ids": [],
                            "predicted_remove_action_ids": ["CA-3"],
                        }
                    ),
                    "input_tokens": 1,
                    "output_tokens": 1,
                }

            result = run_proposed_agent_controller(
                context=context,
                tool_runtime=runtime,
                call_fn=fake_llm,
                model_name="test-model",
                max_tokens=100,
                temperature=0,
                thinking=None,
                output_config=None,
                budget=AgenticRunBudget(max_turns=3, max_tool_calls=2),
                input_cost_per_million=DEFAULT_INPUT_COST_PER_MILLION,
                output_cost_per_million=DEFAULT_OUTPUT_COST_PER_MILLION,
                cache_read_cost_per_million=DEFAULT_CACHE_READ_COST_PER_MILLION,
                cache_write_5m_cost_per_million=DEFAULT_CACHE_WRITE_5M_COST_PER_MILLION,
                cache_write_1h_cost_per_million=DEFAULT_CACHE_WRITE_1H_COST_PER_MILLION,
            )
            scratchpad_entries = scratchpad.read()["entries"]

        self.assertEqual(result.status, "success")
        self.assertEqual(result.parsed_prediction["predicted_add_action_ids"], ["CA-2"])
        self.assertEqual(result.parsed_prediction["predicted_remove_action_ids"], ["CA-3"])
        self.assertEqual(result.add_result.tool_call_count, 1)
        self.assertEqual(scratchpad_entries[0]["phase"], "add")
        self.assertIn('"phase": "add"', calls[2]["prompt_text"])
        self.assertIn("CA-2", calls[2]["prompt_text"])


if __name__ == "__main__":
    unittest.main()
