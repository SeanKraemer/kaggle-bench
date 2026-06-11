# KaggleBench developer entry points.
# Run `make help` for a summary of targets.

.DEFAULT_GOAL := help

TASK ?= spaceship-titanic
DATA_ROOT ?= .data

## ---------- Environment ----------

setup: ## Install the dev environment and pre-commit hooks (requires uv)
	uv sync --dev
	uv run pre-commit install

## ---------- Quality gates ----------

test: ## Run the agent and evaluator unit test suites
	uv run python -m unittest discover -s agent/tests -p 'test_*.py'
	uv run python -m unittest discover -s eval/tests -p 'test_*.py'

lint: ## Ruff lint and format check
	uv run ruff check .
	uv run ruff format --check .

format: ## Apply ruff formatting
	uv run ruff format .

typecheck: ## Pyright static type check
	uv run pyright

validate: ## Validate committed benchmark artifacts against the JSON schemas
	uv run python eval/scripts/validate_artifacts.py

## ---------- Benchmark ----------

demo: ## Score a committed human-baseline run end to end (offline; no credentials needed)
	uv run python eval/eval.py \
		--testcase data/tasks/zillow-prize-1/testcases/tc1_from_scratch.json \
		--input data/tasks/zillow-prize-1/human_baseline/tc1_human.json \
		--pretty

aggregate: _require-outputs ## Regenerate all benchmark reports and presentation assets from local raw outputs
	@for d in data/tasks/*/; do \
		slug=$$(basename $$d); \
		for scope in primary all; do \
			uv run python eval/aggregate.py --task $$slug --stage-scope $$scope \
				--format markdown --success-threshold 0.5 \
				--output eval/results/benchmarks/$$slug-$$scope.md || exit 1; \
		done; \
	done
	uv run python eval/scripts/render_presentation_visuals.py

figures: _require-outputs ## Regenerate the SVG figures and summary CSVs used in the README
	uv run python eval/scripts/render_presentation_visuals.py

data: ## Download one competition's data with the Kaggle CLI (TASK=<slug>; needs kaggle.json + accepted rules)
	@command -v kaggle >/dev/null 2>&1 || { echo "kaggle CLI not found; install with: uv pip install kaggle"; exit 1; }
	mkdir -p $(DATA_ROOT)/$(TASK)
	kaggle competitions download -c $(TASK) -p $(DATA_ROOT)/$(TASK)
	cd $(DATA_ROOT)/$(TASK) && unzip -o '*.zip' >/dev/null
	@echo "Extracted to $(DATA_ROOT)/$(TASK). Competition data is licensed by Kaggle; never commit or redistribute it."

_require-outputs:
	@ls data/tasks/*/outputs >/dev/null 2>&1 || { \
		echo "No raw run outputs found under data/tasks/*/outputs/."; \
		echo "Regenerating reports without them would overwrite the committed results"; \
		echo "with human-only rows, so this target refuses to run. See ARTIFACT_POLICY.md."; \
		exit 1; }

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: setup test lint format typecheck validate demo aggregate figures data help _require-outputs
