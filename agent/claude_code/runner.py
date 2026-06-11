from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

from agent.claude_code.command import build_claude_command, build_claude_environment
from agent.claude_code.stream import normalize_exec_result
from agent.claude_code.trace import build_trace_text
from agent.claude_code.workspace import prepare_claude_workspace
from agent.config import DEFAULT_API_KEY_PATH, DEFAULT_CLAUDE_CODE_AUTH_MODE, DEFAULT_MODEL_NAME
from agent.context_builder import build_benchmark_context
from agent.llm.auth import load_api_key
from agent.output_artifacts import (
    build_provenance_basename,
    write_json,
    write_output_bundle,
    write_text_artifact,
)
from agent.prediction_validation import parse_and_validate_prediction_text
from agent.prompts.claude_code import build_claude_code_prompt

API_KEY_OVERRIDE_ENV_VAR = "CLAUDE_CODE_ALLOW_API_KEY"


def default_executor(*, workdir: Path, command: list[str], env: dict[str, str]) -> dict:
    result = subprocess.run(
        command,
        cwd=workdir,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
        "cost_usd": None,
    }


def load_prediction_text(*, prediction_path: Path, exec_result: dict) -> str | None:
    if prediction_path.exists():
        return prediction_path.read_text(encoding="utf-8")

    final_result = exec_result.get("final_result")
    if isinstance(final_result, dict):
        fallback_text = final_result.get("result")
        if isinstance(fallback_text, str) and fallback_text.strip():
            return fallback_text
    return None


def _claude_provenance_dir(task_dir: str | Path) -> Path:
    provenance_dir = Path(task_dir) / "outputs" / "provenance"
    provenance_dir.mkdir(parents=True, exist_ok=True)
    return provenance_dir


def _persist_failure_debug_artifacts(
    *,
    task_dir: str | Path,
    competition_slug: str,
    testcase_id: str,
    run_id: str,
    run_by: str,
    model_name: str,
    auth_mode: str,
    prompt: str,
    exec_result: dict,
    elapsed_seconds: float,
    error_text: str,
    trace_text: str,
    raw_prediction_text: str | None,
) -> dict[str, Path]:
    provenance_dir = _claude_provenance_dir(task_dir)
    base_name = build_provenance_basename(testcase_id, "claude_code", run_id)
    prompt_path = provenance_dir / f"{base_name}.prompt.md"
    stream_path = provenance_dir / f"{base_name}.stream.jsonl"
    trace_path = provenance_dir / f"{base_name}.trace.md"
    metadata_path = provenance_dir / f"{base_name}.meta.json"

    write_text_artifact(prompt_path, prompt)
    write_text_artifact(stream_path, exec_result.get("stdout", ""))
    write_text_artifact(trace_path, trace_text)
    if raw_prediction_text is not None:
        write_text_artifact(
            provenance_dir / f"{base_name}.raw_prediction.txt",
            raw_prediction_text,
        )

    write_json(
        metadata_path,
        {
            "competition_slug": competition_slug,
            "testcase_id": testcase_id,
            "agent_name": "claude_code",
            "run_id": run_id,
            "run_by": run_by,
            "artifact_type": "output_run_metadata",
            "status": "failed",
            "model_name": model_name,
            "api_provider": "anthropic_cli",
            "auth_mode": auth_mode,
            "api_call_count": None,
            "tool_call_count": exec_result.get("tool_call_count"),
            "cost_usd": exec_result.get("cost_usd"),
            "error_message": error_text,
            "usage_detail": exec_result.get("usage_detail"),
            "model_usage": exec_result.get("model_usage"),
            "permission_denials": exec_result.get("permission_denials"),
            "validation_warnings": [],
            "notes": "Claude Code failure metadata.",
            "time_spent_seconds": elapsed_seconds,
            "token_usage": exec_result.get(
                "usage",
                {"input_tokens": None, "output_tokens": None, "total_tokens": None},
            ),
        },
    )

    return {
        "metadata_path": metadata_path,
        "prompt_path": prompt_path,
        "stream_path": stream_path,
        "trace_path": trace_path,
    }


