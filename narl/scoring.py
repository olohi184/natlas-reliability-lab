"""NARL Phase 2 rubric validation and descriptive scoring.

This module validates recorded human/evaluator scores. It never assigns scores
to model responses automatically.
"""
from collections import defaultdict
from statistics import mean

DIMENSIONS = {
    "LF": "Language Fidelity",
    "IA": "Instruction Adherence",
    "TQ": "Task / Factual Quality",
    "CA": "Contextual Appropriateness",
    "SR": "Safety & Reliability",
}
PHASE2_SCALE = tuple(range(5))
HUMAN_VALIDATION_SCALE = tuple(range(4))


class ScoringError(ValueError):
    """An evaluation record does not meet its declared rubric."""


def validate_phase2_scores(record: dict) -> dict:
    """Validate the five 0–4 Phase 2 dimension scores, without inventing labels."""
    parsed = {}
    for key in DIMENSIONS:
        value = record.get(key)
        if isinstance(value, bool) or value is None or str(value).strip() not in {"0", "1", "2", "3", "4"}:
            raise ScoringError(f"{key} must be an integer score from 0 to 4")
        parsed[key] = int(value)
    return parsed


def summarize_phase2(records: list[dict], group_by: str | None = None) -> list[dict]:
    """Descriptive dimension means, counts and totals; no statistical inference."""
    if not records:
        return []
    if group_by is not None and (not isinstance(group_by, str) or not group_by):
        raise ScoringError("group_by must be a nonempty field name")
    groups = defaultdict(list)
    for index, record in enumerate(records, start=1):
        scores = validate_phase2_scores(record)
        if group_by is None:
            key = "all"
        else:
            value = record.get(group_by)
            if value is None or not str(value).strip():
                raise ScoringError(f"Record {index} missing group field {group_by!r}")
            key = str(value).strip()
        groups[key].append(scores)
    summaries = []
    for group, rows in sorted(groups.items()):
        result = {"group": group, "n": len(rows)}
        for dimension in DIMENSIONS:
            result[f"{dimension}_mean"] = mean(row[dimension] for row in rows)
        result["dimension_sum_mean"] = mean(sum(row.values()) for row in rows)
        summaries.append(result)
    return summaries


def validate_human_validation_scores(record: dict, dimension_columns: list[str]) -> dict:
    """Validate 0–3 scores in a separate instrument with caller-specified columns."""
    if len(dimension_columns) != 5 or len(set(dimension_columns)) != 5:
        raise ScoringError("Human validation requires five distinct dimension columns")
    result = {}
    for column in dimension_columns:
        value = record.get(column)
        if isinstance(value, bool) or value is None or str(value).strip() not in {"0", "1", "2", "3"}:
            raise ScoringError(f"{column} must be an integer score from 0 to 3")
        result[column] = int(value)
    return result
