from __future__ import annotations

import json
from pathlib import Path


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_proposed_tool_task(
    root: Path,
    *,
    context_action_ids: list[str] | None = None,
) -> tuple[Path, Path]:
    task_dir = root / "data" / "tasks" / "tool-test"
    data_root = root / "raw"
    write_json(
        task_dir / "task.json",
        {
            "competition_slug": "tool-test",
            "dataset": {
                "train_files": ["train.csv"],
                "lookup_files": ["lookup.csv"],
                "target_column": "target",
                "primary_key": "id",
            },
            "goal": "Suggest preprocessing actions.",
        },
    )
    write_json(
        task_dir / "candidate_actions.json",
        {
            "actions": [
                {
                    "action_id": "CA-1",
                    "action_type": "JOIN_LOOKUP",
                    "canonical_params": {
                        "left_on": "id",
                        "right_on": "id",
                        "right_table_id": "lookup",
                        "how": "left",
                    },
                    "role": "hidden-good",
                },
                {
                    "action_id": "CA-2",
                    "action_type": "IMPUTE_MISSING",
                    "canonical_params": {"columns": ["feature_num"], "strategy": "median"},
                    "reasoning": "hidden",
                },
                {
                    "action_id": "CA-3",
                    "action_type": "DROP_COLUMNS",
                    "canonical_params": {"columns": ["target"]},
                    "role": "hidden-bad",
                },
                {
                    "action_id": "CA-4",
                    "action_type": "ENCODE_CATEGORICAL",
                    "canonical_params": {"columns": ["cat"], "method": "one_hot"},
                },
            ]
        },
    )
    write_json(
        task_dir / "testcases" / "tc1_from_scratch.json",
        {
            "testcase_id": "tc1_from_scratch",
            "competition_slug": "tool-test",
            "input": {
                "scenario": "from_scratch",
                "context_action_ids": context_action_ids or ["CA-3"],
            },
        },
    )
    write_text(
        data_root / "train.csv",
        "id,target,feature_num,cat,date\n1,0,10,a,2020-01-01\n2,1,,b,2020-01-02\n",
    )
    write_text(data_root / "lookup.csv", "id,lookup_value\n1,100\n2,200\n")
    return task_dir, data_root
