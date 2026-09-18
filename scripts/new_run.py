#!/usr/bin/env python3
"""Create an immutable run directory inside an experiment workspace."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")[:60] or "run"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    parser.add_argument("name")
    parser.add_argument("--comparison", default=None, help="Optional comparison run id/name")
    args = parser.parse_args()

    experiment = args.experiment.resolve()
    runs = experiment / "runs"
    if not runs.exists():
        raise SystemExit(f"Not an experiment workspace (missing runs/): {experiment}")

    pattern = re.compile(r"^(\d{3,})_")
    ids: list[int] = []
    for path in runs.iterdir():
        if path.is_dir() and (match := pattern.match(path.name)):
            ids.append(int(match.group(1)))
    number = max(ids, default=0) + 1

    run_id = f"{number:03d}"
    destination = runs / f"{run_id}_{slugify(args.name)}"
    destination.mkdir()

    config = experiment / "config.yaml"
    if config.exists():
        shutil.copy2(config, destination / "config_snapshot.yaml")

    record = {
        "run_id": run_id,
        "name": args.name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "planned",
        "comparison": args.comparison,
        "command": None,
        "git_commit": None,
        "compute": {"provider": None, "hardware": None, "runtime_seconds": None, "paid_cost_usd": 0.0},
        "metrics": {},
        "decision": None,
        "artifacts": [],
        "notes": None,
    }
    (destination / "run.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()
