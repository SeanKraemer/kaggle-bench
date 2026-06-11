#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ALLOWED_SOURCE_PROFILES = {"winner_style", "explanatory_style"}
ALLOWED_RARENESS = {"common", "uncommon", "rare"}


@dataclass
class NormalizedAction:
    action_type: str
    canonical_params: dict[str, Any]
    provenance_refs: set[str]
    confidence: float
    reasoning_summary: str
    evidence_snippets: list[str]
    context_notes: str
    source_profile: str


def parse_float(value: Any, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def clamp_confidence(value: float) -> float:
    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value


def canonical_signature(action_type: str, canonical_params: dict[str, Any]) -> str:
    return f"{action_type}|{json.dumps(canonical_params, sort_keys=True, ensure_ascii=True, separators=(',', ':'))}"


def read_input_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"input file not found: {path}")

    if path.suffix.lower() == ".json":
        raw = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(raw, dict) and isinstance(raw.get("actions"), list):
            json_rows = raw["actions"]
        elif isinstance(raw, list):
            json_rows = raw
        else:
            raise ValueError(f"unsupported JSON structure in {path}")
        return [row for row in json_rows if isinstance(row, dict)]

    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        text = line.strip()
        if not text:
            continue
        try:
            value = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at line {line_no} in {path}: {exc}") from exc
        if isinstance(value, dict):
            rows.append(value)
    return rows


def normalize_action(
    row: dict[str, Any],
    default_source_profile: str,
    min_confidence: float,
) -> tuple[NormalizedAction | None, str | None]:
    action_type = str(row.get("action_type") or "").strip().upper()
    if not action_type:
        return None, "missing_action_type"

    canonical_params = row.get("canonical_params")
    if canonical_params is None:
        canonical_params = row.get("action_params")
    if not isinstance(canonical_params, dict):
        return None, "missing_or_invalid_canonical_params"

    provenance_refs_raw = row.get("provenance_refs")
    if isinstance(provenance_refs_raw, list):
        provenance_refs = {str(item).strip() for item in provenance_refs_raw if str(item).strip()}
    else:
        provenance_refs = set()
    notebook_ref = str(row.get("notebook_ref") or "").strip()
    if notebook_ref:
        provenance_refs.add(notebook_ref)
    if not provenance_refs:
        return None, "missing_provenance_refs"

    confidence = clamp_confidence(parse_float(row.get("confidence"), 0.6))
    if confidence < min_confidence:
        return None, "below_min_confidence"

    evidence_snippets_raw = row.get("evidence_snippets")
    evidence_snippets: list[str] = []
    if isinstance(evidence_snippets_raw, list):
        evidence_snippets = [str(item).strip() for item in evidence_snippets_raw if str(item).strip()]
    if not evidence_snippets:
        examples = row.get("evidence_examples")
        if isinstance(examples, list):
            for item in examples:
                if not isinstance(item, dict):
                    continue
                snippet = str(item.get("raw_snippet") or "").strip()
                if snippet:
                    evidence_snippets.append(snippet)
    if not evidence_snippets:
        snippet = str(row.get("evidence_snippet") or "").strip()
        if snippet:
            evidence_snippets = [snippet]
    if not evidence_snippets:
        return None, "missing_evidence_snippets"

    source_profile = str(row.get("source_profile") or default_source_profile).strip()
    if source_profile not in ALLOWED_SOURCE_PROFILES:
        source_profile = default_source_profile

    normalized = NormalizedAction(
        action_type=action_type,
        canonical_params=canonical_params,
        provenance_refs=provenance_refs,
        confidence=confidence,
        reasoning_summary=str(row.get("reasoning_summary") or "").strip(),
        evidence_snippets=evidence_snippets,
        context_notes=str(row.get("context_notes") or "").strip(),
        source_profile=source_profile,
    )
    return normalized, None


def merge_action(dst: NormalizedAction, src: NormalizedAction) -> None:
    dst.provenance_refs.update(src.provenance_refs)
    dst.confidence = max(dst.confidence, src.confidence)
    if len(src.reasoning_summary) > len(dst.reasoning_summary):
        dst.reasoning_summary = src.reasoning_summary
    for snippet in src.evidence_snippets:
        if snippet not in dst.evidence_snippets:
            dst.evidence_snippets.append(snippet)
    if src.context_notes and src.context_notes not in dst.context_notes:
        if dst.context_notes:
            dst.context_notes = f"{dst.context_notes}\n{src.context_notes}"
        else:
            dst.context_notes = src.context_notes
    if dst.source_profile != src.source_profile and src.source_profile in ALLOWED_SOURCE_PROFILES:
        if "(estimated)" not in dst.context_notes:
            suffix = "(estimated) source_profile conflict merged"
            dst.context_notes = f"{dst.context_notes}\n{suffix}".strip()


