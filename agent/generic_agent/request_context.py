from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agent.agentic_core.request_controls import build_reasoning_controls
from agent.context_builder import BenchmarkContext, build_benchmark_context
from agent.generic_agent.tools import GENERIC_TOOL_NAMES
from agent.llm.config import (
    DEFAULT_CACHE_ENABLED,
    DEFAULT_CACHE_TTL,
    DEFAULT_CACHE_TYPE,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REASONING_ENABLED,
    DEFAULT_TEMPERATURE,
    DEFAULT_THINKING_DISPLAY,
    DEFAULT_THINKING_TYPE,
)
from agent.prompts.generic_agent import build_generic_agent_prompt_parts, build_generic_output_format


def build_generic_dataset_summary() -> str:
    return (
        "No precomputed dataset summary is provided for this method. Inspect the raw dataset "
        "files under `dataset/` with only the generic tools exposed in this run."
    )


@dataclass(frozen=True)
class GenericAgentRequestContext:
    benchmark: BenchmarkContext
    output_format: str
    prompt_parts: dict[str, str]
    prompt: str
    system_blocks: list[dict]
    message_content_blocks: list[dict]
    thinking: dict | None
    output_config: dict | None
    request_temperature: float


def build_generic_agent_request_context(
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
) -> GenericAgentRequestContext:
    benchmark = build_benchmark_context(
        task_dir=task_dir,
        testcase_id=testcase_id,
        data_root=data_root,
    )
    output_format = build_generic_output_format()
    prompt_parts = build_generic_agent_prompt_parts(
        task_text=benchmark.bundle.task["goal"],
        dataset_summary=build_generic_dataset_summary(),
        context_summary=benchmark.context_summary,
        candidate_actions=benchmark.candidate_actions_json,
        output_format=output_format,
        tool_names=GENERIC_TOOL_NAMES,
    )
    thinking, output_config, request_temperature = build_reasoning_controls(
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
    return GenericAgentRequestContext(
        benchmark=benchmark,
        output_format=output_format,
        prompt_parts=prompt_parts,
        prompt=prompt_parts["full_prompt"],
        system_blocks=system_blocks,
        message_content_blocks=message_content_blocks,
        thinking=thinking,
        output_config=output_config,
        request_temperature=request_temperature,
    )
