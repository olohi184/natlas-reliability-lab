"""Dependency-free benchmark validation tests."""
import csv
import tempfile
import unittest
from pathlib import Path

from narl.benchmark import BenchmarkValidationError, load_benchmark, validate_rows


class BenchmarkTests(unittest.TestCase):
    def test_valid_record(self):
        rows = [{"item_id": "1", "language": "Hausa", "domain": "General", "prompt": "Example prompt"}]
        self.assertEqual(validate_rows(rows)[0]["language"], "Hausa")

    def test_missing_prompt(self):
        with self.assertRaises(BenchmarkValidationError):
            validate_rows([{"item_id": "1", "language": "Igbo", "domain": "General", "prompt": ""}])

    def test_duplicate_id(self):
        rows = [{"item_id": "1", "language": "Yoruba", "domain": "General", "prompt": "A"}] * 2
        with self.assertRaises(BenchmarkValidationError):
            validate_rows(rows)

    def test_csv_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "benchmark.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=["item_id", "language", "domain", "prompt"])
                writer.writeheader()
                writer.writerow({"item_id": "demo-1", "language": "Nigerian English", "domain": "Education", "prompt": "Example"})
            self.assertEqual(load_benchmark(path)[0]["item_id"], "demo-1")


if __name__ == "__main__":
    unittest.main()
