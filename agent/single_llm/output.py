from __future__ import annotations

from pathlib import Path

from agent.llm.telemetry import render_trace_markdown
from agent.output_artifacts import write_output_bundle
from agent.single_llm.execution import SingleLLMExecutionResult
from agent.single_llm.request_context import SingleLLMRequestContext


def write_single_llm_output_bundle(
    *,
    task_dir: str | Path,
    testcase_id: str,
    run_id: str,
    context: SingleLLMRequestContext,
    execution: SingleLLMExecutionResult,
    elapsed_seconds: int | float,
    model_name: str,
    reasoning_enabled: bool,
    thinking_type: str,
    thinking_display: str,
    reasoning_effort: str,
) -> dict[str, Path]:
    trace_text = render_trace_markdown(f"{testcase_id} Single LLM {run_id}", execution.trace_entries)
    return write_output_bundle(
        task_dir=task_dir,
        competition_slug=context.benchmark.bundle.task["competition_slug"],
        testcase_id=testcase_id,
        agent_name="single_llm",
        run_by="agent_runner",
        run_id=run_id,
        predicted_add_action_ids=execution.parsed_prediction.get("predicted_add_action_ids", []),
        predicted_remove_action_ids=execution.parsed_prediction.get("predicted_remove_action_ids", []),
        notes="One-shot LLM baseline run.",
        time_spent_seconds=elapsed_seconds,
        token_usage={
            "input_tokens": None if execution.last_response is None else execution.last_response.get("input_tokens"),
            "output_tokens": None if execution.last_response is None else execution.last_response.get("output_tokens"),
            "total_tokens": None if execution.last_response is None else execution.last_response.get("total_tokens"),
        },
        trace_text=trace_text,
        metadata={
            "artifact_type": "output_run_metadata",
            "status": execution.status,
            "model_name": model_name,
            "api_provider": "anthropic",
            "api_call_count": execution.api_call_count,
            "tool_call_count": 0,
            "cost_usd": execution.cumulative_cost_usd,
            "cache_usage": None
            if execution.last_response is None
            else {
                "cache_creation_input_tokens": execution.last_response.get("cache_creation_input_tokens"),
                "cache_read_input_tokens": execution.last_response.get("cache_read_input_tokens"),
                "cache_creation": execution.last_response.get("cache_creation"),
            },
            "reasoning": {
                "enabled": reasoning_enabled,
                "thinking_type": thinking_type if reasoning_enabled else None,
                "display": thinking_display if reasoning_enabled else None,
                "effort": reasoning_effort if reasoning_enabled else None,
            },
            "error_message": execution.error_message,
            "notes": "Single-call LLM baseline metadata.",
        },
        extra_artifacts=[
            {
                "kind": "prompt",
                "filename": f"{testcase_id.split('_', 1)[0]}_single_llm_{run_id}.prompt.md",
                "description": "Final prompt text sent to the single LLM baseline.",
                "content": context.prompt,
            }
        ],
    )
