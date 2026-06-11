from __future__ import annotations

import copy
import json
from typing import Any, Callable

from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.types import (
    AgenticRunBudget,
    AgenticRunResult,
    AgenticToolCall,
    AgenticToolResult,
    AgenticTurn,
    ValidationCallback,
)
from agent.llm.guards import CostCapExceeded, enforce_cost_cap
from agent.llm.pricing import estimate_cost_usd


def _cache_usage(response: dict[str, Any]) -> dict[str, Any]:
    return {
        "cache_creation_input_tokens": response.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": response.get("cache_read_input_tokens"),
        "cache_creation": response.get("cache_creation"),
    }


def _json_chars(value: Any) -> int:
    return len(json.dumps(value, default=str))


def _summarize_tool_input(value: Any) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "input_ref": "see tool_calls.jsonl for full tool input",
        "input_chars": _json_chars(value),
    }
    if isinstance(value, dict):
        summary["input_keys"] = sorted(str(key) for key in value)
    return summary


def _sanitize_api_content(content: Any) -> Any:
    if isinstance(content, list):
        return [_sanitize_api_content_block(block) for block in content]
    return content


def _sanitize_api_content_block(block: Any) -> Any:
    if not isinstance(block, dict):
        return copy.deepcopy(block)
    block_type = block.get("type")
    if block_type == "tool_use":
        sanitized = {
            "type": "tool_use",
            "id": block.get("id"),
            "name": block.get("name"),
        }
        sanitized.update(_summarize_tool_input(block.get("input", {})))
        return sanitized
    if block_type == "tool_result":
        content = block.get("content", "")
        return {
            "type": "tool_result",
            "tool_use_id": block.get("tool_use_id"),
            "is_error": block.get("is_error"),
            "content_ref": "see tool_calls.jsonl for full tool output",
            "content_chars": len(str(content)),
        }
    return copy.deepcopy(block)


def _sanitize_api_messages(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sanitized = []
    for message in messages:
        sanitized.append(
            {
                "role": message.get("role"),
                "content": _sanitize_api_content(message.get("content")),
            }
        )
    return sanitized


def _build_api_request_record(
    *,
    model_name: str,
    max_tokens: int,
    temperature: float,
    system_blocks: list[dict] | None,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]],
    thinking: dict | None,
    output_config: dict | None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "model": model_name,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": _sanitize_api_messages(messages),
        "tools": copy.deepcopy(tools),
    }
    if system_blocks is not None:
        request["system"] = copy.deepcopy(system_blocks)
    if thinking is not None:
        request["thinking"] = copy.deepcopy(thinking)
    if output_config is not None:
        request["output_config"] = copy.deepcopy(output_config)
    return request


def _summarize_response_tool_calls(response: dict[str, Any]) -> list[dict[str, Any]]:
    summarized = []
    for call in response.get("tool_calls", []) or []:
        item = {
            "id": call.get("id") or call.get("tool_call_id"),
            "name": call.get("name"),
        }
        item.update(_summarize_tool_input(call.get("input", {})))
        summarized.append(item)
    return summarized


def _build_api_response_record(response: dict[str, Any]) -> dict[str, Any]:
    usage = {
        "input_tokens": response.get("input_tokens"),
        "output_tokens": response.get("output_tokens"),
        "total_tokens": response.get("total_tokens"),
        "cache_creation_input_tokens": response.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": response.get("cache_read_input_tokens"),
        "cache_creation": response.get("cache_creation"),
    }
    return {
        "raw_text": response.get("raw_text", ""),
        "stop_reason": response.get("stop_reason"),
        "usage": usage,
        "thinking_summaries": response.get("thinking_summaries") or [],
        "tool_calls": _summarize_response_tool_calls(response),
        "content_blocks": _sanitize_api_content(response.get("content_blocks", [])),
    }


