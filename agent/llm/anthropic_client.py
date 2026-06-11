from __future__ import annotations

import json
from urllib import request

from agent.llm.config import ANTHROPIC_API_URL, ANTHROPIC_API_VERSION


def build_messages_request(
    *,
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
    cache_control: dict | None = None,
) -> dict:
    payload = {
        "model": model_name,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": messages
        if messages is not None
        else [
            {
                "role": "user",
                "content": prompt_text,
            }
        ],
    }
    if system_blocks is not None:
        payload["system"] = system_blocks
        if messages is None:
            payload["messages"][0]["content"] = (
                message_content_blocks if message_content_blocks is not None else prompt_text
            )
    elif message_content_blocks is not None and messages is None:
        payload["messages"][0]["content"] = message_content_blocks
    if tools is not None:
        payload["tools"] = tools
    if thinking is not None:
        payload["thinking"] = thinking
    if output_config is not None:
        payload["output_config"] = output_config
    if cache_control is not None:
        payload["cache_control"] = cache_control
    body = json.dumps(payload).encode("utf-8")
    return {
        "url": ANTHROPIC_API_URL,
        "headers": {
            "content-type": "application/json",
            "anthropic-version": ANTHROPIC_API_VERSION,
        },
        "body": body,
    }


def parse_messages_response(payload: dict) -> dict:
    text_parts = [block.get("text", "") for block in payload.get("content", []) if block.get("type") == "text"]
    tool_calls = [
        {
            "id": block.get("id"),
            "name": block.get("name"),
            "input": block.get("input", {}),
        }
        for block in payload.get("content", [])
        if block.get("type") == "tool_use"
    ]
    thinking_summaries = [
        block.get("thinking", "") for block in payload.get("content", []) if block.get("type") == "thinking"
    ]
    usage = payload.get("usage", {})
    input_tokens = usage.get("input_tokens")
    output_tokens = usage.get("output_tokens")
    return {
        "raw_text": "".join(text_parts),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": (input_tokens or 0) + (output_tokens or 0),
        "thinking_summaries": thinking_summaries,
        "tool_calls": tool_calls,
        "content_blocks": payload.get("content", []),
        "stop_reason": payload.get("stop_reason"),
        "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
        "cache_creation": usage.get("cache_creation"),
    }


def send_messages_request(
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
    cache_control: dict | None = None,
    timeout_seconds: int | float | None = None,
    urlopen=request.urlopen,
) -> dict:
    built = build_messages_request(
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
        cache_control=cache_control,
    )
    headers = dict(built["headers"])
    headers["x-api-key"] = api_key
    http_request = request.Request(
        built["url"],
        data=built["body"],
        headers=headers,
        method="POST",
    )
    with urlopen(http_request, timeout=timeout_seconds) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return parse_messages_response(payload)
