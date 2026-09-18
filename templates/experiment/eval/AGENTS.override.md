# Protected Evaluation Protocol

This directory defines the experiment's evaluation protocol.

## Hard rule

Do not modify evaluation after observing a treatment result merely to improve the apparent result.

If an evaluation change is scientifically necessary:

1. stop comparing against results generated under the old evaluator;
2. explain the defect or reason in `../journal.md`;
3. version the new evaluator/protocol;
4. rerun the relevant baseline under the new protocol;
5. clearly distinguish old-protocol and new-protocol results.

Do not leak held-out labels, gold answers, test examples, or evaluator internals into training or prompt optimization.

Treat changes to dataset splits, reward definitions, judge prompts, rubrics, thresholds, and primary metrics as evaluation changes when they affect comparability.
