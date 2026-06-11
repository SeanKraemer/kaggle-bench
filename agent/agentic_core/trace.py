from __future__ import annotations

import json
from typing import Any

from agent.agentic_core.types import AgenticRunResult, AgenticToolResult


def tool_results_jsonl(tool_results: list[AgenticToolResult]) -> str:
    lines = []
    for result in tool_results:
        lines.append(
            json.dumps(
                {
                    "tool_call_id": result.tool_call_id,
                    "name": result.name,
                    "input": result.input,
                    "output": result.output,
                    "is_error": result.is_error,
                    "error_message": result.error_message,
                },
                default=str,
            )
        )
    return "\n".join(lines) + ("\n" if lines else "")


def api_call_records_jsonl(api_call_records: list[dict[str, Any]]) -> str:
    lines = [json.dumps(record, default=str) for record in api_call_records]
    return "\n".join(lines) + ("\n" if lines else "")


def render_agentic_trace_markdown(
    *,
    title: str,
    result: AgenticRunResult,
    extra_sections: dict[str, str] | None = None,
) -> str:
    lines = [f"# {title}", ""]
    lines.append(f"- Method: `{result.method_name}`")
    if result.phase_name is not None:
        lines.append(f"- Phase: `{result.phase_name}`")
    lines.append(f"- Status: `{result.status}`")
    lines.append(f"- API calls: `{result.api_call_count}`")
    lines.append(f"- Tool calls: `{result.tool_call_count}`")
    lines.append(f"- Cost (USD): `{round(result.cumulative_cost_usd, 6)}`")
    if result.error_message:
        lines.append(f"- Error: {result.error_message}")
    lines.append("")

    if result.parsed_prediction is not None:
        prediction = result.parsed_prediction
        lines.append("## Prediction Summary")
        lines.append(f"- Parsed add ids: `{prediction.get('predicted_add_action_ids', [])}`")
        lines.append(f"- Parsed remove ids: `{prediction.get('predicted_remove_action_ids', [])}`")
        lines.append("")

    if result.validation_warnings:
        lines.append("## Validation Warnings")
        for warning in result.validation_warnings:
            lines.append(f"- {warning}")
        lines.append("")

    lines.append("## Turns")
    for turn in result.turns:
        lines.append(f"### Turn {turn.turn_index}")
        lines.append(f"- Status: `{turn.status}`")
        lines.append(f"- Input tokens: `{turn.input_tokens}`")
        lines.append(f"- Output tokens: `{turn.output_tokens}`")
        lines.append(f"- Cost (USD): `{turn.cost_usd}`")
        if turn.error_message:
            lines.append(f"- Error: {turn.error_message}")
        if turn.response_text:
            lines.append("")
            lines.append("Response:")
            lines.append("")
            lines.append(turn.response_text)
        if turn.tool_calls:
            lines.append("")
            lines.append("Tool calls:")
            for call in turn.tool_calls:
                lines.append(f"- `{call.name}` `{call.tool_call_id}` input={call.input}")
        if turn.tool_results:
            lines.append("")
            lines.append("Tool results:")
            for tool_result in turn.tool_results:
                status = "error" if tool_result.is_error else "success"
                lines.append(f"- `{tool_result.name}` `{tool_result.tool_call_id}` {status}: {tool_result.output_text}")
        lines.append("")

    for heading, content in (extra_sections or {}).items():
        lines.append(f"## {heading}")
        lines.append(content)
        lines.append("")

    return "\n".join(lines).strip() + "\n"
