from __future__ import annotations

from agent.prompts.shared import render_shared_prompt, render_shared_prompt_parts

SINGLE_LLM_INSTRUCTION = (
    "Produce add/remove predictions in one pass without tool use. "
    "Do not ask follow-up questions. Use only the provided benchmark instance "
    "materials and return a single structured JSON prediction."
)


def build_single_llm_prompt(
    *,
    task_text: str,
    dataset_summary: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
) -> str:
    return render_shared_prompt(
        task_text=task_text,
        method_instruction=SINGLE_LLM_INSTRUCTION,
        dataset_summary=dataset_summary,
        context_summary=context_summary,
        candidate_actions=candidate_actions,
        output_format=output_format,
    )


def build_single_llm_prompt_parts(
    *,
    task_text: str,
    dataset_summary: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
) -> dict[str, str]:
    return render_shared_prompt_parts(
        task_text=task_text,
        method_instruction=SINGLE_LLM_INSTRUCTION,
        dataset_summary=dataset_summary,
        context_summary=context_summary,
        candidate_actions=candidate_actions,
        output_format=output_format,
    )
