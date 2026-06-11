from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from agent.agentic_core.execution import run_agentic_loop
from agent.agentic_core.tool_runtime import AgenticToolRuntime
from agent.agentic_core.types import AgenticRunBudget, AgenticRunResult
from agent.prompts.proposed_agent import (
    build_add_phase_message_content_blocks,
    build_add_phase_prompt_text,
    build_remove_phase_message_content_blocks,
    build_remove_phase_prompt_text,
)
from agent.proposed_agent.reconciliation import (
    parse_and_validate_add_phase_text,
    parse_and_validate_remove_phase_text,
    reconcile_phase_outputs,
)
from agent.proposed_agent.request_context import ProposedAgentRequestContext


@dataclass(frozen=True)
class ProposedAgentControllerResult:
    status: str
    add_result: AgenticRunResult
    remove_result: AgenticRunResult | None
    parsed_prediction: dict[str, Any] | None
    validation_warnings: list[str]
    reconciliation_warnings: list[str]
    add_prompt: str
    remove_prompt: str | None
    error_message: str | None = None


def run_proposed_agent_controller(
    *,
    context: ProposedAgentRequestContext,
    tool_runtime: AgenticToolRuntime,
    call_fn: Callable[..., dict[str, Any]],
    model_name: str,
    max_tokens: int,
    temperature: float,
    thinking: dict | None,
    output_config: dict | None,
    budget: AgenticRunBudget,
    input_cost_per_million: float,
    output_cost_per_million: float,
    cache_read_cost_per_million: float,
    cache_write_5m_cost_per_million: float,
    cache_write_1h_cost_per_million: float,
    capture_llm_calls: bool = False,
) -> ProposedAgentControllerResult:
    active_action_ids = set(context.benchmark.bundle.testcase.get("input", {}).get("context_action_ids", []))
    add_prompt = build_add_phase_prompt_text(context.prompt)
    add_message_blocks = build_add_phase_message_content_blocks(context.prompt_parts["dynamic_prompt"])

    add_result = run_agentic_loop(
        method_name="proposed_agent",
        phase_name="add",
        prompt_text=add_prompt,
        system_blocks=context.system_blocks,
        message_content_blocks=add_message_blocks,
        model_name=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        thinking=thinking,
        output_config=output_config,
        tool_runtime=tool_runtime,
        call_fn=call_fn,
        parse_and_validate=lambda text: parse_and_validate_add_phase_text(
            text,
            valid_action_ids=context.benchmark.valid_action_ids,
            active_action_ids=active_action_ids,
        ),
        budget=budget,
        input_cost_per_million=input_cost_per_million,
        output_cost_per_million=output_cost_per_million,
        cache_read_cost_per_million=cache_read_cost_per_million,
        cache_write_5m_cost_per_million=cache_write_5m_cost_per_million,
        cache_write_1h_cost_per_million=cache_write_1h_cost_per_million,
        capture_llm_calls=capture_llm_calls,
    )
    if add_result.parsed_prediction is None:
        return ProposedAgentControllerResult(
            status="failed",
            add_result=add_result,
            remove_result=None,
            parsed_prediction=None,
            validation_warnings=add_result.validation_warnings,
            reconciliation_warnings=[],
            add_prompt=add_prompt,
            remove_prompt=None,
            error_message=f"add phase failed: {add_result.error_message}",
        )

    remove_prompt = build_remove_phase_prompt_text(context.prompt, add_result.parsed_prediction)
    remove_message_blocks = build_remove_phase_message_content_blocks(
        context.prompt_parts["dynamic_prompt"],
        add_result.parsed_prediction,
    )
    remove_result = run_agentic_loop(
        method_name="proposed_agent",
        phase_name="remove",
        prompt_text=remove_prompt,
        system_blocks=context.system_blocks,
        message_content_blocks=remove_message_blocks,
        model_name=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        thinking=thinking,
        output_config=output_config,
        tool_runtime=tool_runtime,
        call_fn=call_fn,
        parse_and_validate=lambda text: parse_and_validate_remove_phase_text(
            text,
            valid_action_ids=context.benchmark.valid_action_ids,
            active_action_ids=active_action_ids,
        ),
        budget=budget,
        input_cost_per_million=input_cost_per_million,
        output_cost_per_million=output_cost_per_million,
        cache_read_cost_per_million=cache_read_cost_per_million,
        cache_write_5m_cost_per_million=cache_write_5m_cost_per_million,
        cache_write_1h_cost_per_million=cache_write_1h_cost_per_million,
        capture_llm_calls=capture_llm_calls,
    )
    if remove_result.parsed_prediction is None:
        return ProposedAgentControllerResult(
            status="failed",
            add_result=add_result,
            remove_result=remove_result,
            parsed_prediction=None,
            validation_warnings=[
                *add_result.validation_warnings,
                *remove_result.validation_warnings,
            ],
            reconciliation_warnings=[],
            add_prompt=add_prompt,
            remove_prompt=remove_prompt,
            error_message=f"remove phase failed: {remove_result.error_message}",
        )

    parsed_prediction, reconciliation_warnings = reconcile_phase_outputs(
        add_prediction=add_result.parsed_prediction,
        remove_prediction=remove_result.parsed_prediction,
        valid_action_ids=context.benchmark.valid_action_ids,
        active_action_ids=active_action_ids,
        visible_actions=context.benchmark.visible_actions,
    )
    return ProposedAgentControllerResult(
        status="success",
        add_result=add_result,
        remove_result=remove_result,
        parsed_prediction=parsed_prediction,
        validation_warnings=[
            *add_result.validation_warnings,
            *remove_result.validation_warnings,
        ],
        reconciliation_warnings=reconciliation_warnings,
        add_prompt=add_prompt,
        remove_prompt=remove_prompt,
        error_message=None,
    )
