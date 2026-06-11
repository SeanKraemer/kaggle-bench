from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

import agent.context_builder as shared_context_builder

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "agent" / "single_llm" / "request_context.py"


def load_module():
    spec = importlib.util.spec_from_file_location("agent_single_llm_request_context", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load single_llm request_context module")
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
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {"how": "left", "right_table_id": "properties_2016"},
                },
                {
                    "action_id": "CA-2",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["parcelid"]},
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
            "input": {"scenario": "from_scratch", "context_action_ids": []},
        },
    )
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


class SingleLLMRequestContextTests(unittest.TestCase):
    def test_build_single_llm_request_context_reuses_cached_profiles_without_reloading_tables(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            cache_dir = root / "profile-cache"

            context = module.build_single_llm_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                profile_cache_dir=cache_dir,
            )

            original_loader = shared_context_builder.load_table_rows_for_summary
            try:
                shared_context_builder.load_table_rows_for_summary = lambda *args, **kwargs: (_ for _ in ()).throw(
                    AssertionError("profile cache hit should avoid reloading dataset tables")
                )
                cached_context = module.build_single_llm_request_context(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    data_root=data_root,
                    profile_cache_dir=cache_dir,
                )
                cache_files_exist = any(cache_dir.iterdir())
            finally:
                shared_context_builder.load_table_rows_for_summary = original_loader

        self.assertEqual(context.prompt, cached_context.prompt)
        self.assertTrue(cache_files_exist)
        self.assertEqual(context.materialized.primary_train_profile, cached_context.materialized.primary_train_profile)

    def test_build_single_llm_request_context_invalidates_cached_profiles_when_dataset_changes(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            cache_dir = root / "profile-cache"

            context = module.build_single_llm_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
                profile_cache_dir=cache_dir,
            )

            original_loader = shared_context_builder.load_table_rows_for_summary
            call_count = 0

            def counting_loader(*args, **kwargs):
                nonlocal call_count
                call_count += 1
                return original_loader(*args, **kwargs)

            write_text(
                data_root / "train_2016_v2.csv",
                "parcelid,logerror,transactiondate\n1,0.1,2016-10-01\n2,9.9,2016-10-02\n",
            )
            try:
                shared_context_builder.load_table_rows_for_summary = counting_loader
                updated_context = module.build_single_llm_request_context(
                    task_dir=task_dir,
                    testcase_id="tc1_from_scratch",
                    data_root=data_root,
                    profile_cache_dir=cache_dir,
                )
            finally:
                shared_context_builder.load_table_rows_for_summary = original_loader

        self.assertGreater(call_count, 0)
        self.assertNotEqual(context.prompt, updated_context.prompt)

    def test_build_single_llm_request_context_does_not_emit_trailing_spaces_for_empty_fields(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            write_json(
                task_dir / "task.json",
                {
                    "competition_slug": "zillow-prize-1",
                    "dataset": {
                        "train_files": ["train_2016_v2.csv"],
                        "lookup_files": [],
                        "target_column": "logerror",
                        "primary_key": "",
                    },
                    "goal": "Suggest preprocessing actions for logerror prediction.",
                },
            )
            context = module.build_single_llm_request_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

        self.assertIn("Lookup files:\n", context.prompt)
        self.assertIn("Primary key:\n", context.prompt)
        self.assertIsNone(re.search(r"[ \t]+$", context.prompt, re.MULTILINE))
