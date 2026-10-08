"""Test original NARL-60 seed and manifest design without model calls."""
import unittest

from narl.manifest import ManifestError, build_manifest


def sample(code="NE", prompt_id="P001"):
    return {
        "prompt_id": prompt_id,
        "matched_task_id": "T001",
        "domain": "Education",
        "language_code": code,
        "language": "Nigerian English",
        "prompt": "Example test prompt",
    }


class ManifestTests(unittest.TestCase):
    def test_three_runs_and_original_parameters(self):
        rows = build_manifest([sample()])
        self.assertEqual([r["run_id"] for r in rows], ["P001-R1", "P001-R2", "P001-R3"])
        self.assertEqual([r["seed"] for r in rows], [101, 202, 303])
        self.assertEqual([r["temperature"] for r in rows], [0.1] * 3)
        self.assertTrue(all(r["max_tokens"] == 400 and r["n_ctx"] == 2048 for r in rows))

    def test_language_offsets(self):
        rows = build_manifest([sample("HA", "P1"), sample("YO", "P2"), sample("IG", "P3")])
        self.assertEqual([r["seed"] for r in rows[::3]], [111, 121, 131])

    def test_duplicate_prompt_rejected(self):
        with self.assertRaises(ManifestError):
            build_manifest([sample(), sample()])

    def test_unknown_language_rejected(self):
        with self.assertRaises(ManifestError):
            build_manifest([sample("XX")])

    def test_missing_field_rejected(self):
        row = sample()
        row["prompt"] = ""
        with self.assertRaises(ManifestError):
            build_manifest([row])


if __name__ == "__main__":
    unittest.main()
