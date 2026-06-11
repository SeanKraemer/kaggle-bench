from __future__ import annotations

from pathlib import Path

from agent.context_builder import build_benchmark_context, materialize_benchmark_context
from agent.output_artifacts import write_output_bundle
from agent.rule_based.policy import predict_actions


def run_rule_based(
    *,
    task_dir: str | Path,
    testcase_id: str,
    run_id: str,
    data_root: str | Path,
    profile_cache_dir: str | Path | None = None,
) -> dict[str, Path]:
    benchmark = build_benchmark_context(
        task_dir=task_dir,
        testcase_id=testcase_id,
        data_root=data_root,
    )
    materialized = materialize_benchmark_context(
        benchmark,
        profile_cache_dir=profile_cache_dir,
    )
    primary_train_profile = materialized.primary_train_profile

    dataset_insights = {
        "schema_profile": primary_train_profile["schema_profile"],
        "missingness_profile": primary_train_profile["missingness_profile"],
        "numeric_profile": primary_train_profile["numeric_profile"],
        "boolean_like_profile": primary_train_profile["boolean_like_profile"],
        "join_profile": materialized.join_profile,
        "target_profile": materialized.target_profile,
        "target_column": benchmark.bundle.task["dataset"]["target_column"],
        "primary_key": benchmark.bundle.task["dataset"].get("primary_key"),
    }
    predictions = predict_actions(
        actions=benchmark.visible_actions,
        context_action_ids=benchmark.bundle.testcase["input"]["context_action_ids"],
        dataset_insights=dataset_insights,
    )

    trace_lines = [
        f"# {testcase_id} Rule-Based {run_id}",
        "",
        "## Dataset insights",
        f"- Join coverage: `{dataset_insights['join_profile']['left_key_coverage_rate']}`",
        f"- Target column: `{dataset_insights['target_column']}`",
        f"- Primary key: `{dataset_insights['primary_key']}`",
        "",
        "## Predictions",
        f"- Add: `{predictions['predicted_add_action_ids']}`",
        f"- Remove: `{predictions['predicted_remove_action_ids']}`",
        "",
        "## Action Decisions",
    ]
    for record in predictions["decision_log"]:
        trace_lines.extend(
            [
                f"### {record['action_id']}",
                f"- Action type: `{record['action_type']}`",
                f"- Candidate side: `{record['candidate_side']}`",
                f"- Decision: `{record['decision']}`",
                f"- triggered rule: `{record['triggered_rule']}`"
                if record["triggered_rule"] is not None
                else "- triggered rule: `none`",
                "- Details:",
            ]
        )
        for detail in record["details"]:
            trace_lines.append(f"  - {detail}")
        trace_lines.append("")

    return write_output_bundle(
        task_dir=task_dir,
        competition_slug=benchmark.bundle.task["competition_slug"],
        testcase_id=testcase_id,
        agent_name="rule_based",
        run_by="agent_runner",
        run_id=run_id,
        predicted_add_action_ids=predictions["predicted_add_action_ids"],
        predicted_remove_action_ids=predictions["predicted_remove_action_ids"],
        notes="Conservative rule-based baseline run.",
        time_spent_seconds=0,
        token_usage={"input_tokens": None, "output_tokens": None, "total_tokens": None},
        trace_text="\n".join(trace_lines),
        metadata={
            "artifact_type": "output_run_metadata",
            "status": "success",
            "model_name": None,
            "api_provider": None,
            "api_call_count": 0,
            "tool_call_count": 0,
            "cost_usd": 0.0,
            "error_message": None,
            "notes": "Rule-based baseline metadata.",
        },
    )
