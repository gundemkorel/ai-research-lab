# Project-local agent skills

Codex can discover skills from `.agents/skills/`.

Recommended setup:

## 1. Hugging Face CLI skill

Install/update the current `hf` CLI first, then from this repository run:

```bash
hf skills add
```

This installs the CLI skill into the current project for clients that load `.agents/skills`.

For a global installation instead:

```bash
hf skills add --global
```

The CLI skill is generated from the locally installed CLI version, so refresh it when the CLI changes:

```bash
hf skills update
```

## 2. Optional workflow skills

Hugging Face also publishes workflow-specific skills for datasets, training, evaluation, and tracking. Add them selectively when they materially help the current research workflow rather than installing every overlapping skill.

The default lab policy is:

- keep the current `hf-cli` skill;
- prefer TRL as the post-training framework;
- add specialized HF workflow skills only when their scope is clear;
- avoid multiple overlapping skills that give contradictory training/compute instructions.

The repository's `AGENTS.md` and `program.md` remain authoritative for scientific process and cost controls.
