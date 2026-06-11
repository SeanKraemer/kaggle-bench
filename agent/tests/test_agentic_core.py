from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agent.agentic_core.execution import run_agentic_loop
from agent.agentic_core.request_controls import build_reasoning_controls
from agent.agentic_core.scratchpad import DEFAULT_SCRATCHPAD_MAX_CHARS, JsonScratchpad
from agent.agentic_core.scratchpad_tools import build_scratchpad_tool_specs
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.types import AgenticRunBudget, AgenticToolCall, AgenticToolSpec


class AgenticCoreTests(unittest.TestCase):
    def test_unknown_tool_is_reported_as_error_result(self) -> None:
        runtime = AgenticToolRuntime([])

        result = runtime.call(AgenticToolCall(tool_call_id="toolu_missing", name="missing_tool", input={}))

        self.assertTrue(result.is_error)
        self.assertIn("Unknown tool", result.output_text)

    def test_scratchpad_read_write_and_size_limit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scratchpad.json"
            scratchpad = JsonScratchpad(path, max_chars=80)

            scratchpad.write({"note": "short"})
            self.assertEqual(scratchpad.list_entries(), [{"note": "short"}])

            with self.assertRaises(ValueError):
                scratchpad.write({"note": "x" * 200})

    def test_default_scratchpad_limit_is_shared_constant(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            scratchpad = JsonScratchpad(Path(tmp) / "scratchpad.json")

        self.assertEqual(scratchpad.max_chars, DEFAULT_SCRATCHPAD_MAX_CHARS)

    def test_shared_scratchpad_tool_specs_read_and_write(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            scratchpad = JsonScratchpad(Path(tmp) / "scratchpad.json")
            runtime = AgenticToolRuntime(build_scratchpad_tool_specs(scratchpad=scratchpad))

            runtime.call(
                AgenticToolCall(
                    tool_call_id="toolu_write",
                    name="scratchpad_write",
                    input={"entry": {"note": "shared"}},
                )
            )
            result = runtime.call(AgenticToolCall(tool_call_id="toolu_read", name="scratchpad_read", input={}))

        self.assertEqual(result.output["entries"], [{"note": "shared"}])

    def test_shared_reasoning_controls_match_method_request_behavior(self) -> None:
        thinking, output_config, temperature = build_reasoning_controls(
            reasoning_enabled=True,
            reasoning_effort="medium",
            thinking_type="adaptive",
            thinking_display="summarized",
            temperature=0.2,
        )
        self.assertEqual(thinking, {"type": "adaptive", "display": "summarized"})
        self.assertEqual(output_config, {"effort": "medium"})
        self.assertEqual(temperature, 1.0)

        thinking, output_config, temperature = build_reasoning_controls(
            reasoning_enabled=False,
            temperature=0.2,
        )
        self.assertIsNone(thinking)
        self.assertIsNone(output_config)
        self.assertEqual(temperature, 0.2)

    def test_final_json_exits_loop_successfully(self) -> None:
        runtime = AgenticToolRuntime([])

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=lambda **_: {
                "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                "input_tokens": 1,
                "output_tokens": 2,
            },
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=2, max_tool_calls=1),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "success")
        self.assertEqual(result.api_call_count, 1)
        self.assertEqual(result.parsed_prediction["predicted_add_action_ids"], ["CA-1"])

    def test_tool_call_sequence_feeds_result_back_to_model(self) -> None:
        runtime = AgenticToolRuntime(
            [
                AgenticToolSpec(
                    name="echo",
                    description="Echo input.",
                    input_schema={"type": "object"},
                    handler=lambda payload: {"seen": payload["value"]},
                )
            ]
        )
        calls = []

        def fake_call(**kwargs):
            calls.append(kwargs)
            if len(calls) == 1:
                return {
                    "raw_text": "",
                    "tool_calls": [{"id": "toolu_1", "name": "echo", "input": {"value": 3}}],
                    "input_tokens": 1,
                    "output_tokens": 1,
                }
            return {
                "raw_text": '{"predicted_add_action_ids":[],"predicted_remove_action_ids":[]}',
                "input_tokens": 1,
                "output_tokens": 1,
            }

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=fake_call,
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=3, max_tool_calls=2),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "success")
        self.assertEqual(result.tool_call_count, 1)
        self.assertEqual(result.tool_results[0].output, {"seen": 3})
        self.assertEqual(calls[1]["messages"][-1]["content"][0]["type"], "tool_result")

    def test_capture_llm_calls_records_sanitized_api_payloads(self) -> None:
        runtime = AgenticToolRuntime(
            [
                AgenticToolSpec(
                    name="echo",
                    description="Echo input.",
                    input_schema={"type": "object"},
                    handler=lambda payload: {"seen": payload["value"]},
                )
            ]
        )
        calls = []

        def fake_call(**kwargs):
            calls.append(kwargs)
            if len(calls) == 1:
                return {
                    "raw_text": "",
                    "tool_calls": [{"id": "toolu_1", "name": "echo", "input": {"value": 3}}],
                    "input_tokens": 1,
                    "output_tokens": 1,
                    "stop_reason": "tool_use",
                }
            return {
                "raw_text": '{"predicted_add_action_ids":[],"predicted_remove_action_ids":[]}',
                "input_tokens": 2,
                "output_tokens": 3,
                "stop_reason": "end_turn",
            }

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=[{"type": "text", "text": "system"}],
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking={"type": "disabled"},
            output_config={"format": "json"},
            tool_runtime=runtime,
            call_fn=fake_call,
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=3, max_tool_calls=2),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
            capture_llm_calls=True,
        )

        self.assertEqual(result.status, "success")
        self.assertEqual(len(result.api_call_records), 2)
        first_record = result.api_call_records[0]
        self.assertEqual(first_record["request"]["model"], "test-model")
        self.assertEqual(first_record["request"]["system"][0]["text"], "system")
        self.assertEqual(first_record["request"]["tools"][0]["name"], "echo")
        self.assertEqual(first_record["response"]["tool_calls"][0]["name"], "echo")
        self.assertNotIn("input", first_record["response"]["tool_calls"][0])
        self.assertEqual(first_record["response"]["tool_calls"][0]["input_keys"], ["value"])

        second_messages = result.api_call_records[1]["request"]["messages"]
        assistant_tool_use = second_messages[1]["content"][0]
        tool_result = second_messages[2]["content"][0]
        self.assertEqual(assistant_tool_use["type"], "tool_use")
        self.assertNotIn("input", assistant_tool_use)
        self.assertEqual(tool_result["type"], "tool_result")
        self.assertEqual(tool_result["content_ref"], "see tool_calls.jsonl for full tool output")
        self.assertNotIn("content", tool_result)

    def test_api_call_exception_returns_failed_result_with_capture_record(self) -> None:
        runtime = AgenticToolRuntime([])

        def failing_call(**_):
            raise TimeoutError("read operation timed out")

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=failing_call,
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=2, max_tool_calls=1),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
            capture_llm_calls=True,
        )

        self.assertEqual(result.status, "failed")
        self.assertEqual(result.api_call_count, 1)
        self.assertEqual(result.tool_call_count, 0)
        self.assertIsNone(result.parsed_prediction)
        self.assertEqual(result.turns[0].status, "api_error")
        self.assertIn("TimeoutError", result.error_message)
        self.assertEqual(len(result.api_call_records), 1)
        self.assertEqual(result.api_call_records[0]["response"]["stop_reason"], "api_error")
        self.assertIn(
            "read operation timed out",
            result.api_call_records[0]["response"]["error_message"],
        )
        self.assertEqual(result.token_usage["total_tokens"], 0)

    def test_max_tool_calls_is_enforced(self) -> None:
        runtime = AgenticToolRuntime(
            [
                AgenticToolSpec(
                    name="noop",
                    description="No-op.",
                    input_schema={"type": "object"},
                    handler=lambda _: {},
                )
            ]
        )

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=lambda **_: {
                "raw_text": "",
                "tool_calls": [{"id": "toolu_1", "name": "noop", "input": {}}],
            },
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=1, max_tool_calls=0),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "failed")
        self.assertIn("max tool calls", result.error_message)

    def test_cost_cap_exceeded_aborts_before_tool_execution(self) -> None:
        tool_executions = []
        runtime = AgenticToolRuntime(
            [
                AgenticToolSpec(
                    name="noop",
                    description="No-op.",
                    input_schema={"type": "object"},
                    handler=lambda _: tool_executions.append("called") or {},
                )
            ]
        )

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=lambda **_: {
                "raw_text": "",
                "tool_calls": [{"id": "toolu_1", "name": "noop", "input": {}}],
                "input_tokens": 2_000_000,
                "output_tokens": 0,
            },
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=3, max_tool_calls=3, cost_cap_usd=1.0),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "failed")
        self.assertEqual(result.api_call_count, 1)
        self.assertEqual(result.tool_call_count, 0)
        self.assertEqual(tool_executions, [])
        self.assertEqual(result.turns[0].status, "cost_cap_exceeded")
        self.assertIn("cost cap", result.error_message.lower())

    def test_cost_cap_exceeded_prevents_validation_retry(self) -> None:
        runtime = AgenticToolRuntime([])
        responses = [
            {
                "raw_text": "not json",
                "input_tokens": 2_000_000,
                "output_tokens": 0,
            },
            {
                "raw_text": '{"predicted_add_action_ids":[],"predicted_remove_action_ids":[]}',
                "input_tokens": 1,
                "output_tokens": 1,
            },
        ]

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=lambda **_: responses.pop(0),
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(
                max_turns=3,
                max_tool_calls=0,
                max_validation_retries=1,
                cost_cap_usd=1.0,
            ),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "failed")
        self.assertEqual(result.api_call_count, 1)
        self.assertEqual(len(responses), 1)
        self.assertEqual(result.turns[0].status, "cost_cap_exceeded")
        self.assertIn("validation error", result.error_message)

    def test_cost_cap_exceeded_with_final_json_returns_partial_success(self) -> None:
        runtime = AgenticToolRuntime([])

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=lambda **_: {
                "raw_text": '{"predicted_add_action_ids":["CA-1"],"predicted_remove_action_ids":[]}',
                "input_tokens": 2_000_000,
                "output_tokens": 0,
            },
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=3, max_tool_calls=0, cost_cap_usd=1.0),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "partial_success")
        self.assertEqual(result.parsed_prediction["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(result.turns[0].status, "cost_cap_exceeded")
        self.assertIn("cost cap", result.error_message.lower())

    def test_validation_failure_retries_then_succeeds(self) -> None:
        runtime = AgenticToolRuntime([])
        responses = [
            {"raw_text": "not json"},
            {"raw_text": '{"predicted_add_action_ids":[],"predicted_remove_action_ids":[]}'},
        ]

        result = run_agentic_loop(
            method_name="test_agent",
            phase_name=None,
            prompt_text="prompt",
            system_blocks=None,
            message_content_blocks=None,
            model_name="test-model",
            max_tokens=100,
            temperature=0,
            thinking=None,
            output_config=None,
            tool_runtime=runtime,
            call_fn=lambda **_: responses.pop(0),
            parse_and_validate=lambda text: (json.loads(text), []),
            budget=AgenticRunBudget(max_turns=2, max_tool_calls=0, max_validation_retries=1),
            input_cost_per_million=1,
            output_cost_per_million=1,
            cache_read_cost_per_million=1,
            cache_write_5m_cost_per_million=1,
            cache_write_1h_cost_per_million=1,
        )

        self.assertEqual(result.status, "success")
        self.assertEqual(result.api_call_count, 2)


if __name__ == "__main__":
    unittest.main()
