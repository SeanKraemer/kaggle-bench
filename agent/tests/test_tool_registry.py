from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "agent" / "tool_registry.py"


def load_module():
    spec = importlib.util.spec_from_file_location("agent_tool_registry", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load tool_registry module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ToolRegistryTests(unittest.TestCase):
    def test_registry_registers_and_invokes_tools(self) -> None:
        module = load_module()
        registry = module.ToolRegistry()

        registry.register(
            module.ToolSpec(
                name="echo",
                description="Return the input payload.",
                handler=lambda payload: {"echo": payload},
            )
        )

        self.assertEqual(registry.list_tool_names(), ["echo"])
        self.assertEqual(registry.call("echo", {"value": 1}), {"echo": {"value": 1}})

    def test_build_benchmark_tool_registry_exposes_profile_and_action_bank_tools(self) -> None:
        module = load_module()

        registry = module.build_benchmark_tool_registry()

        tool_names = registry.list_tool_names()
        self.assertIn("build_agent_visible_action_bank", tool_names)
        self.assertIn("load_task_bundle", tool_names)
        self.assertIn("resolve_dataset_paths", tool_names)
        self.assertIn("profile_table_schema", tool_names)
        self.assertIn("profile_missingness", tool_names)
        self.assertIn("profile_numeric_columns", tool_names)
        self.assertIn("profile_boolean_like_columns", tool_names)
        self.assertIn("profile_join_key", tool_names)
        self.assertIn("profile_target_distribution", tool_names)
