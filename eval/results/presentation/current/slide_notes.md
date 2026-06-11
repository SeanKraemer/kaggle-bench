# Final Presentation Results Visuals

## Recommended Slide Names

- Slide 9: `Results: Agent Performance by Scenario`
- Slide 10: `Trace Examples: Where Agents Help and Fail`
- Slide 11: `Conclusion: What the Benchmark Reveals`

## Slide 9: Results - Number Report

- Use `task_completion_heatmap.svg` as the primary visual.
- Keep the headline to one sentence: agents do better at adding good actions than fixing harmful context.
- Use the human reference as a left-side anchor and the Overall Success column as the cross-scenario headline.
- Black outlines mark the best non-human method in each column.
- Use `task_completion_grouped_bar.svg` only if the heatmap is hard to read in Google Slides.
- Current artifacts include all `20` benchmark tasks with complete raw evaluation coverage.
- Put `primary` scope in the footnote; note that Overall Success is binary pass rate, not another task-completion mean.

## Slide 10: Results - Example Traces

- Use `trace_cards.svg` as one visual with two side-by-side cards.
- The left card should support the claim that tools help with evidence gathering.
- The right card should support the claim that rollback/fault diagnosis is still weak.
- Avoid raw JSON on the slide; use action labels and one-line lessons.

## Slide 11: Conclusion

- Main contribution: deterministic action-bank benchmark from expert Kaggle workflows.
- Main result: LLM-based systems are decent recommenders, weaker debuggers.
- Agent lesson: task-aware tools help, but orchestration needs stronger verification.
- Limitation: exact matching and public Kaggle-derived golden actions can undercount valid alternatives.
- Future work: semantic equivalence, private tasks, explicit rollback checks, downstream model validation.

## Image Generation Guidance

- Do not use image generation for Slides 9 or 10; these should look data-driven and auditable.
- If you use image generation anywhere, reserve it for an intro/motivation visual, not the results section.
- For Sean's slides, deterministic SVG charts and trace cards are clearer and safer.

## Regeneration Command

```bash
uv run python eval/scripts/render_presentation_visuals.py
```

These outputs were generated from the current benchmark artifacts.