def run_claude_code(
    *,
    task_dir: str | Path,
    testcase_id: str,
    run_id: str,
    data_root: str | Path,
    api_key_path: str | Path = DEFAULT_API_KEY_PATH,
    auth_mode: str = DEFAULT_CLAUDE_CODE_AUTH_MODE,
    allow_api_key_override: bool = False,
    model_name: str = DEFAULT_MODEL_NAME,
    max_thinking_tokens: int | None = None,
    executor=default_executor,
) -> dict[str, Path]:
    normalized_auth_mode = auth_mode.strip().lower()
    if normalized_auth_mode not in {"subscription", "api_key"}:
        raise ValueError(f"Unsupported Claude Code auth_mode: {auth_mode}. Use 'subscription' or 'api_key'.")
    if normalized_auth_mode == "api_key" and (
        not allow_api_key_override or os.environ.get(API_KEY_OVERRIDE_ENV_VAR) != "1"
    ):
        raise PermissionError(
            "Claude Code baseline runs must use subscription auth by default. "
            "api_key mode is blocked unless both allow_api_key_override=True "
            f"and {API_KEY_OVERRIDE_ENV_VAR}=1 are set explicitly."
        )

    dataset_root = Path(data_root).expanduser().resolve()
    try:
        context = build_benchmark_context(
            task_dir=task_dir,
            testcase_id=testcase_id,
            data_root=dataset_root,
        )
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            "Actual dataset files are not available for this Claude Code run. "
            f"Expected them under `{dataset_root}`. Please provide the real dataset "
            "files and rerun. "
            f"Details: {exc}"
        ) from exc
    prompt = build_claude_code_prompt(
        task_text=context.bundle.task["goal"],
        context_summary=context.context_summary,
        candidate_actions=context.candidate_actions_json,
        output_format="Write benchmark JSON with predicted_add_action_ids and predicted_remove_action_ids.",
        prediction_filename="prediction.json",
        dataset_symlink_path="dataset",
    )
    api_key = load_api_key(api_key_path) if normalized_auth_mode == "api_key" else None
    workdir = prepare_claude_workspace(
        task_goal=context.bundle.task["goal"],
        testcase=context.bundle.testcase,
        visible_actions=context.visible_actions,
        prompt=prompt,
        dataset_root=dataset_root,
    )
    preserve_workspace = False
    exec_result: dict | None = None
    elapsed_seconds = 0.0
    prediction_text: str | None = None
    try:
        command = build_claude_command(
            model_name=model_name,
            workdir=workdir,
            dataset_root=dataset_root,
            prompt=prompt,
            max_thinking_tokens=max_thinking_tokens,
        )
        env = build_claude_environment(
            workdir=workdir,
            auth_mode=normalized_auth_mode,
            api_key=api_key,
        )
        start_time = time.monotonic()
        exec_result = normalize_exec_result(executor(workdir=workdir, command=command, env=env))
        elapsed_seconds = time.monotonic() - start_time

        prediction_path = workdir / "prediction.json"
        if exec_result.get("returncode", 1) != 0:
            preserve_workspace = True
            raise RuntimeError(
                f"Claude Code exited with code {exec_result.get('returncode')}. "
                f"Workspace preserved at {workdir}. "
                f"stdout={exec_result.get('stdout', '')!r} stderr={exec_result.get('stderr', '')!r}"
            )
        prediction_text = load_prediction_text(prediction_path=prediction_path, exec_result=exec_result)
        if prediction_text is None:
            preserve_workspace = True
            raise FileNotFoundError(
                "Claude Code did not create prediction file: "
                f"{prediction_path}. Workspace preserved at {workdir}. "
                f"stdout={exec_result.get('stdout', '')!r} stderr={exec_result.get('stderr', '')!r}"
            )
        parsed_prediction, validation_warnings = parse_and_validate_prediction_text(
            prediction_text,
            valid_action_ids=context.valid_action_ids,
            allowed_remove_action_ids=set(context.bundle.testcase["input"]["context_action_ids"]),
        )
        trace_text = build_trace_text(
            testcase_id=testcase_id,
            run_id=run_id,
            command=command,
            exec_result=exec_result,
            events=exec_result.get("stream_events", []),
            parsed_prediction=parsed_prediction,
            validation_warnings=validation_warnings,
            raw_prediction_text=prediction_text,
        )

        artifact_paths = write_output_bundle(
            task_dir=task_dir,
            competition_slug=context.bundle.task["competition_slug"],
            testcase_id=testcase_id,
            agent_name="claude_code",
            run_by="agent_runner",
            run_id=run_id,
            predicted_add_action_ids=parsed_prediction.get("predicted_add_action_ids", []),
            predicted_remove_action_ids=parsed_prediction.get("predicted_remove_action_ids", []),
            notes="Claude Code baseline run.",
            time_spent_seconds=elapsed_seconds,
            token_usage=exec_result.get("usage", {"input_tokens": None, "output_tokens": None, "total_tokens": None}),
            trace_text=trace_text,
            metadata={
                "artifact_type": "output_run_metadata",
                "status": "success",
                "model_name": model_name,
                "api_provider": "anthropic_cli",
                "auth_mode": normalized_auth_mode,
                "api_call_count": None,
                "tool_call_count": exec_result.get("tool_call_count"),
                "cost_usd": exec_result.get("cost_usd"),
                "error_message": None,
                "usage_detail": exec_result.get("usage_detail"),
                "model_usage": exec_result.get("model_usage"),
                "permission_denials": exec_result.get("permission_denials"),
                "validation_warnings": validation_warnings,
                "notes": "Claude Code wrapper metadata.",
            },
            extra_artifacts=[
                {
                    "kind": "prompt",
                    "filename": f"{testcase_id.split('_', 1)[0]}_claude_code_{run_id}.prompt.md",
                    "description": "Final prompt text sent to the Claude Code baseline.",
                    "content": prompt,
                },
                {
                    "kind": "stream",
                    "filename": f"{testcase_id.split('_', 1)[0]}_claude_code_{run_id}.stream.jsonl",
                    "description": "Raw Claude Code stream-json event log for this run.",
                    "content": exec_result.get("stdout", ""),
                },
            ],
        )
        shutil.rmtree(workdir)
        return artifact_paths
    except Exception as exc:
        preserve_workspace = True
        if exec_result is not None:
            try:
                failure_trace_text = build_trace_text(
                    testcase_id=testcase_id,
                    run_id=run_id,
                    command=command,
                    exec_result=exec_result,
                    events=exec_result.get("stream_events", []),
                    raw_prediction_text=prediction_text,
                    error_text=str(exc),
                )
                _persist_failure_debug_artifacts(
                    task_dir=task_dir,
                    competition_slug=context.bundle.task["competition_slug"],
                    testcase_id=testcase_id,
                    run_id=run_id,
                    run_by="agent_runner",
                    model_name=model_name,
                    auth_mode=normalized_auth_mode,
                    prompt=prompt,
                    exec_result=exec_result,
                    elapsed_seconds=elapsed_seconds,
                    error_text=str(exc),
                    trace_text=failure_trace_text,
                    raw_prediction_text=prediction_text,
                )
            except Exception:
                pass
        raise
    finally:
        if workdir.exists() and not preserve_workspace:
            shutil.rmtree(workdir)
