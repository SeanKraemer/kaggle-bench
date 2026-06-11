from __future__ import annotations

from agent.llm.config import (
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REASONING_ENABLED,
    DEFAULT_TEMPERATURE,
    DEFAULT_THINKING_DISPLAY,
    DEFAULT_THINKING_TYPE,
)


def build_reasoning_controls(
    *,
    reasoning_enabled: bool = DEFAULT_REASONING_ENABLED,
    reasoning_effort: str = DEFAULT_REASONING_EFFORT,
    thinking_type: str = DEFAULT_THINKING_TYPE,
    thinking_display: str = DEFAULT_THINKING_DISPLAY,
    temperature: float = DEFAULT_TEMPERATURE,
) -> tuple[dict | None, dict | None, float]:
    thinking = None
    output_config = None
    if reasoning_enabled:
        thinking = {"type": thinking_type, "display": thinking_display}
        output_config = {"effort": reasoning_effort}
    request_temperature = 1.0 if reasoning_enabled else temperature
    return thinking, output_config, request_temperature
