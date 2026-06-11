from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLIENT_PATH = ROOT / "agent" / "llm" / "client.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LLMClientTests(unittest.TestCase):
    def test_anthropic_llm_call_forwards_request_fields(self) -> None:
        client = load_module(CLIENT_PATH, "agent_llm_client")
        captured = {}

        def fake_send(**kwargs):
            captured.update(kwargs)
            return {"raw_text": "{}", "input_tokens": 1, "output_tokens": 2, "total_tokens": 3}

        response = client.anthropic_llm_call(
            api_key="test-key",
            model_name="claude-sonnet-4-6",
            prompt_text="solve task",
            max_tokens=512,
            temperature=1.0,
            system_blocks=[{"type": "text", "text": "system"}],
            message_content_blocks=[{"type": "text", "text": "user"}],
            thinking={"type": "adaptive"},
            output_config={"effort": "medium"},
            timeout_seconds=42,
            send_fn=fake_send,
        )

        self.assertEqual(captured["api_key"], "test-key")
        self.assertEqual(captured["model_name"], "claude-sonnet-4-6")
        self.assertEqual(captured["prompt_text"], "solve task")
        self.assertEqual(captured["system_blocks"][0]["text"], "system")
        self.assertEqual(captured["timeout_seconds"], 42)
        self.assertEqual(response["total_tokens"], 3)

    def test_build_llm_caller_binds_api_key_for_anthropic_provider(self) -> None:
        client = load_module(CLIENT_PATH, "agent_llm_client")
        captured = {}

        def fake_send(**kwargs):
            captured.update(kwargs)
            return {"raw_text": "{}", "input_tokens": 2, "output_tokens": 3, "total_tokens": 5}

        caller = client.build_llm_caller(
            provider="anthropic",
            api_key="bound-key",
            send_fn=fake_send,
        )
        response = caller(
            model_name="claude-sonnet-4-6",
            prompt_text="hello",
            max_tokens=256,
            temperature=0.0,
        )

        self.assertEqual(captured["api_key"], "bound-key")
        self.assertEqual(captured["prompt_text"], "hello")
        self.assertEqual(response["input_tokens"], 2)
        self.assertNotIn("api_key", caller.__code__.co_varnames)

    def test_build_llm_caller_rejects_unknown_provider(self) -> None:
        client = load_module(CLIENT_PATH, "agent_llm_client")

        with self.assertRaises(ValueError):
            client.build_llm_caller(provider="unknown", api_key="test-key")


if __name__ == "__main__":
    unittest.main()
