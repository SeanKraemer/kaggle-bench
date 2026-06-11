from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUTH_PATH = ROOT / "agent" / "llm" / "auth.py"


def load_auth_module():
    spec = importlib.util.spec_from_file_location("agent_llm_auth", AUTH_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load auth module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ApiKeyLoadingTests(unittest.TestCase):
    def test_load_api_key_strips_whitespace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            key_path = Path(tmp) / "api_key.txt"
            key_path.write_text("  test-key-123  \n", encoding="utf-8")

            auth = load_auth_module()

            self.assertEqual(auth.load_api_key(key_path), "test-key-123")

    def test_load_api_key_raises_for_blank_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            key_path = Path(tmp) / "api_key.txt"
            key_path.write_text(" \n", encoding="utf-8")

            auth = load_auth_module()

            with self.assertRaisesRegex(ValueError, "empty API key"):
                auth.load_api_key(key_path)
