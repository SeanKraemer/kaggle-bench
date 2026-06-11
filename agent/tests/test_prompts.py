from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED_PATH = ROOT / "agent" / "prompts" / "shared.py"
SINGLE_LLM_PATH = ROOT / "agent" / "prompts" / "single_llm.py"
CLAUDE_CODE_PATH = ROOT / "agent" / "prompts" / "claude_code.py"
GENERIC_AGENT_PATH = ROOT / "agent" / "prompts" / "generic_agent.py"
PROPOSED_AGENT_PATH = ROOT / "agent" / "prompts" / "proposed_agent.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PromptTests(unittest.TestCase):
    def test_shared_scaffold_renders_all_sections(self) -> None:
        shared = load_module(SHARED_PATH, "agent_prompts_shared")

        prompt = shared.render_shared_prompt(
            task_text="task text",
            method_instruction="method text",
            dataset_summary="dataset text",
            context_summary="context text",
            candidate_actions="actions text",
            output_format="output text",
        )

        self.assertIn("[TASK]", prompt)
        self.assertIn("[Method-specific instruction]", prompt)
        self.assertIn("[Dataset summary]", prompt)
        self.assertIn("[Current context (testcase)]", prompt)
        self.assertIn("[Candidate actions]", prompt)
        self.assertIn("[Output format]", prompt)

    def test_shared_prompt_states_benchmark_repair_constraints(self) -> None:
        shared = load_module(SHARED_PATH, "agent_prompts_shared")

        prompt = shared.render_shared_prompt(
            task_text="task text",
            method_instruction="method text",
            dataset_summary="dataset text",
            context_summary="context text",
            candidate_actions="actions text",
            output_format="output text",
        )

        self.assertIn("constrained action-selection task", prompt)
        self.assertIn("current pipeline state", prompt)
        self.assertIn("predicted_add_action_ids", prompt)
        self.assertIn("predicted_remove_action_ids", prompt)
        self.assertIn("Do not invent actions outside the candidate bank", prompt)
        self.assertIn("Do not include actions just because they are generally useful", prompt)
        self.assertIn("If `context_action_ids` is empty", prompt)

    def test_single_llm_prompt_mentions_one_pass_behavior(self) -> None:
        single_llm = load_module(SINGLE_LLM_PATH, "agent_prompts_single_llm")

        prompt = single_llm.build_single_llm_prompt(
            task_text="repair Zillow preprocessing",
            dataset_summary="summary",
            context_summary="context",
            candidate_actions='[{"action_id":"CA-1"}]',
            output_format="return JSON with predicted_add_action_ids, predicted_remove_action_ids, optional notes, optional action_rationales",
        )

        self.assertIn("one pass", prompt.lower())
        self.assertIn("without tool use", prompt.lower())
        self.assertIn("CA-1", prompt)
        self.assertIn("optional action_rationales", prompt)

    def test_shared_prompt_can_be_split_into_cacheable_static_and_dynamic_parts(self) -> None:
        shared = load_module(SHARED_PATH, "agent_prompts_shared")

        prompt_parts = shared.render_shared_prompt_parts(
            task_text="task text",
            method_instruction="method text",
            dataset_summary="dataset text",
            context_summary="context text",
            candidate_actions="actions text",
            output_format="output text",
        )

        self.assertIn("[TASK]", prompt_parts["full_prompt"])
        self.assertIn("[Current context (testcase)]", prompt_parts["dynamic_prompt"])
        self.assertIn("[Candidate actions]", prompt_parts["static_prompt"])
        self.assertNotIn("[Current context (testcase)]", prompt_parts["static_prompt"])

    def test_claude_code_prompt_mentions_prediction_file(self) -> None:
        claude_code = load_module(CLAUDE_CODE_PATH, "agent_prompts_claude_code")

        prompt = claude_code.build_claude_code_prompt(
            task_text="repair Zillow preprocessing",
            context_summary="context",
            candidate_actions='[{"action_id":"CA-1"}]',
            output_format="return JSON",
            prediction_filename="prediction.json",
            dataset_symlink_path="dataset",
        )

        self.assertIn("prediction.json", prompt)
        self.assertIn("dataset", prompt)
        self.assertIn("write", prompt.lower())
        self.assertIn("No precomputed dataset summary is provided", prompt)
        self.assertIn("Avoid loading large dataset files fully into memory", prompt)

    def test_generic_agent_prompt_mentions_generic_only_tools(self) -> None:
        generic_agent = load_module(GENERIC_AGENT_PATH, "agent_prompts_generic_agent")

        prompt = generic_agent.build_generic_agent_prompt(
            task_text="repair Zillow preprocessing",
            dataset_summary="No precomputed dataset summary is provided",
            context_summary="context",
            candidate_actions='[{"action_id":"CA-1"}]',
            output_format="return JSON with predicted_add_action_ids and predicted_remove_action_ids",
            tool_names=["bash", "python", "scratchpad_read", "scratchpad_write"],
        )

        self.assertIn("generic tools", prompt.lower())
        self.assertIn("bash", prompt)
        self.assertIn("python", prompt)
        self.assertIn("scratchpad_read", prompt)
        self.assertIn("predicted_add_action_ids", prompt)
        self.assertIn("predicted_remove_action_ids", prompt)
        self.assertIn("prepared workspace files", prompt)
        self.assertIn("raw dataset files under `dataset/`", prompt)
        self.assertIn("full visible candidate action bank", prompt)
        self.assertIn("candidate_actions_visible.json", prompt)
        self.assertIn("Use only visible candidate actions", prompt)
        self.assertIn("fresh process", prompt)
        self.assertIn("Do not import or call repository benchmark helpers", prompt)
        self.assertIn("agent.tool_registry", prompt)
        self.assertIn("agent.profiles", prompt)
        self.assertIn("Do not assume pandas", prompt)

    def test_proposed_agent_prompt_mentions_specific_tools_and_phase_contract(self) -> None:
        proposed_agent = load_module(PROPOSED_AGENT_PATH, "agent_prompts_proposed_agent")

        prompt = proposed_agent.build_proposed_agent_prompt(
            task_text="repair Zillow preprocessing",
            dataset_summary="Primary train profile",
            context_summary="context",
            candidate_actions='[{"action_id":"CA-1"}]',
            output_format=proposed_agent.build_proposed_output_format(),
            tool_names=[
                "lookup_actions",
                "inspect_columns",
                "scratchpad_read",
                "scratchpad_write",
            ],
        )
        add_prompt = proposed_agent.build_add_phase_prompt_text(prompt)
        remove_prompt = proposed_agent.build_remove_phase_prompt_text(
            prompt,
            {
                "phase": "add",
                "predicted_add_action_ids": ["CA-1"],
                "predicted_remove_action_ids": [],
            },
        )

        self.assertIn("benchmark-specific tools", prompt)
        self.assertIn("lookup_actions", prompt)
        self.assertIn("inspect_columns", prompt)
        self.assertIn("scratchpad_write", prompt)
        self.assertIn("Do not use bash", prompt)
        self.assertIn("Python", prompt)
        self.assertIn("full visible candidate action bank", prompt)
        self.assertIn("visible candidate action bank", prompt)
        self.assertIn("phase", prompt)
        self.assertIn("predicted_add_action_ids", prompt)
        self.assertIn("predicted_remove_action_ids", prompt)
        self.assertIn("You are in add phase", add_prompt)
        self.assertIn("predicted_remove_action_ids` must be an empty array", add_prompt)
        self.assertIn("You are in remove phase", remove_prompt)
        self.assertIn("Use the add-phase result below", remove_prompt)
        self.assertIn("blocks, conflicts with, or harms", remove_prompt)
        self.assertIn("Do not remove active actions that remain compatible", remove_prompt)
        self.assertIn("CA-1", remove_prompt)
