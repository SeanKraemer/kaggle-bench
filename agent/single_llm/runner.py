from __future__ import annotations

import time
from pathlib import Path

from agent.llm.auth import load_api_key
from agent.llm.client import build_llm_caller
from agent.llm.config import (
    DEFAULT_CACHE_ENABLED,
    DEFAULT_CACHE_READ_COST_PER_MILLION,
    DEFAULT_CACHE_TTL,
    DEFAULT_CACHE_TYPE,
    DEFAULT_CACHE_WRITE_1H_COST_PER_MILLION,
    DEFAULT_CACHE_WRITE_5M_COST_PER_MILLION,
    DEFAULT_COST_CAP_USD,
    DEFAULT_INPUT_COST_PER_MILLION,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL_NAME,
    DEFAULT_OUTPUT_COST_PER_MILLION,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REASONING_ENABLED,
    DEFAULT_REQUEST_TIMEOUT_SECONDS,
    DEFAULT_TEMPERATURE,
    DEFAULT_THINKING_DISPLAY,
    DEFAULT_THINKING_TYPE,
)
from agent.single_llm.execution import run_single_llm_execution
from agent.single_llm.output import write_single_llm_output_bundle
from agent.single_llm.request_context import build_single_llm_request_context


def run_single_llm(
    *,
    task_dir: str | Path,
    testcase_id: str,
    run_id: str,
    data_root: str | Path,
    api_key_path: str | Path,
    llm_call=None,
    model_name: str = DEFAULT_MODEL_NAME,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    cost_cap_usd: float = DEFAULT_COST_CAP_USD,
    input_cost_per_million: float = DEFAULT_INPUT_COST_PER_MILLION,
    output_cost_per_million: float = DEFAULT_OUTPUT_COST_PER_MILLION,
    cache_read_cost_per_million: float = DEFAULT_CACHE_READ_COST_PER_MILLION,
    cache_write_5m_cost_per_million: float = DEFAULT_CACHE_WRITE_5M_COST_PER_MILLION,
    cache_write_1h_cost_per_million: float = DEFAULT_CACHE_WRITE_1H_COST_PER_MILLION,
    max_attempts: int = 1,
    request_timeout_seconds: int | float = DEFAULT_REQUEST_TIMEOUT_SECONDS,
    reasoning_enabled: bool = DEFAULT_REASONING_ENABLED,
    thinking_type: str = DEFAULT_THINKING_TYPE,
    thinking_display: str = DEFAULT_THINKING_DISPLAY,
    reasoning_effort: str = DEFAULT_REASONING_EFFORT,
    cache_enabled: bool = DEFAULT_CACHE_ENABLED,
    cache_type: str = DEFAULT_CACHE_TYPE,
    cache_ttl: str = DEFAULT_CACHE_TTL,
    profile_cache_dir: str | Path | None = None,
    time_fn=time.perf_counter,
) -> dict[str, Path]:
    started_at = time_fn()
    context = build_single_llm_request_context(
        task_dir=task_dir,
        testcase_id=testcase_id,
        data_root=data_root,
        reasoning_enabled=reasoning_enabled,
        reasoning_effort=reasoning_effort,
        thinking_type=thinking_type,
        thinking_display=thinking_display,
        temperature=temperature,
        cache_enabled=cache_enabled,
        cache_type=cache_type,
        cache_ttl=cache_ttl,
        profile_cache_dir=profile_cache_dir,
    )

    if llm_call is None:
        api_key = load_api_key(api_key_path)
        call_fn = build_llm_caller(provider="anthropic", api_key=api_key)
    else:
        call_fn = llm_call
    execution = run_single_llm_execution(
        prompt=context.prompt,
        valid_action_ids=context.benchmark.valid_action_ids,
        model_name=model_name,
        max_tokens=max_tokens,
        temperature=context.request_temperature,
        system_blocks=context.system_blocks,
        message_content_blocks=context.message_content_blocks,
        thinking=context.thinking,
        output_config=context.output_config,
        timeout_seconds=request_timeout_seconds,
        call_fn=call_fn,
        max_attempts=max_attempts,
        input_cost_per_million=input_cost_per_million,
        output_cost_per_million=output_cost_per_million,
        cache_read_cost_per_million=cache_read_cost_per_million,
        cache_write_5m_cost_per_million=cache_write_5m_cost_per_million,
        cache_write_1h_cost_per_million=cache_write_1h_cost_per_million,
        cost_cap_usd=cost_cap_usd,
    )

    elapsed_seconds = round(time_fn() - started_at, 3)
    return write_single_llm_output_bundle(
        task_dir=task_dir,
        testcase_id=testcase_id,
        run_id=run_id,
        context=context,
        execution=execution,
        elapsed_seconds=elapsed_seconds,
        model_name=model_name,
        reasoning_enabled=reasoning_enabled,
        thinking_type=thinking_type,
        thinking_display=thinking_display,
        reasoning_effort=reasoning_effort,
    )
