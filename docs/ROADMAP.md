# NARL Public Repository Roadmap

This roadmap describes the **public GitHub repository**, not all experimental work performed outside it.

| Capability | Status in this repository | Next verification step |
| --- | --- | --- |
| Streamlit evaluation playground UI | Implemented | Run interface locally |
| Language and domain selectors | Implemented | Verify UI behavior |
| Prompt entry and request preview | Implemented | Verify validation behavior |
| CSV upload widget | Implemented (upload only) | Validate dataset schema and errors |
| N-ATLAS model inference | Not integrated | Add authenticated adapter and mocked tests |
| Benchmark execution | Not integrated | Add deterministic runner and run manifest |
| Evaluation scoring | Not integrated | Define rubric, then implement scoring |
| Reliability dashboard with actual results | Not integrated | Load validated run outputs |
| Automated CI tests | Not yet configured | Add dependency-light smoke tests |
| Public benchmark datasets and logs | Not present in current root inventory | Audit provenance and publish approved artifacts |

## Suggested delivery sequence

1. Validate the current app's startup and dependency versions.
2. Add a typed benchmark CSV schema and sample synthetic records clearly labelled as examples.
3. Introduce an N-ATLAS integration adapter with credentials managed via environment variables or Streamlit secrets.
4. Add mock-backed unit tests and CI; verify no live inference is needed for tests.
5. Integrate genuine model responses and scoring only after confirming dataset permissions and rubric validity.
6. Replace placeholder dashboard values with traceable measured metrics.

**Release rule:** Do not mark a capability complete until its code, instructions and tests are present and verified in this repository.
