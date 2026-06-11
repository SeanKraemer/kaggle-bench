from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "agent" / "context_builder.py"


def load_module():
    spec = importlib.util.spec_from_file_location("agent_context_builder", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load context_builder module")
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
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                },
                {
                    "action_id": "CA-2",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["parcelid"]},
                    "reasoning": "hidden",
                    "provenance_type": "synthetic",
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


def build_temp_single_table_task_bundle(root: Path) -> Path:
    task_dir = root / "data" / "tasks" / "amex-default-prediction"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "amex-default-prediction",
            "dataset": {
                "train_files": ["train_data.csv"],
                "target_column": "target",
                "primary_key": "customer_ID",
            },
            "goal": "Suggest preprocessing actions for default prediction.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "amex-default-prediction",
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["customer_ID"]},
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                }
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "amex-default-prediction",
            "task_ref": "../task.json",
            "input": {"scenario": "from_scratch", "context_action_ids": []},
        },
    )
    return task_dir


def build_temp_label_sidecar_task_bundle(root: Path) -> Path:
    task_dir = root / "data" / "tasks" / "amex-default-prediction"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "amex-default-prediction",
            "dataset": {
                "train_files": ["train_data.csv", "train_labels.csv"],
                "target_column": "target",
                "primary_key": "customer_ID",
            },
            "goal": "Suggest preprocessing actions for default prediction.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "amex-default-prediction",
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["customer_ID"]},
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                }
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "amex-default-prediction",
            "task_ref": "../task.json",
            "input": {"scenario": "from_scratch", "context_action_ids": []},
        },
    )
    return task_dir


def build_temp_inferred_join_task_bundle(root: Path) -> Path:
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
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {
                        "right_table_id": "store",
                        "left_on": "Store",
                        "right_on": "Store",
                        "how": "left",
                    },
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                }
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "rossmann-store-sales",
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


def build_temp_large_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train_2016_v2.csv",
        "parcelid,logerror,transactiondate\n"
        "1,0.1,2016-10-01\n"
        "2,0.2,2016-10-02\n"
        "3,0.3,2016-10-03\n"
        "4,0.4,2016-10-04\n"
        "5,0.5,2016-10-05\n",
    )
    write_text(
        data_root / "properties_2016.csv",
        "parcelid,feature_num\n1,10\n2,11\n3,12\n4,13\n5,14\n",
    )
    return data_root


def build_temp_single_table_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train_data.csv",
        "customer_ID,target,feature_num\nC1,1,10\nC2,0,\n",
    )
    return data_root


def build_temp_label_sidecar_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train_data.csv",
        "customer_ID,feature_num\nC1,10\nC2,\n",
    )
    write_text(
        data_root / "train_labels.csv",
        "customer_ID,target\nC1,1\nC2,0\n",
    )
    return data_root


def build_temp_inferred_join_data_root(root: Path) -> Path:
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


def build_temp_multi_train_join_task_bundle(root: Path) -> Path:
    task_dir = root / "data" / "tasks" / "ieee-fraud-detection"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "ieee-fraud-detection",
            "dataset": {
                "train_files": ["train_transaction.csv", "train_identity.csv"],
                "target_column": "isFraud",
            },
            "goal": "Suggest preprocessing actions for fraud detection.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "ieee-fraud-detection",
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {
                        "left_table_id": "train_transaction",
                        "right_table_id": "train_identity",
                        "left_on": "TransactionID",
                        "right_on": "TransactionID",
                        "how": "left",
                    },
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                }
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "ieee-fraud-detection",
            "task_ref": "../task.json",
            "input": {"scenario": "from_scratch", "context_action_ids": []},
        },
    )
    return task_dir


def build_temp_composite_join_task_bundle(root: Path) -> Path:
    task_dir = root / "data" / "tasks" / "recruit-restaurant-visitor-forecasting"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "recruit-restaurant-visitor-forecasting",
            "dataset": {
                "train_files": ["air_visit_data.csv"],
                "lookup_files": ["air_reserve.csv"],
                "target_column": "visitors",
            },
            "goal": "Suggest preprocessing actions for restaurant demand forecasting.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "competition_slug": "recruit-restaurant-visitor-forecasting",
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {
                        "left_table_id": "air_visit_data",
                        "right_table_id": "air_reserve",
                        "left_on": ["air_store_id", "visit_date"],
                        "right_on": ["air_store_id", "visit_date"],
                        "how": "left",
                    },
                    "eval_stage": "core_preprocessing",
                    "role": "good",
                }
            ],
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "recruit-restaurant-visitor-forecasting",
            "task_ref": "../task.json",
            "input": {"scenario": "from_scratch", "context_action_ids": []},
        },
    )
    return task_dir


def build_temp_multi_train_join_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "train_transaction.csv",
        "TransactionID,isFraud,TransactionAmt\n1,0,10.5\n2,1,20.0\n",
    )
    write_text(
        data_root / "train_identity.csv",
        "TransactionID,DeviceType\n1,desktop\n2,mobile\n",
    )
    return data_root


def build_temp_composite_join_data_root(root: Path) -> Path:
    data_root = root / "raw"
    write_text(
        data_root / "air_visit_data.csv",
        "air_store_id,visit_date,visitors\nA,2017-01-01,10\nA,2017-01-02,20\n",
    )
    write_text(
        data_root / "air_reserve.csv",
        "air_store_id,visit_date,reserve_visitors\nA,2017-01-01,4\nA,2017-01-03,9\n",
    )
    return data_root


