# Compute backends

Experiments should be written so that the **research logic does not depend on the compute provider**.

Default preference:

```text
local → Kaggle → Hugging Face Jobs
```

## Local

Always use local execution for smoke tests when feasible.

Example:

```bash
uv run python experiments/exp_001_example/src/train.py \
  --config experiments/exp_001_example/config.yaml \
  --smoke-test
```

## Kaggle

Kaggle is the preferred free GPU path when the experiment fits its notebook/kernel model and quota is available.

The official CLI can initialize metadata, push a kernel (which runs it), select an accelerator, set a timeout, check status, and download output.

Typical workflow:

```bash
kaggle kernels init -p <staging-directory>
kaggle kernels push -p <staging-directory> --accelerator NvidiaTeslaT4 --timeout 3600
kaggle kernels status <owner/slug>
kaggle kernels output <owner/slug> -p <output-directory>
```

Do not make experiment source code depend on Kaggle-specific APIs unless required. Prefer a small staging wrapper around the same experiment entrypoint used locally.

## Hugging Face Jobs

HF Jobs is paid compute and therefore requires explicit user authorization for the experiment.

Example:

```bash
hf jobs uv run \
  --with trl \
  --flavor t4-small \
  --timeout 30m \
  experiments/exp_001_example/src/train.py
```

HF Jobs uploads a local script automatically. Persist important model/data artifacts to the Hugging Face Hub or another durable store; do not assume the remote filesystem survives the job.

Never launch an HF Job merely because Kaggle is inconvenient when paid compute has not been authorized.
