#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import itertools
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import TypedDict


class MetricRow(TypedDict):
    competition_slug: str
    fe_notebooks_count: int
    precision: float
    recall: float
    f1: float
    schema_pass_rate: float
    unresolved_action_proposals: int


class EvaluationRow(TypedDict):
    min_fe_notebooks: int
    min_precision: float
    min_recall: float
    min_f1: float
    min_schema_pass_rate: float
    max_unresolved_action_proposals: int
    pass_count: int
    total_competitions: int
    pass_rate: float


def parse_int_list(value: str) -> list[int]:
    parsed = []
    for item in value.split(","):
        text = item.strip()
        if not text:
            continue
        parsed.append(int(text))
    if not parsed:
        raise ValueError("list must not be empty")
    return sorted(set(parsed))


def parse_float_list(value: str) -> list[float]:
    parsed = []
    for item in value.split(","):
        text = item.strip()
        if not text:
            continue
        parsed.append(float(text))
    if not parsed:
        raise ValueError("list must not be empty")
    return sorted(set(parsed))


def parse_float(value: str | None) -> float:
    if value is None:
        return 0.0
    text = value.strip()
    if not text:
        return 0.0
    return float(text)


def parse_int(value: str | None) -> int:
    if value is None:
        return 0
    text = value.strip()
    if not text:
        return 0
    return int(float(text))


def read_metrics(path: Path) -> list[MetricRow]:
    if not path.exists():
        raise FileNotFoundError(f"metrics csv not found: {path}")

    reader = csv.DictReader(path.open("r", encoding="utf-8", newline=""))
    required = {"competition_slug", "fe_notebooks_count", "precision", "recall", "f1"}
    fieldnames = reader.fieldnames or []
    missing = [col for col in required if col not in fieldnames]
    if missing:
        raise ValueError(f"metrics csv missing required columns: {', '.join(sorted(missing))}")
    rows = list(reader)
    if not rows:
        raise ValueError(f"metrics csv has no data rows: {path}")

    parsed_rows: list[MetricRow] = []
    for row in rows:
        unresolved = row.get("unresolved_action_proposals")
        if unresolved is None:
            unresolved = row.get("action_proposals_pending")
        schema_pass_rate = row.get("schema_pass_rate")
        if schema_pass_rate is None:
            schema_pass_rate = row.get("schema_validation_pass_rate")
        parsed_rows.append(
            {
                "competition_slug": (row.get("competition_slug") or "").strip(),
                "fe_notebooks_count": parse_int(row.get("fe_notebooks_count")),
                "precision": parse_float(row.get("precision")),
                "recall": parse_float(row.get("recall")),
                "f1": parse_float(row.get("f1")),
                "schema_pass_rate": parse_float(schema_pass_rate),
                "unresolved_action_proposals": parse_int(unresolved),
            }
        )
    return [row for row in parsed_rows if row["competition_slug"]]


@dataclass(frozen=True)
class ThresholdCombo:
    min_fe_notebooks: int
    min_precision: float
    min_recall: float
    min_f1: float
    min_schema_pass_rate: float
    max_unresolved_action_proposals: int


def row_passes(row: MetricRow, combo: ThresholdCombo) -> bool:
    return (
        row["fe_notebooks_count"] >= combo.min_fe_notebooks
        and row["precision"] >= combo.min_precision
        and row["recall"] >= combo.min_recall
        and row["f1"] >= combo.min_f1
        and row["schema_pass_rate"] >= combo.min_schema_pass_rate
        and row["unresolved_action_proposals"] <= combo.max_unresolved_action_proposals
    )


