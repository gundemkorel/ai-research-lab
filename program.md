# Autonomous Research Program

This file defines the operating loop for research work in this repository. `AGENTS.md` contains durable rules; this file describes **how to conduct an investigation**.

## Phase 0 — Classify the request

Decide whether the user's message is:

- a new research idea → create a new experiment directory;
- a continuation of an existing idea → resume the matching experiment;
- a question about the lab infrastructure → do not create an experiment unnecessarily.

If it is a new idea, run:

```bash
uv run python scripts/new_experiment.py "<short descriptive title>"
```

Then work inside the newly created experiment folder.

## Phase 1 — Formalize the idea

Write `hypothesis.md` before meaningful compute.

Capture:

- research question;
- falsifiable hypothesis;
- why it may matter;
- closest known baseline / related work;
- independent variable / intervention;
- dependent variable / primary metric;
- main confounders;
- what result would count as support, contradiction, or inconclusive evidence.

If the user gave only an intuition, turn it into the smallest empirical question that can test the mechanism.

## Phase 2 — Discover before spending

When relevant, inspect current papers, docs, issues, benchmarks, or prior experiments.

Goal: determine whether we are doing:

- replication;
- extension;
- ablation;
- new algorithmic variant;
- implementation check;
- exploratory phenomenon study.

Do enough discovery to avoid wasting compute, but do not turn a cheap experiment into an endless literature review.

## Phase 3 — Freeze the first evaluation protocol

Before treatment results are known:

1. define train/validation/test split;
2. define primary metric;
3. define secondary metrics if useful;
4. define seed policy;
5. define stopping / comparison rule;
6. create or review the experiment-local evaluator.

The `eval/` directory has stricter instructions. Follow them.

## Phase 4 — Establish baseline

Run the simplest valid baseline first unless an equivalent baseline result already exists under the same evaluation protocol.

Record baseline outputs as a run under:

```text
runs/001_baseline/
```

A baseline run should produce a `run.json` and retain logs/artifact references needed for comparison.

## Phase 5 — Propose the next informative change

Before each non-baseline run, state:

- the exact conceptual change;
- why it is informative;
- expected direction of effect;
- what result would cause us to keep, reject, or refine it.

Prefer one conceptual change per run.

## Phase 6 — Smoke test

Before remote GPU use:

- import all dependencies;
- load a tiny dataset slice;
- instantiate the model/config when feasible;
- run the shortest meaningful forward/training/evaluation path;
- verify output paths and metrics;
- fail fast on NaNs, empty datasets, missing labels, broken reward functions, or obvious device errors.

A successful smoke test does not count as evidence for the research hypothesis.

## Phase 7 — Select compute

Read `configs/compute.yaml` and experiment `config.yaml`.

Default preference:

```text
local → Kaggle free GPU → Hugging Face Jobs (paid, explicit authorization)
```

Choose the cheapest environment that can answer the question.

Set explicit timeouts for remote jobs.

## Phase 8 — Run and observe

Create a new run directory with:

```bash
uv run python scripts/new_run.py <experiment-path> "<short run name>"
```

This creates `runs/NNN_<short_name>/` with a config snapshot and initial `run.json`.

Store or reference:

- config snapshot;
- command;
- stdout/stderr or remote job URL/id;
- metrics;
- artifacts;
- `run.json` summary.

Do not edit the run's recorded result after the fact. Add a new run if something changes.

## Phase 9 — Evaluate

Compare the run to the relevant baseline under the same evaluator.

Ask:

- Did the primary metric move in the expected direction?
- Is the magnitude meaningful relative to noise?
- Did secondary metrics reveal a tradeoff?
- Is the result likely to be leakage, evaluator gaming, a data bug, or a seed artifact?
- Did runtime/memory/cost change materially?

## Phase 10 — Decide

Assign one decision:

### KEEP
The variant provides credible improvement or a scientifically useful effect.

### REJECT
The variant is worse, invalid, or fails to support the mechanism.

### INCONCLUSIVE
Evidence is insufficient; state the cheapest experiment that would resolve the ambiguity.

### CONFIRM
The effect is promising but should be repeated across seeds/conditions before drawing a conclusion.

Do not keep a change because the code looks elegant.

## Phase 11 — Journal immediately

Append to `journal.md`:

```markdown
## Run NNN — <name>

**Reason**  
Why this run was informative.

**Change**  
What differed from the comparison run.

**Result**  
Primary metric and important secondary observations.

**Decision**  
KEEP / REJECT / INCONCLUSIVE / CONFIRM.

**Next**  
Next informative action.
```

## Phase 12 — Iterate within bounds

Continue only while another run has positive expected information value and the experiment remains within its budgets.

Possible next steps:

- confirm with more seeds;
- run an ablation;
- test a boundary condition;
- simplify the method;
- inspect failures;
- compare against a stronger baseline.

A new scientific question should become a new experiment directory rather than expanding the current experiment without limit.

## Phase 13 — Conclude

When stopping, update:

- `report.md`;
- `metadata.yaml` status;
- lab-level `results/experiments.csv`.

The report should say what was learned, not merely what was executed.
