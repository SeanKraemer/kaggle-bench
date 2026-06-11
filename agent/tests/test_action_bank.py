from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ACTION_BANK_PATH = ROOT / "agent" / "action_bank.py"


def load_action_bank_module():
    spec = importlib.util.spec_from_file_location("agent_action_bank", ACTION_BANK_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load action_bank module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AgentVisibleActionBankTests(unittest.TestCase):
    def test_build_agent_visible_actions_whitelists_only_public_fields(self) -> None:
        action_bank = load_action_bank_module()
        actions = [
            {
                "action_id": "CA-1",
                "action_type": "JOIN_LOOKUP",
                "canonical_params": {"how": "left"},
                "eval_stage": "core_preprocessing",
                "role": "good",
                "difficulty": "easy",
                "equivalence_group": "g1",
                "must_follow_action_ids": ["CA-0"],
                "invalidates_action_ids": ["CA-X"],
                "conflicts_with_action_ids": ["CA-Y"],
                "reasoning": "test",
            }
        ]

        visible_actions = action_bank.build_agent_visible_actions(actions)

        self.assertEqual(len(visible_actions), 1)
        self.assertEqual(
            visible_actions[0],
            {
                "action_id": "CA-1",
                "action_type": "JOIN_LOOKUP",
                "canonical_params": {"how": "left"},
            },
        )

    def test_resolve_action_ids_filters_by_type_and_params(self) -> None:
        action_bank = load_action_bank_module()
        actions = [
            {
                "action_id": "CA-1",
                "action_type": "JOIN_LOOKUP",
                "canonical_params": {"how": "left", "right_table_id": "properties_2016"},
            },
            {
                "action_id": "CA-2",
                "action_type": "JOIN_LOOKUP",
                "canonical_params": {"how": "outer", "right_table_id": "properties_2016"},
            },
        ]

        matches = action_bank.resolve_action_ids(
            actions,
            action_type="JOIN_LOOKUP",
            canonical_param_filters={"how": "left"},
        )

        self.assertEqual(matches, ["CA-1"])

    def test_build_agent_visible_action_bank_does_not_filter_on_eval_stage(self) -> None:
        action_bank = load_action_bank_module()
        bundle = type(
            "Bundle",
            (),
            {
                "actions": [
                    {
                        "action_id": "CA-1",
                        "action_type": "JOIN_LOOKUP",
                        "canonical_params": {},
                        "eval_stage": "core_preprocessing",
                    },
                    {
                        "action_id": "CA-2",
                        "action_type": "FEATURE_SELECTION",
                        "canonical_params": {},
                        "eval_stage": "model_specific_preprocessing",
                    },
                ]
            },
        )()

        visible = action_bank.build_agent_visible_action_bank(bundle, stage_scope="primary")

        self.assertEqual([row["action_id"] for row in visible], ["CA-1", "CA-2"])
        self.assertNotIn("eval_stage", visible[0])