def compute_rareness(unique_notebooks: set[str], action_notebooks: set[str]) -> str:
    if not unique_notebooks:
        return "uncommon"
    ratio = len(action_notebooks) / float(len(unique_notebooks))
    if ratio >= 0.20:
        return "common"
    if ratio >= 0.05:
        return "uncommon"
    return "rare"


def validate_action(action: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = [
        "action_id",
        "action_type",
        "canonical_params",
        "provenance_refs",
        "confidence",
        "rareness",
        "reasoning_summary",
        "evidence_snippets",
        "context_notes",
        "source_profile",
    ]
    for field in required:
        if field not in action:
            errors.append(f"missing_{field}")

    if not isinstance(action.get("action_type"), str) or not action.get("action_type"):
        errors.append("invalid_action_type")
    if not isinstance(action.get("canonical_params"), dict):
        errors.append("invalid_canonical_params")
    if not isinstance(action.get("provenance_refs"), list) or not action.get("provenance_refs"):
        errors.append("invalid_provenance_refs")
    if not isinstance(action.get("confidence"), float):
        errors.append("invalid_confidence")
    if action.get("rareness") not in ALLOWED_RARENESS:
        errors.append("invalid_rareness")
    if action.get("source_profile") not in ALLOWED_SOURCE_PROFILES:
        errors.append("invalid_source_profile")
    if not isinstance(action.get("evidence_snippets"), list) or not action.get("evidence_snippets"):
        errors.append("invalid_evidence_snippets")
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build deduplicated golden actions JSON from curated action candidates")
    parser.add_argument("--competition", required=True)
    parser.add_argument("--input", default=None)
    parser.add_argument("--output", default=None)
    parser.add_argument("--proposals-output", default=None)
    parser.add_argument("--schema", default="data/schema/golden_action.schema.json")
    parser.add_argument("--default-source-profile", default="winner_style")
    parser.add_argument("--min-confidence", type=float, default=0.0)
    parser.add_argument("--strict", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    competition = args.competition.strip()
    if not competition:
        raise ValueError("--competition is required")

    input_path = Path(args.input or f"data/collector/data/golden/{competition}/action_candidates.jsonl")
    output_path = Path(args.output or f"data/tasks/{competition}/golden_actions.json")
    proposals_path = Path(args.proposals_output or f"data/collector/data/golden/{competition}/action_proposals.jsonl")

    rows = read_input_rows(input_path)
    dedup: dict[str, NormalizedAction] = {}
    rejected_rows: list[dict[str, Any]] = []

    for row in rows:
        normalized, reason = normalize_action(
            row=row,
            default_source_profile=args.default_source_profile,
            min_confidence=args.min_confidence,
        )
        if normalized is None:
            rejected_rows.append({"reason": reason, "raw": row})
            continue

        signature = canonical_signature(normalized.action_type, normalized.canonical_params)
        existing = dedup.get(signature)
        if existing is None:
            dedup[signature] = normalized
        else:
            merge_action(existing, normalized)

    all_notebooks: set[str] = set()
    for action in dedup.values():
        all_notebooks.update(action.provenance_refs)

    actions_payload: list[dict[str, Any]] = []
    for idx, key in enumerate(sorted(dedup.keys()), start=1):
        action = dedup[key]
        payload = {
            "action_id": f"GA-{idx:06d}",
            "action_type": action.action_type,
            "canonical_params": action.canonical_params,
            "provenance_refs": sorted(action.provenance_refs),
            "confidence": float(f"{action.confidence:.3f}"),
            "rareness": compute_rareness(all_notebooks, action.provenance_refs),
            "reasoning_summary": action.reasoning_summary,
            "evidence_snippets": action.evidence_snippets,
            "context_notes": action.context_notes,
            "source_profile": action.source_profile,
        }
        errors = validate_action(payload)
        if errors:
            rejected_rows.append({"reason": ",".join(errors), "raw": payload})
            continue
        actions_payload.append(payload)

    golden_payload = {
        "competition_slug": competition,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "actions": actions_payload,
    }

    schema_path = Path(args.schema)
    if not schema_path.exists():
        raise FileNotFoundError(f"schema file not found: {schema_path}")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(golden_payload), key=lambda e: list(e.path))
    if schema_errors:
        first = schema_errors[0]
        location = "/".join(str(item) for item in first.path) or "<root>"
        raise SystemExit(f"schema_validation_failed: {location}: {first.message}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(golden_payload, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")

    proposals_path.parent.mkdir(parents=True, exist_ok=True)
    with proposals_path.open("w", encoding="utf-8") as f:
        for row in rejected_rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")

    summary = {
        "competition_slug": competition,
        "input_rows": len(rows),
        "golden_actions": len(actions_payload),
        "proposals": len(rejected_rows),
        "output": str(output_path),
        "proposals_output": str(proposals_path),
        "schema": args.schema,
    }
    if args.strict and rejected_rows:
        raise SystemExit(json.dumps(summary, ensure_ascii=True, sort_keys=True))
    print(json.dumps(summary, ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    main()
