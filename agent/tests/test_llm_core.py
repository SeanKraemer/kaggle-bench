from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRICING_PATH = ROOT / "agent" / "llm" / "pricing.py"
GUARDS_PATH = ROOT / "agent" / "llm" / "guards.py"
TELEMETRY_PATH = ROOT / "agent" / "llm" / "telemetry.py"
ANTHROPIC_PATH = ROOT / "agent" / "llm" / "anthropic_client.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PricingTests(unittest.TestCase):
    def test_estimate_cost_uses_input_and_output_token_rates(self) -> None:
        pricing = load_module(PRICING_PATH, "agent_llm_pricing")

        cost = pricing.estimate_cost_usd(
            input_tokens=1000,
            output_tokens=500,
            input_cost_per_million=3.0,
            output_cost_per_million=15.0,
        )

        self.assertAlmostEqual(cost, 0.0105, places=6)

    def test_estimate_cost_includes_cache_reads_and_writes(self) -> None:
        pricing = load_module(PRICING_PATH, "agent_llm_pricing")

        cost = pricing.estimate_cost_usd(
            input_tokens=1000,
            output_tokens=500,
            input_cost_per_million=3.0,
            output_cost_per_million=15.0,
            cache_read_input_tokens=4000,
            cache_creation={"ephemeral_5m_input_tokens": 8000, "ephemeral_1h_input_tokens": 2000},
            cache_read_cost_per_million=0.3,
            cache_write_5m_cost_per_million=3.75,
            cache_write_1h_cost_per_million=6.0,
        )

        self.assertAlmostEqual(cost, 0.0537, places=6)


class GuardTests(unittest.TestCase):
    def test_enforce_cost_cap_raises_when_cap_exceeded(self) -> None:
        guards = load_module(GUARDS_PATH, "agent_llm_guards")

        with self.assertRaises(guards.CostCapExceeded):
            guards.enforce_cost_cap(current_cost_usd=1.01, cost_cap_usd=1.0)


class TelemetryTests(unittest.TestCase):
    def test_build_trace_entry_captures_status_and_usage(self) -> None:
        telemetry = load_module(TELEMETRY_PATH, "agent_llm_telemetry")

        entry = telemetry.build_trace_entry(
            attempt_index=1,
            status="success",
            prompt_text="hello",
            response_text="world",
            input_tokens=10,
            output_tokens=20,
            cost_usd=0.001,
        )

        self.assertEqual(entry["attempt_index"], 1)
        self.assertEqual(entry["status"], "success")
        self.assertEqual(entry["usage"]["total_tokens"], 30)

    def test_render_trace_markdown_shows_thinking_and_cache_usage(self) -> None:
        telemetry = load_module(TELEMETRY_PATH, "agent_llm_telemetry")

        trace = telemetry.render_trace_markdown(
            "title",
            [
                telemetry.build_trace_entry(
                    attempt_index=1,
                    status="success",
                    prompt_text="prompt",
                    response_text="response",
                    input_tokens=10,
                    output_tokens=20,
                    cost_usd=0.001,
                    thinking_summaries=["First think", "Second think"],
                    cache_usage={
                        "cache_creation_input_tokens": 100,
                        "cache_read_input_tokens": 200,
                        "cache_creation": {"ephemeral_5m_input_tokens": 100},
                    },
                )
            ],
        )

        self.assertIn("### Thinking Summary", trace)
        self.assertIn("First think", trace)
        self.assertIn("### Cache Usage", trace)
        self.assertIn("cache_read_input_tokens", trace)


class AnthropicClientTests(unittest.TestCase):
    def test_parse_messages_response_extracts_text_and_usage(self) -> None:
        anthropic = load_module(ANTHROPIC_PATH, "agent_llm_anthropic")

        payload = {
            "id": "msg_123",
            "content": [
                {"type": "thinking", "thinking": "Let me reason."},
                {"type": "text", "text": "{\"predicted_add_action_ids\": [], \"predicted_remove_action_ids\": []}"}
            ],
            "usage": {
                "input_tokens": 100,
                "output_tokens": 20,
                "cache_creation_input_tokens": 500,
                "cache_read_input_tokens": 1000,
                "cache_creation": {
                    "ephemeral_5m_input_tokens": 500,
                },
            },
        }

        parsed = anthropic.parse_messages_response(payload)

        self.assertEqual(parsed["raw_text"], payload["content"][1]["text"])
        self.assertEqual(parsed["input_tokens"], 100)
        self.assertEqual(parsed["output_tokens"], 20)
        self.assertEqual(parsed["thinking_summaries"], ["Let me reason."])
        self.assertEqual(parsed["cache_read_input_tokens"], 1000)
        self.assertEqual(parsed["cache_creation"]["ephemeral_5m_input_tokens"], 500)

    def test_build_messages_request_contains_model_and_prompt(self) -> None:
        anthropic = load_module(ANTHROPIC_PATH, "agent_llm_anthropic")

        request = anthropic.build_messages_request(
            model_name="claude-sonnet-4-6",
            prompt_text="solve task",
            max_tokens=512,
            temperature=0.2,
        )

        body = json.loads(request["body"].decode("utf-8"))
        self.assertEqual(body["model"], "claude-sonnet-4-6")
        self.assertEqual(body["messages"][0]["content"], "solve task")

    def test_build_messages_request_supports_thinking_and_cacheable_blocks(self) -> None:
        anthropic = load_module(ANTHROPIC_PATH, "agent_llm_anthropic")

        request = anthropic.build_messages_request(
            model_name="claude-sonnet-4-6",
            prompt_text="unused",
            max_tokens=512,
            temperature=0.0,
            system_blocks=[
                {
                    "type": "text",
                    "text": "static instructions",
                    "cache_control": {"type": "ephemeral", "ttl": "5m"},
                }
            ],
            message_content_blocks=[
                {
                    "type": "text",
                    "text": "dynamic context",
                }
            ],
            thinking={"type": "adaptive", "display": "summarized"},
            output_config={"effort": "high"},
        )

        body = json.loads(request["body"].decode("utf-8"))
        self.assertEqual(body["thinking"]["type"], "adaptive")
        self.assertEqual(body["thinking"]["display"], "summarized")
        self.assertEqual(body["output_config"]["effort"], "high")
        self.assertEqual(body["system"][0]["cache_control"]["type"], "ephemeral")
        self.assertEqual(body["messages"][0]["content"][0]["text"], "dynamic context")

    def test_send_messages_request_passes_timeout_to_urlopen(self) -> None:
        anthropic = load_module(ANTHROPIC_PATH, "agent_llm_anthropic")
        captured = {}

        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

            def read(self):
                return json.dumps(
                    {
                        "content": [{"type": "text", "text": "{}"}],
                        "usage": {"input_tokens": 1, "output_tokens": 1},
                    }
                ).encode("utf-8")

        def fake_urlopen(request_obj, timeout=None):
            captured["timeout"] = timeout
            return FakeResponse()

        anthropic.send_messages_request(
            api_key="test-key",
            model_name="claude-sonnet-4-6",
            prompt_text="solve task",
            max_tokens=256,
            temperature=0.0,
            timeout_seconds=42,
            urlopen=fake_urlopen,
        )

        self.assertEqual(captured["timeout"], 42)
