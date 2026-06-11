#!/usr/bin/env python3
"""Render slide-ready visuals from benchmark aggregate results.

This script intentionally uses only the Python standard library so it can run in
the course repo without adding plotting dependencies. It reuses the evaluator
and aggregate code as the source of truth, then writes SVG, CSV, HTML, and
Markdown assets for the final presentation.
"""

from __future__ import annotations

import argparse
import csv
import html
import importlib.util
import json
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
AGGREGATE_PATH = REPO_ROOT / "eval" / "aggregate.py"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "eval" / "results" / "presentation" / "current"

DEFAULT_SUCCESS_OUTPUT = (
    REPO_ROOT
    / "data"
    / "tasks"
    / "recruit-restaurant-visitor-forecasting"
    / "outputs"
    / "tc1_proposed_agent_try1.json"
)
DEFAULT_STRUGGLE_OUTPUT = (
    REPO_ROOT
    / "data"
    / "tasks"
    / "lish-moa"
    / "outputs"
    / "tc4_proposed_agent_try1.json"
)

TESTCASE_ORDER = [
    "tc1_from_scratch",
    "tc2_partial_good",
    "tc3_fault_injected",
    "tc4_mixed_history",
]
TESTCASE_LABELS = {
    "tc1_from_scratch": "TC1\nScratch",
    "tc2_partial_good": "TC2\nGood prior",
    "tc3_fault_injected": "TC3\nBad prior",
    "tc4_mixed_history": "TC4\nMixed",
}
OVERALL_SUCCESS_COLUMN = "overall_success_rate"
OVERALL_SUCCESS_LABEL = "Overall\nSuccess"

AGENT_ORDER = [
    "rule_based",
    "single_llm",
    "generic_agent",
    "claude_code",
    "proposed_agent",
]
AGENT_LABELS = {
    "human": "Human reference",
    "rule_based": "Rule-based",
    "single_llm": "Single LLM",
    "generic_agent": "Generic agent",
    "claude_code": "Claude Code",
    "proposed_agent": "Proposed agent",
}
AGENT_COLORS = {
    "rule_based": "#8f99a8",
    "single_llm": "#2563eb",
    "generic_agent": "#0f766e",
    "claude_code": "#7c3aed",
    "proposed_agent": "#e11d48",
    "human": "#111827",
}


def load_module(path: Path, module_name: str) -> Any:
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def build_report(
    aggregate: Any,
    task_filters: list[str],
    stage_scope: str,
    success_threshold: float,
) -> dict[str, Any]:
    task_dirs = aggregate.discover_task_dirs(task_filters)
    task_profiles = {task_dir.name: aggregate.load_task_profile(task_dir) for task_dir in task_dirs}

    single_runs: list[dict[str, Any]] = []
    grouped_rows: list[dict[str, Any]] = []

    for task_dir in task_dirs:
        groups = aggregate.discover_output_groups(task_dir)
        for (testcase_id, _agent_name), input_paths in sorted(groups.items()):
            testcase_path = task_dir / "testcases" / f"{testcase_id}.json"
            if not testcase_path.exists():
                raise SystemExit(f"missing testcase file for {task_dir.name}/{testcase_id}")

            group_result = aggregate.evaluate_group(
                testcase_path=testcase_path,
                input_paths=input_paths,
                stage_scope=stage_scope,
                success_threshold=success_threshold,
            )

            if "runs" in group_result:
                for run in group_result["runs"]:
                    single_runs.append(aggregate.summarize_run(run, task_dir.name))
            else:
                single_runs.append(aggregate.summarize_run(group_result, task_dir.name))

            grouped_rows.append(aggregate.summarize_group_result(group_result, task_dir.name))

    return {
        "tasks": [task_dir.name for task_dir in task_dirs],
        "stage_scope": stage_scope,
        "success_threshold": aggregate.TASK_EVAL.round_metric(success_threshold),
        "single_run_count": len(single_runs),
        "group_count": len(grouped_rows),
        "single_runs": sorted(
            single_runs,
            key=lambda row: (row["task_slug"], row["testcase_id"], row["agent_name"], row["run_id"]),
        ),
        "groups": sorted(grouped_rows, key=lambda row: (row["task_slug"], row["testcase_id"], row["agent_name"])),
        "overall_summary": aggregate.build_overall_summary(grouped_rows),
        "task_summary": aggregate.build_task_summary(task_profiles, grouped_rows),
        "agent_summary": aggregate.build_agent_summary(grouped_rows),
    }


def mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def round_or_none(value: float | None, places: int = 6) -> float | None:
    if value is None:
        return None
    return round(value, places)


def build_agent_testcase_summary(
    report: dict[str, Any],
    include_human: bool,
) -> dict[str, dict[str, dict[str, float | int | None]]]:
    buckets: dict[str, dict[str, dict[str, list[float]]]] = defaultdict(
        lambda: defaultdict(
            lambda: {
                "task_completion_score": [],
                "add_f1": [],
                "remove_recall": [],
                "total_tokens": [],
            }
        )
    )
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    allowed_agents = set(AGENT_ORDER)
    if include_human:
        allowed_agents.add("human")

    for row in report["groups"]:
        agent = row["agent_name"]
        testcase = row["testcase_id"]
        if agent not in allowed_agents or testcase not in TESTCASE_ORDER:
            continue
        counts[agent][testcase] += 1
        for key in ("task_completion_score", "add_f1", "remove_recall"):
            buckets[agent][testcase][key].append(float(row[key]))
        if row["total_tokens"] is not None:
            buckets[agent][testcase]["total_tokens"].append(float(row["total_tokens"]))

    summary: dict[str, dict[str, dict[str, float | int | None]]] = {}
    agents = (["human"] if include_human else []) + AGENT_ORDER
    for agent in agents:
        summary[agent] = {}
        for testcase in TESTCASE_ORDER:
            values = buckets[agent][testcase]
            summary[agent][testcase] = {
                "group_count": counts[agent][testcase],
                "task_completion_score": round_or_none(mean(values["task_completion_score"])),
                "add_f1": round_or_none(mean(values["add_f1"])),
                "remove_recall": round_or_none(mean(values["remove_recall"])),
                "total_tokens": round_or_none(mean(values["total_tokens"])),
            }
    return summary


def build_agent_summary_by_name(report: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["agent_name"]: row for row in report["agent_summary"]}


def write_csv_outputs(
    output_dir: Path,
    report: dict[str, Any],
    testcase_summary: dict[str, dict[str, dict[str, float | int | None]]],
) -> None:
    agent_summary_path = output_dir / "agent_summary.csv"
    with agent_summary_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "agent_name",
                "group_count",
                "task_success_rate",
                "mean_add_f1",
                "mean_remove_recall",
                "mean_task_completion_score",
                "mean_total_tokens",
                "mean_tool_call_count",
                "mean_cost_usd",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        for row in report["agent_summary"]:
            writer.writerow({key: row.get(key) for key in writer.fieldnames})

    scores_path = output_dir / "agent_testcase_scores.csv"
    with scores_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "agent_name",
                "testcase_id",
                "testcase_label",
                "group_count",
                "task_completion_score",
                "add_f1",
                "remove_recall",
                "total_tokens",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        for agent, testcase_rows in testcase_summary.items():
            for testcase in TESTCASE_ORDER:
                row = testcase_rows[testcase]
                writer.writerow(
                    {
                        "agent_name": agent,
                        "testcase_id": testcase,
                        "testcase_label": TESTCASE_LABELS[testcase].replace("\n", " "),
                        **row,
                    }
                )


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def rgb_from_hex(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)


def hex_from_rgb(rgb: tuple[int, int, int]) -> str:
    return "#" + "".join(f"{component:02x}" for component in rgb)


def interpolate_color(a: str, b: str, ratio: float) -> str:
    ratio = max(0.0, min(1.0, ratio))
    ar, ag, ab = rgb_from_hex(a)
    br, bg, bb = rgb_from_hex(b)
    return hex_from_rgb(
        (
            round(ar + (br - ar) * ratio),
            round(ag + (bg - ag) * ratio),
            round(ab + (bb - ab) * ratio),
        )
    )


def score_color(score: float | None) -> str:
    if score is None:
        return "#f3f4f6"
    if score < 0.5:
        return interpolate_color("#f7c6c7", "#f4f1d0", score / 0.5)
    return interpolate_color("#f4f1d0", "#0f766e", (score - 0.5) / 0.5)


