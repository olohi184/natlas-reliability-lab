# NARL Benchmark Protocol — documentation template

**Status:** Protocol outline. This file does not claim that the public repository includes completed N-ATLAS benchmark runs.

## 1. Evaluation objective

Measure and describe multilingual model reliability in specified Nigerian-language and domain contexts. Define each reliability dimension operationally before reporting a score.

## 2. Benchmark manifest (complete before publication)

For each dataset or subset, record:

| Field | Required information |
| --- | --- |
| Dataset name/version | Stable identifier and release |
| Origin and license | Provenance and redistribution permissions |
| Language | Nigerian English, Hausa, Yoruba, Igbo or other clearly defined variant |
| Domain/task | E.g., education, agriculture or general reasoning |
| Number of items | Actual validated count |
| Ground truth | Source and validation method, where applicable |
| Splits | Development, test and held-out partitions, if used |
| Limitations | Coverage, ambiguity, representativeness and known gaps |

## 3. Model run manifest

Record the exact N-ATLAS endpoint or local model identifier, model revision, inference parameters, prompt template, environment, timestamp, and any filtering or retry policy. Store secrets outside the repository.

## 4. Example evaluation record schema

`item_id,language,domain,prompt,model_id,model_version,response,timestamp,evaluator_id,score,flag,notes`

This is a proposed schema, **not evidence that such records exist in the public repository**. Document score ranges and evaluation rubrics before using the `score` field.

## 5. Scoring and quality assurance

- Define objective task metrics and human rating rubrics separately.
- Report inter-rater agreement when multiple human validators are used.
- Distinguish refusals, invalid outputs, factual errors, harmful content and language-quality failures.
- Check duplicates, missing fields and inconsistent labels before analysis.
- Preserve raw outputs and provenance; do not silently overwrite failed runs.

## 6. Reporting

Publish the tested sample size, per-language results, failure counts, model version, scoring methodology, confidence/uncertainty where appropriate, and limitations. Avoid interpreting sparse or unvalidated samples as population-wide performance.

## 7. Reproducibility checklist

- [ ] Benchmark data or access instructions committed with license information
- [ ] Executable inference runner and configuration documented
- [ ] Example output schema validated
- [ ] Scoring script and rubric published
- [ ] Test results verified on a fresh environment
- [ ] Dashboard connected to genuine evaluation outputs
- [ ] Model and data version identifiers included in reports
