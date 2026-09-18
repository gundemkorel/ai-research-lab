# AI Research Lab

A portable, agent-first template for small-scale AI research with Codex or Claude Code.

The lab is designed around a simple principle: **one research idea = one isolated experiment workspace**. The agent can autonomously design, implement, run, evaluate, and iterate on an idea, but only inside explicit scientific and compute budgets.

## Philosophy

This repository adapts the *autoresearch* mindset to a general research lab:

1. State a falsifiable hypothesis.
2. Establish a baseline before claiming improvement.
3. Make the smallest informative change.
4. Smoke-test before spending real compute.
5. Run the experiment.
6. Evaluate against a fixed protocol.
7. Record the result whether it worked or failed.
8. Keep, reject, or refine based on evidence.
9. Iterate until the question is resolved or a budget/stopping condition is reached.

The agent should advance through **measured evidence, not confidence**.

## Repository layout

```text
ai-research-lab/
├── AGENTS.md                 # durable rules / scientific constitution
├── program.md                # autonomous research loop
├── experiments/              # one directory per research idea
│   ├── AGENTS.md             # isolation rules for all experiments
│   └── exp_###_.../
│       ├── metadata.yaml
│       ├── hypothesis.md
│       ├── journal.md
│       ├── report.md
│       ├── config.yaml
│       ├── src/
│       ├── eval/             # protected evaluation protocol
│       ├── analysis/
│       └── runs/             # baseline, variants, seeds, confirmations
├── templates/experiment/     # copied for every new idea
├── compute/                  # local / Kaggle / HF Jobs guidance
├── research/                 # cross-project literature notes + lessons
├── results/experiments.csv   # lightweight lab-wide index
├── scripts/                  # experiment creation and validation helpers
└── .agents/skills/           # project-local agent skills (optional)
```

## Quick start

### 1. Clone and bootstrap

```bash
git clone <your-repo-url> ai-research-lab
cd ai-research-lab
./scripts/bootstrap.sh
```

The bootstrap script installs the Python environment with `uv` when available and gives instructions for Hugging Face agent skills.

### 2. Authenticate external services as needed

Hugging Face:

```bash
hf auth login
hf skills add
```

Kaggle:

Install the Kaggle CLI and configure credentials according to Kaggle's official CLI documentation.

### 3. Start Codex in the repository

```bash
codex
```

Then describe the research idea naturally, for example:

> I suspect GRPO's group standard-deviation normalization becomes unstable when reward variance is low. Check whether this is already established, formulate the smallest useful experiment on a small Qwen model, create a new experiment workspace, run a baseline and the proposed variant, and tell me what we learn. Use free compute when possible; do not use paid compute without explicit authorization.

The repository instructions tell the agent how to proceed.

## Creating an experiment manually

Normally the agent should do this itself when it recognizes a new research idea:

```bash
uv run python scripts/new_experiment.py "GRPO low reward variance"
```

This creates something like:

```text
experiments/exp_001_grpo_low_reward_variance/
```

A distinct idea gets a new directory. Repeated attempts, parameter variants, and seeds for the *same idea* belong under that experiment's `runs/` directory. Create runs with `uv run python scripts/new_run.py <experiment-path> "<run name>"`.

## Default stack

The default post-training stack is deliberately conventional:

- PyTorch
- Hugging Face Transformers
- Datasets
- TRL
- PEFT / LoRA / QLoRA where appropriate
- optional Unsloth when it materially lowers memory or runtime

Do not migrate to a heavier distributed RL stack unless the experiment actually requires it.

## Compute policy

Default priority:

```text
local CPU / local accelerator
        ↓
free Kaggle GPU when appropriate
        ↓
Hugging Face Jobs only when explicitly authorized
```

Paid compute is disabled by default. See `compute/README.md` and `configs/compute.yaml`.

## Experiment records

Every experiment should leave behind three human-readable artifacts:

- `hypothesis.md` — what question was tested and why
- `journal.md` — chronological record of runs and decisions
- `report.md` — final concise interpretation and limitations

The lab-wide `results/experiments.csv` is only an index. Detailed outputs stay inside each experiment folder or in external artifact storage such as the Hugging Face Hub.

## Hugging Face skills

Do not vendor large copies of third-party skills into this repository unless there is a strong reason. Prefer the current Hugging Face CLI skill plus selective workflow skills. See `.agents/skills/README.md`.

## Scientific guardrail

An experiment must never silently alter its evaluator to make the treatment look better. Each experiment's `eval/` directory contains an `AGENTS.override.md` that makes this explicit.
