from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUMMARIES_PATH = ROOT / "agent" / "summaries.py"


def load_summaries_module():
    spec = importlib.util.spec_from_file_location("agent_summaries", SUMMARIES_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load summaries module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SummaryRenderingTests(unittest.TestCase):
    def test_render_dataset_summary_mentions_key_profiles(self) -> None:
        summaries = load_summaries_module()

        text = summaries.render_dataset_summary(
            task={"goal": "predict logerror", "dataset": {"target_column": "logerror", "primary_key": "parcelid"}},
            dataset_paths={
                "train_files": [Path("/tmp/train_2016_v2.csv")],
                "lookup_files": [Path("/tmp/properties_2016.csv")],
            },
            table_profiles=[
                {
                    "table_name": "train_2016_v2.csv",
                    "table_role": "train",
                    "sampling": {
                        "mode": "full",
                        "source_row_count": 100,
                        "source_column_count": 3,
                        "loaded_row_count": 100,
                        "file_size_bytes": 1000,
                        "estimated_cells": 300,
                        "sample_row_count": None,
                    },
                    "schema_profile": {"row_count": 100, "column_count": 3},
                    "missingness_profile": {"columns": {"logerror": {"missing_rate": 0.0}}},
                    "numeric_profile": {"columns": {"logerror": {"min": -0.1, "max": 0.1}}},
                    "boolean_like_profile": {"columns": {}},
                },
                {
                    "table_name": "properties_2016.csv",
                    "table_role": "lookup",
                    "sampling": {
                        "mode": "sampled",
                        "source_row_count": 1000000,
                        "source_column_count": 2,
                        "loaded_row_count": 50000,
                        "file_size_bytes": 100000000,
                        "estimated_cells": 2000000,
                        "sample_row_count": 50000,
                    },
                    "schema_profile": {"row_count": 100, "column_count": 2},
                    "missingness_profile": {"columns": {"feature_num": {"missing_rate": 0.3}}},
                    "numeric_profile": {"columns": {"feature_num": {"min": 0.0, "max": 1.0}}},
                    "boolean_like_profile": {"columns": {"flag_col": {"true_ratio": 0.2}}},
                },
            ],
            primary_train_profile={
                "table_name": "train_2016_v2.csv",
                "table_role": "train",
                "sampling": {
                    "mode": "full",
                    "source_row_count": 100,
                    "source_column_count": 3,
                    "loaded_row_count": 100,
                    "file_size_bytes": 1000,
                    "estimated_cells": 300,
                    "sample_row_count": None,
                },
                "schema_profile": {"row_count": 100, "column_count": 3},
                "missingness_profile": {"columns": {"logerror": {"missing_rate": 0.0}}},
                "numeric_profile": {"columns": {"logerror": {"min": -0.1, "max": 0.1}}},
                "boolean_like_profile": {"columns": {}},
            },
            join_profile={
                "left_key_coverage_rate": 0.95,
                "sampling": {
                    "left_mode": "full",
                    "left_source_row_count": 100,
                    "left_loaded_row_count": 100,
                    "right_mode": "sampled",
                    "right_source_row_count": 1000000,
                    "right_loaded_row_count": 50000,
                },
            },
            target_profile={"p25": -0.1, "p50": 0.0, "p75": 0.1},
        )

        self.assertIn("predict logerror", text)
        self.assertIn("train_2016_v2.csv", text)
        self.assertIn("properties_2016.csv", text)
        self.assertIn("Primary train profile:", text)
        self.assertIn("Table profiles:", text)
        self.assertIn("left_key_coverage_rate", text)
        self.assertIn('"mode": "sampled"', text)
        self.assertIn("feature_num", text)
        self.assertIn("flag_col", text)
        self.assertIn("Target column: logerror", text)
        self.assertIn("Primary key: parcelid", text)
        self.assertNotIn("Combined schema profile", text)
        self.assertEqual(text.count("Table profiles:"), 1)

    def test_render_context_summary_mentions_scenario_and_context_ids(self) -> None:
        summaries = load_summaries_module()

        text = summaries.render_context_summary(
            testcase={
                "testcase_id": "tc3_fault_injected",
                "input": {"scenario": "fault_injected", "context_action_ids": ["CA-1", "CA-2"]},
            }
        )

        self.assertIn("fault_injected", text)
        self.assertIn("CA-1", text)
        self.assertIn("CA-2", text)

    def test_render_candidate_actions_json_serializes_rows(self) -> None:
        summaries = load_summaries_module()

        text = summaries.render_candidate_actions_json([{"action_id": "CA-1", "action_type": "JOIN_LOOKUP"}])

        self.assertIn('"action_id": "CA-1"', text)

    def test_render_single_llm_dataset_summary_keeps_only_action_referenced_columns(self) -> None:
        summaries = load_summaries_module()

        text = summaries.render_single_llm_dataset_summary(
            task={"goal": "predict logerror", "dataset": {"target_column": "logerror", "primary_key": "parcelid"}},
            dataset_paths={
                "train_files": [Path("/tmp/train_2016_v2.csv")],
                "lookup_files": [Path("/tmp/properties_2016.csv")],
            },
            visible_actions=[
                {
                    "action_id": "CA-1",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["parcelid"]},
                },
                {
                    "action_id": "CA-2",
                    "action_type": "APPLY_EXPRESSION",
                    "canonical_params": {
                        "expression": "feature_ratio = feature_num / 10",
                        "output_columns": ["feature_ratio"],
                    },
                },
            ],
            table_profiles=[
                {
                    "table_name": "train_2016_v2.csv",
                    "table_role": "train",
                    "sampling": {
                        "mode": "full",
                        "source_row_count": 100,
                        "source_column_count": 4,
                        "loaded_row_count": 100,
                        "file_size_bytes": 1000,
                        "estimated_cells": 400,
                        "sample_row_count": None,
                    },
                    "schema_profile": {
                        "row_count": 100,
                        "column_count": 4,
                        "columns": {
                            "parcelid": {"inferred_type": "integer_like"},
                            "feature_num": {"inferred_type": "numeric_like"},
                            "unused_feature": {"inferred_type": "numeric_like"},
                            "logerror": {"inferred_type": "numeric_like"},
                        },
                    },
                    "missingness_profile": {
                        "row_count": 100,
                        "columns": {
                            "parcelid": {"missing_rate": 0.0},
                            "feature_num": {"missing_rate": 0.1},
                            "unused_feature": {"missing_rate": 0.8},
                            "logerror": {"missing_rate": 0.0},
                        },
                    },
                    "numeric_profile": {
                        "columns": {
                            "feature_num": {"min": 0.0, "max": 1.0},
                            "unused_feature": {"min": -1.0, "max": 2.0},
                            "logerror": {"min": -0.1, "max": 0.1},
                        }
                    },
                    "boolean_like_profile": {"columns": {}},
                },
                {
                    "table_name": "properties_2016.csv",
                    "table_role": "lookup",
                    "sampling": {
                        "mode": "full",
                        "source_row_count": 100,
                        "source_column_count": 2,
                        "loaded_row_count": 100,
                        "file_size_bytes": 1000,
                        "estimated_cells": 200,
                        "sample_row_count": None,
                    },
                    "schema_profile": {
                        "row_count": 100,
                        "column_count": 2,
                        "columns": {
                            "parcelid": {"inferred_type": "integer_like"},
                            "lookup_only": {"inferred_type": "string"},
                        },
                    },
                    "missingness_profile": {
                        "row_count": 100,
                        "columns": {
                            "parcelid": {"missing_rate": 0.0},
                            "lookup_only": {"missing_rate": 0.0},
                        },
                    },
                    "numeric_profile": {"columns": {}},
                    "boolean_like_profile": {"columns": {}},
                },
            ],
            primary_train_profile={
                "table_name": "train_2016_v2.csv",
                "table_role": "train",
                "sampling": {
                    "mode": "full",
                    "source_row_count": 100,
                    "source_column_count": 4,
                    "loaded_row_count": 100,
                    "file_size_bytes": 1000,
                    "estimated_cells": 400,
                    "sample_row_count": None,
                },
                "schema_profile": {
                    "row_count": 100,
                    "column_count": 4,
                    "columns": {
                        "parcelid": {"inferred_type": "integer_like"},
                        "feature_num": {"inferred_type": "numeric_like"},
                        "unused_feature": {"inferred_type": "numeric_like"},
                        "logerror": {"inferred_type": "numeric_like"},
                    },
                },
                "missingness_profile": {
                    "row_count": 100,
                    "columns": {
                        "parcelid": {"missing_rate": 0.0},
                        "feature_num": {"missing_rate": 0.1},
                        "unused_feature": {"missing_rate": 0.8},
                        "logerror": {"missing_rate": 0.0},
                    },
                },
                "numeric_profile": {
                    "columns": {
                        "feature_num": {"min": 0.0, "max": 1.0},
                        "unused_feature": {"min": -1.0, "max": 2.0},
                        "logerror": {"min": -0.1, "max": 0.1},
                    }
                },
                "boolean_like_profile": {"columns": {}},
            },
            join_profile={"left_key_coverage_rate": 0.95},
            target_profile={"p25": -0.1, "p50": 0.0, "p75": 0.1},
        )

        self.assertIn("Referenced dataset columns in visible actions: 2 / 4", text)
        self.assertIn('"parcelid"', text)
        self.assertIn('"feature_num"', text)
        self.assertNotIn('"unused_feature"', text)
        self.assertNotIn('"lookup_only"', text)
        self.assertIn("Target column: logerror", text)
