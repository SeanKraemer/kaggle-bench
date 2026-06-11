from __future__ import annotations

import argparse
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
PRESENTATION_PATH = ROOT / "eval" / "scripts" / "render_presentation_visuals.py"


def load_presentation_module():
    spec = importlib.util.spec_from_file_location("presentation_module", PRESENTATION_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load presentation module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PRESENTATION = load_presentation_module()


class PresentationVisualTests(unittest.TestCase):
    def test_main_removes_stale_trace_cards_when_examples_are_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_dir = Path(tmp)
            output_dir = temp_dir / "presentation"
            output_dir.mkdir()
            trace_cards = output_dir / "trace_cards.svg"
            trace_cards.write_text("<svg>stale</svg>", encoding="utf-8")

            args = argparse.Namespace(
                task=[],
                stage_scope="primary",
                success_threshold=0.5,
                output_dir=output_dir,
                include_human=False,
                exclude_human=False,
                success_output=temp_dir / "missing-success.json",
                struggle_output=temp_dir / "missing-struggle.json",
            )

            with (
                mock.patch.object(PRESENTATION, "parse_args", return_value=args),
                mock.patch.object(PRESENTATION, "load_module", return_value=object()),
                mock.patch.object(PRESENTATION, "build_report", return_value={"tasks": []}),
                mock.patch.object(PRESENTATION, "build_agent_testcase_summary", return_value=[]),
                mock.patch.object(PRESENTATION, "write_csv_outputs"),
                mock.patch.object(PRESENTATION, "render_heatmap_svg"),
                mock.patch.object(PRESENTATION, "render_grouped_bar_svg"),
            ):
                PRESENTATION.main()

            self.assertFalse(trace_cards.exists())
            dashboard = (output_dir / "presentation_visuals.html").read_text(encoding="utf-8")
            self.assertNotIn("Trace Cards", dashboard)
            slide_notes = (output_dir / "slide_notes.md").read_text(encoding="utf-8")
            self.assertIn("Trace-card example inputs were unavailable", slide_notes)


if __name__ == "__main__":
    unittest.main()