def best_nonhuman_scores_by_column(
    testcase_summary: dict[str, dict[str, dict[str, float | int | None]]],
    agent_summaries: dict[str, dict[str, Any]],
) -> dict[str, float]:
    best_scores: dict[str, float] = {}
    for column in [*TESTCASE_ORDER, OVERALL_SUCCESS_COLUMN]:
        scores: list[float] = []
        for agent in AGENT_ORDER:
            if column == OVERALL_SUCCESS_COLUMN:
                value = agent_summaries.get(agent, {}).get("task_success_rate")
            else:
                value = testcase_summary[agent][column]["task_completion_score"]
            if value is not None:
                scores.append(float(value))
        if scores:
            best_scores[column] = max(scores)
    return best_scores


def tspan_block(
    lines: list[str],
    x: int,
    y: int,
    *,
    width_chars: int = 44,
    line_height: int = 18,
    class_name: str = "body",
) -> str:
    tspans: list[str] = []
    current_y = y
    for line in lines:
        wrapped = textwrap.wrap(line, width=width_chars) or [""]
        for piece in wrapped:
            tspans.append(f'<tspan x="{x}" y="{current_y}">{esc(piece)}</tspan>')
            current_y += line_height
    return f'<text class="{class_name}">' + "".join(tspans) + "</text>"


