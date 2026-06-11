from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TASK_BUNDLE_PATH = ROOT / "agent" / "task_bundle.py"
ZILLOW_TASK_DIR = ROOT / "data" / "tasks" / "zillow-prize-1"


def load_task_bundle_module():
    spec = importlib.util.spec_from_file_location("agent_task_bundle", TASK_BUNDLE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load task_bundle module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TaskBundleLoadingTests(unittest.TestCase):
    def test_load_task_bundle_reads_task_testcase_and_actions(self) -> None:
        task_bundle = load_task_bundle_module()

        bundle = task_bundle.load_task_bundle(
            task_dir=ZILLOW_TASK_DIR,
            testcase_id="tc1_from_scratch",
        )

        self.assertEqual(bundle.task["competition_slug"], "zillow-prize-1")
        self.assertEqual(bundle.testcase["testcase_id"], "tc1_from_scratch")
        self.assertIn("CA-000107", bundle.action_by_id)
        self.assertEqual(bundle.action_by_id["CA-000107"]["action_type"], "JOIN_LOOKUP")
