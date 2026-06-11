from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agent.context_builder import (
    BenchmarkContext,
    MaterializedBenchmarkContext,
    build_benchmark_context,
    materialize_benchmark_context,
)
from agent.llm.config import (
    DEFAULT_CACHE_ENABLED,
    DEFAULT_CACHE_TTL,
    DEFAULT_CACHE_TYPE,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REASONING_ENABLED,
    DEFAULT_THINKING_DISPLAY,
    DEFAULT_THINKING_TYPE,
    DEFAULT_TEMPERATURE,
)
from agent.prompts.single_llm import build_single_llm_prompt_parts
from agent.summaries import render_single_llm_dataset_summary


def _build_output_format() -> str:
    return (
        "Return ONLY a single JSON object with required keys `predicted_add_action_ids` and "
        "`predicted_remove_action_ids`, each containing arrays of candidate action IDs. "
        "You may also include optional `notes` and optional `action_rationales`, where "
        "`action_rationales` is an array of objects with `action_id`, `decision`, and `reason`. "
        "Do not output any prose outside the JSON object."
    )


def _build_reasoning_controls(
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


@dataclass(frozen=True)
class SingleLLMRequestContext:
    benchmark: BenchmarkContext
    materialized: MaterializedBenchmarkContext
    output_format: str
    prompt_parts: dict[str, str]
    prompt: str
    system_blocks: list[dict]
    message_content_blocks: list[dict]
    thinking: dict | None
    output_config: dict | None
    request_temperature: float


def build_single_llm_request_context(
    *,
    task_dir: str | Path,
    testcase_id: str,
    data_root: str | Path,
    reasoning_enabled: bool = DEFAULT_REASONING_ENABLED,
    reasoning_effort: str = DEFAULT_REASONING_EFFORT,
    thinking_type: str = DEFAULT_THINKING_TYPE,
    thinking_display: str = DEFAULT_THINKING_DISPLAY,
    temperature: float = DEFAULT_TEMPERATURE,
    cache_enabled: bool = DEFAULT_CACHE_ENABLED,
    cache_type: str = DEFAULT_CACHE_TYPE,
    cache_ttl: str = DEFAULT_CACHE_TTL,
    profile_cache_dir: str | Path | None = None,
) -> SingleLLMRequestContext:
    benchmark = build_benchmark_context(
        task_dir=task_dir,
        testcase_id=testcase_id,
        data_root=data_root,
    )
    materialized = materialize_benchmark_context(
        benchmark,
        profile_cache_dir=profile_cache_dir,
    )
    dataset_summary = render_single_llm_dataset_summary(
        task=benchmark.bundle.task,
        dataset_paths=benchmark.dataset_paths,
        visible_actions=benchmark.visible_actions,
        table_profiles=materialized.table_profiles,
        primary_train_profile=materialized.primary_train_profile,
        join_profile=materialized.join_profile,
        target_profile=materialized.target_profile,
    )
    output_format = _build_output_format()
    prompt_parts = build_single_llm_prompt_parts(
        task_text=benchmark.bundle.task["goal"],
        dataset_summary=dataset_summary,
        context_summary=benchmark.context_summary,
        candidate_actions=benchmark.candidate_actions_json,
        output_format=output_format,
    )
    thinking, output_config, request_temperature = _build_reasoning_controls(
        reasoning_enabled=reasoning_enabled,
        reasoning_effort=reasoning_effort,
        thinking_type=thinking_type,
        thinking_display=thinking_display,
        temperature=temperature,
    )
    system_blocks = [{"type": "text", "text": prompt_parts["static_prompt"]}]
    if cache_enabled:
        system_blocks[0]["cache_control"] = {"type": cache_type, "ttl": cache_ttl}
    message_content_blocks = [{"type": "text", "text": prompt_parts["dynamic_prompt"]}]
    return SingleLLMRequestContext(
        benchmark=benchmark,
        materialized=materialized,
        output_format=output_format,
        prompt_parts=prompt_parts,
        prompt=prompt_parts["full_prompt"],
        system_blocks=system_blocks,
        message_content_blocks=message_content_blocks,
        thinking=thinking,
        output_config=output_config,
        request_temperature=request_temperature,
    )
