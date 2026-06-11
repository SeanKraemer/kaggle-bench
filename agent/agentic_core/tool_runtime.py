from __future__ import annotations

import json
from typing import Any

from agent.agentic_core.types import AgenticToolCall, AgenticToolResult, AgenticToolSpec


def _compact_text(value: Any, *, max_chars: int) -> str:
    if isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, indent=2, default=str)
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n...<truncated {len(text) - max_chars} chars>"


class AgenticToolRuntime:
    def __init__(self, tools: list[AgenticToolSpec], *, max_result_chars: int = 4000) -> None:
        self._tools = {tool.name: tool for tool in tools}
        self.max_result_chars = max_result_chars

    def list_tool_names(self) -> list[str]:
        return sorted(self._tools)

    def anthropic_tool_schemas(self) -> list[dict[str, Any]]:
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema,
            }
            for tool in self._tools.values()
        ]

    def call(self, tool_call: AgenticToolCall) -> AgenticToolResult:
        tool = self._tools.get(tool_call.name)
        if tool is None:
            message = f"Unknown tool: {tool_call.name}"
            return AgenticToolResult(
                tool_call_id=tool_call.tool_call_id,
                name=tool_call.name,
                input=tool_call.input,
                output={"error": message},
                output_text=message,
                is_error=True,
                error_message=message,
            )
        try:
            output = tool.handler(tool_call.input)
            return AgenticToolResult(
                tool_call_id=tool_call.tool_call_id,
                name=tool_call.name,
                input=tool_call.input,
                output=output,
                output_text=_compact_text(output, max_chars=self.max_result_chars),
                is_error=False,
            )
        except Exception as exc:
            message = str(exc)
            return AgenticToolResult(
                tool_call_id=tool_call.tool_call_id,
                name=tool_call.name,
                input=tool_call.input,
                output={"error": message},
                output_text=message,
                is_error=True,
                error_message=message,
            )