class ContextBuilderTests(unittest.TestCase):
    def test_build_benchmark_context_returns_non_materialized_shared_fields(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)

            context = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

        self.assertEqual(context.bundle.task["competition_slug"], "zillow-prize-1")
        self.assertEqual(context.dataset_paths["train_files"][0].name, "train_2016_v2.csv")
        self.assertEqual(context.dataset_paths["lookup_files"][0].name, "properties_2016.csv")
        self.assertEqual(context.valid_action_ids, {"CA-1", "CA-2"})
        self.assertEqual(
            context.visible_actions,
            [
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
        )
        self.assertIn("Current context_action_ids: []", context.context_summary)
        self.assertIn('"action_id": "CA-1"', context.candidate_actions_json)
        self.assertFalse(hasattr(context, "train_rows"))
        self.assertFalse(hasattr(context, "dataset_summary"))

    def test_build_materialized_benchmark_context_returns_profiles_and_dataset_summary(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(len(materialized.train_rows), 2)
        self.assertEqual(materialized.primary_train_profile["table_name"], "train_2016_v2.csv")
        self.assertIn("Primary train profile:", materialized.dataset_summary)
        self.assertIn("Join profile:", materialized.dataset_summary)
        self.assertIn("Target column: logerror", materialized.dataset_summary)
        self.assertIn("Primary key: parcelid", materialized.dataset_summary)
        self.assertEqual(materialized.benchmark.valid_action_ids, {"CA-1", "CA-2"})
        self.assertFalse(hasattr(materialized, "joined_rows"))
        self.assertFalse(hasattr(materialized, "schema_profile"))
        self.assertFalse(hasattr(materialized, "missingness_profile"))
        self.assertFalse(hasattr(materialized, "numeric_profile"))
        self.assertFalse(hasattr(materialized, "boolean_like_profile"))

    def test_materialize_benchmark_context_supports_single_table_tasks_without_lookup_files(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_single_table_task_bundle(root)
            data_root = build_temp_single_table_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(len(materialized.train_rows), 2)
        self.assertEqual(materialized.lookup_rows, [])
        self.assertIn("Train files: train_data.csv", materialized.dataset_summary)
        self.assertIn("Lookup files:", materialized.dataset_summary)
        self.assertIn("Target column: target", materialized.dataset_summary)

    def test_materialize_benchmark_context_profiles_target_from_label_sidecar(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_label_sidecar_task_bundle(root)
            data_root = build_temp_label_sidecar_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(materialized.target_profile["count"], 2)
        self.assertEqual(materialized.target_profile["max"], 1.0)

    def test_materialize_benchmark_context_infers_join_keys_from_visible_join_actions(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_inferred_join_task_bundle(root)
            data_root = build_temp_inferred_join_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(materialized.join_profile["left_key_coverage_rate"], 1.0)
        self.assertEqual(materialized.join_profile["right_key_coverage_rate"], 1.0)

    def test_materialize_benchmark_context_supports_join_profiles_for_multi_train_tasks(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_multi_train_join_task_bundle(root)
            data_root = build_temp_multi_train_join_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(materialized.join_profile["left_key_coverage_rate"], 1.0)
        self.assertEqual(materialized.lookup_rows[0]["DeviceType"], "desktop")

    def test_materialize_benchmark_context_supports_composite_join_specs(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_composite_join_task_bundle(root)
            data_root = build_temp_composite_join_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(materialized.join_profile["left_key_columns"], ["air_store_id", "visit_date"])
        self.assertEqual(materialized.join_profile["right_key_columns"], ["air_store_id", "visit_date"])
        self.assertEqual(materialized.join_profile["overlap_key_count"], 1)

    def test_materialize_benchmark_context_does_not_materialize_joined_view(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            def fail_if_called(*args, **kwargs):
                raise AssertionError("joined view materialization should not be called")

            module.load_joined_training_view = fail_if_called
            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(materialized.join_profile["left_key_coverage_rate"], 1.0)
        self.assertEqual(materialized.primary_train_profile["table_name"], "train_2016_v2.csv")

    def test_materialize_benchmark_context_includes_per_table_profiles_in_summary(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(
            [profile["table_name"] for profile in materialized.table_profiles],
            ["train_2016_v2.csv", "properties_2016.csv"],
        )
        self.assertIn("Table profiles:", materialized.dataset_summary)
        self.assertIn("Table: train_2016_v2.csv", materialized.dataset_summary)
        self.assertIn("Table: properties_2016.csv", materialized.dataset_summary)

    def test_materialize_benchmark_context_samples_large_tables_for_summary(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            data_root = build_temp_large_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            original_load_table_rows_for_summary = module.load_table_rows_for_summary

            def force_sampling(path):
                return original_load_table_rows_for_summary(
                    path,
                    full_load_max_cells=1,
                    full_load_max_bytes=1_000_000,
                    sample_row_count=2,
                )

            module.load_table_rows_for_summary = force_sampling
            materialized = module.materialize_benchmark_context(benchmark)

        self.assertEqual(len(materialized.train_rows), 2)
        self.assertEqual(materialized.primary_train_profile["sampling"]["mode"], "sampled")
        self.assertEqual(materialized.primary_train_profile["sampling"]["source_row_count"], 5)
        self.assertEqual(materialized.primary_train_profile["sampling"]["loaded_row_count"], 2)

    def test_materialize_benchmark_context_requires_at_least_one_train_file(self) -> None:
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            task_dir = build_temp_task_bundle(root)
            task_payload = json.loads((task_dir / "task.json").read_text(encoding="utf-8"))
            task_payload["dataset"]["train_files"] = []
            write_json(task_dir / "task.json", task_payload)
            data_root = build_temp_data_root(root)
            benchmark = module.build_benchmark_context(
                task_dir=task_dir,
                testcase_id="tc1_from_scratch",
                data_root=data_root,
            )

            with self.assertRaises(ValueError) as context:
                module.materialize_benchmark_context(benchmark)

        self.assertIn("at least one train file", str(context.exception))
