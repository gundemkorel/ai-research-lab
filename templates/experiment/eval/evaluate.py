"""Experiment-local evaluator.

Define the primary evaluation protocol before inspecting treatment results whenever possible.
"""

from __future__ import annotations


def evaluate() -> dict[str, float]:
    raise NotImplementedError("Define the experiment-specific evaluation protocol.")
