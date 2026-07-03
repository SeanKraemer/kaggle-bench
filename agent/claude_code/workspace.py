from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path


def _expose_dataset(dataset_path: Path, dataset_root: Path) -> None:
    """Expose the dataset root inside the workspace.

    A symlink keeps the workspace cheap and pointed at the live dataset. On
    platforms where symlinks are unavailable (e.g. Windows without Developer
    Mode), fall back to copying the dataset tree into the workspace.
    """
    try:
        dataset_path.symlink_to(dataset_root, target_is_directory=True)
    except OSError:
        shutil.copytree(dataset_root, dataset_path)


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
    _expose_dataset(workdir / "dataset", dataset_root)
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