def render_heatmap_svg(
    output_path: Path,
    report: dict[str, Any],
    testcase_summary: dict[str, dict[str, dict[str, float | int | None]]],
    include_human: bool,
) -> None:
    task_count_label = (
        f"{len(report['tasks'])} benchmark tasks"
        if len(report["tasks"]) == 20
        else f"{len(report['tasks'])} tasks with currently available artifacts"
    )
    agents = (["human"] if include_human else []) + AGENT_ORDER
    agent_summaries = build_agent_summary_by_name(report)
    best_scores = best_nonhuman_scores_by_column(testcase_summary, agent_summaries)
    columns = [*TESTCASE_ORDER, OVERALL_SUCCESS_COLUMN]
    cell_w = 156
    cell_h = 82
    left = 230
    top = 142
    width = left + len(columns) * cell_w + 82
    height = top + len(agents) * cell_h + 118

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>",
        ".title{font:700 30px Arial,sans-serif;fill:#111827}",
        ".subtitle{font:400 15px Arial,sans-serif;fill:#4b5563}",
        ".label{font:700 15px Arial,sans-serif;fill:#111827}",
        ".small{font:400 12px Arial,sans-serif;fill:#4b5563}",
        ".score{font:700 24px Arial,sans-serif}",
        ".best{font-weight:900}",
        ".n{font:400 12px Arial,sans-serif}",
        "</style>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text class="title" x="36" y="48">Task Completion by Scenario</text>',
        (
            f'<text class="subtitle" x="36" y="76">Stage scope: {esc(report["stage_scope"])}; '
            f'{esc(task_count_label)}; '
            "scenario cells are task completion, right column is binary success rate.</text>"
        ),
    ]

    for col, column in enumerate(columns):
        x = left + col * cell_w + cell_w / 2
        label = OVERALL_SUCCESS_LABEL if column == OVERALL_SUCCESS_COLUMN else TESTCASE_LABELS[column]
        for idx, line in enumerate(label.splitlines()):
            parts.append(f'<text class="label" text-anchor="middle" x="{x}" y="{108 + idx * 18}">{esc(line)}</text>')

    for row, agent in enumerate(agents):
        y = top + row * cell_h
        label = AGENT_LABELS.get(agent, agent)
        parts.append(f'<text class="label" x="36" y="{y + 46}">{esc(label)}</text>')
        for col, column in enumerate(columns):
            x = left + col * cell_w
            if column == OVERALL_SUCCESS_COLUMN:
                agent_summary = agent_summaries.get(agent, {})
                score = agent_summary.get("task_success_rate")
                group_count = agent_summary.get("group_count", 0)
            else:
                cell = testcase_summary[agent][column]
                score = cell["task_completion_score"]
                group_count = cell["group_count"]
            fill = score_color(None if score is None else float(score))
            text_fill = "#111827"
            score_class = "score"
            is_best_cell = (
                agent != "human"
                and score is not None
                and column in best_scores
                and abs(float(score) - best_scores[column]) < 0.0000005
            )
            if is_best_cell:
                score_class = "score best"
            stroke = "#111827" if is_best_cell else "#ffffff"
            stroke_width = 4 if is_best_cell else 2
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cell_w - 8}" height="{cell_h - 8}" rx="8" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
            )
            if score is None:
                parts.append(
                    f'<text class="score" fill="{text_fill}" text-anchor="middle" '
                    f'x="{x + (cell_w - 8) / 2}" y="{y + 42}">n/a</text>'
                )
            else:
                parts.append(
                    f'<text class="{score_class}" fill="{text_fill}" text-anchor="middle" '
                    f'x="{x + (cell_w - 8) / 2}" y="{y + 37}">{float(score):.2f}</text>'
                )
                parts.append(
                    f'<text class="n" fill="{text_fill}" text-anchor="middle" '
                    f'x="{x + (cell_w - 8) / 2}" y="{y + 58}">n={int(group_count)}</text>'
                )
        if agent == "human" and row == 0 and len(agents) > 1:
            separator_y = y + cell_h - 4
            parts.append(
                f'<line x1="36" y1="{separator_y}" x2="{width - 36}" y2="{separator_y}" '
                'stroke="#111827" stroke-width="2" stroke-dasharray="6 5"/>'
            )

    legend_y = height - 56
    parts.extend(
        [
            f'<text class="small" x="36" y="{legend_y}">Lower</text>',
            f'<rect x="82" y="{legend_y - 12}" width="65" height="14" fill="{score_color(0.2)}"/>',
            f'<rect x="147" y="{legend_y - 12}" width="65" height="14" fill="{score_color(0.5)}"/>',
            f'<rect x="212" y="{legend_y - 12}" width="65" height="14" fill="{score_color(0.8)}"/>',
            f'<text class="small" x="288" y="{legend_y}">Higher task completion</text>',
            f'<text class="small" x="36" y="{legend_y + 24}">Human reference uses available human artifacts; Overall Success is pass rate across all testcase groups.</text>',
            "</svg>",
        ]
    )
    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def render_grouped_bar_svg(
    output_path: Path,
    report: dict[str, Any],
    testcase_summary: dict[str, dict[str, dict[str, float | int | None]]],
    include_human: bool,
) -> None:
    agents = (["human"] if include_human else []) + AGENT_ORDER
    groups = [*TESTCASE_ORDER, OVERALL_SUCCESS_COLUMN]
    agent_summaries = build_agent_summary_by_name(report)
    width = 1320
    height = 680
    plot_left = 90
    plot_top = 118
    plot_width = 1120
    plot_height = 420
    baseline = plot_top + plot_height
    group_w = plot_width / len(groups)
    bar_w = 22
    gap = 5

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>",
        ".title{font:700 30px Arial,sans-serif;fill:#111827}",
        ".subtitle{font:400 15px Arial,sans-serif;fill:#4b5563}",
        ".axis{font:400 12px Arial,sans-serif;fill:#4b5563}",
        ".label{font:700 14px Arial,sans-serif;fill:#111827}",
        ".legend{font:400 13px Arial,sans-serif;fill:#111827}",
        "</style>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text class="title" x="36" y="48">Task Completion by Scenario</text>',
        (
            f'<text class="subtitle" x="36" y="76">Grouped bar view of the same {esc(report["stage_scope"])} '
            "scores, with an overall binary success-rate group on the right.</text>"
        ),
    ]

    for tick in range(0, 6):
        value = tick / 5
        y = baseline - value * plot_height
        parts.append(f'<line x1="{plot_left}" y1="{y:.1f}" x2="{plot_left + plot_width}" y2="{y:.1f}" stroke="#e5e7eb"/>')
        parts.append(f'<text class="axis" text-anchor="end" x="{plot_left - 10}" y="{y + 4:.1f}">{value:.1f}</text>')
    parts.append(f'<line x1="{plot_left}" y1="{baseline}" x2="{plot_left + plot_width}" y2="{baseline}" stroke="#111827"/>')
    parts.append(f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{baseline}" stroke="#111827"/>')

    for group_idx, group in enumerate(groups):
        group_x = plot_left + group_idx * group_w
        bars_total_w = len(agents) * bar_w + (len(agents) - 1) * gap
        start_x = group_x + (group_w - bars_total_w) / 2
        for agent_idx, agent in enumerate(agents):
            if group == OVERALL_SUCCESS_COLUMN:
                score = agent_summaries.get(agent, {}).get("task_success_rate")
            else:
                score = testcase_summary[agent][group]["task_completion_score"]
            if score is None:
                continue
            bar_h = float(score) * plot_height
            x = start_x + agent_idx * (bar_w + gap)
            y = baseline - bar_h
            color = AGENT_COLORS[agent]
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w}" height="{bar_h:.1f}" fill="{color}" rx="4"/>')
        label_x = group_x + group_w / 2
        label = OVERALL_SUCCESS_LABEL if group == OVERALL_SUCCESS_COLUMN else TESTCASE_LABELS[group]
        for idx, line in enumerate(label.splitlines()):
            parts.append(f'<text class="label" text-anchor="middle" x="{label_x:.1f}" y="{baseline + 32 + idx * 17}">{esc(line)}</text>')

    legend_x = 120
    legend_y = height - 74
    for idx, agent in enumerate(agents):
        x = legend_x + idx * 190
        parts.append(f'<rect x="{x}" y="{legend_y}" width="16" height="16" fill="{AGENT_COLORS[agent]}" rx="3"/>')
        parts.append(f'<text class="legend" x="{x + 24}" y="{legend_y + 13}">{esc(AGENT_LABELS[agent])}</text>')

    parts.append("</svg>")
    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def action_map_for_task(task_dir: Path) -> dict[str, dict[str, Any]]:
    bank = load_json(task_dir / "candidate_actions.json")
    return {action["action_id"]: action for action in bank["actions"]}


