from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "agent" / "rule_based" / "policy.py"
DECISION_RECORDS_PATH = ROOT / "agent" / "rule_based" / "decision_records.py"


def load_policy_module():
    spec = importlib.util.spec_from_file_location("agent_rule_based_policy", POLICY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load rule_based policy module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_decision_records_module():
    spec = importlib.util.spec_from_file_location("agent_rule_based_decision_records", DECISION_RECORDS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load rule_based decision_records module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RuleBasedPolicyTests(unittest.TestCase):
    def test_build_decision_record_shape(self) -> None:
        decision_records = load_decision_records_module()

        record = decision_records.build_decision_record(
            action={"action_id": "CA-1", "action_type": "JOIN_LOOKUP"},
            candidate_side="add",
            decision="selected_add",
            triggered_rule="should_add_join",
            details=["how=left", "threshold=0.8"],
        )

        self.assertEqual(
            record,
            {
                "action_id": "CA-1",
                "action_type": "JOIN_LOOKUP",
                "candidate_side": "add",
                "decision": "selected_add",
                "triggered_rule": "should_add_join",
                "details": ["how=left", "threshold=0.8"],
            },
        )

    def test_predict_actions_adds_conservative_core_steps(self) -> None:
        policy = load_policy_module()
        actions = [
            {"action_id": "CA-JOIN-GOOD", "action_type": "JOIN_LOOKUP", "canonical_params": {"how": "left", "right_table_id": "lookup_table"}},
            {"action_id": "CA-JOIN-BAD", "action_type": "JOIN_LOOKUP", "canonical_params": {"how": "outer", "right_table_id": "lookup_table"}},
            {"action_id": "CA-PARSE", "action_type": "PARSE_DATETIME", "canonical_params": {"columns": ["transactiondate"]}},
            {"action_id": "CA-MEDIAN", "action_type": "IMPUTE_MISSING", "canonical_params": {"strategy": "median", "columns": ["feature_num"]}},
            {"action_id": "CA-DROP", "action_type": "DROP_COLUMNS", "canonical_params": {"columns": ["entity_id", "target_value", "event_date"]}},
            {"action_id": "CA-ONEHOT", "action_type": "ENCODE_CATEGORICAL", "canonical_params": {"method": "onehot", "columns": ["category_code"]}},
            {"action_id": "CA-DATEPART", "action_type": "DATE_PART_FEATURE", "canonical_params": {"date_columns": ["event_date"], "parts": ["month"], "drop_original": False}},
            {"action_id": "CA-INDICATOR", "action_type": "CREATE_MISSING_INDICATOR", "canonical_params": {"columns": ["feature_num"], "indicator_suffix": "_missing"}},
            {"action_id": "CA-HIGHNULL", "action_type": "DROP_HIGH_NULL_COLUMNS", "canonical_params": {"columns": ["mostly_null"], "null_ratio_threshold": 0.9}},
            {"action_id": "CA-CLIP", "action_type": "CLIP_OUTLIERS", "canonical_params": {"columns": ["heavy_tail"], "method": "iqr", "iqr_k": 1.5}},
        ]

        predictions = policy.predict_actions(
            actions=actions,
            context_action_ids=[],
            dataset_insights={
                "join_profile": {"left_key_coverage_rate": 0.95},
                "schema_profile": {
                    "row_count": 100,
                    "columns": {
                        "transactiondate": {"inferred_type": "datetime_like", "distinct_count": 90, "distinct_ratio": 0.9},
                        "event_date": {"inferred_type": "datetime_like", "distinct_count": 90, "distinct_ratio": 0.9},
                        "entity_id": {"inferred_type": "integer_like", "distinct_count": 100, "distinct_ratio": 1.0},
                        "target_value": {"inferred_type": "numeric_like", "distinct_count": 100, "distinct_ratio": 1.0},
                        "category_code": {"inferred_type": "string", "distinct_count": 5, "distinct_ratio": 0.05},
                        "feature_num": {"inferred_type": "numeric_like", "distinct_count": 50, "distinct_ratio": 0.5},
                        "mostly_null": {"inferred_type": "string", "distinct_count": 2, "distinct_ratio": 0.02},
                        "heavy_tail": {"inferred_type": "numeric_like", "distinct_count": 80, "distinct_ratio": 0.8},
                    },
                },
                "missingness_profile": {"columns": {"feature_num": {"missing_rate": 0.3}, "mostly_null": {"missing_rate": 0.96}}},
                "numeric_profile": {
                    "columns": {
                        "feature_num": {"min": 0.0, "max": 10.0, "p25": 1.0, "p75": 3.0, "distinct_count": 10},
                        "target_value": {"min": -5.0, "max": 5.0, "p25": -1.0, "p75": 1.0, "distinct_count": 100},
                        "heavy_tail": {"min": 0.0, "max": 1000.0, "p25": 10.0, "p75": 20.0, "distinct_count": 80},
                    }
                },
                "boolean_like_profile": {"columns": {}},
                "target_column": "target_value",
                "primary_key": "entity_id",
            },
        )

        self.assertEqual(predictions["predicted_remove_action_ids"], [])
        self.assertIn("CA-JOIN-GOOD", predictions["predicted_add_action_ids"])
        self.assertNotIn("CA-JOIN-BAD", predictions["predicted_add_action_ids"])
        self.assertIn("CA-PARSE", predictions["predicted_add_action_ids"])
        self.assertIn("CA-MEDIAN", predictions["predicted_add_action_ids"])
        self.assertIn("CA-DROP", predictions["predicted_add_action_ids"])
        self.assertIn("CA-ONEHOT", predictions["predicted_add_action_ids"])
        self.assertIn("CA-DATEPART", predictions["predicted_add_action_ids"])
        self.assertIn("CA-INDICATOR", predictions["predicted_add_action_ids"])
        self.assertIn("CA-HIGHNULL", predictions["predicted_add_action_ids"])
        self.assertIn("CA-CLIP", predictions["predicted_add_action_ids"])

    def test_predict_actions_removes_obviously_bad_context_actions(self) -> None:
        policy = load_policy_module()
        actions = [
            {"action_id": "CA-BAD-JOIN", "action_type": "JOIN_LOOKUP", "canonical_params": {"how": "outer", "right_table_id": "lookup_table"}},
            {"action_id": "CA-BAD-DROP", "action_type": "DROP_COLUMNS", "canonical_params": {"columns": ["entity_id"]}},
            {"action_id": "CA-BAD-FILTER", "action_type": "FILTER_ROWS", "canonical_params": {"predicate": "(measurement > -0.04) and (measurement < 0.04)"}},
        ]

        predictions = policy.predict_actions(
            actions=actions,
            context_action_ids=["CA-BAD-JOIN", "CA-BAD-DROP", "CA-BAD-FILTER"],
            dataset_insights={
                "join_profile": {"left_key_coverage_rate": 0.95},
                "schema_profile": {
                    "columns": {
                        "entity_id": {"inferred_type": "integer_like", "distinct_count": 100, "distinct_ratio": 1.0},
                        "measurement": {"inferred_type": "numeric_like", "distinct_count": 80, "distinct_ratio": 0.8},
                    }
                },
                "missingness_profile": {"columns": {}},
                "numeric_profile": {"columns": {"measurement": {"min": -10.0, "max": 10.0, "p25": -2.0, "p75": 2.0, "distinct_count": 80}}},
                "boolean_like_profile": {"columns": {}},
                "target_column": "target_value",
                "primary_key": "entity_id",
            },
        )

        self.assertEqual(predictions["predicted_add_action_ids"], [])
        self.assertEqual(
            set(predictions["predicted_remove_action_ids"]),
            {"CA-BAD-JOIN", "CA-BAD-DROP", "CA-BAD-FILTER"},
        )

    def test_predict_actions_removes_incompatible_context_families(self) -> None:
        policy = load_policy_module()
        actions = [
            {"action_id": "CA-BAD-PARSE", "action_type": "PARSE_DATETIME", "canonical_params": {"columns": ["region_code"]}},
            {
                "action_id": "CA-BAD-DATEPART",
                "action_type": "DATE_PART_FEATURE",
                "canonical_params": {"date_columns": ["region_code"], "parts": ["month"], "drop_original": False},
            },
            {
                "action_id": "CA-BAD-MEDIAN",
                "action_type": "IMPUTE_MISSING",
                "canonical_params": {"strategy": "median", "columns": ["region_code"]},
            },
            {
                "action_id": "CA-BAD-FALSE-FILL",
                "action_type": "IMPUTE_MISSING",
                "canonical_params": {"strategy": "constant", "fill_value": "FALSE", "columns": ["feature_num"]},
            },
            {
                "action_id": "CA-BAD-ZERO-FILL",
                "action_type": "IMPUTE_MISSING",
                "canonical_params": {"strategy": "constant", "fill_value": 0, "columns": ["signed_value"]},
            },
            {
                "action_id": "CA-BAD-INDICATOR",
                "action_type": "CREATE_MISSING_INDICATOR",
                "canonical_params": {"columns": ["low_missing"], "indicator_suffix": "_missing"},
            },
            {
                "action_id": "CA-BAD-HIGHNULL",
                "action_type": "DROP_HIGH_NULL_COLUMNS",
                "canonical_params": {"columns": ["low_missing"], "null_ratio_threshold": 0.9},
            },
            {
                "action_id": "CA-BAD-ENCODE",
                "action_type": "ENCODE_CATEGORICAL",
                "canonical_params": {"method": "onehot", "columns": ["entity_id"]},
            },
            {
                "action_id": "CA-BAD-CLIP",
                "action_type": "CLIP_OUTLIERS",
                "canonical_params": {"columns": ["flat_feature"], "method": "iqr", "iqr_k": 1.5},
            },
            {
                "action_id": "CA-BAD-INNER-JOIN",
                "action_type": "JOIN_LOOKUP",
                "canonical_params": {"how": "inner", "right_table_id": "lookup_table"},
            },
        ]

        predictions = policy.predict_actions(
            actions=actions,
            context_action_ids=[action["action_id"] for action in actions],
            dataset_insights={
                "join_profile": {"left_key_coverage_rate": 0.4},
                "schema_profile": {
                    "columns": {
                        "entity_id": {"inferred_type": "integer_like", "distinct_count": 100, "distinct_ratio": 1.0},
                        "region_code": {"inferred_type": "string", "distinct_count": 50, "distinct_ratio": 0.5},
                        "feature_num": {"inferred_type": "numeric_like", "distinct_count": 40, "distinct_ratio": 0.4},
                        "signed_value": {"inferred_type": "numeric_like", "distinct_count": 30, "distinct_ratio": 0.3},
                        "low_missing": {"inferred_type": "numeric_like", "distinct_count": 20, "distinct_ratio": 0.2},
                        "flat_feature": {"inferred_type": "numeric_like", "distinct_count": 10, "distinct_ratio": 0.1},
                    }
                },
                "missingness_profile": {
                    "columns": {
                        "region_code": {"missing_rate": 0.3},
                        "feature_num": {"missing_rate": 0.3},
                        "signed_value": {"missing_rate": 0.3},
                        "low_missing": {"missing_rate": 0.01},
                        "flat_feature": {"missing_rate": 0.0},
                    }
                },
                "numeric_profile": {
                    "columns": {
                        "feature_num": {"min": 0.0, "max": 10.0, "p25": 2.0, "p75": 4.0, "distinct_count": 40},
                        "signed_value": {"min": -5.0, "max": 10.0, "p25": -1.0, "p75": 3.0, "distinct_count": 30},
                        "low_missing": {"min": 0.0, "max": 5.0, "p25": 1.0, "p75": 3.0, "distinct_count": 20},
                        "flat_feature": {"min": 9.0, "max": 13.0, "p25": 10.0, "p75": 12.0, "distinct_count": 10},
                    }
                },
                "boolean_like_profile": {"columns": {}},
                "target_column": "target_value",
                "primary_key": "entity_id",
            },
        )

        self.assertEqual(predictions["predicted_add_action_ids"], [])
        self.assertEqual(
            set(predictions["predicted_remove_action_ids"]),
            {action["action_id"] for action in actions},
        )
