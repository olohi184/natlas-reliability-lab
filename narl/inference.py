"""NARL-60 llama-cpp generation adapter based on notebook cell 36.

Importing this module does not download or load a model.
"""
import platform
import time

MODEL_REPO = "tosinamuda/N-ATLaS-GGUF"
MODEL_FILE = "N-ATLaS-GGUF-Q4_K_M.gguf"


def load_model():
    """Load the original CPU GGUF model; requires optional llama-cpp-python."""
    from llama_cpp import Llama
    return Llama.from_pretrained(
        repo_id=MODEL_REPO, filename=MODEL_FILE,
        n_ctx=2048, n_gpu_layers=0, verbose=False,
    )


def generate_one(llm, row: dict, *, clock=time.perf_counter) -> dict:
    """Run one original chat completion with manifest-specified seed and limits."""
    started = clock()
    output = llm.create_chat_completion(
        messages=[{"role": "user", "content": str(row["prompt"])}],
        temperature=float(row["temperature"]),
        max_tokens=int(row["max_tokens"]),
        seed=int(row["seed"]),
    )
    choice = output["choices"][0]
    usage = output.get("usage") or {}
    return {
        "response": choice["message"]["content"],
        "finish_reason": choice.get("finish_reason", ""),
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "total_tokens": usage.get("total_tokens"),
        "generation_seconds": round(clock() - started, 3),
    }
