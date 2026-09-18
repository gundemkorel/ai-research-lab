#!/usr/bin/env python3
"""Validate the minimum structure of one experiment workspace."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = [
    "metadata.yaml",
    "hypothesis.md",
    "config.yaml",
    "journal.md",
    "report.md",
    "src/train.py",
    "eval/evaluate.py",
    "eval/AGENTS.override.md",
    "analysis/analyze.py",
    "runs",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    args = parser.parse_args()

    root = args.experiment.resolve()
    missing = [item for item in REQUIRED if not (root / item).exists()]
    if missing:
        for item in missing:
            print(f"MISSING: {item}")
        raise SystemExit(1)
    print(f"OK: {root}")


if __name__ == "__main__":
    main()
