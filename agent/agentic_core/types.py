from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

ToolHandler = Callable[[dict[str, Any]], Any]
ValidationCallback = Callable[[str], tuple[dict[str, Any], list[str]]]


@dataclass(frozen=True)
class AgenticToolSpec:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: ToolHandler


@dataclass(frozen=True)
class AgenticToolCall:
    tool_call_id: str
    name: str
    input: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AgenticToolResult:
    tool_call_id: str
    name: str
    input: dict[str, Any]
    output: Any
    output_text: str
    is_error: bool = False
    error_message: str | None = None


@dataclass(frozen=True)
class AgenticTurn:
    turn_index: int
    response_text: str
    tool_calls: list[AgenticToolCall]
    tool_results: list[AgenticToolResult]
    input_tokens: int | None = None
    output_tokens: int | None = None
    cost_usd: float | None = None
    status: str = "success"
    error_message: str | None = None
    thinking_summaries: list[str] = field(default_factory=list)
    cache_usage: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AgenticRunBudget:
    max_turns: int = 8
    max_tool_calls: int = 12
    max_validation_retries: int = 1
    timeout_seconds: int | float = 120
    cost_cap_usd: float | None = None


@dataclass(frozen=True)
class AgenticRunResult:
    method_name: str
    phase_name: str | None
    status: str
    parsed_prediction: dict[str, Any] | None
    validation_warnings: list[str]
    turns: list[AgenticTurn]
    tool_results: list[AgenticToolResult]
    last_response: dict[str, Any] | None
    api_call_count: int
    tool_call_count: int
    cumulative_cost_usd: float
    token_usage: dict[str, int | None]
    api_call_records: list[dict[str, Any]] = field(default_factory=list)
    error_message: str | None = None
