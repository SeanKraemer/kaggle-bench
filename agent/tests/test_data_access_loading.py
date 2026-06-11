from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_ACCESS_PATH = ROOT / "agent" / "data_access.py"


def load_data_access_module():
    spec = importlib.util.spec_from_file_location("agent_data_access", DATA_ACCESS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load data_access module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_text(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


class DataAccessLoadingTests(unittest.TestCase):
    def test_resolve_dataset_paths_validates_required_files(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            data_root = Path(tmp)
            write_text(data_root / "train_2016_v2.csv", "parcelid,logerror\n1,0.1\n")
            write_text(data_root / "properties_2016.csv", "parcelid,feature_a\n1,10\n")
            task = {
                "dataset": {
                    "train_files": ["train_2016_v2.csv"],
                    "lookup_files": ["properties_2016.csv"],
                }
            }

            resolved = data_access.resolve_dataset_paths(data_root, task)

        self.assertEqual(resolved["train_files"][0].name, "train_2016_v2.csv")
        self.assertEqual(resolved["lookup_files"][0].name, "properties_2016.csv")

    def test_resolve_dataset_paths_raises_for_missing_required_file(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            data_root = Path(tmp)
            task = {
                "dataset": {
                    "train_files": ["train_2016_v2.csv"],
                    "lookup_files": ["properties_2016.csv"],
                }
            }

            with self.assertRaisesRegex(FileNotFoundError, "train_2016_v2.csv"):
                data_access.resolve_dataset_paths(data_root, task)

    def test_load_csv_rows_reads_records(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            csv_path = write_text(Path(tmp) / "sample.csv", "a,b\n1,x\n2,y\n")

            rows = data_access.load_csv_rows(csv_path)

        self.assertEqual(rows, [{"a": "1", "b": "x"}, {"a": "2", "b": "y"}])

    def test_load_csv_rows_reads_zipped_csv_records(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            zip_path = Path(tmp) / "sample.csv.zip"
            with zipfile.ZipFile(zip_path, "w") as archive:
                archive.writestr("sample.csv", "a,b\n1,x\n2,y\n")

            rows = data_access.load_csv_rows(zip_path)

        self.assertEqual(rows, [{"a": "1", "b": "x"}, {"a": "2", "b": "y"}])

    def test_inspect_csv_table_reports_shape(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            csv_path = write_text(Path(tmp) / "sample.csv", "a,b,c\n1,x,7\n2,y,8\n3,z,9\n")

            inspection = data_access.inspect_csv_table(csv_path)

        self.assertEqual(inspection.row_count, 3)
        self.assertEqual(inspection.column_count, 3)
        self.assertEqual(inspection.column_names, ["a", "b", "c"])
        self.assertGreater(inspection.file_size_bytes, 0)
        self.assertEqual(inspection.estimated_cells, 9)

    def test_build_table_load_plan_switches_to_sampling_for_large_tables(self) -> None:
        data_access = load_data_access_module()
        inspection = data_access.TableInspection(
            row_count=100,
            column_names=["a", "b", "c"],
            column_count=3,
            file_size_bytes=1024,
            estimated_cells=300,
        )

        plan = data_access.build_table_load_plan(
            inspection,
            full_load_max_cells=50,
            full_load_max_bytes=10_000,
            sample_row_count=10,
        )

        self.assertEqual(plan.mode, "sampled")
        self.assertEqual(plan.sample_row_count, 10)

    def test_load_uniform_sample_rows_returns_bounded_non_prefix_sample(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            csv_path = write_text(
                Path(tmp) / "sample.csv",
                "row_id,value\n" + "\n".join(f"{index},v{index}" for index in range(100)) + "\n",
            )

            rows = data_access.load_uniform_sample_rows(csv_path, sample_row_count=10, random_seed=0)

        sampled_ids = [int(row["row_id"]) for row in rows]
        self.assertEqual(len(rows), 10)
        self.assertEqual(len(set(sampled_ids)), 10)
        self.assertNotEqual(sampled_ids, list(range(10)))
        self.assertTrue(all(0 <= row_id < 100 for row_id in sampled_ids))

    def test_load_table_rows_for_summary_uses_sampling_plan(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            csv_path = write_text(
                Path(tmp) / "sample.csv",
                "row_id,value\n" + "\n".join(f"{index},v{index}" for index in range(20)) + "\n",
            )

            rows, plan = data_access.load_table_rows_for_summary(
                csv_path,
                full_load_max_cells=10,
                full_load_max_bytes=10_000,
                sample_row_count=5,
            )

        self.assertEqual(plan.mode, "sampled")
        self.assertEqual(plan.source_row_count, 20)
        self.assertEqual(len(rows), 5)

    def test_load_joined_training_view_filters_lookup_to_train_keys(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            data_root = Path(tmp)
            train_path = write_text(
                data_root / "train_2016_v2.csv",
                "parcelid,logerror,transactiondate\n1,0.1,2016-10-01\n2,0.2,2016-10-02\n",
            )
            lookup_path = write_text(
                data_root / "properties_2016.csv",
                "parcelid,feature_a,feature_b\n1,10,\n3,99,z\n2,20,y\n",
            )

            rows = data_access.load_joined_training_view(
                train_path=train_path,
                lookup_path=lookup_path,
                key_column="parcelid",
            )

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["parcelid"], "1")
        self.assertEqual(rows[0]["feature_a"], "10")
        self.assertEqual(rows[1]["parcelid"], "2")
        self.assertEqual(rows[1]["feature_b"], "y")

    def test_load_joined_training_view_supports_distinct_left_and_right_join_columns(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            data_root = Path(tmp)
            train_path = write_text(
                data_root / "train.csv",
                "store_id,Sales\n1,100\n2,200\n",
            )
            lookup_path = write_text(
                data_root / "store.csv",
                "Store,StoreType\n1,a\n2,b\n",
            )

            rows = data_access.load_joined_training_view(
                train_path=train_path,
                lookup_path=lookup_path,
                left_on="store_id",
                right_on="Store",
            )

        self.assertEqual(rows[0]["StoreType"], "a")
        self.assertEqual(rows[1]["StoreType"], "b")

    def test_load_joined_training_view_supports_composite_join_keys(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            data_root = Path(tmp)
            train_path = write_text(
                data_root / "train.csv",
                "air_store_id,visit_date,visitors\nA,2017-01-01,10\nA,2017-01-02,20\n",
            )
            lookup_path = write_text(
                data_root / "reservations.csv",
                "air_store_id,visit_date,reserve_visitors\nA,2017-01-01,4\nA,2017-01-03,9\n",
            )

            rows = data_access.load_joined_training_view(
                train_path=train_path,
                lookup_path=lookup_path,
                left_on=["air_store_id", "visit_date"],
                right_on=["air_store_id", "visit_date"],
            )

        self.assertEqual(rows[0]["reserve_visitors"], "4")
        self.assertNotIn("reserve_visitors", rows[1])

    def test_load_train_and_lookup_table_delegate_to_csv_reader(self) -> None:
        data_access = load_data_access_module()

        with tempfile.TemporaryDirectory() as tmp:
            data_root = Path(tmp)
            train_path = write_text(data_root / "train_2016_v2.csv", "parcelid,logerror\n1,0.1\n")
            lookup_path = write_text(data_root / "properties_2016.csv", "parcelid,feature_a\n1,10\n")

            train_rows = data_access.load_train_table(train_path)
            lookup_rows = data_access.load_lookup_table(lookup_path)

        self.assertEqual(train_rows[0]["parcelid"], "1")
        self.assertEqual(lookup_rows[0]["feature_a"], "10")
