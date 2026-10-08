"""Validation and descriptive summaries for NARL-60 AI-assisted evaluations."""
import pandas as pd

SCORES = ("task_completion_score", "language_fidelity_score",
          "clarity_coherence_score", "factual_appropriateness_score", "safety_score")
FLAGS = ("semantic_complete", "major_factual_error", "unsafe_advice_present")


def analyze(raw, evaluations):
    required_raw = {"run_id", "language", "finish_reason"}
    required_eval = {"run_id", "language", *SCORES, *FLAGS}
    for name, frame, required in (
        ("Raw responses", raw, required_raw),
        ("Unblinded evaluations", evaluations, required_eval),
    ):
        missing = required.difference(frame.columns)
        if missing:
            raise ValueError(f"{name} missing columns: {sorted(missing)}")
        if frame.empty or frame["run_id"].isna().any() or frame["run_id"].duplicated().any():
            raise ValueError(f"{name} has missing or duplicate run IDs")
    if set(raw.run_id) != set(evaluations.run_id):
        raise ValueError("Raw and evaluation run IDs do not match")
    merged = raw[["run_id", "language", "finish_reason"]].merge(
        evaluations[["run_id", "language", *SCORES, *FLAGS]],
        on="run_id", validate="one_to_one", suffixes=("_raw", "_eval"))
    if not merged.language_raw.astype(str).equals(merged.language_eval.astype(str)):
        raise ValueError("Language mismatch between raw and evaluated responses")
    merged["language"] = merged.language_raw
    for score in SCORES:
        values = pd.to_numeric(merged[score], errors="coerce")
        if values.isna().any() or not values.between(1, 3).all() or not values.mod(1).eq(0).all():
            raise ValueError(f"Invalid 1-3 evaluator score: {score}")
        merged[score] = values.astype(int)
    for flag in FLAGS:
        values = merged[flag].astype(str).str.strip().str.lower()
        mapping = {"true": 1, "false": 0, "1": 1, "0": 0, "yes": 1, "no": 0}
        if not values.isin(mapping).all():
            raise ValueError(f"Invalid binary flag: {flag}")
        merged[flag] = values.map(mapping).astype(int)
    merged["length_limit_stop"] = merged.finish_reason.astype(str).str.lower().eq("length").astype(int)
    summary = merged.groupby("language", as_index=False).agg(
        responses=("run_id", "size"),
        semantic_complete=("semantic_complete", "sum"),
        major_factual_error=("major_factual_error", "sum"),
        unsafe_advice=("unsafe_advice_present", "sum"),
        length_limit_stops=("length_limit_stop", "sum"))
    for field in ("semantic_complete", "major_factual_error", "unsafe_advice", "length_limit_stops"):
        summary[field + "_pct"] = (summary[field] / summary.responses * 100).round(1)
    means = merged.groupby("language")[list(SCORES)].mean().round(2)
    return merged, summary, means
