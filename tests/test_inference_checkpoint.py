"""Mocked model tests and crash-safe checkpoint recovery."""
import tempfile
import unittest
from pathlib import Path

from narl.checkpoint import CheckpointError, read_checkpoint, resume_runs
from narl.inference import generate_one
from narl.manifest import build_manifest


def prompt():
    return {"prompt_id": "P1", "matched_task_id": "T1", "domain": "General",
            "language_code": "NE", "language": "Nigerian English", "prompt": "Hello"}


class FakeModel:
    def __init__(self):
        self.kwargs = None

    def create_chat_completion(self, **kwargs):
        self.kwargs = kwargs
        return {"choices": [{"message": {"content": "Test reply"}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 3, "completion_tokens": 2, "total_tokens": 5}}


class InferenceCheckpointTests(unittest.TestCase):
    def test_generation_parameters_and_tokens(self):
        llm = FakeModel()
        result = generate_one(llm, build_manifest([prompt()])[0], clock=lambda: 1.0)
        self.assertEqual(llm.kwargs["seed"], 101)
        self.assertEqual(llm.kwargs["max_tokens"], 400)
        self.assertEqual(llm.kwargs["temperature"], 0.1)
        self.assertEqual(result["response"], "Test reply")
        self.assertEqual(result["total_tokens"], 5)

    def test_resume_skips_completed(self):
        manifest = build_manifest([prompt()])
        calls = []
        def generate(row):
            calls.append(row["run_id"])
            return {"response": "mock"}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "checkpoint.csv"
            self.assertEqual(len(resume_runs(manifest, path, generate)), 3)
            self.assertEqual(len(resume_runs(manifest, path, generate)), 3)
            self.assertEqual(len(calls), 3)
            self.assertEqual(len(read_checkpoint(path)), 3)

    def test_failure_preserves_prior_success(self):
        manifest = build_manifest([prompt()])
        def generate(row):
            if row["run_number"] == 2:
                raise RuntimeError("simulated interruption")
            return {"response": "saved"}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "checkpoint.csv"
            with self.assertRaises(RuntimeError):
                resume_runs(manifest, path, generate)
            self.assertEqual([r["run_id"] for r in read_checkpoint(path)], ["P1-R1"])

    def test_duplicate_manifest_rejected(self):
        manifest = build_manifest([prompt()])
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(CheckpointError):
                resume_runs(manifest + manifest, Path(folder) / "out.csv", lambda _: {})


if __name__ == "__main__":
    unittest.main()
