from __future__ import annotations

from agent.prompts.shared import render_shared_prompt, render_shared_prompt_parts

GENERIC_AGENT_INSTRUCTION = """Use only the generic tools exposed by this run:
{tool_allowlist}

The [Candidate actions] section contains the full visible candidate action bank.
You may inspect the prepared workspace files, raw dataset files under `dataset/`, and `candidate_actions_visible.json` for tool-based checks.
Use tools only to gather concise evidence needed for the prediction. Avoid printing or relying on large verbatim file dumps.
Each python tool call runs in a fresh process: reload files inside each call and do not rely on variables from earlier tool calls.
Do not assume pandas or other third-party packages are installed; use the Python standard library such as json, csv, collections, and statistics unless you have verified availability.
Do not import or call repository benchmark helpers such as `agent.*`, `agent.tool_registry`, `agent.profiles`, `agent.context_builder`, or `agent.data_access` from inside tool calls.
Do not use hidden action metadata, gold labels, evaluation results, or invented preprocessing actions.

Use only visible candidate actions and dataset/context evidence.
Only return add IDs that are missing from the current context, and remove IDs that are present in current context_action_ids.
Keep the repair compact and return only the required JSON prediction."""


def build_generic_output_format() -> str:
    return (
        "Return ONLY a single JSON object with required keys `predicted_add_action_ids` and "
        "`predicted_remove_action_ids`, each containing arrays of candidate action IDs. "
        "You may also include optional `notes` and optional `action_rationales`, where "
        "`action_rationales` is an array of objects with `action_id`, `decision`, and `reason`. "
        "Do not output any prose outside the JSON object unless you have already written "
        "`prediction.json` in the prepared workspace."
    )


def build_generic_agent_prompt(
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


def build_generic_agent_prompt_parts(
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


def _method_instruction(*, tool_names: list[str] | None) -> str:
    names = tool_names or []
    tool_allowlist = "\n".join(f"- `{name}`" for name in names)
    return GENERIC_AGENT_INSTRUCTION.format(tool_allowlist=tool_allowlist)
