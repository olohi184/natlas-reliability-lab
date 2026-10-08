"""Validation and loading of NARL benchmark CSV inputs (no model calls)."""
import csv
from pathlib import Path

REQUIRED_COLUMNS = ("item_id", "language", "domain", "prompt")


class BenchmarkValidationError(ValueError):
    """Benchmark CSV cannot be used safely for evaluation."""


def validate_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    if not rows:
        raise BenchmarkValidationError("Benchmark contains no records")
    seen = set()
    validated = []
    for number, row in enumerate(rows, start=2):
        missing = [field for field in REQUIRED_COLUMNS if not str(row.get(field) or "").strip()]
        if missing:
            raise BenchmarkValidationError(f"CSV row {number}: missing {', '.join(missing)}")
        item_id = row["item_id"].strip()
        if item_id in seen:
            raise BenchmarkValidationError(f"CSV row {number}: duplicate item_id {item_id!r}")
        seen.add(item_id)
        validated.append({field: row[field].strip() for field in REQUIRED_COLUMNS})
    return validated


def load_benchmark(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or any(field not in reader.fieldnames for field in REQUIRED_COLUMNS):
            raise BenchmarkValidationError("CSV must contain item_id, language, domain, prompt headers")
        try:
            return validate_rows(list(reader))
        except csv.Error as exc:
            raise BenchmarkValidationError("Unable to parse benchmark CSV") from exc