def short_action(action_id: str, actions: dict[str, dict[str, Any]]) -> str:
    action = actions.get(action_id)
    if action is None:
        return action_id
    action_type = action.get("action_type", action_id)
    params = action.get("canonical_params", {})
    if action_type == "JOIN_LOOKUP":
        detail = params.get("right_table_id") or params.get("right_table")
    elif action_type == "PARSE_DATETIME":
        detail = ", ".join(params.get("columns", []))
    elif action_type == "TIME_SINCE_REFERENCE":
        detail = f"{', '.join(params.get('columns', []))} vs {params.get('reference')}"
    elif action_type in {"DROP_COLUMNS", "ENCODE_CATEGORICAL"}:
        detail = ", ".join(params.get("columns", []))
    elif action_type == "FILTER_ROWS":
        detail = params.get("predicate")
    elif action_type == "PCA_REDUCTION":
        cols = ", ".join(params.get("feature_columns", []))
        detail = f"{cols}, n={params.get('n_components')}"
    elif action_type == "APPLY_EXPRESSION":
        detail = params.get("expression")
    else:
        detail = ", ".join(params.get("columns", [])) if isinstance(params.get("columns"), list) else None

    if detail:
        detail = textwrap.shorten(str(detail), width=64, placeholder="...")
        return f"{action_id}: {action_type} ({detail})"
    return f"{action_id}: {action_type}"


def ordered_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique


def tool_evidence(output_path: Path) -> list[str]:
    output = load_json(output_path)
    tool_ref = None
    for ref in output.get("artifact_refs", []):
        if ref.get("kind") == "tool_calls":
            tool_ref = output_path.parent / ref["path"]
            break

    if tool_ref is None or not tool_ref.exists():
        return ["Tool-call provenance not available for this run."]

    tool_names: list[str] = []
    table_count = None
    lookup_types: list[str] = []
    context_count = None
    column_hint = None
    for line in tool_ref.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        name = record.get("name", "unknown_tool")
        tool_names.append(name)
        output_obj = record.get("output") or {}
        if name == "inspect_dataset_tables" and isinstance(output_obj.get("tables"), list):
            table_count = len(output_obj["tables"])
        if name == "lookup_actions":
            action_type = (record.get("input") or {}).get("action_type")
            if action_type:
                lookup_types.append(action_type)
        if name == "summarize_context_actions":
            context_count = len(output_obj.get("context_action_ids", []))
        if name == "inspect_columns":
            requested = (record.get("input") or {}).get("columns")
            if requested:
                column_hint = ", ".join(requested)

    evidence = [f"Used tools: {', '.join(ordered_unique(tool_names)[:5])}."]
    if table_count is not None:
        evidence.append(f"Inspected {table_count} dataset tables before selecting actions.")
    if lookup_types:
        evidence.append(f"Looked up candidate action families: {', '.join(ordered_unique(lookup_types)[:4])}.")
    if context_count is not None and context_count > 0:
        evidence.append(f"Reviewed {context_count} existing context actions.")
    if column_hint:
        evidence.append(f"Profiled columns: {column_hint}.")
    return evidence[:3]


