from __future__ import annotations

from collections.abc import Callable

from agent.llm.anthropic_client import send_messages_request
from agent.llm.types import LLMResponse


def anthropic_llm_call(
    *,
    api_key: str,
    model_name: str,
    prompt_text: str,
    max_tokens: int,
    temperature: float,
    system_blocks: list[dict] | None = None,
    message_content_blocks: list[dict] | None = None,
    messages: list[dict] | None = None,
    tools: list[dict] | None = None,
    thinking: dict | None = None,
    output_config: dict | None = None,
    timeout_seconds: int | float | None = None,
    send_fn: Callable[..., dict] = send_messages_request,
) -> LLMResponse:
    return send_fn(
        api_key=api_key,
        model_name=model_name,
        prompt_text=prompt_text,
        max_tokens=max_tokens,
        temperature=temperature,
        system_blocks=system_blocks,
        message_content_blocks=message_content_blocks,
        messages=messages,
        tools=tools,
        thinking=thinking,
        output_config=output_config,
        timeout_seconds=timeout_seconds,
    )


def build_llm_caller(
    *,
    provider: str,
    api_key: str,
    send_fn: Callable[..., dict] = send_messages_request,
) -> Callable[..., LLMResponse]:
    if provider != "anthropic":
        raise ValueError(f"Unsupported provider: {provider}")

    def caller(**kwargs) -> LLMResponse:
        return anthropic_llm_call(api_key=api_key, send_fn=send_fn, **kwargs)

    return caller
