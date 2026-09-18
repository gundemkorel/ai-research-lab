from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "new_experiment.py"
    spec = importlib.util.spec_from_file_location("new_experiment", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_slugify():
    module = load_module()
    assert module.slugify("GRPO: Low Reward Variance!") == "grpo_low_reward_variance"
    assert module.slugify("  A / B  ") == "a_b"
