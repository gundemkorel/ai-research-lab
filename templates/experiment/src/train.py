"""Experiment training/implementation entrypoint.

Replace this template with the smallest code that tests the hypothesis.
Keep provider-specific compute logic outside the scientific core when possible.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=False)
    parser.add_argument("--smoke-test", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke_test:
        print("Smoke-test placeholder: implement the minimal execution path for this experiment.")
        return
    raise SystemExit("Implement this experiment before running a full training job.")


if __name__ == "__main__":
    main()
