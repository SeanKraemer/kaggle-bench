#!/usr/bin/env bash
set -euo pipefail

WORKDIR="$1"
PROMPT_FILE="$WORKDIR/PROMPT.md"

mkdir -p "$WORKDIR/.claude-home"
export HOME="$WORKDIR/.claude-home"

cd "$WORKDIR"
claude --print --output-format json "$(cat "$PROMPT_FILE")"