def output_task_dir(output_path: Path) -> Path:
    resolved = output_path.resolve()
    for parent in resolved.parents:
        if parent.parent.name == "tasks" and (parent / "task.json").exists():
            return parent
    raise ValueError(f"could not infer task directory from {output_path}")


def evaluate_single_output(aggregate: Any, output_path: Path, stage_scope: str, success_threshold: float) -> dict[str, Any]:
    output = load_json(output_path)
    task_dir = output_task_dir(output_path)
    testcase_path = task_dir / "testcases" / f"{output['testcase_id']}.json"
    return aggregate.TASK_EVAL.evaluate(
        testcase_path=testcase_path,
        input_path=output_path,
        stage_scope=stage_scope,
        success_threshold=success_threshold,
    )


def build_trace_card(
    aggregate: Any,
    output_path: Path,
    stage_scope: str,
    success_threshold: float,
    title: str,
    lesson: str,
) -> dict[str, Any]:
    result = evaluate_single_output(aggregate, output_path, stage_scope, success_threshold)
    output = load_json(output_path)
    task_dir = output_task_dir(output_path)
    actions = action_map_for_task(task_dir)
    context_count = len(result["context_action_ids"])
    scenario = result["testcase_id"].replace("_", " ")

    matched_add = [
        short_action(item["predicted_action_id"], actions)
        for item in result["add"]["matched_units"][:4]
    ]
    missed_remove = [
        short_action(action_id, actions)
        for action_id in result["remove"]["missed_action_ids"][:4]
    ]
    matched_remove = [
        short_action(action_id, actions)
        for action_id in result["remove"]["matched_action_ids"][:3]
    ]

    if matched_add:
        decision_lines = ["Correct selected actions:", *[f"- {item}" for item in matched_add]]
    else:
        decision_lines = ["Correct selected actions:", "- None matched in this run."]

    if missed_remove:
        outcome_lines = ["Missed removals:", *[f"- {item}" for item in missed_remove]]
    elif matched_remove:
        outcome_lines = ["Removed harmful actions:", *[f"- {item}" for item in matched_remove]]
    else:
        outcome_lines = ["Rollback outcome:", "- No harmful context actions were expected."]

    return {
        "title": title,
        "task": task_dir.name,
        "scenario": scenario,
        "context_count": context_count,
        "score": result["summary"]["task_completion_score"],
        "add_f1": result["add"]["add_f1"],
        "remove_recall": result["remove"]["remove_recall"],
        "evidence": tool_evidence(output_path),
        "decision_lines": decision_lines[:5],
        "outcome_lines": outcome_lines[:5],
        "lesson": lesson,
    }


