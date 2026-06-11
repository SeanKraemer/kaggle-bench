from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def testcase_prefix(testcase_id: str) -> str:
    return testcase_id.split("_", 1)[0]


def build_output_filename(testcase_id: str, agent_name: str, run_id: str) -> str:
    return f"{testcase_prefix(testcase_id)}_{agent_name}_{run_id}.json"


def build_provenance_basename(testcase_id: str, agent_name: str, run_id: str) -> str:
    return f"{testcase_prefix(testcase_id)}_{agent_name}_{run_id}"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    write_text_artifact(path, json.dumps(payload, indent=2))


def ensure_trailing_newline(text: str) -> str:
    return text if not text or text.endswith("\n") else text + "\n"


def strip_line_trailing_whitespace(text: str) -> str:
    if not text:
        return text
    return "\n".join(line.rstrip(" \t") for line in text.splitlines())


def write_text_artifact(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = strip_line_trailing_whitespace(content)
    path.write_text(ensure_trailing_newline(normalized), encoding="utf-8")


def write_output_bundle(
    *,
    task_dir: str | Path,
    competition_slug: str,
    testcase_id: str,
    agent_name: str,
    run_by: str,
    run_id: str,
    predicted_add_action_ids: list[str],
    predicted_remove_action_ids: list[str],
    notes: str,
    time_spent_seconds: int | float,
    token_usage: dict[str, int | None],
    trace_text: str,
    metadata: dict[str, Any],
    extra_artifacts: list[dict[str, Any]] | None = None,
) -> dict[str, Path]:
    root = Path(task_dir)
    outputs_dir = root / "outputs"
    provenance_dir = outputs_dir / "provenance"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    provenance_dir.mkdir(parents=True, exist_ok=True)

    base_name = build_provenance_basename(testcase_id, agent_name, run_id)
    output_filename = build_output_filename(testcase_id, agent_name, run_id)
    metadata_filename = f"{base_name}.meta.json"
    trace_filename = f"{base_name}.trace.md"

    output_path = outputs_dir / output_filename
    metadata_path = provenance_dir / metadata_filename
    trace_path = provenance_dir / trace_filename

    artifact_refs = [
        {
            "kind": "metadata",
            "path": f"provenance/{metadata_filename}",
            "description": "Run metadata for this benchmark output.",
        },
        {
            "kind": "trace",
            "path": f"provenance/{trace_filename}",
            "description": "Trace for this benchmark output.",
        },
    ]
    extra_paths: dict[str, Path] = {}
    for artifact in extra_artifacts or []:
        artifact_filename = artifact["filename"]
        artifact_path = provenance_dir / artifact_filename
        content = artifact["content"]
        write_text_artifact(artifact_path, content)
        artifact_refs.append(
            {
                "kind": artifact["kind"],
                "path": f"provenance/{artifact_filename}",
                "description": artifact["description"],
            }
        )
        extra_paths[f"{artifact['kind']}_path"] = artifact_path

    output_payload = {
        "competition_slug": competition_slug,
        "testcase_id": testcase_id,
        "agent_name": agent_name,
        "run_by": run_by,
        "run_id": run_id,
        "artifact_refs": artifact_refs,
        "predicted_add_action_ids": predicted_add_action_ids,
        "predicted_remove_action_ids": predicted_remove_action_ids,
        "time_spent_seconds": time_spent_seconds,
        "token_usage": token_usage,
        "notes": notes,
    }
    write_json(output_path, output_payload)
    write_text_artifact(trace_path, trace_text)

    metadata_payload = {
        "competition_slug": competition_slug,
        "testcase_id": testcase_id,
        "agent_name": agent_name,
        "run_id": run_id,
        "run_by": run_by,
        **metadata,
    }
    write_json(metadata_path, metadata_payload)

    result = {
        "output_path": output_path,
        "metadata_path": metadata_path,
        "trace_path": trace_path,
    }
    result.update(extra_paths)
    return result


def write_failed_provenance_bundle(
    *,
    task_dir: str | Path,
    competition_slug: str,
    testcase_id: str,
    agent_name: str,
    run_by: str,
    run_id: str,
    trace_text: str,
    metadata: dict[str, Any],
    extra_artifacts: list[dict[str, Any]] | None = None,
) -> dict[str, Path]:
    root = Path(task_dir)
    provenance_dir = root / "outputs" / "provenance"
    provenance_dir.mkdir(parents=True, exist_ok=True)

    base_name = f"{build_provenance_basename(testcase_id, agent_name, run_id)}.failed"
    metadata_filename = f"{base_name}.meta.json"
    trace_filename = f"{base_name}.trace.md"
    metadata_path = provenance_dir / metadata_filename
    trace_path = provenance_dir / trace_filename

    artifact_refs = [
        {
            "kind": "metadata",
            "path": f"provenance/{metadata_filename}",
            "description": "Failed run metadata for this benchmark output.",
        },
        {
            "kind": "trace",
            "path": f"provenance/{trace_filename}",
            "description": "Trace for this failed benchmark output.",
        },
    ]
    extra_paths: dict[str, Path] = {}
    for artifact in extra_artifacts or []:
        artifact_filename = artifact["filename"]
        artifact_path = provenance_dir / artifact_filename
        content = artifact["content"]
        write_text_artifact(artifact_path, content)
        artifact_refs.append(
            {
                "kind": artifact["kind"],
                "path": f"provenance/{artifact_filename}",
                "description": artifact["description"],
            }
        )
        extra_paths[f"{artifact['kind']}_path"] = artifact_path

    write_text_artifact(trace_path, trace_text)
    write_json(
        metadata_path,
        {
            "competition_slug": competition_slug,
            "testcase_id": testcase_id,
            "agent_name": agent_name,
            "run_id": run_id,
            "run_by": run_by,
            "artifact_refs": artifact_refs,
            **metadata,
        },
    )

    result = {
        "metadata_path": metadata_path,
        "trace_path": trace_path,
    }
    result.update(extra_paths)
    return result
