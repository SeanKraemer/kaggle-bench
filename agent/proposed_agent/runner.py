from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path
from typing import Any

from agent.agentic_core.scratchpad import JsonScratchpad
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.trace import (
    api_call_records_jsonl,
    render_agentic_trace_markdown,
    tool_results_jsonl,
)
from agent.agentic_core.types import AgenticRunBudget, AgenticRunResult
from agent.config import DEFAULT_API_KEY_PATH
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
from agent.output_artifacts import (
    build_provenance_basename,
    write_failed_provenance_bundle,
    write_output_bundle,
)
from agent.proposed_agent.controller import (
    ProposedAgentControllerResult,
    run_proposed_agent_controller,
)
from agent.proposed_agent.request_context import build_proposed_agent_request_context
from agent.proposed_agent.tools import (
    DEFAULT_SCRATCHPAD_MAX_CHARS,
    DEFAULT_TOOL_OUTPUT_MAX_CHARS,
    build_proposed_tool_specs,
)


def run_proposed_agent(
    *,
    task_dir: str | Path,
    testcase_id: str,
    run_id: str,
    data_root: str | Path,
    profile_cache_dir: str | Path | None = None,
    api_key_path: str | Path = DEFAULT_API_KEY_PATH,
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
    max_turns_per_phase: int = 8,
    max_tool_calls_per_phase: int = 20,
    max_validation_retries: int = 1,
    request_timeout_seconds: int | float = DEFAULT_REQUEST_TIMEOUT_SECONDS,
    max_tool_output_chars: int = DEFAULT_TOOL_OUTPUT_MAX_CHARS,
    max_scratchpad_chars: int = DEFAULT_SCRATCHPAD_MAX_CHARS,
    reasoning_enabled: bool = DEFAULT_REASONING_ENABLED,
    thinking_type: str = DEFAULT_THINKING_TYPE,
    thinking_display: str = DEFAULT_THINKING_DISPLAY,
    reasoning_effort: str = DEFAULT_REASONING_EFFORT,
    cache_enabled: bool = DEFAULT_CACHE_ENABLED,
    cache_type: str = DEFAULT_CACHE_TYPE,
    cache_ttl: str = DEFAULT_CACHE_TTL,
    capture_llm_calls: bool = False,
    time_fn=time.perf_counter,
) -> dict[str, Path]:
    started_at = time_fn()
    context = build_proposed_agent_request_context(
        task_dir=task_dir,
        testcase_id=testcase_id,
        data_root=Path(data_root).expanduser().resolve(),
        profile_cache_dir=profile_cache_dir,
        reasoning_enabled=reasoning_enabled,
        reasoning_effort=reasoning_effort,
        thinking_type=thinking_type,
        thinking_display=thinking_display,
        temperature=temperature,
        cache_enabled=cache_enabled,
        cache_type=cache_type,
        cache_ttl=cache_ttl,
    )
    if llm_call is None:
        api_key = load_api_key(api_key_path)
        call_fn = build_llm_caller(provider="anthropic", api_key=api_key)
    else:
        call_fn = llm_call

    with tempfile.TemporaryDirectory(prefix="proposed_agent_") as tmp:
        scratchpad_path = Path(tmp) / "scratchpad.json"
        scratchpad = JsonScratchpad(scratchpad_path, max_chars=max_scratchpad_chars)
        tool_runtime = AgenticToolRuntime(
            build_proposed_tool_specs(
                materialized=context.materialized,
                scratchpad=scratchpad,
            ),
            max_result_chars=max_tool_output_chars,
        )
        controller_result = run_proposed_agent_controller(
            context=context,
            tool_runtime=tool_runtime,
            call_fn=call_fn,
            model_name=model_name,
            max_tokens=max_tokens,
            temperature=context.request_temperature,
            thinking=context.thinking,
            output_config=context.output_config,
            budget=AgenticRunBudget(
                max_turns=max_turns_per_phase,
                max_tool_calls=max_tool_calls_per_phase,
                max_validation_retries=max_validation_retries,
                timeout_seconds=request_timeout_seconds,
                cost_cap_usd=cost_cap_usd,
            ),
            input_cost_per_million=input_cost_per_million,
            output_cost_per_million=output_cost_per_million,
            cache_read_cost_per_million=cache_read_cost_per_million,
            cache_write_5m_cost_per_million=cache_write_5m_cost_per_million,
            cache_write_1h_cost_per_million=cache_write_1h_cost_per_million,
            capture_llm_calls=capture_llm_calls,
        )
        elapsed_seconds = round(time_fn() - started_at, 3)
        base_artifact_name = build_provenance_basename(
            testcase_id,
            "proposed_agent",
            run_id,
        )
        extra_artifacts = _build_extra_artifacts(
            base_artifact_name=base_artifact_name,
            failed=controller_result.parsed_prediction is None,
            context_prompt=context.prompt,
            controller_result=controller_result,
            scratchpad_path=scratchpad_path,
            capture_llm_calls=capture_llm_calls,
        )
        trace_text = _render_combined_trace(
            testcase_id=testcase_id,
            run_id=run_id,
            controller_result=controller_result,
            tool_allowlist=tool_runtime.list_tool_names(),
        )
        metadata = _build_metadata(
            controller_result=controller_result,
            model_name=model_name,
            elapsed_seconds=elapsed_seconds,
            tool_allowlist=tool_runtime.list_tool_names(),
        )
        if controller_result.parsed_prediction is None:
            failed_paths = write_failed_provenance_bundle(
                task_dir=task_dir,
                competition_slug=context.benchmark.bundle.task["competition_slug"],
                testcase_id=testcase_id,
                agent_name="proposed_agent",
                run_by="agent_runner",
                run_id=run_id,
                trace_text=trace_text,
                metadata={
                    "artifact_type": "failed_output_run_metadata",
                    **metadata,
                },
                extra_artifacts=extra_artifacts,
            )
            raise ValueError(
                f"proposed_agent did not produce a valid prediction. "
                f"Failed provenance written to {failed_paths['metadata_path']}. "
                f"Error: {controller_result.error_message}"
            )

        return write_output_bundle(
            task_dir=task_dir,
            competition_slug=context.benchmark.bundle.task["competition_slug"],
            testcase_id=testcase_id,
            agent_name="proposed_agent",
            run_by="agent_runner",
            run_id=run_id,
            predicted_add_action_ids=controller_result.parsed_prediction.get(
                "predicted_add_action_ids", []
            ),
            predicted_remove_action_ids=controller_result.parsed_prediction.get(
                "predicted_remove_action_ids", []
            ),
            notes="Proposed specific-tool agent run.",
            time_spent_seconds=elapsed_seconds,
            token_usage=_combined_token_usage(controller_result),
            trace_text=trace_text,
            metadata={
                "artifact_type": "output_run_metadata",
                **metadata,
            },
            extra_artifacts=extra_artifacts,
        )