def _build_api_error_response_record(error_message: str) -> dict[str, Any]:
    return {
        "raw_text": "",
        "stop_reason": "api_error",
        "usage": {
            "input_tokens": None,
            "output_tokens": None,
            "total_tokens": None,
            "cache_creation_input_tokens": None,
            "cache_read_input_tokens": None,
            "cache_creation": None,
        },
        "thinking_summaries": [],
        "tool_calls": [],
        "content_blocks": [],
        "error_message": error_message,
    }


def _extract_tool_calls(response: dict[str, Any]) -> list[AgenticToolCall]:
    calls: list[AgenticToolCall] = []
    for index, call in enumerate(response.get("tool_calls", []) or []):
        name = call.get("name")
        if not isinstance(name, str):
            continue
        tool_input = call.get("input", {})
        if not isinstance(tool_input, dict):
            tool_input = {}
        tool_call_id = call.get("id") or call.get("tool_call_id") or f"tool_call_{index}"
        calls.append(
            AgenticToolCall(
                tool_call_id=str(tool_call_id),
                name=name,
                input=tool_input,
            )
        )
    return calls


def _assistant_content_from_response(response: dict[str, Any]) -> list[dict[str, Any]] | str:
    blocks = response.get("content_blocks")
    if isinstance(blocks, list) and blocks:
        return blocks
    content: list[dict[str, Any]] = []
    raw_text = response.get("raw_text") or ""
    if raw_text:
        content.append({"type": "text", "text": raw_text})
    for call in response.get("tool_calls", []) or []:
        content.append(
            {
                "type": "tool_use",
                "id": call.get("id") or call.get("tool_call_id"),
                "name": call.get("name"),
                "input": call.get("input", {}),
            }
        )
    return content or raw_text


def _tool_result_content(tool_results: list[AgenticToolResult]) -> list[dict[str, Any]]:
    return [
        {
            "type": "tool_result",
            "tool_use_id": result.tool_call_id,
            "content": result.output_text,
            "is_error": result.is_error,
        }
        for result in tool_results
    ]


def _cost_cap_error_message(*, current_cost_usd: float, cost_cap_usd: float | None) -> str | None:
    if cost_cap_usd is None:
        return None
    try:
        enforce_cost_cap(
            current_cost_usd=current_cost_usd,
            cost_cap_usd=cost_cap_usd,
        )
    except CostCapExceeded as exc:
        return str(exc) + " (cost cap)"
    return None


