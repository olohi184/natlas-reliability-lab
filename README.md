# N-ATLAS Reliability Lab (NARL)

**A developer-oriented research toolkit for evaluating multilingual AI reliability in Nigerian deployment contexts.**

**Project lead:** Olohimai Juliet Michael · African University of Science and Technology (AUST), Abuja, Nigeria  
**Status:** Public Streamlit prototype; model integration and reproducible benchmark execution are not yet present in this repository.  
**Programme:** National AI Innovation Challenge 2026 — Academia & Research / Developer Infrastructure  
**License:** MIT

## Purpose

NARL aims to support repeatable evaluation of N-ATLAS across languages, application domains and reliability dimensions. It is designed to make failures visible rather than treating a model response as proof of correctness.

## What is implemented in this repository

- Streamlit navigation for an evaluation playground, benchmark lab, reliability dashboard and project information.
- Language selectors for Nigerian English, Hausa, Yoruba and Igbo, and domain selectors for several application contexts.
- Prompt entry and display of a timestamped evaluation request.
- CSV upload interface for future benchmark workflows.
- Placeholder dashboard indicators, currently displaying zero evaluations, languages and flagged cases.

**Important:** The current `app.py` does **not** call an N-ATLAS model, score uploaded benchmark records, save model outputs or generate actual reliability metrics. The interface explicitly informs users when no model response has been generated. The displayed zeros are placeholders, **not empirical evaluation results**.

## Planned or separately developed components

The research programme includes multilingual benchmark development, automated model inference, structured scoring, reliability analysis, recovery/safety checks and reporting. These components must be integrated, documented and validated in this public repository before they can be described as runnable features here. Work conducted in separate Colab notebooks or private environments is not automatically reproducible from this repository.

## Quick start — run the current interface

Requires Python 3.10+.

```bash
git clone https://github.com/olohi184/natlas-reliability-lab.git
cd natlas-reliability-lab
python -m pip install -r requirements.txt
streamlit run app.py
```

The interface can be explored without N-ATLAS credentials, but **it does not perform model inference**.

## Repository contents

- `app.py` — current Streamlit prototype
- `requirements.txt` — Python dependencies
- `docs/BENCHMARK_PROTOCOL.md` — benchmark documentation template and reproducibility checklist
- `docs/ROADMAP.md` — implemented versus planned features and verification milestones

## Evaluation principles

- Record model identifier/version, prompt, language, domain and timestamp for each actual run.
- Keep benchmark data, model outputs and human/automated scores distinct.
- Report sample sizes and uncertainty; do not treat placeholder dashboard values as measurements.
- Document scoring criteria, annotator or evaluator procedures, failure categories and known limitations.
- Avoid sharing credentials, private user data or unlicensed benchmark material.

## Team and attribution

**Project lead:** Olohimai Juliet Michael (AUST, Abuja). Additional collaborators and advisors should be credited in future updates with confirmed roles and permissions.

## Disclaimer

NARL is an independent evaluation research project. Any future reported findings will apply only to the documented datasets, tested model versions, scoring procedures and deployment contexts. The public prototype currently contains **no verified N-ATLAS evaluation results**.

[GitHub profile](https://github.com/olohi184) · [Professional portfolio](https://olohi184.github.io)
