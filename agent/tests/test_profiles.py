from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "agent" / "profiles" / "schema.py"
MISSINGNESS_PATH = ROOT / "agent" / "profiles" / "missingness.py"
NUMERIC_PATH = ROOT / "agent" / "profiles" / "numeric.py"
CATEGORICAL_PATH = ROOT / "agent" / "profiles" / "categorical.py"
DATETIME_PATH = ROOT / "agent" / "profiles" / "datetime.py"
JOIN_PATH = ROOT / "agent" / "profiles" / "join.py"
TARGET_PATH = ROOT / "agent" / "profiles" / "target.py"
ROLES_PATH = ROOT / "agent" / "profiles" / "roles.py"
BOOLEAN_PATH = ROOT / "agent" / "profiles" / "boolean_like.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROWS = [
    {
        "parcelid": "1",
        "transactiondate": "2016-10-01",
        "logerror": "0.10",
        "feature_num": "10",
        "feature_cat": "A",
        "flag": "FALSE",
        "mostly_missing": "",
    },
    {
        "parcelid": "2",
        "transactiondate": "2016-10-02",
        "logerror": "0.20",
        "feature_num": "",
        "feature_cat": "B",
        "flag": "TRUE",
        "mostly_missing": "",
    },
    {
        "parcelid": "3",
        "transactiondate": "2016-10-03",
        "logerror": "-0.30",
        "feature_num": "30",
        "feature_cat": "A",
        "flag": "FALSE",
        "mostly_missing": "x",
    },
]


class ProfileTests(unittest.TestCase):
    def test_profile_table_schema_infers_basic_types(self) -> None:
        schema = load_module(SCHEMA_PATH, "agent_profiles_schema")

        profile = schema.profile_table_schema(ROWS)

        self.assertEqual(profile["row_count"], 3)
        self.assertEqual(profile["columns"]["parcelid"]["inferred_type"], "integer_like")
        self.assertEqual(profile["columns"]["transactiondate"]["inferred_type"], "datetime_like")
        self.assertEqual(profile["columns"]["feature_cat"]["inferred_type"], "string")

    def test_profile_missingness_reports_null_rates(self) -> None:
        missingness = load_module(MISSINGNESS_PATH, "agent_profiles_missingness")

        profile = missingness.profile_missingness(ROWS)

        self.assertEqual(profile["columns"]["feature_num"]["missing_count"], 1)
        self.assertAlmostEqual(profile["columns"]["feature_num"]["missing_rate"], 1 / 3, places=6)
        self.assertEqual(profile["columns"]["mostly_missing"]["missing_count"], 2)

    def test_profile_numeric_columns_computes_summary_stats(self) -> None:
        numeric = load_module(NUMERIC_PATH, "agent_profiles_numeric")

        profile = numeric.profile_numeric_columns(ROWS)

        self.assertIn("feature_num", profile["columns"])
        self.assertEqual(profile["columns"]["feature_num"]["count"], 2)
        self.assertEqual(profile["columns"]["feature_num"]["min"], 10.0)
        self.assertEqual(profile["columns"]["feature_num"]["max"], 30.0)

    def test_profile_categorical_columns_tracks_cardinality(self) -> None:
        categorical = load_module(CATEGORICAL_PATH, "agent_profiles_categorical")

        profile = categorical.profile_categorical_columns(ROWS)

        self.assertEqual(profile["columns"]["feature_cat"]["distinct_count"], 2)
        self.assertEqual(profile["columns"]["flag"]["top_values"][0]["value"], "FALSE")

    def test_profile_boolean_like_columns_finds_flag_columns(self) -> None:
        boolean_like = load_module(BOOLEAN_PATH, "agent_profiles_boolean_like")

        profile = boolean_like.profile_boolean_like_columns(ROWS)

        self.assertIn("flag", profile["columns"])
        self.assertEqual(profile["columns"]["flag"]["distinct_values"], ["FALSE", "TRUE"])

    def test_profile_datetime_columns_tracks_parse_rate(self) -> None:
        dt_profile = load_module(DATETIME_PATH, "agent_profiles_datetime")

        profile = dt_profile.profile_datetime_columns(ROWS)

        self.assertEqual(profile["columns"]["transactiondate"]["parseable_count"], 3)
        self.assertEqual(profile["columns"]["transactiondate"]["min"], "2016-10-01T00:00:00")

    def test_profile_join_key_reports_overlap_and_uniqueness(self) -> None:
        join = load_module(JOIN_PATH, "agent_profiles_join")
        left_rows = [{"parcelid": "1"}, {"parcelid": "2"}, {"parcelid": "2"}]
        right_rows = [{"parcelid": "1"}, {"parcelid": "2"}, {"parcelid": "3"}]

        profile = join.profile_join_key(left_rows, right_rows, "parcelid")

        self.assertEqual(profile["left_row_count"], 3)
        self.assertEqual(profile["left_distinct_key_count"], 2)
        self.assertEqual(profile["right_distinct_key_count"], 3)
        self.assertAlmostEqual(profile["left_key_coverage_rate"], 1.0, places=6)

    def test_profile_join_key_supports_distinct_and_composite_keys(self) -> None:
        join = load_module(JOIN_PATH, "agent_profiles_join")
        left_rows = [
            {"store_id": "1", "visit_date": "2017-01-01"},
            {"store_id": "1", "visit_date": "2017-01-02"},
        ]
        right_rows = [
            {"Store": "1", "Date": "2017-01-01"},
            {"Store": "2", "Date": "2017-01-01"},
        ]

        profile = join.profile_join_key(
            left_rows,
            right_rows,
            left_key=["store_id", "visit_date"],
            right_key=["Store", "Date"],
        )

        self.assertEqual(profile["left_key_columns"], ["store_id", "visit_date"])
        self.assertEqual(profile["right_key_columns"], ["Store", "Date"])
        self.assertEqual(profile["overlap_key_count"], 1)
        self.assertAlmostEqual(profile["left_key_coverage_rate"], 0.5, places=6)

    def test_profile_target_distribution_reports_quantiles(self) -> None:
        target = load_module(TARGET_PATH, "agent_profiles_target")

        profile = target.profile_target_distribution(ROWS, "logerror")

        self.assertEqual(profile["count"], 3)
        self.assertEqual(profile["min"], -0.3)
        self.assertEqual(profile["max"], 0.2)

    def test_infer_column_roles_identifies_common_roles(self) -> None:
        roles = load_module(ROLES_PATH, "agent_profiles_roles")
        task = {
            "dataset": {
                "primary_key": "parcelid",
                "target_column": "logerror",
            }
        }

        profile = roles.infer_column_roles(ROWS, task)

        self.assertEqual(profile["parcelid"], "primary_key")
        self.assertEqual(profile["logerror"], "target")
        self.assertEqual(profile["transactiondate"], "datetime_feature")
        self.assertEqual(profile["feature_cat"], "categorical_feature")
