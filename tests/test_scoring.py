import unittest

from narl.scoring import (
    ScoringError, summarize_phase2, validate_phase2_scores,
    validate_human_validation_scores,
)


class ScoringTests(unittest.TestCase):
    def test_valid_phase2(self):
        self.assertEqual(validate_phase2_scores(
            {"LF": "4", "IA": 3, "TQ": 2, "CA": 1, "SR": 0})["LF"], 4)

    def test_missing_dimension_rejected(self):
        with self.assertRaises(ScoringError):
            validate_phase2_scores({"LF": 4})

    def test_out_of_range_rejected(self):
        with self.assertRaises(ScoringError):
            validate_phase2_scores({"LF": 5, "IA": 3, "TQ": 2, "CA": 1, "SR": 0})

    def test_grouped_summary(self):
        records = [
            {"language": "HA", "LF": 4, "IA": 3, "TQ": 2, "CA": 1, "SR": 0},
            {"language": "HA", "LF": 2, "IA": 3, "TQ": 2, "CA": 1, "SR": 0},
        ]
        result = summarize_phase2(records, group_by="language")
        self.assertEqual(result[0]["n"], 2)
        self.assertEqual(result[0]["LF_mean"], 3)
        self.assertEqual(result[0]["dimension_sum_mean"], 9)

    def test_human_scale_separate(self):
        cols = ["a", "b", "c", "d", "e"]
        self.assertEqual(validate_human_validation_scores(dict.fromkeys(cols, 3), cols)["a"], 3)
        with self.assertRaises(ScoringError):
            validate_human_validation_scores(dict.fromkeys(cols, 4), cols)


if __name__ == "__main__":
    unittest.main()
