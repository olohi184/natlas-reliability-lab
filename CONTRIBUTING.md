# Contributing to N-ATLaS Reliability Lab (NARL)

Thank you for your interest in improving NARL, an open-source toolkit for evaluating multilingual AI reliability in Nigerian deployment contexts.

## Ways to contribute

- Report reproducible bugs in CSV validation, reliability dashboards, documentation, or the independent inference workflow.
- Suggest improvements to evaluation methodology, accessibility, reproducibility, and support for Nigerian languages.
- Propose benchmark prompts or evaluation criteria with clear provenance, language labels, and intended use.
- Improve documentation, examples, and automated tests.

## Before opening an issue

Search existing issues first. For a bug, include:
1. The page or component affected and the steps to reproduce.
2. The expected and actual behaviour, including any error message.
3. Your browser, operating system, and relevant package versions, if known.
4. A minimal **non-sensitive** example CSV or prompt where possible.

Do not post API keys, access tokens, personal information, private datasets, or sensitive model outputs.

## Contributing code

1. Fork the repository and create a descriptively named branch.
2. Review the README and relevant examples before making changes.
3. Keep changes focused, and document any new configuration, input schema, or dependency.
4. Test affected workflows locally where possible; include clear steps to reproduce the test.
5. Open a pull request against `main` explaining the change, its motivation, and testing performed.
6. Respond to review feedback. Maintainers may request revisions before merging.

For changes to scoring logic or benchmark datasets, explain the methodology, provenance, assumptions, and any limitations. Clearly distinguish illustrative or synthetic data from empirical N-ATLaS responses and human-verified scores.

## Reliability and inference limitations

NARL's benchmark validation and dashboard workflows are distinct from live model inference. Hosted inference may be unavailable because of external GPU quotas or service limits. Contributors should not describe CSV validation as model inference, or AI-assisted ratings as independently verified human judgments. When proposing inference changes, document model provenance, compute requirements, failure handling, and reproducibility steps.

## Responsible contributions

Please be respectful and constructive. Avoid including copyrighted, private, or otherwise unauthorized datasets. Report security vulnerabilities privately to the repository maintainer rather than posting exploit details in a public issue.

## Licensing

By submitting a contribution, you agree that it may be distributed under this repository's [MIT License](LICENSE).

Thank you for helping make NARL more transparent, reproducible, and useful.
