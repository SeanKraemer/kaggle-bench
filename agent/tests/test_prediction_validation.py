from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "agent" / "prediction_validation.py"


def load_module():
    spec = importlib.util.spec_from_file_location("agent_prediction_validation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load prediction_validation module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PredictionValidationTests(unittest.TestCase):
    def test_parse_prediction_text_extracts_wrapped_json(self) -> None:
        module = load_module()

        parsed = module.parse_prediction_text(
            'prefix {"predicted_add_action_ids": ["CA-1"], "predicted_remove_action_ids": []} suffix'
        )

        self.assertEqual(parsed["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(parsed["predicted_remove_action_ids"], [])

    def test_parse_prediction_text_extracts_prediction_shaped_object_when_unrelated_json_follows(self) -> None:
        module = load_module()

        parsed = module.parse_prediction_text(
            '\n'.join(
                [
                    "Here is the prediction:",
                    '{"predicted_add_action_ids": ["CA-1"], "predicted_remove_action_ids": []}',
                    "Debug note:",
                    '{"irrelevant": true}',
                ]
            )
        )

        self.assertEqual(parsed["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(parsed["predicted_remove_action_ids"], [])

    def test_parse_prediction_text_prefers_last_prediction_shaped_object(self) -> None:
        module = load_module()

        parsed = module.parse_prediction_text(
            '\n'.join(
                [
                    "Template:",
                    '{"predicted_add_action_ids": [], "predicted_remove_action_ids": []}',
                    "Final answer:",
                    '{"predicted_add_action_ids": ["CA-2"], "predicted_remove_action_ids": ["CA-3"]}',
                ]
            )
        )

        self.assertEqual(parsed["predicted_add_action_ids"], ["CA-2"])
        self.assertEqual(parsed["predicted_remove_action_ids"], ["CA-3"])

    def test_parse_prediction_text_rejects_dicts_without_prediction_keys(self) -> None:
        module = load_module()

        with self.assertRaisesRegex(
            ValueError,
            "prediction payload must include predicted_add_action_ids and predicted_remove_action_ids",
        ):
            module.parse_prediction_text(
                '\n'.join(
                    [
                        "Debug note:",
                        '{"irrelevant": true}',
                        "Another object:",
                        '{"notes": "still not the prediction"}',
                    ]
                )
            )

    def test_validate_prediction_payload_normalizes_ids_rationales_and_remove_scope(self) -> None:
        module = load_module()

        payload = {
            "predicted_add_action_ids": ["CA-1", "CA-1", "CA-999", 7],
            "predicted_remove_action_ids": ["CA-1", "CA-2", "CA-2", "CA-3"],
            "notes": 123,
            "action_rationales": [
                {"action_id": "CA-1", "decision": "add", "reason": "needed"},
                {"action_id": "CA-999", "decision": "add", "reason": "unknown"},
            ],
        }

        normalized, warnings = module.validate_prediction_payload(
            payload,
            valid_action_ids={"CA-1", "CA-2", "CA-3"},
            allowed_remove_action_ids={"CA-2"},
        )

        self.assertEqual(normalized["predicted_add_action_ids"], [])
        self.assertEqual(normalized["predicted_remove_action_ids"], ["CA-2"])
        self.assertIsNone(normalized["notes"])
        self.assertEqual(
            normalized["action_rationales"],
            [{"action_id": "CA-1", "decision": "add", "reason": "needed"}],
        )
        self.assertIn("unknown_add_action_ids=['CA-999']", warnings)
        self.assertIn("dropped_non_string_add_action_ids=[7]", warnings)
        self.assertIn("deduplicated_add_action_ids=['CA-1']", warnings)
        self.assertIn("removed_conflicting_action_ids=['CA-1']", warnings)
        self.assertIn("ignored_notes=not_a_string", warnings)
        self.assertIn("ignored_rationales_for_unknown_action_ids=['CA-999']", warnings)
        self.assertIn("removed_out_of_scope_remove_action_ids=['CA-3']", warnings)

    def test_parse_and_validate_prediction_text_normalizes_wrapped_json(self) -> None:
        module = load_module()

        normalized, warnings = module.parse_and_validate_prediction_text(
            'prefix {"predicted_add_action_ids":["CA-1","CA-1"],"predicted_remove_action_ids":["CA-2"]} suffix',
            valid_action_ids={"CA-1", "CA-2"},
            allowed_remove_action_ids=set(),
        )

        self.assertEqual(normalized["predicted_add_action_ids"], ["CA-1"])
        self.assertEqual(normalized["predicted_remove_action_ids"], [])
        self.assertIn("deduplicated_add_action_ids=['CA-1']", warnings)
        self.assertIn("removed_out_of_scope_remove_action_ids=['CA-2']", warnings)
