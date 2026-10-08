"""NARL-60 run manifest generation, faithfully derived from Colab cells 1–3.

No model inference, data publication or external network calls occur here.
"""
import csv
from pathlib import Path

RUN_SEEDS = {1: 101, 2: 202, 3: 303}
LANGUAGE_OFFSETS = {"NE": 0, "HA": 10, "YO": 20, "IG": 30}
BENCHMARK_COLUMNS = ("prompt_id", "matched_task_id", "domain", "language_code", "language", "prompt")
MANIFEST_COLUMNS = (
    "run_id", "prompt_id", "matched_task_id", "domain", "language_code",
    "language", "run_number", "seed", "prompt", "temperature", "max_tokens", "n_ctx"
)


class ManifestError(ValueError):
    """Invalid NARL-60 benchmark for the recorded experimental design."""


def build_manifest(benchmark_rows: list[dict]) -> list[dict]:
    """Generate three deterministic runs per prompt, retaining original notebook settings."""
    if not benchmark_rows:
        raise ManifestError("Benchmark must contain at least one prompt")
    manifest = []
    seen_prompt_ids = set()
    for index, row in enumerate(benchmark_rows, start=2):
        missing = [col for col in BENCHMARK_COLUMNS if not str(row.get(col) or "").strip()]
        if missing:
            raise ManifestError(f"Benchmark row {index}: missing {', '.join(missing)}")
        prompt_id = str(row["prompt_id"]).strip()
        if prompt_id in seen_prompt_ids:
            raise ManifestError(f"Duplicate prompt_id: {prompt_id}")
        seen_prompt_ids.add(prompt_id)
        code = str(row["language_code"]).strip()
        if code not in LANGUAGE_OFFSETS:
            raise ManifestError(f"Unknown language_code: {code}")
        for run_number in (1, 2, 3):
            manifest.append({
                "run_id": f"{prompt_id}-R{run_number}",
                "prompt_id": prompt_id,
                "matched_task_id": str(row["matched_task_id"]).strip(),
                "domain": str(row["domain"]).strip(),
                "language_code": code,
                "language": str(row["language"]).strip(),
                "run_number": run_number,
                "seed": RUN_SEEDS[run_number] + LANGUAGE_OFFSETS[code],
                "prompt": str(row["prompt"]).strip(),
                "temperature": 0.1,
                "max_tokens": 400,
                "n_ctx": 2048,
            })
    return manifest


def load_original_benchmark(path: str | Path) -> list[dict]:
    """Read original NARL-60 benchmark schema, distinct from prototype CSV schema."""
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or any(c not in reader.fieldnames for c in BENCHMARK_COLUMNS):
            raise ManifestError("Missing original NARL-60 benchmark columns")
        return list(reader)


def write_manifest(rows: list[dict], path: str | Path) -> None:
    with Path(path).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
