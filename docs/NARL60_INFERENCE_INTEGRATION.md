# NARL-60 inference and checkpoint integration — phase 2

Source: user-supplied `NARL_60_NATLAS_Experiment_v1.ipynb`, especially notebook cells 7, 36 and 38. The original notebook is not publicly uploaded.

## Implemented

- `narl/inference.py`: original GGUF model identifier `tosinamuda/N-ATLaS-GGUF`, filename `N-ATLaS-GGUF-Q4_K_M.gguf`, CPU mode (`n_gpu_layers=0`), 2048-token context; chat-completion call with manifest seed, temperature and max tokens; response, finish reason and token metadata.
- `narl/checkpoint.py`: resume unfinished run IDs from a CSV checkpoint, detect duplicates and unknown checkpoint IDs, save each successful run immediately using atomic file replacement.
- `tests/test_inference_checkpoint.py`: model-mocked generation and interrupted-run recovery tests.

## What is not done

No model weights have been downloaded, no real N-ATLaS generation has been executed here, and no prior NARL-60 research result has been re-created or published. The original notebook uses Google Drive paths; these modules use caller-provided local paths. This is a code extraction, not a replication claim.

## Dependencies

`llama-cpp-python` is an **optional runtime dependency** for actual inference and may require platform-specific installation. The standard GitHub Actions unit tests do not load a model and do not require it. Model loading can download large weights; run it only on an authorized machine with suitable disk and memory.

## Example integration (after providing the original benchmark CSV)

```python
from narl.manifest import load_original_benchmark, build_manifest
from narl.inference import load_model, generate_one, MODEL_REPO, MODEL_FILE
from narl.checkpoint import resume_runs
import platform
import llama_cpp

manifest = build_manifest(load_original_benchmark("NARL_60_Prompt_Benchmark_v1.csv"))
llm = load_model()
metadata = {"model_repo": MODEL_REPO, "model_file": MODEL_FILE,
            "llama_cpp_version": llama_cpp.__version__,
            "python_version": platform.python_version(), "backend": "CPU"}
resume_runs(manifest, "NARL60_generation_checkpoint.csv",
            lambda row: generate_one(llm, row), metadata=metadata)
```

**Recovery warning:** Before using an existing checkpoint, back it up and compare its schema, model metadata, and manifest against the notebook's original files. Do not overwrite original experiment archives. The integration example is for a controlled test on copies, not direct operation on frozen research artifacts.