def run_agentic_loop(
    *,
    method_name: str,
    phase_name: str | None,
    prompt_text: str,
    system_blocks: list[dict] | None,
    message_content_blocks: list[dict] | None,
    model_name: str,
    max_tokens: int,
    temperature: float,
    thinking: dict | None,
    output_config: dict | None,
    tool_runtime: AgenticToolRuntime,
    call_fn: Callable[..., dict[str, Any]],
    parse_and_validate: ValidationCallback,
    budget: AgenticRunBudget,
    input_cost_per_million: float,
    output_cost_per_million: float,
    cache_read_cost_per_million: float,
    cache_write_5m_cost_per_million: float,
    cache_write_1h_cost_per_million: float,
    capture_llm_calls: bool = False,
) -> AgenticRunResult:
    messages: list[dict[str, Any]] = [
        {
            "role": "user",
            "content": message_content_blocks if message_content_blocks is not None else prompt_text,
        }
    ]
    turns: list[AgenticTurn] = []
    all_tool_results: list[AgenticToolResult] = []
    api_call_count = 0
    tool_call_count = 0
    cumulative_cost_usd = 0.0
    parsed_prediction: dict[str, Any] | None = None
    validation_warnings: list[str] = []
    last_response: dict[str, Any] | None = None
    error_message: str | None = None
    validation_retries = 0
    api_call_records: list[dict[str, Any]] = []

    for turn_index in range(1, budget.max_turns + 1):
        tool_schemas = tool_runtime.anthropic_tool_schemas()
        request_record = None
        if capture_llm_calls:
            request_record = _build_api_request_record(
                model_name=model_name,
                max_tokens=max_tokens,
                temperature=temperature,
                system_blocks=system_blocks,
                messages=messages,
                tools=tool_schemas,
                thinking=thinking,
                output_config=output_config,
            )
        try:
            response = call_fn(
                model_name=model_name,
                prompt_text=prompt_text,
                max_tokens=max_tokens,
                temperature=temperature,
                system_blocks=system_blocks,
                message_content_blocks=message_content_blocks if turn_index == 1 else None,
                messages=messages,
                tools=tool_schemas,
                thinking=thinking,
                output_config=output_config,
                timeout_seconds=budget.timeout_seconds,
            )
        except Exception as exc:
            error_message = f"{type(exc).__name__}: {exc}"
            api_call_count += 1
            if capture_llm_calls:
                api_call_records.append(
                    {
                        "turn_index": turn_index,
                        "request": request_record,
                        "response": _build_api_error_response_record(error_message),
                    }
                )
            turns.append(
                AgenticTurn(
                    turn_index=turn_index,
                    response_text="",
                    tool_calls=[],
                    tool_results=[],
                    status="api_error",
                    error_message=error_message,
                    thinking_summaries=[],
                    cache_usage={},
                )
            )
            break
        if capture_llm_calls:
            api_call_records.append(
                {
                    "turn_index": turn_index,
                    "request": request_record,
                    "response": _build_api_response_record(response),
                }
            )
        last_response = response
        api_call_count += 1
        attempt_cost = estimate_cost_usd(
            input_tokens=response.get("input_tokens"),
            output_tokens=response.get("output_tokens"),
            input_cost_per_million=input_cost_per_million,
            output_cost_per_million=output_cost_per_million,
            cache_read_input_tokens=response.get("cache_read_input_tokens"),
            cache_creation=response.get("cache_creation"),
            cache_creation_input_tokens=response.get("cache_creation_input_tokens"),
            cache_read_cost_per_million=cache_read_cost_per_million,
            cache_write_5m_cost_per_million=cache_write_5m_cost_per_million,
            cache_write_1h_cost_per_million=cache_write_1h_cost_per_million,
        )
        cumulative_cost_usd += attempt_cost
        tool_calls = _extract_tool_calls(response)
        cost_cap_error_message = _cost_cap_error_message(
            current_cost_usd=cumulative_cost_usd,
            cost_cap_usd=budget.cost_cap_usd,
        )

        if tool_calls:
            if cost_cap_error_message is not None:
                error_message = cost_cap_error_message
                turns.append(
                    AgenticTurn(
                        turn_index=turn_index,
                        response_text=response.get("raw_text", ""),
                        tool_calls=tool_calls,
                        tool_results=[],
                        input_tokens=response.get("input_tokens"),
                        output_tokens=response.get("output_tokens"),
                        cost_usd=attempt_cost,
                        status="cost_cap_exceeded",
                        error_message=error_message,
                        thinking_summaries=response.get("thinking_summaries") or [],
                        cache_usage=_cache_usage(response),
                    )
                )
                break
            if tool_call_count + len(tool_calls) > budget.max_tool_calls:
                error_message = "max tool calls exceeded"
                turns.append(
                    AgenticTurn(
                        turn_index=turn_index,
                        response_text=response.get("raw_text", ""),
                        tool_calls=tool_calls,
                        tool_results=[],
                        input_tokens=response.get("input_tokens"),
                        output_tokens=response.get("output_tokens"),
                        cost_usd=attempt_cost,
                        status="max_tool_calls_exceeded",
                        error_message=error_message,
                        thinking_summaries=response.get("thinking_summaries") or [],
                        cache_usage=_cache_usage(response),
                    )
                )
                break
            tool_results = [tool_runtime.call(call) for call in tool_calls]
            tool_call_count += len(tool_calls)
            all_tool_results.extend(tool_results)
            turns.append(
                AgenticTurn(
                    turn_index=turn_index,
                    response_text=response.get("raw_text", ""),
                    tool_calls=tool_calls,
                    tool_results=tool_results,
                    input_tokens=response.get("input_tokens"),
                    output_tokens=response.get("output_tokens"),
                    cost_usd=attempt_cost,
                    thinking_summaries=response.get("thinking_summaries") or [],
                    cache_usage=_cache_usage(response),
                )
            )
            messages.append({"role": "assistant", "content": _assistant_content_from_response(response)})
            messages.append({"role": "user", "content": _tool_result_content(tool_results)})
            continue

        try:
            parsed_prediction, validation_warnings = parse_and_validate(response.get("raw_text", ""))
            turns.append(
                AgenticTurn(
                    turn_index=turn_index,
                    response_text=response.get("raw_text", ""),
                    tool_calls=[],
                    tool_results=[],
                    input_tokens=response.get("input_tokens"),
                    output_tokens=response.get("output_tokens"),
                    cost_usd=attempt_cost,
                    status="cost_cap_exceeded" if cost_cap_error_message is not None else "success",
                    error_message=cost_cap_error_message,
                    thinking_summaries=response.get("thinking_summaries") or [],
                    cache_usage=_cache_usage(response),
                )
            )
            break
        except Exception as exc:
            error_message = str(exc)
            turn_status = "validation_error"
            if cost_cap_error_message is not None:
                error_message = f"{cost_cap_error_message}; validation error: {error_message}"
                turn_status = "cost_cap_exceeded"
            turns.append(
                AgenticTurn(
                    turn_index=turn_index,
                    response_text=response.get("raw_text", ""),
                    tool_calls=[],
                    tool_results=[],
                    input_tokens=response.get("input_tokens"),
                    output_tokens=response.get("output_tokens"),
                    cost_usd=attempt_cost,
                    status=turn_status,
                    error_message=error_message,
                    thinking_summaries=response.get("thinking_summaries") or [],
                    cache_usage=_cache_usage(response),
                )
            )
            if cost_cap_error_message is not None:
                break
            if validation_retries >= budget.max_validation_retries:
                break
            validation_retries += 1
            messages.append({"role": "assistant", "content": response.get("raw_text", "")})
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "The previous response was not a valid benchmark prediction. "
                        "Return only JSON with predicted_add_action_ids and "
                        f"predicted_remove_action_ids. Error: {error_message}"
                    ),
                }
            )

    else:
        error_message = "max turns exceeded"

    status = "success" if parsed_prediction is not None else "failed"
    cost_cap_error_message = _cost_cap_error_message(
        current_cost_usd=cumulative_cost_usd,
        cost_cap_usd=budget.cost_cap_usd,
    )
    if cost_cap_error_message is not None:
        status = "partial_success" if parsed_prediction is not None else "failed"
        if error_message is None or "cost cap" not in error_message.lower():
            error_message = cost_cap_error_message

    input_tokens = sum(turn.input_tokens or 0 for turn in turns) if turns else None
    output_tokens = sum(turn.output_tokens or 0 for turn in turns) if turns else None
    token_usage = {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": (
            (input_tokens or 0) + (output_tokens or 0)
            if input_tokens is not None or output_tokens is not None
            else None
        ),
    }
    return AgenticRunResult(
        method_name=method_name,
        phase_name=phase_name,
        status=status,
        parsed_prediction=parsed_prediction,
        validation_warnings=validation_warnings,
        turns=turns,
        tool_results=all_tool_results,
        last_response=last_response,
        api_call_count=api_call_count,
        tool_call_count=tool_call_count,
        cumulative_cost_usd=cumulative_cost_usd,
        token_usage=token_usage,
        api_call_records=api_call_records,
        error_message=error_message,
    )
