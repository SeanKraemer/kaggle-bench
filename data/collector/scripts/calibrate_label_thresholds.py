#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ALLOWED_RARENESS = {"common", "uncommon", "rare"}


def parse_float(value: Any, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


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


def classify_rareness(ratio: float, common_min: float, uncommon_min: float) -> str:
    if ratio >= common_min:
        return "common"
    if ratio >= uncommon_min:
        return "uncommon"
    return "rare"


def macro_f1(truth: list[str], pred: list[str]) -> float:
    if not truth:
        return 0.0
    labels = sorted(ALLOWED_RARENESS)
    score_sum = 0.0
    for label in labels:
        tp = sum(1 for t, p in zip(truth, pred) if t == label and p == label)
        fp = sum(1 for t, p in zip(truth, pred) if t != label and p == label)
        fn = sum(1 for t, p in zip(truth, pred) if t == label and p != label)
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 0.0 if (precision + recall) == 0 else 2 * precision * recall / (precision + recall)
        score_sum += f1
    return score_sum / len(labels)


@dataclass(frozen=True)
class ActionPoint:
    confidence: float
    support_ratio: float
    labeled_rareness: str | None


def load_action_points(golden_root: Path) -> list[ActionPoint]:
    points: list[ActionPoint] = []
    for json_path in sorted(golden_root.glob("*/golden_actions.json")):
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        actions = payload.get("actions")
        if not isinstance(actions, list):
            continue
        competition_refs: set[str] = set()
        for action in actions:
            if not isinstance(action, dict):
                continue
            refs = action.get("provenance_refs")
            if isinstance(refs, list):
                competition_refs.update(str(item).strip() for item in refs if str(item).strip())
        ref_total = max(1, len(competition_refs))
        for action in actions:
            if not isinstance(action, dict):
                continue
            refs = action.get("provenance_refs")
            ref_count = 0
            if isinstance(refs, list):
                ref_count = len({str(item).strip() for item in refs if str(item).strip()})
            support_ratio = ref_count / float(ref_total)
            labeled_text = str(action.get("rareness") or "").strip().lower()
            labeled: str | None = labeled_text if labeled_text in ALLOWED_RARENESS else None
            conf_value = parse_float(action.get("confidence"), 0.0)
            points.append(
                ActionPoint(
                    confidence=max(0.0, min(1.0, conf_value)),
                    support_ratio=max(0.0, min(1.0, support_ratio)),
                    labeled_rareness=labeled,
                )
            )
    return points


def main() -> None:
    parser = argparse.ArgumentParser(description="Calibrate confidence/rareness thresholds from golden actions")
    parser.add_argument("--golden-root", default="data/tasks")
    parser.add_argument("--confidence-cutoffs", default="0.4,0.6,0.75,0.9")
    parser.add_argument("--common-thresholds", default="0.15,0.2,0.25")
    parser.add_argument("--uncommon-thresholds", default="0.03,0.05,0.1")
    parser.add_argument("--min-f1", type=float, default=0.70)
    parser.add_argument("--output-csv", default="data/reports/label_threshold_calibration.csv")
    parser.add_argument("--output-report", default="data/reports/label_threshold_calibration.md")
    args = parser.parse_args()

    confidence_cutoffs = parse_float_list(args.confidence_cutoffs)
    common_thresholds = parse_float_list(args.common_thresholds)
    uncommon_thresholds = parse_float_list(args.uncommon_thresholds)

    points = load_action_points(Path(args.golden_root))
    total = len(points)
    if total == 0:
        raise SystemExit("no golden actions found")

    confidence_rows: list[dict[str, Any]] = []
    for cutoff in confidence_cutoffs:
        retained = sum(1 for p in points if p.confidence >= cutoff)
        confidence_rows.append(
            {
                "metric_type": "confidence_cutoff",
                "threshold_1": cutoff,
                "threshold_2": "",
                "retained_count": retained,
                "retained_rate": retained / float(total),
                "macro_f1": "",
            }
        )

    labeled_points = [p for p in points if p.labeled_rareness is not None]
    rareness_rows: list[dict[str, Any]] = []
    for common_min in common_thresholds:
        for uncommon_min in uncommon_thresholds:
            if uncommon_min >= common_min:
                continue
            preds = [
                classify_rareness(p.support_ratio, common_min=common_min, uncommon_min=uncommon_min) for p in points
            ]
            distribution = Counter(preds)

            if labeled_points:
                truth = [p.labeled_rareness or "" for p in labeled_points]
                labeled_preds = [
                    classify_rareness(p.support_ratio, common_min=common_min, uncommon_min=uncommon_min)
                    for p in labeled_points
                ]
                score = macro_f1(truth, labeled_preds)
            else:
                score = 0.0

            rareness_rows.append(
                {
                    "metric_type": "rareness_threshold",
                    "threshold_1": common_min,
                    "threshold_2": uncommon_min,
                    "retained_count": distribution["common"] + distribution["uncommon"] + distribution["rare"],
                    "retained_rate": 1.0,
                    "macro_f1": score if labeled_points else "",
                    "common_count": distribution["common"],
                    "uncommon_count": distribution["uncommon"],
                    "rare_count": distribution["rare"],
                }
            )

    # Prefer the strictest confidence cutoff that still retains at least 70% of actions.
    eligible_conf_cutoffs = [
        float(row["threshold_1"]) for row in confidence_rows if float(row["retained_rate"]) >= 0.70
    ]
    if eligible_conf_cutoffs:
        recommended_conf = max(eligible_conf_cutoffs)
    else:
        recommended_conf = min(float(row["threshold_1"]) for row in confidence_rows)

    best_rareness = None
    if labeled_points:
        rareness_sorted = sorted(
            rareness_rows,
            key=lambda item: float(item.get("macro_f1") or 0.0),
            reverse=True,
        )
        if rareness_sorted and float(rareness_sorted[0].get("macro_f1") or 0.0) >= args.min_f1:
            best_rareness = rareness_sorted[0]
    if best_rareness is None:
        best_rareness = {"threshold_1": 0.2, "threshold_2": 0.05, "macro_f1": ""}

    output_rows = confidence_rows + rareness_rows
    output_csv = Path(args.output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "metric_type",
            "threshold_1",
            "threshold_2",
            "retained_count",
            "retained_rate",
            "macro_f1",
            "common_count",
            "uncommon_count",
            "rare_count",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in output_rows:
            writer.writerow(row)

    output_report = Path(args.output_report)
    output_report.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Label Threshold Calibration",
        "",
        f"- Generated at (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Total actions analyzed: {total}",
        f"- Actions with labeled rareness: {len(labeled_points)}",
        "",
        "## Confidence Cutoff Sweep",
        "",
        "| confidence_cutoff | retained_count | retained_rate |",
        "|---:|---:|---:|",
    ]
    for row in confidence_rows:
        lines.append(
            f"| {float(row['threshold_1']):.2f} | {int(row['retained_count'])} | {float(row['retained_rate']):.3f} |"
        )

    lines.extend(
        [
            "",
            "## Rareness Threshold Sweep",
            "",
            "| common_min | uncommon_min | macro_f1 | common_count | uncommon_count | rare_count |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rareness_rows:
        macro_f1_value = row["macro_f1"]
        macro_f1_text = f"{float(macro_f1_value):.3f}" if macro_f1_value != "" else "n/a"
        lines.append(
            f"| {float(row['threshold_1']):.2f} | {float(row['threshold_2']):.2f} | {macro_f1_text} | "
            f"{int(row.get('common_count', 0))} | {int(row.get('uncommon_count', 0))} | {int(row.get('rare_count', 0))} |"
        )

    recommendation = {
        "recommended_confidence_cutoff": recommended_conf,
        "recommended_common_threshold": float(best_rareness["threshold_1"]),
        "recommended_uncommon_threshold": float(best_rareness["threshold_2"]),
        "rareness_macro_f1": best_rareness.get("macro_f1", ""),
    }
    lines.extend(
        [
            "",
            "## Recommendation",
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
                "actions": total,
                "labeled_actions": len(labeled_points),
                "output_csv": args.output_csv,
                "output_report": args.output_report,
                "recommended_confidence_cutoff": recommended_conf,
                "recommended_common_threshold": recommendation["recommended_common_threshold"],
                "recommended_uncommon_threshold": recommendation["recommended_uncommon_threshold"],
            },
            ensure_ascii=True,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
