from __future__ import annotations

import shutil
import time
from pathlib import Path
from typing import Any

from agent.agentic_core.execution import run_agentic_loop
from agent.agentic_core.parsing import parse_text_or_prediction_file
from agent.agentic_core.scratchpad import JsonScratchpad
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.trace import (
    api_call_records_jsonl,
    render_agentic_trace_markdown,
    tool_results_jsonl,
)
from agent.agentic_core.types import AgenticRunBudget, AgenticRunResult
from agent.config import DEFAULT_API_KEY_PATH, ROOT
from agent.generic_agent.request_context import build_generic_agent_request_context
from agent.generic_agent.tools import (
    DEFAULT_SCRATCHPAD_MAX_CHARS,
    DEFAULT_TOOL_TIMEOUT_SECONDS,
    DEFAULT_TOOL_OUTPUT_MAX_CHARS,
    build_generic_tool_specs,
)
from agent.generic_agent.workspace import prepare_generic_workspace
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
from agent.prediction_validation import parse_and_validate_prediction_text


def run_generic_agent(
    *,
    task_dir: str | Path,
    testcase_id: str,
    run_id: str,
    data_root: str | Path,
    api_key_path: str | Path = DEFAULT_API_KEY_PATH,
    llm_call=None,
    bash_executor=None,
    python_executor=None,
    model_name: str = DEFAULT_MODEL_NAME,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    cost_cap_usd: float = DEFAULT_COST_CAP_USD,
    input_cost_per_million: float = DEFAULT_INPUT_COST_PER_MILLION,
    output_cost_per_million: float = DEFAULT_OUTPUT_COST_PER_MILLION,
    cache_read_cost_per_million: float = DEFAULT_CACHE_READ_COST_PER_MILLION,
    cache_write_5m_cost_per_million: float = DEFAULT_CACHE_WRITE_5M_COST_PER_MILLION,
    cache_write_1h_cost_per_million: float = DEFAULT_CACHE_WRITE_1H_COST_PER_MILLION,
    max_turns: int = 10,
    max_tool_calls: int = 30,
    max_validation_retries: int = 1,
    request_timeout_seconds: int | float = DEFAULT_REQUEST_TIMEOUT_SECONDS,
    tool_timeout_seconds: int | float = DEFAULT_TOOL_TIMEOUT_SECONDS,
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
    dataset_root = Path(data_root).expanduser().resolve()
    context = build_generic_agent_request_context(
        task_dir=task_dir,
        testcase_id=testcase_id,
        data_root=dataset_root,
        reasoning_enabled=reasoning_enabled,
        reasoning_effort=reasoning_effort,
        thinking_type=thinking_type,
        thinking_display=thinking_display,
        temperature=temperature,
        cache_enabled=cache_enabled,
        cache_type=cache_type,
        cache_ttl=cache_ttl,
    )
    workspace = prepare_generic_workspace(
        task_goal=context.benchmark.bundle.task["goal"],
        testcase=context.benchmark.bundle.testcase,
        visible_actions=context.benchmark.visible_actions,
        prompt=context.prompt,
        dataset_root=dataset_root,
    )
    preserve_workspace = False
    try:
        scratchpad = JsonScratchpad(
            workspace.scratchpad_path,
            max_chars=max_scratchpad_chars,
        )
        tool_kwargs: dict[str, Any] = {}
        if bash_executor is not None:
            tool_kwargs["bash_executor"] = bash_executor
        if python_executor is not None:
            tool_kwargs["python_executor"] = python_executor
        tool_runtime = AgenticToolRuntime(
            build_generic_tool_specs(
                workdir=workspace.workdir,
                scratchpad=scratchpad,
                repo_root=ROOT,
                timeout_seconds=tool_timeout_seconds,
                max_output_chars=max_tool_output_chars,
                **tool_kwargs,
            )
        )
        if llm_call is None:
            api_key = load_api_key(api_key_path)
            call_fn = build_llm_caller(provider="anthropic", api_key=api_key)
        else:
            call_fn = llm_call

        allowed_remove_action_ids = set(
            context.benchmark.bundle.testcase["input"]["context_action_ids"]
        )

        def parse_callback(raw_text: str) -> tuple[dict, list[str]]:
            return parse_text_or_prediction_file(
                raw_text,
                prediction_path=workspace.prediction_path,
                parse_and_validate=lambda text: parse_and_validate_prediction_text(
                    text,
                    valid_action_ids=context.benchmark.valid_action_ids,
                    allowed_remove_action_ids=allowed_remove_action_ids,
                ),
            )

        execution = run_agentic_loop(
            method_name="generic_agent",
            phase_name=None,
            prompt_text=context.prompt,
            system_blocks=context.system_blocks,
            message_content_blocks=context.message_content_blocks,
            model_name=model_name,
            max_tokens=max_tokens,
            temperature=context.request_temperature,
            thinking=context.thinking,
            output_config=context.output_config,
            tool_runtime=tool_runtime,
            call_fn=call_fn,
            parse_and_validate=parse_callback,
            budget=AgenticRunBudget(
                max_turns=max_turns,
                max_tool_calls=max_tool_calls,
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
            "generic_agent",
            run_id,
        )

        if execution.parsed_prediction is None:
            preserve_workspace = True
            trace_text = render_agentic_trace_markdown(
                title=f"{testcase_id}_{run_id} Generic Agent Failed Trace",
                result=execution,
                extra_sections={
                    "Workspace Preserved": str(workspace.workdir),
                    "Tool Allowlist": ", ".join(tool_runtime.list_tool_names()),
                },
            )
            failed_paths = write_failed_provenance_bundle(
                task_dir=task_dir,
                competition_slug=context.benchmark.bundle.task["competition_slug"],
                testcase_id=testcase_id,
                agent_name="generic_agent",
                run_by="agent_runner",
                run_id=run_id,
                trace_text=trace_text,
                metadata={
                    "artifact_type": "failed_output_run_metadata",
                    "status": execution.status,
                    "model_name": model_name,
                    "api_provider": "anthropic",
                    "api_call_count": execution.api_call_count,
                    "tool_call_count": execution.tool_call_count,
                    "cost_usd": execution.cumulative_cost_usd,
                    "time_spent_seconds": elapsed_seconds,
                    "token_usage": execution.token_usage,
                    "error_message": execution.error_message,
                    "validation_warnings": execution.validation_warnings,
                    "tool_allowlist": tool_runtime.list_tool_names(),
                    "workspace_preserved": True,
                    "workspace_path": str(workspace.workdir),
                },
                extra_artifacts=_build_extra_artifacts(
                    base_artifact_name=base_artifact_name,
                    failed=True,
                    prompt=context.prompt,
                    scratchpad_path=workspace.scratchpad_path,
                    execution=execution,
                    capture_llm_calls=capture_llm_calls,
                ),
            )
            raise ValueError(
                f"generic_agent did not produce a valid prediction. "
                f"Workspace preserved at {workspace.workdir}. "
                f"Failed provenance written to {failed_paths['metadata_path']}. "
                f"Error: {execution.error_message}"
            )

        trace_text = render_agentic_trace_markdown(
            title=f"{testcase_id}_{run_id} Generic Agent Trace",
            result=execution,
            extra_sections={
                "Workspace": str(workspace.workdir),
                "Tool Allowlist": ", ".join(tool_runtime.list_tool_names()),
            },
        )
        artifact_paths = write_output_bundle(
            task_dir=task_dir,
            competition_slug=context.benchmark.bundle.task["competition_slug"],
            testcase_id=testcase_id,
            agent_name="generic_agent",
            run_by="agent_runner",
            run_id=run_id,
            predicted_add_action_ids=execution.parsed_prediction.get("predicted_add_action_ids", []),
            predicted_remove_action_ids=execution.parsed_prediction.get(
                "predicted_remove_action_ids", []
            ),
            notes="Generic tool agent run.",
            time_spent_seconds=elapsed_seconds,
            token_usage=execution.token_usage,
            trace_text=trace_text,
            metadata={
                "artifact_type": "output_run_metadata",
                "status": execution.status,
                "model_name": model_name,
                "api_provider": "anthropic",
                "api_call_count": execution.api_call_count,
                "tool_call_count": execution.tool_call_count,
                "cost_usd": execution.cumulative_cost_usd,
                "time_spent_seconds": elapsed_seconds,
                "token_usage": execution.token_usage,
                "error_message": execution.error_message,
                "validation_warnings": execution.validation_warnings,
                "tool_allowlist": tool_runtime.list_tool_names(),
                "workspace_preserved": False,
            },
            extra_artifacts=_build_extra_artifacts(
                base_artifact_name=base_artifact_name,
                failed=False,
                prompt=context.prompt,
                scratchpad_path=workspace.scratchpad_path,
                execution=execution,
                capture_llm_calls=capture_llm_calls,
            ),
        )
        shutil.rmtree(workspace.workdir)
        return artifact_paths
    except Exception:
        preserve_workspace = True
        raise
    finally:
        if workspace.workdir.exists() and not preserve_workspace:
            shutil.rmtree(workspace.workdir)


def _build_extra_artifacts(
    *,
    base_artifact_name: str,
    failed: bool,
    prompt: str,
    scratchpad_path: Path,
    execution: AgenticRunResult,
    capture_llm_calls: bool,
) -> list[dict[str, str]]:
    infix = ".failed" if failed else ""
    artifacts = [
        {
            "kind": "prompt",
            "filename": f"{base_artifact_name}{infix}.prompt.md",
            "description": "Final prompt text sent to the generic agent.",
            "content": prompt,
        },
        {
            "kind": "scratchpad",
            "filename": f"{base_artifact_name}{infix}.scratchpad.json",
            "description": "Scratchpad contents at the end of the generic-agent run.",
            "content": scratchpad_path.read_text(encoding="utf-8"),
        },
        {
            "kind": "tool_calls",
            "filename": f"{base_artifact_name}{infix}.tool_calls.jsonl",
            "description": "Normalized tool-call records for the generic-agent run.",
            "content": tool_results_jsonl(execution.tool_results),
        },
    ]
    if capture_llm_calls:
        artifacts.append(
            {
                "kind": "api_calls",
                "filename": f"{base_artifact_name}{infix}.api_calls.jsonl",
                "description": "Sanitized model request and response records for each agentic turn.",
                "content": api_call_records_jsonl(execution.api_call_records),
            }
        )
    return artifacts