def _build_extra_artifacts(
    *,
    base_artifact_name: str,
    failed: bool,
    context_prompt: str,
    controller_result: ProposedAgentControllerResult,
    scratchpad_path: Path,
    capture_llm_calls: bool,
) -> list[dict[str, str]]:
    infix = ".failed" if failed else ""
    add_result = controller_result.add_result
    remove_result = controller_result.remove_result
    tool_results = [
        *add_result.tool_results,
        *((remove_result.tool_results if remove_result is not None else [])),
    ]
    artifacts = [
        {
            "kind": "prompt",
            "filename": f"{base_artifact_name}{infix}.prompt.md",
            "description": "Base prompt text sent to the proposed agent.",
            "content": context_prompt,
        },
        {
            "kind": "scratchpad",
            "filename": f"{base_artifact_name}{infix}.scratchpad.json",
            "description": "Scratchpad contents at the end of the proposed-agent run.",
            "content": scratchpad_path.read_text(encoding="utf-8"),
        },
        {
            "kind": "tool_calls",
            "filename": f"{base_artifact_name}{infix}.tool_calls.jsonl",
            "description": "Normalized tool-call records for the proposed-agent run.",
            "content": tool_results_jsonl(tool_results),
        },
    ]
    if capture_llm_calls:
        api_call_records = [
            *add_result.api_call_records,
            *((remove_result.api_call_records if remove_result is not None else [])),
        ]
        artifacts.append(
            {
                "kind": "api_calls",
                "filename": f"{base_artifact_name}{infix}.api_calls.jsonl",
                "description": "Sanitized model request and response records for each proposed-agent turn.",
                "content": api_call_records_jsonl(api_call_records),
            }
        )
    return artifacts


