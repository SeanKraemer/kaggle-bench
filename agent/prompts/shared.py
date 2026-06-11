from __future__ import annotations


COMMON_TASK_GUIDANCE = """You are solving a benchmark instance for preprocessing diagnosis and repair in a tabular ML workflow.

This is a constrained action-selection task, not an open-ended pipeline design task.
You must choose only from the provided candidate action bank.

The testcase defines the current pipeline state through `context_action_ids`.
Your goal is to produce a minimal, defensible repair of that current pipeline state.

Interpret the outputs strictly as:
- `predicted_add_action_ids`: actions from the candidate bank that are not currently active but should be added.
- `predicted_remove_action_ids`: actions that are currently active in `context_action_ids` and should be removed because they are harmful in the current state.

Important constraints:
- Do not invent actions outside the candidate bank.
- Do not include actions just because they are generally useful in tabular ML.
- Prefer a small, high-confidence edit set over a broad speculative pipeline.
- Do not put an action in `predicted_remove_action_ids` unless it is currently active.
- If `context_action_ids` is empty, `predicted_remove_action_ids` should normally be empty.
- Use dataset evidence only to judge whether candidate actions are necessary and appropriate for this benchmark instance."""


def render_shared_prompt_parts(
    *,
    task_text: str,
    method_instruction: str,
    dataset_summary: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
) -> dict[str, str]:
    task_block = "[TASK]\n" + task_text.strip() + "\n\n" + COMMON_TASK_GUIDANCE
    method_block = "[Method-specific instruction]\n" + method_instruction.strip()
    dataset_block = "[Dataset summary]\n" + dataset_summary.strip()
    context_block = "[Current context (testcase)]\n" + context_summary.strip()
    candidate_block = "[Candidate actions]\n" + candidate_actions.strip()
    output_block = "[Output format]\n" + output_format.strip()
    return {
        "static_prompt": "\n\n".join(
            [
                task_block,
                method_block,
                dataset_block,
                candidate_block,
                output_block,
            ]
        ),
        "dynamic_prompt": context_block,
        "full_prompt": "\n\n".join(
            [
                task_block,
                method_block,
                dataset_block,
                context_block,
                candidate_block,
                output_block,
            ]
        ),
    }


def render_shared_prompt(
    *,
    task_text: str,
    method_instruction: str,
    dataset_summary: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
) -> str:
    return render_shared_prompt_parts(
        task_text=task_text,
        method_instruction=method_instruction,
        dataset_summary=dataset_summary,
        context_summary=context_summary,
        candidate_actions=candidate_actions,
        output_format=output_format,
    )["full_prompt"]
