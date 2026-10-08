"""Resumable NARL-60 CSV checkpointing, adapted from notebook cell 38.

Each successful response is saved atomically before the next model call.
Existing completed run IDs are never regenerated.
"""
import csv
import os
from pathlib import Path
import tempfile

from .manifest import MANIFEST_COLUMNS

RESULT_COLUMNS = (*MANIFEST_COLUMNS, "response", "finish_reason",
                  "prompt_tokens", "completion_tokens", "total_tokens",
                  "generation_seconds", "model_repo", "model_file",
                  "llama_cpp_version", "python_version", "backend", "timestamp")


class CheckpointError(ValueError):
    pass


def read_checkpoint(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "run_id" not in reader.fieldnames:
            raise CheckpointError("Checkpoint missing run_id column")
        rows = list(reader)
    ids = [row["run_id"] for row in rows]
    if len(ids) != len(set(ids)) or any(not rid for rid in ids):
        raise CheckpointError("Checkpoint has duplicate or empty run IDs")
    return rows


def save_checkpoint(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Atomic replacement prevents a partial CSV from overwriting prior results.
    fd, temporary = tempfile.mkstemp(prefix=".narl-", suffix=".csv", dir=path.parent)
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=RESULT_COLUMNS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def resume_runs(manifest, checkpoint_path, generate, *, metadata=None):
    """Generate only missing runs, preserving existing checkpoint rows.

    'generate' is injected to permit mocked testing without model access.
    """
    saved = read_checkpoint(checkpoint_path)
    manifest_ids = [str(row["run_id"]) for row in manifest]
    if len(manifest_ids) != len(set(manifest_ids)):
        raise CheckpointError("Manifest contains duplicate run IDs")
    unknown = set(row["run_id"] for row in saved) - set(manifest_ids)
    if unknown:
        raise CheckpointError("Checkpoint contains run IDs absent from manifest")
    completed = {row["run_id"] for row in saved}
    for row in manifest:
        run_id = str(row["run_id"])
        if run_id in completed:
            continue
        generated = generate(row)
        record = {**row, **generated, **(metadata or {})}
        # Save first; only then consider the run completed.
        save_checkpoint(checkpoint_path, [*saved, record])
        saved.append(record)
        completed.add(run_id)
    return saved
