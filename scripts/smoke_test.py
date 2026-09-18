#!/usr/bin/env python3
"""Run an experiment's standard local smoke-test entrypoint."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    args = parser.parse_args()

    experiment = args.experiment.resolve()
    train = experiment / "src" / "train.py"
    config = experiment / "config.yaml"
    if not train.exists():
        raise SystemExit(f"Missing train entrypoint: {train}")
    if not config.exists():
        raise SystemExit(f"Missing config: {config}")

    command = [sys.executable, str(train), "--config", str(config), "--smoke-test"]
    print("+", " ".join(command))
    subprocess.run(command, check=True, cwd=experiment)


if __name__ == "__main__":
    main()
