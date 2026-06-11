from __future__ import annotations

import json
from collections import Counter

from agent.claude_code.stream import collect_assistant_messages, collect_thinking_text, collect_tool_calls


def _append_tool_input(trace_lines: list[str], tool_call: dict) -> None:
    tool_input = tool_call.get("input")
    if tool_call.get("name") == "Bash" and isinstance(tool_input, dict):
        description = tool_input.get("description")
        if description:
            trace_lines.append(f"- Description: {description}")
        command = tool_input.get("command")
        if command:
            trace_lines.extend(
                [
                    "- Command",
                    "```bash",
                    command,
                    "```",
                ]
            )
        extra_input = {
            key: value
            for key, value in tool_input.items()
            if key not in {"command", "description"}
        }
        if extra_input:
            trace_lines.extend(
                [
                    "- Extra input",
                    "```json",
                    json.dumps(extra_input, indent=2, sort_keys=True),
                    "```",
                ]
            )
        return
    trace_lines.extend(
        [
            "- Input",
            "```json",
            json.dumps(tool_input, indent=2, sort_keys=True),
            "```",
        ]
    )


def _append_tool_result(trace_lines: list[str], tool_call: dict) -> None:
    result_text = tool_call.get("result")
    if result_text is None:
        trace_lines.append("- Result: none")
        return
    result_status = "error" if tool_call.get("is_error") else "success"
    trace_lines.append(f"- Result status: `{result_status}`")
    trace_lines.extend(
        [
            "```text",
            result_text,
            "```",
        ]
    )


def build_trace_text(
    *,
    testcase_id: str,
    run_id: str,
    command: list[str],
    exec_result: dict,
    events: list[dict],
    parsed_prediction: dict | None = None,
    validation_warnings: list[str] | None = None,
    raw_prediction_text: str | None = None,
    error_text: str | None = None,
) -> str:
    event_counts = dict(Counter(event.get("type", "unknown") for event in events))
    tool_calls = collect_tool_calls(events)
    thinking_text = collect_thinking_text(events)
    assistant_messages = collect_assistant_messages(events)
    final_result = exec_result.get("final_result", {})
    trace_lines = [
        f"# {testcase_id} Claude Code {run_id}",
        "",
        "## Command",
        "```bash",
        " ".join(command),
        "```",
        "",
        "## Raw Event Counts",
        "```json",
        json.dumps(event_counts, indent=2, sort_keys=True),
        "```",
        "",
        "## Tool Calls",
    ]
    if tool_calls:
        for tool_call in tool_calls:
            trace_lines.append(f"### `{tool_call.get('name')}` `{tool_call.get('id')}`")
            _append_tool_input(trace_lines, tool_call)
            _append_tool_result(trace_lines, tool_call)
            trace_lines.append("")
    else:
        trace_lines.append("- none")
    if parsed_prediction is not None:
        trace_lines.extend(
            [
                "",
                "## Parsed Prediction",
                "```json",
                json.dumps(parsed_prediction, indent=2, sort_keys=True),
                "```",
            ]
        )
    if raw_prediction_text is not None:
        trace_lines.extend(
            [
                "",
                "## Raw Prediction Text",
                "```text",
                raw_prediction_text,
                "```",
            ]
        )
    if validation_warnings:
        trace_lines.extend(["", "## Validation warnings"])
        for warning in validation_warnings:
            trace_lines.append(f"- {warning}")
    if error_text:
        trace_lines.extend(
            [
                "",
                "## Failure",
                "```text",
                error_text,
                "```",
            ]
        )
    trace_lines.extend(["", "## Thinking"])
    trace_lines.append(thinking_text or "none")
    trace_lines.extend(["", "## Assistant Messages"])
    if assistant_messages:
        for message in assistant_messages:
            trace_lines.append(f"- {message}")
    else:
        trace_lines.append("- none")
    trace_lines.extend(
        [
            "",
            "## Final Result",
            "```json",
            json.dumps(final_result, indent=2, sort_keys=True),
            "```",
            "",
            "## Stderr",
            exec_result.get("stderr", ""),
            "",
        ]
    )
    return "\n".join(trace_lines)
