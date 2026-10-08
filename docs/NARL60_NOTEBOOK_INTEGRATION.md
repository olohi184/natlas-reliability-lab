# NARL-60 notebook integration — phase 1

## Provenance

Source: `NARL_60_NATLAS_Experiment_v1.ipynb`, supplied separately by the project lead. The notebook is **not published** in this repository.

The new `narl/manifest.py` is a reusable implementation of the benchmark-to-manifest logic in notebook cells 1–3. It preserves:
- Three runs per prompt with base seeds 101, 202, 303
- Language seed offsets: NE=0, HA=10, YO=20, IG=30
- Temperature=0.1, max_tokens=400, n_ctx=2048
- Run IDs in the form `<prompt_id>-R<run_number>`
- The original benchmark fields: `prompt_id,matched_task_id,domain,language_code,language,prompt`

The original notebook loads `/content/NARL_60_Prompt_Benchmark_v1.csv`. That dataset has **not** been uploaded or included here.

## Distinct CSV formats

The existing `narl/benchmark.py` validates the earlier *prototype* format (`item_id,language,domain,prompt`). The new `narl/manifest.py` handles the **original NARL-60 experimental benchmark format**. These are not interchangeable; do not rename columns or assume they represent the same dataset.

## How to generate the original manifest

With the authorized original benchmark CSV available locally:

```python
from narl.manifest import load_original_benchmark, build_manifest, write_manifest
rows = load_original_benchmark("NARL_60_Prompt_Benchmark_v1.csv")
manifest = build_manifest(rows)
write_manifest(manifest, "NARL60_run_manifest.csv")
print(len(manifest))
```

This does **not** run N-ATLaS or regenerate experimental results. It only creates the planned run manifest.

## Remaining work

The notebook also contains GGUF inference with llama-cpp-python, resumable checkpoint generation, blinded semantic evaluation, statistical analyses and human-validation packet creation. These require separate extraction, dependency verification and review of credentials, output artifacts and data-sharing permissions. No model execution or empirical result has been reproduced in this phase.
