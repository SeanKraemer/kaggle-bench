from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Callable

from agent.llm.guards import CostCapExceeded, enforce_cost_cap
from agent.llm.pricing import estimate_cost_usd
from agent.llm.telemetry import build_trace_entry
from agent.single_llm.parsing import parse_and_validate_prediction_text


@dataclass(frozen=True)
class SingleLLMExecutionResult:
    trace_entries: list[dict]
    parsed_prediction: dict | None
    validation_warnings: list[str]
    last_response: dict | None
    api_call_count: int
    cumulative_cost_usd: float
    status: str
    error_message: str | None


def _build_cache_usage(response: dict) -> dict:
    return {
        "cache_creation_input_tokens": response.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": response.get("cache_read_input_tokens"),
        "cache_creation": response.get("cache_creation"),
    }


def run_single_llm_execution(
    *,
    prompt: str,
    valid_action_ids: set[str],
    model_name: str,
    max_tokens: int,
    temperature: float,
    system_blocks: list[dict] | None,
    message_content_blocks: list[dict] | None,
    thinking: dict | None,
    output_config: dict | None,
    timeout_seconds: int | float,
    call_fn: Callable[..., dict],
    max_attempts: int,
    input_cost_per_million: float,
    output_cost_per_million: float,
    cache_read_cost_per_million: float,
    cache_write_5m_cost_per_million: float,
    cache_write_1h_cost_per_million: float,
    cost_cap_usd: float,
) -> SingleLLMExecutionResult:
    trace_entries = []
    api_call_count = 0
    cumulative_cost_usd = 0.0
    parsed_prediction = None
    validation_warnings: list[str] = []
    last_response = None
    status = "success"
    error_message = None

    for attempt_index in range(1, max_attempts + 1):
        response = call_fn(
            model_name=model_name,
            prompt_text=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            system_blocks=system_blocks,
            message_content_blocks=message_content_blocks,
            thinking=thinking,
            output_config=output_config,
            timeout_seconds=timeout_seconds,
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
        cache_usage = _build_cache_usage(response)
        try:
            parsed_prediction, validation_warnings = parse_and_validate_prediction_text(
                response["raw_text"],
                valid_action_ids=valid_action_ids,
            )
            trace_entries.append(
                build_trace_entry(
                    attempt_index=attempt_index,
                    status="success",
                    prompt_text=prompt,
                    response_text=response["raw_text"],
                    input_tokens=response.get("input_tokens"),
                    output_tokens=response.get("output_tokens"),
                    cost_usd=attempt_cost,
                    parsed_prediction=parsed_prediction,
                    validation_warnings=validation_warnings,
                    thinking_summaries=response.get("thinking_summaries"),
                    cache_usage=cache_usage,
                )
            )
            break
        except json.JSONDecodeError as exc:
            trace_entries.append(
                build_trace_entry(
                    attempt_index=attempt_index,
                    status="parse_error",
                    prompt_text=prompt,
                    response_text=response["raw_text"],
                    input_tokens=response.get("input_tokens"),
                    output_tokens=response.get("output_tokens"),
                    cost_usd=attempt_cost,
                    error_message=f"Parse failure: {exc}",
                    thinking_summaries=response.get("thinking_summaries"),
                    cache_usage=cache_usage,
                )
            )
            error_message = f"Parse failure: {exc}"
        except ValueError as exc:
            trace_entries.append(
                build_trace_entry(
                    attempt_index=attempt_index,
                    status="validation_error",
                    prompt_text=prompt,
                    response_text=response["raw_text"],
                    input_tokens=response.get("input_tokens"),
                    output_tokens=response.get("output_tokens"),
                    cost_usd=attempt_cost,
                    error_message=str(exc),
                    thinking_summaries=response.get("thinking_summaries"),
                    cache_usage=cache_usage,
                )
            )
            error_message = str(exc)
    if parsed_prediction is None:
        raise ValueError(error_message or "LLM response could not be parsed")

    status = "success"
    try:
        enforce_cost_cap(current_cost_usd=cumulative_cost_usd, cost_cap_usd=cost_cap_usd)
    except CostCapExceeded as exc:
        status = "partial_success"
        error_message = str(exc) + " (cost cap)"

    return SingleLLMExecutionResult(
        trace_entries=trace_entries,
        parsed_prediction=parsed_prediction,
        validation_warnings=validation_warnings,
        last_response=last_response,
        api_call_count=api_call_count,
        cumulative_cost_usd=cumulative_cost_usd,
        status=status,
        error_message=error_message,
    )
