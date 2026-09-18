# Experiment Workspace Rules

Everything below `experiments/` is organized around strict isolation.

## Isolation

- One distinct research idea = one `exp_###_<slug>/` directory.
- Do not change files in another experiment while working on the current idea.
- Do not import experiment-specific modules from another experiment.
- If a previous experiment is scientifically relevant, cite or copy the minimal stable idea with provenance rather than creating hidden mutable coupling.
- Shared infrastructure may be used, but experiment-specific state must remain local.

## Runs

Different seeds, baselines, ablations, and parameter variants for the same scientific question belong under `runs/` inside the experiment.

Create run directories with monotonically increasing ids such as:

```text
runs/001_baseline/
runs/002_no_std_norm/
runs/003_seed_123/
```

Do not overwrite a completed run. Create a new run.

## Required experiment artifacts

Before concluding an experiment, ensure the directory contains useful versions of:

- `metadata.yaml`
- `hypothesis.md`
- `config.yaml`
- `journal.md`
- `report.md`
- runnable source code
- evaluation code/protocol
- run summaries
