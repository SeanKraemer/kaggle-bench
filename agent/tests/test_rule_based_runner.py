from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import agent.context_builder as shared_context_builder


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "agent" / "rule_based" / "runner.py"
REQUEST_CONTEXT_PATH = ROOT / "agent" / "single_llm" / "request_context.py"


def load_runner_module():
    spec = importlib.util.spec_from_file_location("agent_rule_based_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load rule_based runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_request_context_module():
    spec = importlib.util.spec_from_file_location("agent_single_llm_request_context", REQUEST_CONTEXT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load single_llm request_context")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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
                "train_files": ["train_2016_v2.csv"],
                "lookup_files": ["properties_2016.csv"],
                "target_column": "logerror",
                "primary_key": "parcelid",
            },
            "goal": "Suggest preprocessing actions for logerror prediction.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "zillow-prize-1",
            "actions": [
                {
                    "action_id": "CA-JOIN",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {"how": "left", "right_table_id": "properties_2016"},
                },
                {
                    "action_id": "CA-PARSE",
                    "action_type": "PARSE_DATETIME",
                    "canonical_params": {"columns": ["transactiondate"]},
                },
                {
                    "action_id": "CA-MEDIAN",
                    "action_type": "IMPUTE_MISSING",
                    "canonical_params": {"strategy": "median", "columns": ["feature_num"]},
                },
                {
                    "action_id": "CA-DROP",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["parcelid", "logerror", "transactiondate"]},
                },
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "zillow-prize-1",
            "task_ref": "../task.json",
            "input": {
                "scenario": "from_scratch",
                "context_action_ids": [],
            },
        },
    )
    (task_dir / "outputs" / "provenance").mkdir(parents=True, exist_ok=True)
    return task_dir


def build_temp_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train_2016_v2.csv",
        "parcelid,logerror,transactiondate\n1,0.1,2016-10-01\n2,0.2,2016-10-02\n",
    )
    write_text(
        data_root / "properties_2016.csv",
        "parcelid,feature_num\n1,10\n2,\n",
    )
    return data_root


def build_temp_no_primary_key_task_bundle(root: Path) -> Path:
    task_dir = root / "data" / "tasks" / "rossmann-store-sales"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "rossmann-store-sales",
            "dataset": {
                "train_files": ["train.csv"],
                "lookup_files": ["store.csv"],
                "target_column": "Sales",
            },
            "goal": "Suggest preprocessing actions for store sales forecasting.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "rossmann-store-sales",
            "actions": [
                {
                    "action_id": "CA-JOIN",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {
                        "how": "left",
                        "right_table_id": "store",
                        "left_on": "Store",
                        "right_on": "Store",
                    },
                },
                {
                    "action_id": "CA-DROP",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["Sales"]},
                },
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "rossmann-store-sales",
            "task_ref": "../task.json",
            "input": {
                "scenario": "from_scratch",
                "context_action_ids": [],
            },
        },
    )
    (task_dir / "outputs" / "provenance").mkdir(parents=True, exist_ok=True)
    return task_dir


def build_temp_no_primary_key_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train.csv",
        "Store,Sales,Date\n1,100,2015-07-01\n2,200,2015-07-02\n",
    )
    write_text(
        data_root / "store.csv",
        "Store,StoreType\n1,a\n2,b\n",
    )
    return data_root


class RuleBasedRunnerTests(unittest.TestCase):
    def test_run_rule_based_writes_artifact(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)

            result = runner.run_rule_based(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            metadata_payload = json.loads(result["metadata_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")

        self.assertIn("CA-JOIN", output_payload["predicted_add_action_ids"])
        self.assertIn("CA-PARSE", output_payload["predicted_add_action_ids"])
        self.assertEqual(metadata_payload["status"], "success")
        self.assertEqual(metadata_payload["api_call_count"], 0)
        self.assertIn("## Action Decisions", trace_text)
        self.assertIn("### CA-JOIN", trace_text)
        self.assertIn("Decision: `selected_add`", trace_text)
        self.assertIn("left_key_coverage_rate", trace_text)
        self.assertIn("### CA-DROP", trace_text)
        self.assertIn("triggered rule", trace_text)
        self.assertNotIn("CA-MEDIAN", output_payload["predicted_add_action_ids"])

    def test_run_rule_based_supports_tasks_without_primary_key(self) -> None:
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_no_primary_key_task_bundle(root)
            data_root = build_temp_no_primary_key_data_root(root)

            result = runner.run_rule_based(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                run_id="try1",
                data_root=data_root,
            )

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))
            trace_text = result["trace_path"].read_text(encoding="utf-8")

        self.assertIn("CA-JOIN", output_payload["predicted_add_action_ids"])
        self.assertIn("Primary key: `None`", trace_text)

    def test_run_rule_based_reuses_profile_cache_seeded_by_single_llm(self) -> None:
        runner = load_runner_module()
        request_context = load_request_context_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            cache_dir = root / "profile-cache"

            request_context.build_single_llm_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                profile_cache_dir=cache_dir,
            )

            original_loader = shared_context_builder.load_table_rows_for_summary
            try:
                shared_context_builder.load_table_rows_for_summary = lambda *args, **kwargs: (_ for _ in ()).throw(
                    AssertionError("rule_based should reuse shared profile cache without reloading tables")
                )
                result = runner.run_rule_based(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    run_id="try1",
                    data_root=data_root,
                    profile_cache_dir=cache_dir,
                )
            finally:
                shared_context_builder.load_table_rows_for_summary = original_loader

            output_payload = json.loads(result["output_path"].read_text(encoding="utf-8"))

        self.assertIn("CA-JOIN", output_payload["predicted_add_action_ids"])