def combo_strictness(combo: ThresholdCombo) -> tuple[float, ...]:
    return (
        float(combo.min_fe_notebooks),
        combo.min_precision,
        combo.min_recall,
        combo.min_f1,
        combo.min_schema_pass_rate,
        -float(combo.max_unresolved_action_proposals),
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calibrate QA gate thresholds from competition-level evaluation metrics"
    )
    parser.add_argument("--metrics-csv", default="data/reports/qa_metrics.csv")
    parser.add_argument("--min-fe-notebooks", default="30")
    parser.add_argument("--min-precision", default="0.70,0.75,0.80")
    parser.add_argument("--min-recall", default="0.70,0.75,0.80")
    parser.add_argument("--min-f1", default="0.70,0.75,0.80")
    parser.add_argument("--min-schema-pass-rate", default="1.0")
    parser.add_argument("--max-unresolved-action-proposals", default="0")
    parser.add_argument("--min-pass-competitions", type=int, default=3)
    parser.add_argument("--output-csv", default="data/reports/qa_gate_calibration.csv")
    parser.add_argument("--output-report", default="data/reports/qa_threshold_decision.md")
    args = parser.parse_args()

    rows = read_metrics(Path(args.metrics_csv))
    if not rows:
        raise SystemExit("no metrics rows found")

    min_fe_list = parse_int_list(args.min_fe_notebooks)
    min_precision_list = parse_float_list(args.min_precision)
    min_recall_list = parse_float_list(args.min_recall)
    min_f1_list = parse_float_list(args.min_f1)
    min_schema_list = parse_float_list(args.min_schema_pass_rate)
    max_unresolved_list = parse_int_list(args.max_unresolved_action_proposals)

    combos = [
        ThresholdCombo(
            min_fe_notebooks=min_fe,
            min_precision=min_precision,
            min_recall=min_recall,
            min_f1=min_f1,
            min_schema_pass_rate=min_schema,
            max_unresolved_action_proposals=max_unresolved,
        )
        for min_fe, min_precision, min_recall, min_f1, min_schema, max_unresolved in itertools.product(
            min_fe_list,
            min_precision_list,
            min_recall_list,
            min_f1_list,
            min_schema_list,
            max_unresolved_list,
        )
    ]

    evaluation_rows: list[EvaluationRow] = []
    for combo in combos:
        pass_count = sum(1 for row in rows if row_passes(row, combo))
        evaluation_rows.append(
            {
                "min_fe_notebooks": combo.min_fe_notebooks,
                "min_precision": combo.min_precision,
                "min_recall": combo.min_recall,
                "min_f1": combo.min_f1,
                "min_schema_pass_rate": combo.min_schema_pass_rate,
                "max_unresolved_action_proposals": combo.max_unresolved_action_proposals,
                "pass_count": pass_count,
                "total_competitions": len(rows),
                "pass_rate": pass_count / float(len(rows)),
            }
        )

    candidates = [row for row in evaluation_rows if row["pass_count"] >= max(1, args.min_pass_competitions)]
    if candidates:
        candidates.sort(
            key=lambda item: (
                combo_strictness(
                    ThresholdCombo(
                        min_fe_notebooks=item["min_fe_notebooks"],
                        min_precision=item["min_precision"],
                        min_recall=item["min_recall"],
                        min_f1=item["min_f1"],
                        min_schema_pass_rate=item["min_schema_pass_rate"],
                        max_unresolved_action_proposals=item["max_unresolved_action_proposals"],
                    )
                ),
                item["pass_rate"],
            ),
            reverse=True,
        )
        recommendation = candidates[0]
    else:
        recommendation = max(evaluation_rows, key=lambda item: (int(item["pass_count"]), float(item["pass_rate"])))

    output_csv = Path(args.output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "min_fe_notebooks",
                "min_precision",
                "min_recall",
                "min_f1",
                "min_schema_pass_rate",
                "max_unresolved_action_proposals",
                "pass_count",
                "total_competitions",
                "pass_rate",
            ],
        )
        writer.writeheader()
        for row in sorted(
            evaluation_rows,
            key=lambda item: (
                item["pass_rate"],
                combo_strictness(
                    ThresholdCombo(
                        min_fe_notebooks=item["min_fe_notebooks"],
                        min_precision=item["min_precision"],
                        min_recall=item["min_recall"],
                        min_f1=item["min_f1"],
                        min_schema_pass_rate=item["min_schema_pass_rate"],
                        max_unresolved_action_proposals=item["max_unresolved_action_proposals"],
                    )
                ),
            ),
            reverse=True,
        ):
            writer.writerow(row)

    output_report = Path(args.output_report)
    output_report.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# QA Threshold Decision",
        "",
        f"- Generated at (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Evaluated competitions: {len(rows)}",
        f"- Candidate combinations: {len(evaluation_rows)}",
        "",
        "## Top 10 Combinations",
        "",
        "| min_fe_notebooks | min_precision | min_recall | min_f1 | min_schema_pass_rate | max_unresolved_action_proposals | pass_count | total_competitions | pass_rate |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    top_rows = sorted(
        evaluation_rows,
        key=lambda item: (item["pass_rate"], item["pass_count"]),
        reverse=True,
    )[:10]
    for row in top_rows:
        lines.append(
            "| {min_fe_notebooks} | {min_precision:.2f} | {min_recall:.2f} | {min_f1:.2f} | "
            "{min_schema_pass_rate:.2f} | {max_unresolved_action_proposals} | {pass_count} | "
            "{total_competitions} | {pass_rate:.3f} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## Recommended Thresholds",
            "",
            "```json",
            json.dumps(recommendation, ensure_ascii=True, indent=2, sort_keys=True),
            "```",
        ]
    )
    output_report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "evaluated_competitions": len(rows),
                "evaluated_combinations": len(evaluation_rows),
                "output_csv": args.output_csv,
                "output_report": args.output_report,
                "recommended": recommendation,
            },
            ensure_ascii=True,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
