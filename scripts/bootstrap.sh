#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "== AI Research Lab bootstrap =="

if command -v uv >/dev/null 2>&1; then
  echo "Using uv to create/sync the environment..."
  uv sync --extra dev
else
  echo "uv is not installed. Install uv, then run: uv sync --extra dev"
fi

if command -v hf >/dev/null 2>&1; then
  echo
  echo "Hugging Face CLI found."
  echo "To install the project-local hf CLI skill for Codex-compatible agents:"
  echo "  hf skills add"
  echo "Authenticate when needed with:"
  echo "  hf auth login"
else
  echo
  echo "Hugging Face CLI not found. Install/update the hf CLI before using Hub or HF Jobs."
fi

if command -v kaggle >/dev/null 2>&1; then
  echo "Kaggle CLI found."
else
  echo "Kaggle CLI not found. Install it only if you want free Kaggle GPU dispatch."
fi

echo
echo "Bootstrap guidance complete. Paid compute remains disabled by default."
