#!/usr/bin/env python3
"""Create a new isolated experiment workspace from templates/experiment."""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
TEMPLATE = ROOT / "templates" / "experiment"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value[:70] or "untitled"


def next_id() -> int:
    pattern = re.compile(r"^exp_(\d{3,})_")
    ids: list[int] = []
    for path in EXPERIMENTS.iterdir():
        if not path.is_dir():
            continue
        match = pattern.match(path.name)
        if match:
            ids.append(int(match.group(1)))
    return max(ids, default=0) + 1


def replace_placeholders(directory: Path, mapping: dict[str, str]) -> None:
    for path in directory.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for key, value in mapping.items():
            text = text.replace("{{" + key + "}}", value)
        path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Short descriptive title for the research idea")
    args = parser.parse_args()

    if not TEMPLATE.exists():
        raise SystemExit(f"Missing experiment template: {TEMPLATE}")

    number = next_id()
    experiment_id = f"exp_{number:03d}"
    slug = slugify(args.title)
    destination = EXPERIMENTS / f"{experiment_id}_{slug}"

    if destination.exists():
        raise SystemExit(f"Experiment already exists: {destination}")

    shutil.copytree(TEMPLATE, destination)
    mapping = {
        "EXPERIMENT_ID": experiment_id,
        "TITLE": args.title.strip(),
        "SLUG": slug,
        "CREATED_AT": datetime.now(timezone.utc).isoformat(),
    }
    replace_placeholders(destination, mapping)

    print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
