# N-ATLAS Reliability Lab (NARL)

**An open-source developer toolkit for benchmarking multilingual AI reliability in Nigerian deployment contexts.**

**Project Lead & Lead Developer:** Olohimai Juliet Michael  
**Professional background:** Principal Communication Engineer, NASRDA; PhD Researcher, African University of Science and Technology (AUST)  
**Programme:** National AI Innovation Challenge 2026 — Developer Infrastructure  
**License:** MIT  
**Project status:** Working evaluation and visualization toolkit; live N-ATLaS inference in the public Streamlit app is not yet connected.

## What NARL does

NARL helps developers inspect multilingual reliability rather than treating a generated answer as automatically correct. It supports documented, reproducible evaluation workflows and makes differences between Nigerian English, Hausa, Igbo and Yoruba visible.

### Implemented and testable

| Feature | What a reviewer can test |
| --- | --- |
| Challenge Overview | View a frozen aggregate snapshot of the NARL-60 experiment, including language-level semantic completion and generation-length stopping. No CSV upload required. |
| NARL-60 Automated Evaluation | Upload compatible raw model-response and AI-assisted evaluation CSVs, validate one-to-one run-ID linkage, and view language-level outcome and score summaries. |
| Truncation-adjusted results | Optionally upload the Stage 3G H3 results CSV for a separate display of adjusted findings. |
| Reliability Dashboard | Upload evaluator-scored Phase 2 CSVs (LF, IA, TQ, CA, SR; integer scores 0–4), inspect dimension means, flag low-score records and export a descriptive summary. |
| Evaluation Playground | Enter a language, domain and prompt to prepare an evaluation request; **no live N-ATLaS response is generated**. |
| Benchmark Lab | Upload a CSV to the interface; automated model execution is not yet enabled. |

The Challenge Overview summarizes **60 benchmark prompts, 180 model responses and four languages**. These are frozen results from the documented experiment, not live inference. AI-assisted semantic ratings and flags should not be interpreted as independently adjudicated human judgments. The snapshot is not a substitute for access to the original records and evaluation protocol.

## Quick start

Python 3.10+ recommended.

```bash
git clone https://github.com/olohi184/natlas-reliability-lab.git
cd natlas-reliability-lab
python -m pip install -r requirements.txt
streamlit run app.py
```

In the sidebar, select **Challenge Overview** to inspect results without files. For hands-on evaluation, use **Reliability Dashboard** with a scored CSV, or **NARL-60 Automated Evaluation** with matching experiment CSVs.

### Reviewer test: Phase 2 scored CSV

Create a file named `reviewer_phase2.csv` with these *illustrative input scores* (not empirical N-ATLaS results):

```csv
run_id,language,LF,IA,TQ,CA,SR
demo-001,Hausa,3,2,2,3,3
demo-002,Igbo,2,1,2,2,3
demo-003,Yoruba,3,2,1,2,3
demo-004,Nigerian English,4,4,3,4,4
```

1. Open **Reliability Dashboard**.
2. Upload `reviewer_phase2.csv`.
3. Confirm four rows are validated; inspect dimension averages and language comparison.
4. Change the low-score threshold to flag cases for review.
5. Download the descriptive summary CSV.

This example tests the software's CSV validation and aggregation; it does **not** validate the model or reproduce the NARL-60 experiment.

### Reviewer test: NARL-60 analysis

To reproduce the experiment-level analysis, obtain the compatible original response CSV and unblinded Stage 3F evaluation CSV from the project lead (subject to data-sharing permissions). Upload both files under **NARL-60 Automated Evaluation**. The application checks unique run IDs, matching sets and language alignment before reporting aggregates. Original responses and evaluation records are not included in the public repository.

## Research method and interpretation

- **NARL-60:** 60 prompts, 180 recorded N-ATLaS responses across Nigerian English, Hausa, Igbo and Yoruba (45 responses per language).
- **Semantic assessment:** AI-assisted evaluator scores (1–3) and separate completion, factual-error and safety flags.
- **Generation-length stopping:** Read from recorded model finish reasons; it may overlap with semantic incompleteness and does not independently establish causality.
- **Phase 2 dashboard:** A separate evaluator-scored protocol with LF, IA, TQ, CA and SR dimensions on a 0–4 scale. Do not combine these scales as if equivalent.
- **Adjusted analysis:** Stage 3G H3 results are displayed when uploaded; uploading them does not rerun the regression.

For technical details, see the [benchmark protocol](docs/BENCHMARK_PROTOCOL.md) and [scoring protocol](docs/SCORING_PROTOCOL.md).

## Repository structure

- `app.py` — Streamlit dashboard, upload workflows and frozen aggregate overview
- `narl/automated_evaluation.py` — NARL-60 record validation and descriptive aggregation
- `narl/scoring.py` — Phase 2 score validation and summarization
- `tests/` — automated software tests
- `docs/` — benchmark, scoring and project documentation
- `requirements.txt` — Python dependencies

## Known limitations and roadmap

- The public app does not yet send prompts to a live N-ATLaS endpoint. The historical Colab experiment and the public dashboard are separate execution paths.
- The original NARL-60 raw and evaluation CSVs are not publicly distributed here; therefore third parties cannot independently reproduce that exact experiment from the repository alone.
- AI-assisted judgments have not yet been independently validated by expert annotators.
- External beta testing and a reproducible live inference path are priorities before final submission.

## Attribution

**Olohimai Juliet Michael** — Project Lead & Lead Developer.  
[GitHub profile](https://github.com/olohi184) · [Professional portfolio](https://olohi184.github.io)

Contributions and acknowledgements should reflect confirmed participation and roles.
