# Integrating existing NARL evaluation work

The public repository currently contains a Streamlit prototype and a **benchmark CSV validator**. It does not yet contain an N-ATLAS inference runner or scored evaluation logs.

## Supported input CSV format

The validator requires the following columns:

`item_id,language,domain,prompt`

An illustrative, **synthetic** input file is available at `examples/benchmark_example.csv`. These examples are not validated NARL-60 or NARL-300 research datasets.

## Validate a CSV locally

From the repository root:

```bash
python -c "from narl.benchmark import load_benchmark; print(len(load_benchmark('examples/benchmark_example.csv')))"
python -m unittest discover -s tests -v
```

## What is needed to integrate the existing Colab runner

1. Export the actual Colab notebook as `.ipynb` or `.py` and review it for credentials, personal information and licensed data.
2. Record the model identifier, exact N-ATLAS integration method, generation settings, runtime environment and output schema.
3. Move reusable inference code into a Python module while retaining the original notebook for provenance.
4. Add mocked integration tests that verify output formatting without making live N-ATLAS calls.
5. Verify a genuine model-backed run before connecting results to the dashboard.

Do not commit API keys, tokens, confidential prompts, or unpublished data without permission.

## Status

No real N-ATLAS model integration or research results are claimed by this validation-only module.
