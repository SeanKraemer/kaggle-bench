from __future__ import annotations

import json
from typing import Any

from agent.prompts.shared import render_shared_prompt, render_shared_prompt_parts

PROPOSED_AGENT_INSTRUCTION = """Use only the benchmark-specific tools exposed by this run.

The available tools are:
{tool_allowlist}

Do not use bash, Python, shell commands, notebooks, or general filesystem exploration.
Do not import or call repository helpers directly.
Do not use hidden action metadata, gold labels, evaluation results, or invented preprocessing actions.

This method runs in two phases:
- add phase: identify missing beneficial inactive candidate actions
- remove phase: identify harmful active context actions

Use the provided summaries and benchmark-specific tools only to gather evidence needed for the current decision.
The [Candidate actions] section contains the full visible candidate action bank.
Do not treat tool-provided summaries or groupings as sufficient evidence by themselves; verify final action IDs against the visible candidate action bank and current context.
Prefer a compact, evidence-backed repair set over broad speculative edits.
Only choose action IDs from the visible candidate action bank."""

ADD_PHASE_INSTRUCTION = """[Phase instruction]
You are in add phase.

Find inactive candidate actions that should be added to repair the current pipeline.
Do not propose removals in this phase.
`predicted_remove_action_ids` must be an empty array.
Only include action IDs that are visible in the candidate bank and not currently active in `context_action_ids`.
Return only the JSON object for this phase."""


REMOVE_PHASE_INSTRUCTION = """[Phase instruction]
You are in remove phase.

Find active context actions that are harmful and should be removed.
Do not propose additions in this phase.
`predicted_add_action_ids` must be an empty array.
Only include action IDs that are visible in the candidate bank and currently active in `context_action_ids`.

Use the add-phase result below only to reason about compatibility between selected additions and current active actions.
Remove an active action only when there is clear evidence that it blocks, conflicts with, or harms the repaired pipeline state.
Do not remove active actions that remain compatible with the selected repair set.
Return only the JSON object for this phase.

[Add-phase result]
{add_phase_result}"""


def build_proposed_output_format() -> str:
    return (
        "Return ONLY a single JSON object with required keys `phase`, "
        "`predicted_add_action_ids`, and `predicted_remove_action_ids`. "
        "`phase` must be either `add` or `remove` for the current phase. "
        "The prediction fields must be arrays of candidate action IDs. "
        "You may also include optional `notes` and optional `action_rationales`, "
        "where `action_rationales` is an array of objects with `action_id`, "
        "`decision`, and `reason`. Do not output prose outside the JSON object."
    )


def build_proposed_agent_prompt(
    *,
    task_text: str,
    dataset_summary: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
    tool_names: list[str] | None = None,
) -> str:
    return render_shared_prompt(
        task_text=task_text,
        method_instruction=_method_instruction(tool_names=tool_names),
        dataset_summary=dataset_summary,
        context_summary=context_summary,
        candidate_actions=candidate_actions,
        output_format=output_format,
    )


def build_proposed_agent_prompt_parts(
    *,
    task_text: str,
    dataset_summary: str,
    context_summary: str,
    candidate_actions: str,
    output_format: str,
    tool_names: list[str] | None = None,
) -> dict[str, str]:
    return render_shared_prompt_parts(
        task_text=task_text,
        method_instruction=_method_instruction(tool_names=tool_names),
        dataset_summary=dataset_summary,
        context_summary=context_summary,
        candidate_actions=candidate_actions,
        output_format=output_format,
    )


def build_add_phase_prompt_text(base_prompt: str) -> str:
    return "\n\n".join([base_prompt.strip(), ADD_PHASE_INSTRUCTION.strip()])


def build_remove_phase_prompt_text(base_prompt: str, add_phase_result: dict[str, Any]) -> str:
    rendered_add_result = json.dumps(add_phase_result, indent=2, sort_keys=True)
    return "\n\n".join(
        [
            base_prompt.strip(),
            REMOVE_PHASE_INSTRUCTION.format(add_phase_result=rendered_add_result).strip(),
        ]
    )


def build_add_phase_message_content_blocks(dynamic_prompt: str) -> list[dict[str, str]]:
    return [
        {
            "type": "text",
            "text": "\n\n".join([dynamic_prompt.strip(), ADD_PHASE_INSTRUCTION.strip()]),
        }
    ]


def build_remove_phase_message_content_blocks(
    dynamic_prompt: str,
    add_phase_result: dict[str, Any],
) -> list[dict[str, str]]:
    rendered_add_result = json.dumps(add_phase_result, indent=2, sort_keys=True)
    return [
        {
            "type": "text",
            "text": "\n\n".join(
                [
                    dynamic_prompt.strip(),
                    REMOVE_PHASE_INSTRUCTION.format(add_phase_result=rendered_add_result).strip(),
                ]
            ),
        }
    ]


def _method_instruction(*, tool_names: list[str] | None) -> str:
    names = tool_names or []
    tool_allowlist = "\n".join(f"- `{name}`" for name in names)
    return PROPOSED_AGENT_INSTRUCTION.format(tool_allowlist=tool_allowlist)
