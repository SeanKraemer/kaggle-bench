from __future__ import annotations

import json


TOOL_TYPES = {"tool_use", "server_tool_use", "mcp_tool_use"}


def parse_stream_events(stdout: str) -> list[dict]:
    events: list[dict] = []
    for line in stdout.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        try:
            payload = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            events.append(payload)
    return events


def _iter_message_content_blocks(events: list[dict], *, event_type: str) -> list[dict]:
    blocks: list[dict] = []
    for event in events:
        if event.get("type") != event_type:
            continue
        message = event.get("message", {})
        content = message.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict):
                blocks.append(block)
    return blocks


def _normalize_tool_result_content(content) -> str | None:
    if content is None:
        return None
    if isinstance(content, str):
        return content
    if isinstance(content, (dict, list)):
        return json.dumps(content, indent=2, sort_keys=True)
    return str(content)


def collect_tool_calls(events: list[dict]) -> list[dict]:
    tool_calls_by_id: dict[str, dict] = {}
    ordered_ids: list[str] = []

    def upsert_tool_call(*, tool_use_id: str | None, name=None, tool_input=None) -> dict | None:
        if not tool_use_id:
            return None
        if tool_use_id not in tool_calls_by_id:
            tool_calls_by_id[tool_use_id] = {
                "id": tool_use_id,
                "name": name,
                "input": tool_input,
                "result": None,
                "is_error": None,
            }
            ordered_ids.append(tool_use_id)
        tool_call = tool_calls_by_id[tool_use_id]
        if name is not None:
            tool_call["name"] = name
        if tool_input not in (None, {}) or tool_call.get("input") in (None, {}):
            tool_call["input"] = tool_input
        return tool_call

    for block in _iter_message_content_blocks(events, event_type="assistant"):
        if block.get("type") not in TOOL_TYPES:
            continue
        upsert_tool_call(
            tool_use_id=block.get("id"),
            name=block.get("name"),
            tool_input=block.get("input"),
        )

    for event in events:
        if event.get("type") != "stream_event":
            continue
        stream_event = event.get("event", {})
        if stream_event.get("type") != "content_block_start":
            continue
        content_block = stream_event.get("content_block", {})
        if content_block.get("type") not in TOOL_TYPES:
            continue
        upsert_tool_call(
            tool_use_id=content_block.get("id"),
            name=content_block.get("name"),
            tool_input=content_block.get("input"),
        )

    for block in _iter_message_content_blocks(events, event_type="user"):
        if block.get("type") != "tool_result":
            continue
        tool_call = upsert_tool_call(tool_use_id=block.get("tool_use_id"))
        if tool_call is None:
            continue
        normalized_result = _normalize_tool_result_content(block.get("content"))
        if normalized_result:
            existing_result = tool_call.get("result")
            if existing_result:
                tool_call["result"] = existing_result + "\n" + normalized_result
            else:
                tool_call["result"] = normalized_result
        if block.get("is_error") is not None:
            tool_call["is_error"] = block.get("is_error")

    return [tool_calls_by_id[tool_use_id] for tool_use_id in ordered_ids]


def collect_thinking_text(events: list[dict]) -> str:
    chunks: list[str] = []
    for event in events:
        if event.get("type") != "stream_event":
            continue
        stream_event = event.get("event", {})
        if stream_event.get("type") == "content_block_start":
            content_block = stream_event.get("content_block", {})
            if content_block.get("type") == "thinking" and content_block.get("thinking"):
                chunks.append(content_block["thinking"])
        elif stream_event.get("type") == "content_block_delta":
            delta = stream_event.get("delta", {})
            if delta.get("type") == "thinking_delta" and delta.get("thinking"):
                chunks.append(delta["thinking"])
    return "".join(chunks).strip()


def collect_assistant_messages(events: list[dict]) -> list[str]:
    messages: list[str] = []
    for event in events:
        if event.get("type") != "assistant":
            continue
        message = event.get("message", {})
        content = message.get("content", [])
        if not isinstance(content, list):
            continue
        text_parts = [
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        ]
        text = "".join(text_parts).strip()
        if text:
            messages.append(text)
    return messages


def normalize_exec_result(exec_result: dict) -> dict:
    normalized = dict(exec_result)
    stdout = normalized.get("stdout", "")
    usage = normalized.get("usage") or {"input_tokens": None, "output_tokens": None, "total_tokens": None}
    cost_usd = normalized.get("cost_usd")
    events = parse_stream_events(stdout)
    payload = {}
    if events:
        for event in reversed(events):
            if event.get("type") == "result":
                payload = event
                break
        if not payload:
            payload = events[-1]
    else:
        try:
            payload = json.loads(stdout) if stdout else {}
        except json.JSONDecodeError:
            payload = {}
    payload_usage = payload.get("usage") if isinstance(payload, dict) else None
    if isinstance(payload_usage, dict):
        input_tokens = payload_usage.get("input_tokens")
        output_tokens = payload_usage.get("output_tokens")
        total_tokens = None
        if input_tokens is not None and output_tokens is not None:
            total_tokens = input_tokens + output_tokens
        usage = {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
        }
    if cost_usd is None and isinstance(payload, dict):
        cost_usd = payload.get("total_cost_usd")
    normalized["usage"] = usage
    normalized["cost_usd"] = cost_usd
    normalized["usage_detail"] = payload_usage if isinstance(payload_usage, dict) else None
    normalized["model_usage"] = payload.get("modelUsage") if isinstance(payload, dict) else None
    normalized["permission_denials"] = payload.get("permission_denials") if isinstance(payload, dict) else None
    normalized["final_result"] = payload if isinstance(payload, dict) else {}
    normalized["stream_events"] = events
    normalized["tool_call_count"] = len(collect_tool_calls(events))
    return normalized
