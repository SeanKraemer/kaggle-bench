from __future__ import annotations

import unittest

from agent.proposed_agent.reconciliation import (
    reconcile_phase_outputs,
    validate_add_phase,
    validate_remove_phase,
)


class ProposedAgentReconciliationTests(unittest.TestCase):
    def test_add_phase_rejects_remove_decisions(self) -> None:
        with self.assertRaises(ValueError):
            validate_add_phase(
                {
                    "phase": "add",
                    "predicted_add_action_ids": [],
                    "predicted_remove_action_ids": ["CA-2"],
                },
                valid_action_ids={"CA-1", "CA-2"},
                active_action_ids={"CA-2"},
            )

    def test_remove_phase_rejects_add_decisions(self) -> None:
        with self.assertRaises(ValueError):
            validate_remove_phase(
                {
                    "phase": "remove",
                    "predicted_add_action_ids": ["CA-1"],
                    "predicted_remove_action_ids": [],
                },
                valid_action_ids={"CA-1", "CA-2"},
                active_action_ids={"CA-2"},
            )

    def test_add_phase_normalizes_unknown_duplicate_and_active_ids(self) -> None:
        prediction, warnings = validate_add_phase(
            {
                "phase": "add",
                "predicted_add_action_ids": ["CA-1", "CA-1", "CA-X", "CA-2"],
                "predicted_remove_action_ids": [],
            },
            valid_action_ids={"CA-1", "CA-2"},
            active_action_ids={"CA-2"},
        )

        self.assertEqual(prediction["predicted_add_action_ids"], ["CA-1"])
        self.assertIn("unknown_add_action_ids=['CA-X']", warnings)
        self.assertIn("deduplicated_add_action_ids=['CA-1']", warnings)
        self.assertIn("dropped_active_add_action_ids=['CA-2']", warnings)

    def test_remove_phase_normalizes_unknown_duplicate_and_inactive_ids(self) -> None:
        prediction, warnings = validate_remove_phase(
            {
                "phase": "remove",
                "predicted_add_action_ids": [],
                "predicted_remove_action_ids": ["CA-2", "CA-2", "CA-X", "CA-1"],
            },
            valid_action_ids={"CA-1", "CA-2"},
            active_action_ids={"CA-2"},
        )

        self.assertEqual(prediction["predicted_remove_action_ids"], ["CA-2"])
        self.assertIn("unknown_remove_action_ids=['CA-X']", warnings)
        self.assertIn("deduplicated_remove_action_ids=['CA-2']", warnings)
        self.assertIn("dropped_inactive_remove_action_ids=['CA-1']", warnings)

    def test_reconciliation_keeps_remove_side_on_conflict(self) -> None:
        prediction, warnings = reconcile_phase_outputs(
            add_prediction={
                "phase": "add",
                "predicted_add_action_ids": ["CA-1", "CA-2"],
                "predicted_remove_action_ids": [],
            },
            remove_prediction={
                "phase": "remove",
                "predicted_add_action_ids": [],
                "predicted_remove_action_ids": ["CA-2"],
            },
            valid_action_ids={"CA-1", "CA-2"},
            active_action_ids={"CA-2"},
        )

        self.assertEqual(prediction["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(prediction["predicted_remove_action_ids"], ["CA-2"])
        self.assertIn(
            "reconciliation_kept_remove_and_dropped_add_conflicts=['CA-2']",
            warnings,
        )

    def test_reconciliation_auto_removes_active_drop_that_blocks_selected_raw_column(self) -> None:
        prediction, warnings = reconcile_phase_outputs(
            add_prediction={
                "phase": "add",
                "predicted_add_action_ids": ["ADD-GROUP-FEATURE"],
                "predicted_remove_action_ids": [],
            },
            remove_prediction={
                "phase": "remove",
                "predicted_add_action_ids": [],
                "predicted_remove_action_ids": [],
            },
            valid_action_ids={"ADD-GROUP-FEATURE", "DROP-RAW-ID"},
            active_action_ids={"DROP-RAW-ID"},
            visible_actions=[
                {
                    "action_id": "ADD-GROUP-FEATURE",
                    "action_type": "APPLY_EXPRESSION",
                    "canonical_params": {
                        "expression": "Split CustomerId into group and sequence features",
                        "output_columns": ["CustomerGroup", "CustomerSequence"],
                    },
                },
                {
                    "action_id": "DROP-RAW-ID",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {
                        "columns": ["CustomerId"],
                        "reason": "drop_raw_identifier_before_group_features",
                    },
                },
            ],
        )

        self.assertEqual(prediction["predicted_add_action_ids"], ["ADD-GROUP-FEATURE"])
        self.assertEqual(prediction["predicted_remove_action_ids"], ["DROP-RAW-ID"])
        self.assertTrue(
            any(
                warning.startswith("auto_added_remove_raw_column_blockers=")
                and "DROP-RAW-ID" in warning
                and "ADD-GROUP-FEATURE" in warning
                and "CustomerId" in warning
                for warning in warnings
            )
        )

    def test_reconciliation_auto_removes_active_drop_that_blocks_expression_source_column(self) -> None:
        prediction, warnings = reconcile_phase_outputs(
            add_prediction={
                "phase": "add",
                "predicted_add_action_ids": ["ADD-SPLIT-RAW"],
                "predicted_remove_action_ids": [],
            },
            remove_prediction={
                "phase": "remove",
                "predicted_add_action_ids": [],
                "predicted_remove_action_ids": [],
            },
            valid_action_ids={"ADD-SPLIT-RAW", "DROP-RAW-COMPOSITE"},
            active_action_ids={"DROP-RAW-COMPOSITE"},
            visible_actions=[
                {
                    "action_id": "ADD-SPLIT-RAW",
                    "action_type": "APPLY_EXPRESSION",
                    "canonical_params": {
                        "expression": "Split RawComposite into PartA and PartB",
                        "output_columns": ["PartA", "PartB"],
                    },
                },
                {
                    "action_id": "DROP-RAW-COMPOSITE",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {
                        "columns": ["RawComposite"],
                        "reason": "drop_raw_composite_before_feature_extraction",
                    },
                },
            ],
        )

        self.assertEqual(prediction["predicted_remove_action_ids"], ["DROP-RAW-COMPOSITE"])
        self.assertTrue(any("RawComposite" in warning for warning in warnings))

    def test_reconciliation_does_not_auto_remove_safe_post_feature_cleanup_drop(self) -> None:
        prediction, warnings = reconcile_phase_outputs(
            add_prediction={
                "phase": "add",
                "predicted_add_action_ids": ["ADD-GROUP-FEATURE"],
                "predicted_remove_action_ids": [],
            },
            remove_prediction={
                "phase": "remove",
                "predicted_add_action_ids": [],
                "predicted_remove_action_ids": [],
            },
            valid_action_ids={"ADD-GROUP-FEATURE", "DROP-POST-FEATURE-ID"},
            active_action_ids={"DROP-POST-FEATURE-ID"},
            visible_actions=[
                {
                    "action_id": "ADD-GROUP-FEATURE",
                    "action_type": "APPLY_EXPRESSION",
                    "canonical_params": {
                        "expression": "Split CustomerId into group and sequence features",
                        "output_columns": ["CustomerGroup", "CustomerSequence"],
                    },
                },
                {
                    "action_id": "DROP-POST-FEATURE-ID",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {
                        "columns": ["CustomerId"],
                        "reason": "remove_identifier_high_cardinality_or_post_split_columns",
                    },
                },
            ],
        )

        self.assertEqual(prediction["predicted_remove_action_ids"], [])
        self.assertFalse(
            any(warning.startswith("auto_added_remove_raw_column_blockers=") for warning in warnings)
        )


if __name__ == "__main__":
    unittest.main()
