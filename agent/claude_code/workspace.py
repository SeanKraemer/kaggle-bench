from __future__ import annotations

import json
import tempfile
from pathlib import Path


def prepare_claude_workspace(
    *,
    task_goal: str,
    testcase: dict,
    visible_actions: list[dict],
    prompt: str,
    dataset_root: Path,
) -> Path:
    workdir = Path(tempfile.mkdtemp(prefix="claude_code_")).resolve()
    (workdir / ".claude-home").mkdir(parents=True, exist_ok=True)
    (workdir / "dataset").symlink_to(dataset_root, target_is_directory=True)
    (workdir / "TASK.md").write_text(task_goal, encoding="utf-8")
    (workdir / "testcase.json").write_text(json.dumps(testcase, indent=2), encoding="utf-8")
    (workdir / "candidate_actions_visible.json").write_text(json.dumps(visible_actions, indent=2), encoding="utf-8")
    (workdir / "output_schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["predicted_add_action_ids", "predicted_remove_action_ids"],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (workdir / "PROMPT.md").write_text(prompt, encoding="utf-8")
    return workdir
