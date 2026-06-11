from __future__ import annotations

from typing import TypedDict


class LLMUsage(TypedDict):
    input_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None


class LLMResponse(TypedDict):
    raw_text: str
    input_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None
    thinking_summaries: list[str]
    tool_calls: list[dict]
    content_blocks: list[dict]
    stop_reason: str | None
    cache_creation_input_tokens: int | None
    cache_read_input_tokens: int | None
    cache_creation: dict | None