def _render_combined_trace(
    *,
    testcase_id: str,
    run_id: str,
    controller_result: ProposedAgentControllerResult,
    tool_allowlist: list[str],
) -> str:
    sections = [
        f"# {testcase_id}_{run_id} Proposed Agent Trace",
        "",
        f"- Status: `{controller_result.status}`",
        f"- Tool allowlist: `{', '.join(tool_allowlist)}`",
        "",
        render_agentic_trace_markdown(
            title="Add Phase",
            result=controller_result.add_result,
        ).strip(),
    ]
    if controller_result.remove_result is not None:
        sections.append(
            render_agentic_trace_markdown(
                title="Remove Phase",
                result=controller_result.remove_result,
            ).strip()
        )
    sections.extend(
        [
            "## Reconciliation",
            _render_reconciliation_notes(controller_result).strip(),
        ]
    )
    return "\n\n".join(sections).strip() + "\n"


def _render_reconciliation_notes(controller_result: ProposedAgentControllerResult) -> str:
    lines = [
        f"- Status: `{controller_result.status}`",
        f"- Error: `{controller_result.error_message}`",
        "- Final prediction:",
        "```json",
        json.dumps(controller_result.parsed_prediction, indent=2, sort_keys=True),
        "```",
    ]
    if controller_result.validation_warnings:
        lines.append("- Phase validation warnings:")
        lines.extend(f"  - {warning}" for warning in controller_result.validation_warnings)
    if controller_result.reconciliation_warnings:
        lines.append("- Reconciliation warnings:")
        lines.extend(f"  - {warning}" for warning in controller_result.reconciliation_warnings)
    return "\n".join(lines) + "\n"


def _build_metadata(
    *,
    controller_result: ProposedAgentControllerResult,
    model_name: str,
    elapsed_seconds: int | float,
    tool_allowlist: list[str],
) -> dict[str, Any]:
    add_result = controller_result.add_result
    remove_result = controller_result.remove_result
    results = [result for result in [add_result, remove_result] if result is not None]
    return {
        "status": controller_result.status,
        "model_name": model_name,
        "api_provider": "anthropic",
        "api_call_count": sum(result.api_call_count for result in results),
        "tool_call_count": sum(result.tool_call_count for result in results),
        "cost_usd": sum(result.cumulative_cost_usd for result in results),
        "time_spent_seconds": elapsed_seconds,
        "token_usage": _combined_token_usage(controller_result),
        "error_message": controller_result.error_message,
        "validation_warnings": controller_result.validation_warnings,
        "reconciliation_warnings": controller_result.reconciliation_warnings,
        "phase_statuses": {
            "add": add_result.status,
            "remove": remove_result.status if remove_result is not None else None,
        },
        "tool_allowlist": tool_allowlist,
    }


def _combined_token_usage(controller_result: ProposedAgentControllerResult) -> dict[str, int | None]:
    results: list[AgenticRunResult] = [
        result
        for result in [controller_result.add_result, controller_result.remove_result]
        if result is not None
    ]
    if not results:
        return {"input_tokens": None, "output_tokens": None, "total_tokens": None}
    input_tokens = sum(result.token_usage.get("input_tokens") or 0 for result in results)
    output_tokens = sum(result.token_usage.get("output_tokens") or 0 for result in results)
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
    }
