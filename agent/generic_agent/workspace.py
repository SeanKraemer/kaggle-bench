from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GenericAgentWorkspace:
    workdir: Path
    dataset_path: Path
    prediction_path: Path
    scratchpad_path: Path


def prepare_generic_workspace(
    *,
    task_goal: str,
    testcase: dict,
    visible_actions: list[dict],
    prompt: str,
    dataset_root: Path,
) -> GenericAgentWorkspace:
    workdir = Path(tempfile.mkdtemp(prefix="generic_agent_"))
    dataset_path = workdir / "dataset"
    dataset_path.symlink_to(dataset_root, target_is_directory=True)
    (workdir / "TASK.md").write_text(task_goal, encoding="utf-8")
    (workdir / "testcase.json").write_text(json.dumps(testcase, indent=2), encoding="utf-8")
    (workdir / "candidate_actions_visible.json").write_text(
        json.dumps(visible_actions, indent=2),
        encoding="utf-8",
    )
    (workdir / "output_schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["predicted_add_action_ids", "predicted_remove_action_ids"],
                "properties": {
                    "predicted_add_action_ids": {"type": "array", "items": {"type": "string"}},
                    "predicted_remove_action_ids": {"type": "array", "items": {"type": "string"}},
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (workdir / "PROMPT.md").write_text(prompt, encoding="utf-8")
    scratchpad_path = workdir / "scratchpad.json"
    scratchpad_path.write_text(json.dumps({"entries": []}, indent=2), encoding="utf-8")
    return GenericAgentWorkspace(
        workdir=workdir,
        dataset_path=dataset_path,
        prediction_path=workdir / "prediction.json",
        scratchpad_path=scratchpad_path,
    )