def render_trace_cards_svg(output_path: Path, success_card: dict[str, Any], struggle_card: dict[str, Any]) -> None:
    width = 1280
    height = 720
    card_w = 560
    card_h = 570
    top = 104
    lefts = [62, 658]
    cards = [
        (success_card, "#0f766e", lefts[0]),
        (struggle_card, "#b45309", lefts[1]),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>",
        ".title{font:700 31px Arial,sans-serif;fill:#111827}",
        ".subtitle{font:400 16px Arial,sans-serif;fill:#4b5563}",
        ".cardTitle{font:700 23px Arial,sans-serif;fill:#ffffff}",
        ".metric{font:700 18px Arial,sans-serif;fill:#111827}",
        ".section{font:700 14px Arial,sans-serif;fill:#111827}",
        ".body{font:400 13px Arial,sans-serif;fill:#374151}",
        ".small{font:400 12px Arial,sans-serif;fill:#6b7280}",
        "</style>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text class="title" x="44" y="48">Trace Examples: What the Scores Mean</text>',
        '<text class="subtitle" x="44" y="76">Use this as a qualitative companion to the numeric results slide.</text>',
    ]

    for card, accent, left in cards:
        parts.append(f'<rect x="{left}" y="{top}" width="{card_w}" height="{card_h}" rx="12" fill="#ffffff" stroke="#d1d5db"/>')
        parts.append(f'<rect x="{left}" y="{top}" width="{card_w}" height="58" rx="12" fill="{accent}"/>')
        parts.append(f'<text class="cardTitle" x="{left + 24}" y="{top + 38}">{esc(card["title"])}</text>')
        y = top + 88
        parts.append(f'<text class="metric" x="{left + 24}" y="{y}">{esc(card["task"])}</text>')
        y += 26
        parts.append(
            f'<text class="small" x="{left + 24}" y="{y}">{esc(card["scenario"])}; '
            f'context actions: {card["context_count"]}</text>'
        )
        y += 36
        parts.append(
            f'<text class="metric" x="{left + 24}" y="{y}">Completion {card["score"]:.2f} | '
            f'Add F1 {card["add_f1"]:.2f} | Remove recall {card["remove_recall"]:.2f}</text>'
        )
        y += 34
        parts.append(f'<text class="section" x="{left + 24}" y="{y}">Input -&gt; tool evidence</text>')
        y += 22
        parts.append(tspan_block(card["evidence"], left + 24, y, width_chars=70, line_height=17))
        y += 96
        parts.append(f'<text class="section" x="{left + 24}" y="{y}">Decision</text>')
        y += 22
        parts.append(tspan_block(card["decision_lines"], left + 24, y, width_chars=70, line_height=17))
        y += 110
        parts.append(f'<text class="section" x="{left + 24}" y="{y}">Outcome</text>')
        y += 22
        parts.append(tspan_block(card["outcome_lines"], left + 24, y, width_chars=70, line_height=17))
        y += 54
        parts.append(f'<text class="section" x="{left + 24}" y="{y}">Lesson learned</text>')
        y += 22
        parts.append(tspan_block([card["lesson"]], left + 24, y, width_chars=70, line_height=17))

    parts.append("</svg>")
    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def write_slide_notes(output_path: Path, report: dict[str, Any], has_trace_cards: bool = True) -> None:
    task_count = len(report["tasks"])
    coverage_note = (
        f"- Current artifacts include all `{task_count}` benchmark tasks with complete raw evaluation coverage."
        if task_count == 20
        else f"- Current artifacts include `{task_count}` tasks with result coverage for this filtered run; run without `--task` for the full benchmark."
    )
    trace_example_notes = (
        [
            "- Use `trace_cards.svg` as one visual with two side-by-side cards.",
            "- The left card should support the claim that tools help with evidence gathering.",
            "- The right card should support the claim that rollback/fault diagnosis is still weak.",
            "- Avoid raw JSON on the slide; use action labels and one-line lessons.",
        ]
        if has_trace_cards
        else [
            "- Trace-card example inputs were unavailable for this run; regenerate with valid `--success-output` and `--struggle-output` paths before using Slide 10.",
        ]
    )

    lines = [
        "# Final Presentation Results Visuals",
        "",
        "## Recommended Slide Names",
        "",
        "- Slide 9: `Results: Agent Performance by Scenario`",
        "- Slide 10: `Trace Examples: Where Agents Help and Fail`",
        "- Slide 11: `Conclusion: What the Benchmark Reveals`",
        "",
        "## Slide 9: Results - Number Report",
        "",
        "- Use `task_completion_heatmap.svg` as the primary visual.",
        "- Keep the headline to one sentence: agents do better at adding good actions than fixing harmful context.",
        "- Use the human reference as a left-side anchor and the Overall Success column as the cross-scenario headline.",
        "- Black outlines mark the best non-human method in each column.",
        "- Use `task_completion_grouped_bar.svg` only if the heatmap is hard to read in Google Slides.",
        coverage_note,
        "- Put `primary` scope in the footnote; note that Overall Success is binary pass rate, not another task-completion mean.",
        "",
        "## Slide 10: Results - Example Traces",
        "",
        *trace_example_notes,
        "",
        "## Slide 11: Conclusion",
        "",
        "- Main contribution: deterministic action-bank benchmark from expert Kaggle workflows.",
        "- Main result: LLM-based systems are decent recommenders, weaker debuggers.",
        "- Agent lesson: task-aware tools help, but orchestration needs stronger verification.",
        "- Limitation: exact matching and public Kaggle-derived golden actions can undercount valid alternatives.",
        "- Future work: semantic equivalence, private tasks, explicit rollback checks, downstream model validation.",
        "",
        "## Image Generation Guidance",
        "",
        "- Do not use image generation for Slides 9 or 10; these should look data-driven and auditable.",
        "- If you use image generation anywhere, reserve it for an intro/motivation visual, not the results section.",
        "- For Sean's slides, deterministic SVG charts and trace cards are clearer and safer.",
        "",
        "## Regeneration Command",
        "",
        "```bash",
        "uv run python eval/scripts/render_presentation_visuals.py",
        "```",
        "",
        "These outputs were generated from the current benchmark artifacts.",
        "",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def clear_stale_trace_cards(output_path: Path) -> None:
    if output_path.exists():
        output_path.unlink()
        print(f"warning: trace-card example outputs not found; removed stale {output_path.name}")
    else:
        print(f"warning: trace-card example outputs not found; skipped {output_path.name}")


def write_html_dashboard(output_path: Path, output_dir: Path) -> None:
    figures = [
        ("Task Completion Heatmap", output_dir / "task_completion_heatmap.svg"),
        ("Task Completion Grouped Bar", output_dir / "task_completion_grouped_bar.svg"),
        ("Trace Cards", output_dir / "trace_cards.svg"),
    ]
    sections = []
    for title, path in figures:
        if path.exists():
            sections.append(f"<h2>{esc(title)}</h2>\n{path.read_text(encoding='utf-8')}")

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>KaggleBench Results Visuals</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 32px; color: #111827; }}
    h1 {{ margin-bottom: 4px; }}
    h2 {{ margin-top: 42px; }}
    svg {{ max-width: 100%; height: auto; border: 1px solid #e5e7eb; }}
    .note {{ color: #4b5563; margin-bottom: 24px; }}
  </style>
</head>
<body>
  <h1>KaggleBench Results Visuals</h1>
  <p class="note">Generated from the current local benchmark artifacts.</p>
  {''.join(sections)}
</body>
</html>
"""
    output_path.write_text(html_doc, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render final-presentation result visuals.")
    parser.add_argument("--task", action="append", default=[], help="Task slug to include. Repeat for multiple tasks.")
    parser.add_argument("--stage-scope", choices=("primary", "all"), default="primary")
    parser.add_argument("--success-threshold", type=float, default=0.5)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--include-human", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--exclude-human", action="store_true", help="Exclude human reference from presentation charts.")
    parser.add_argument("--success-output", type=Path, default=DEFAULT_SUCCESS_OUTPUT)
    parser.add_argument("--struggle-output", type=Path, default=DEFAULT_STRUGGLE_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    aggregate = load_module(AGGREGATE_PATH, "presentation_aggregate")
    include_human = not args.exclude_human or args.include_human
    report = build_report(
        aggregate=aggregate,
        task_filters=args.task,
        stage_scope=args.stage_scope,
        success_threshold=args.success_threshold,
    )
    testcase_summary = build_agent_testcase_summary(report, include_human=include_human)

    write_json(output_dir / f"aggregate_{args.stage_scope}.json", report)
    write_csv_outputs(output_dir, report, testcase_summary)
    render_heatmap_svg(output_dir / "task_completion_heatmap.svg", report, testcase_summary, include_human)
    render_grouped_bar_svg(output_dir / "task_completion_grouped_bar.svg", report, testcase_summary, include_human)

    success_output = args.success_output.resolve()
    struggle_output = args.struggle_output.resolve()
    trace_cards_path = output_dir / "trace_cards.svg"
    has_trace_cards = False
    if success_output.exists() and struggle_output.exists():
        success_card = build_trace_card(
            aggregate,
            success_output,
            args.stage_scope,
            args.success_threshold,
            title="Works well",
            lesson="Tool-grounded inspection helped the agent recover relational date, reservation, store, and calendar preprocessing.",
        )
        struggle_card = build_trace_card(
            aggregate,
            struggle_output,
            args.stage_scope,
            args.success_threshold,
            title="Struggles",
            lesson="The agent caught one direct conflict, but missed subtler semantic faults that required stronger rollback checks.",
        )
        render_trace_cards_svg(trace_cards_path, success_card, struggle_card)
        has_trace_cards = True
    else:
        clear_stale_trace_cards(trace_cards_path)

    write_slide_notes(output_dir / "slide_notes.md", report, has_trace_cards=has_trace_cards)
    write_html_dashboard(output_dir / "presentation_visuals.html", output_dir)

    print(f"Wrote presentation assets to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
