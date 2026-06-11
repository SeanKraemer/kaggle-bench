from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


class TaskBundle:
    def __init__(
        self,
        *,
        task_dir: Path,
        task: dict[str, Any],
        testcase: dict[str, Any],
        actions: list[dict[str, Any]],
        action_by_id: dict[str, dict[str, Any]],
    ) -> None:
        self.task_dir = task_dir
        self.task = task
        self.testcase = testcase
        self.actions = actions
        self.action_by_id = action_by_id


def load_task_bundle(task_dir: str | Path, testcase_id: str) -> TaskBundle:
    root = Path(task_dir)
    task = load_json(root / "task.json")
    testcase = load_json(root / "testcases" / f"{testcase_id}.json")
    candidate_bundle = load_json(root / "candidate_actions.json")
    actions = candidate_bundle["actions"]
    return TaskBundle(
        task_dir=root,
        task=task,
        testcase=testcase,
        actions=actions,
        action_by_id={action["action_id"]: action for action in actions},
    )
