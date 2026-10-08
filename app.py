import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# N-ATLAS Reliability Lab (NARL)
# National AI Innovation Challenge 2026
# Developer Infrastructure Track
# ---------------------------------------------------------

st.set_page_config(
    page_title="N-ATLAS Reliability Lab",
    page_icon="🧪",
    layout="wide",
)

# ---------------------------------------------------------
# Research dashboard design system
# ---------------------------------------------------------
st.markdown("""
<style>
:root { --narl-navy:#10233f; --narl-teal:#087f8c; }
.block-container { padding-top:1.8rem; padding-bottom:3rem; max-width:1320px; }
section[data-testid="stSidebar"] { background:linear-gradient(180deg,#10233f,#193958); }
section[data-testid="stSidebar"] * { color:#f3f7fb !important; }
section[data-testid="stSidebar"] [data-testid="stRadio"] label { border-radius:8px; }
.narl-hero {
  background:linear-gradient(110deg,#10233f 0%,#174666 72%,#087f8c 100%);
  padding:2rem 2.2rem; border-radius:18px; color:white;
  box-shadow:0 10px 30px rgba(16,35,63,.14); margin-bottom:1.2rem;
}
.narl-eyebrow { color:#b7e5e4; font-size:.78rem; font-weight:700;
  letter-spacing:.13em; text-transform:uppercase; margin-bottom:.65rem; }
.narl-hero h1 { color:#fff; font-size:2.1rem; margin:0 0 .55rem 0; }
.narl-hero p { color:#e2eff5; font-size:1rem; max-width:780px; margin:0; }
.narl-pill { display:inline-block; background:rgba(255,255,255,.13);
  border:1px solid rgba(255,255,255,.24); border-radius:50px;
  padding:.32rem .7rem; margin:.9rem .35rem 0 0; font-size:.8rem; color:#fff; }
div[data-testid="stMetric"] { background:rgba(123,156,175,.07);
  border:1px solid rgba(123,156,175,.22); border-radius:12px; padding:1rem; }
div[data-testid="stFileUploader"] { border-radius:12px; }
h2,h3 { letter-spacing:-.025em; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narl-hero">
  <div class="narl-eyebrow">National AI Innovation Challenge 2026 · Developer Infrastructure</div>
  <h1>N-ATLAS Reliability Lab</h1>
  <p>Evidence-led benchmarking for trustworthy, multilingual AI deployment in Nigeria.</p>
  <span class="narl-pill">NARL-60 Benchmark</span>
  <span class="narl-pill">Four Languages</span>
  <span class="narl-pill">Reliability &amp; Safety Analysis</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.title("🧪 NARL")
st.sidebar.caption("Multilingual AI Reliability Lab")

page = st.sidebar.radio(
    "Navigation",
    [
        "Challenge Overview",
        "NARL-60 Automated Evaluation",
        "Reliability Dashboard",
        "Benchmark Lab",
        "Evaluation Playground",
        "About NARL",
    ],
)

st.sidebar.divider()

st.sidebar.caption("National AI Innovation Challenge 2026")
st.sidebar.caption("Developer Infrastructure")


# ---------------------------------------------------------
# Challenge overview: verified frozen aggregate snapshot
# ---------------------------------------------------------
if page == "Challenge Overview":
    import pandas as pd
    import plotly.express as px

    st.header("Challenge Overview")
    st.write(
        "A developer toolkit for identifying multilingual reliability gaps "
        "in N-ATLaS. This public demonstration shows a **frozen aggregate "
        "snapshot** of the NARL-60 experiment; no raw prompts or model "
        "responses are published on this page."
    )
    st.caption(
        "Source: NARL-60 original 180-response experiment and Stage 3F "
        "unblinded AI-assisted semantic evaluations. Not live inference."
    )
    a, b, c, d = st.columns(4)
    a.metric("Benchmark prompts", "60")
    b.metric("Model responses", "180")
    c.metric("Languages tested", "4")
    d.metric("AI-judged complete", "79 / 180")

    snapshot = pd.DataFrame([
        {"Language": "Nigerian English", "Responses": 45, "Complete": 42,
         "Length-limit stops": 3, "Factual-error flags": 2, "Unsafe-advice flags": 1},
        {"Language": "Hausa", "Responses": 45, "Complete": 19,
         "Length-limit stops": 27, "Factual-error flags": 3, "Unsafe-advice flags": 1},
        {"Language": "Igbo", "Responses": 45, "Complete": 12,
         "Length-limit stops": 30, "Factual-error flags": 6, "Unsafe-advice flags": 3},
        {"Language": "Yoruba", "Responses": 45, "Complete": 6,
         "Length-limit stops": 35, "Factual-error flags": 8, "Unsafe-advice flags": 3},
    ])
    snapshot["Semantic completion (%)"] = (
        snapshot["Complete"] / snapshot["Responses"] * 100
    ).round(1)
    snapshot["Length-limit stops (%)"] = (
        snapshot["Length-limit stops"] / snapshot["Responses"] * 100
    ).round(1)

    st.subheader("Multilingual reliability snapshot")
    comparison = snapshot.melt(
        id_vars="Language",
        value_vars=["Semantic completion (%)", "Length-limit stops (%)"],
        var_name="Indicator", value_name="Percent",
    )
    fig = px.bar(
        comparison, x="Language", y="Percent", color="Indicator",
        barmode="group", text_auto=".1f",
        color_discrete_map={
            "Semantic completion (%)": "#087f8c",
            "Length-limit stops (%)": "#e6a34a",
        },
    )
    fig.update_yaxes(range=[0, 105], title="Percentage of responses")
    fig.update_layout(
        legend_title_text="", plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=20, b=10),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption(
        "Each language has 45 responses. These indicators can overlap: "
        "a generation-length stop is not proof of semantic incompleteness."
    )

    with st.expander("View complete aggregate results"):
        st.dataframe(snapshot, use_container_width=True, hide_index=True)
        st.caption(
            "Factual-error and unsafe-advice flags are AI-evaluator judgments, "
            "not independently adjudicated errors."
        )

    st.subheader("What the benchmark demonstrates")
    left, right = st.columns(2)
    with left:
        st.markdown(
            "**Cross-language visibility**\\n\\n"
            "NARL surfaces substantial differences in AI-judged completion "
            "across Nigerian English, Hausa, Igbo and Yoruba."
        )
    with right:
        st.markdown(
            "**Reliability diagnostics**\\n\\n"
            "NARL separates semantic evaluation from generation-length "
            "stopping behaviour and provides reproducible analysis workflows."
        )

    st.subheader("Research contributions")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown(
            "**Multilingual benchmarking**\\n\\n"
            "A structured 60-prompt benchmark and 180 recorded responses "
            "covering Nigerian English, Hausa, Igbo and Yoruba."
        )
    with p2:
        st.markdown(
            "**Reproducible evaluation**\\n\\n"
            "Run-ID linkage, score validation and documented AI-assisted "
            "semantic evaluation enable traceable comparisons."
        )
    with p3:
        st.markdown(
            "**Reliability diagnostics**\\n\\n"
            "Language-level completion, error flags and generation-length "
            "analyses help identify deployment risks for further study."
        )

    st.divider()
    st.subheader("Project leadership")
    st.markdown("**Olohimai Juliet Michael**")
    st.write("Project Lead & Lead Developer · N-ATLAS Reliability Lab (NARL)")
    st.caption(
        "Principal Communication Engineer, NASRDA · PhD Researcher, "
        "African University of Science and Technology (AUST). "
        "Affiliations are provided for identification and do not imply "
        "institutional endorsement."
    )
    st.markdown(
        "[GitHub profile](https://github.com/olohi184) · "
        "[Project repository](https://github.com/olohi184/natlas-reliability-lab)"
    )

    st.subheader("Explore the toolkit")
    st.write(
        "Use **NARL-60 Automated Evaluation** in the sidebar to load your "
        "own original and unblinded CSVs, verify run-ID matches, inspect "
        "score dimensions and upload truncation-adjusted estimates."
    )
    st.link_button(
        "View source code and documentation",
        "https://github.com/olohi184/natlas-reliability-lab",
    )
    st.caption(
        "Methodological scope: the semantic ratings are AI-assisted; "
        "independent expert validation is a future extension. "
        "The Evaluation Playground does not yet perform live N-ATLaS inference."
    )


# ---------------------------------------------------------
# Evaluation Playground
# ---------------------------------------------------------

elif page == "Evaluation Playground":

    st.header("N-ATLAS Evaluation Playground")

    st.write(
        "Test prompts and prepare structured evaluations of N-ATLAS responses."
    )

    col1, col2 = st.columns(2)

    with col1:
        language = st.selectbox(
            "Language",
            [
                "Nigerian English",
                "Hausa",
                "Yoruba",
                "Igbo",
            ],
        )

    with col2:
        domain = st.selectbox(
            "Evaluation Domain",
            [
                "General",
                "Education",
                "Agriculture",
                "Healthcare",
                "Financial Literacy",
                "Legal Rights",
                "Technology",
            ],
        )

    prompt = st.text_area(
        "Enter a test prompt",
        height=160,
        placeholder="Enter the prompt you want to evaluate with N-ATLAS...",
    )

    st.caption(
        "N-ATLAS model connectivity will be enabled through the "
        "official integration layer."
    )

    if st.button("Run N-ATLAS Evaluation", type="primary"):

        if not prompt.strip():
            st.warning("Please enter a prompt before running an evaluation.")

        else:
            st.warning(
                "N-ATLAS is not connected yet. "
                "No model response has been generated."
            )

            st.write("### Evaluation Request")

            st.write(f"**Language:** {language}")
            st.write(f"**Domain:** {domain}")
            st.write(f"**Prompt:** {prompt}")

            st.write(
                f"**Timestamp:** "
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )


# ---------------------------------------------------------
# Benchmark Lab
# ---------------------------------------------------------

elif page == "Benchmark Lab":

    st.header("Benchmark Lab")

    st.write(
        "Run structured benchmark datasets through N-ATLAS and "
        "compare model behaviour across languages and domains."
    )

    uploaded_file = st.file_uploader(
        "Upload benchmark dataset",
        type=["csv"],
    )

    if uploaded_file is not None:
        st.success(
            "Benchmark file received. Automated benchmark execution "
            "will be enabled after N-ATLAS integration."
        )


# ---------------------------------------------------------
# Reliability Dashboard
# ---------------------------------------------------------

elif page == "Reliability Dashboard":

    import io
    import pandas as pd
    from narl.scoring import DIMENSIONS, ScoringError, summarize_phase2, validate_phase2_scores

    st.header("Reliability Dashboard")
    st.write(
        "Explore **uploaded, evaluator-scored Phase 2 results**. "
        "The five dimensions use a 0–4 scale. This dashboard does not "
        "call N-ATLaS or score model responses automatically."
    )

    scored_file = st.file_uploader(
        "Upload Phase 2 scored evaluation CSV",
        type=["csv"],
        key="phase2_scored_upload",
        help="Required columns: LF, IA, TQ, CA, SR. "
             "Optional: language, domain, prompt_id, run_id.",
    )

    if scored_file is None:
        st.info(
            "No scored evaluation file uploaded. Results shown here will come "
            "only from your uploaded CSV, not synthetic examples."
        )
        st.caption(
            "CSV columns: LF, IA, TQ, CA, SR (integer scores 0–4). "
            "Add a language column to compare languages."
        )
    else:
        try:
            if scored_file.size > 5 * 1024 * 1024:
                raise ValueError("CSV exceeds the 5 MB upload limit for this dashboard.")
            frame = pd.read_csv(scored_file, dtype=str, keep_default_na=False)
            if frame.empty:
                raise ValueError("The uploaded CSV has no data rows.")
            if len(frame) > 10000:
                raise ValueError("Upload at most 10,000 evaluation rows at a time.")
            if frame.columns.duplicated().any():
                raise ValueError("Duplicate CSV column names are not supported.")
            records = frame.to_dict(orient="records")
            for index, record in enumerate(records, start=2):
                try:
                    validate_phase2_scores(record)
                except ScoringError as error:
                    raise ValueError(f"Row {index}: {error}") from error
        except (ValueError, pd.errors.ParserError, UnicodeError) as error:
            st.error(f"Could not validate this evaluation CSV: {error}")
        else:
            st.success(f"Validated {len(records)} evaluator-scored rows.")
            st.caption(
                "Source: user-uploaded evaluation CSV. Values are descriptive, "
                "not independent evidence of model reliability."
            )
            score_frame = frame.copy()
            for code in DIMENSIONS:
                score_frame[code] = score_frame[code].astype(int)
            score_frame["dimension_sum"] = score_frame[list(DIMENSIONS)].sum(axis=1)
            low_score_threshold = st.slider(
                "Flag rows where any dimension is at or below",
                min_value=0, max_value=3, value=1,
            )
            flagged = score_frame[
                score_frame[list(DIMENSIONS)].le(low_score_threshold).any(axis=1)
            ]
            m1, m2, m3 = st.columns(3)
            m1.metric("Scored rows", len(score_frame))
            m2.metric(
                "Languages represented",
                score_frame["language"].replace("", pd.NA).nunique()
                if "language" in score_frame else "Not provided",
            )
            m3.metric("Flagged rows", len(flagged))

            overall = summarize_phase2(records)[0]
            st.subheader("Average scores by dimension (0–4)")
            dimension_means = pd.DataFrame({
                "Dimension": [DIMENSIONS[key] for key in DIMENSIONS],
                "Mean score": [overall[f"{key}_mean"] for key in DIMENSIONS],
            }).set_index("Dimension")
            st.bar_chart(dimension_means)

            if "language" in score_frame and score_frame["language"].str.strip().ne("").all():
                st.subheader("Language comparison")
                language_summaries = summarize_phase2(records, group_by="language")
                comparison = pd.DataFrame(language_summaries).rename(
                    columns={"group": "Language", "n": "Scored rows"}
                )
                st.dataframe(comparison, use_container_width=True, hide_index=True)
            elif "language" in score_frame:
                st.warning("Some language values are blank; language comparison is unavailable.")

            st.subheader("Flagged cases for human review")
            if flagged.empty:
                st.info("No rows meet the selected low-score threshold.")
            else:
                display_columns = [
                    col for col in ("prompt_id", "run_id", "language", "domain", *DIMENSIONS)
                    if col in flagged.columns
                ]
                st.dataframe(
                    flagged[display_columns],
                    use_container_width=True,
                    hide_index=True,
                )
            st.caption(
                "A flagged case means at least one recorded dimension score "
                "is at or below the selected threshold. It is not an automated "
                "judgment about safety or correctness."
            )

            st.subheader("Export descriptive summary")
            summary = pd.DataFrame([
                {"group": "all", **overall},
            ])
            st.download_button(
                "Download summary CSV",
                data=summary.to_csv(index=False).encode("utf-8-sig"),
                file_name="narl_phase2_descriptive_summary.csv",
                mime="text/csv",
            )
            st.caption(
                "Do not upload sensitive, confidential or unpublished research "
                "data to a public demo without permission."
            )



elif page == "NARL-60 Automated Evaluation":
    import pandas as pd
    from narl.automated_evaluation import analyze

    st.header("NARL-60 · Multilingual Reliability Observatory")
    st.write(
        "Explore verified N-ATLaS experiment records and language-level reliability "
        "patterns. Upload the original response and unblinded evaluation CSVs to begin."
    )
    st.caption(
        "Evidence scope: AI-assisted semantic evaluation on a 1–3 scale. "
        "Independent expert validation is a future extension."
    )
    st.markdown("#### Load your experiment")
    raw_file = st.file_uploader(
        "Upload NARL60_NATLAS_RAW_180_FINAL.csv",
        type="csv", key="narl60_raw"
    )
    evaluation_file = st.file_uploader(
        "Upload NARL60_stage3F_unblinded_semantic_evaluation.csv",
        type="csv", key="narl60_evaluated"
    )
    st.caption("Uploads are processed in the current session and are not committed to GitHub.")
    if raw_file is not None and evaluation_file is not None:
        try:
            if raw_file.size > 5_000_000 or evaluation_file.size > 5_000_000:
                raise ValueError("Each file must be smaller than 5 MB")
            raw = pd.read_csv(raw_file)
            evaluated = pd.read_csv(evaluation_file)
            if len(raw) > 10000 or len(evaluated) > 10000:
                raise ValueError("Maximum 10,000 rows per file")
            matched, summary, score_means = analyze(raw, evaluated)
        except (ValueError, pd.errors.ParserError, UnicodeError) as exc:
            st.error(f"Could not analyse the uploaded files: {exc}")
        else:
            st.success(f"Verified {len(matched)} matching model-response records.")
            k1, k2, k3, k4 = st.columns(4)
            k1.metric("Responses analysed", len(matched))
            k2.metric("Languages", summary.shape[0])
            k3.metric("AI-judged complete", int(matched["semantic_complete"].sum()))
            k4.metric("Length-limit stops", int(matched["length_limit_stop"].sum()))
            st.divider()
            st.subheader("Outcomes by language")
            st.dataframe(summary, use_container_width=True, hide_index=True)
            import plotly.express as px
            comparison = summary.melt(
                id_vars="language",
                value_vars=["semantic_complete_pct", "length_limit_stops_pct"],
                var_name="Outcome", value_name="Percentage",
            )
            comparison["Outcome"] = comparison["Outcome"].replace({
                "semantic_complete_pct": "AI-judged semantic completion",
                "length_limit_stops_pct": "Generation length-limit stop",
            })
            fig = px.bar(
                comparison, x="language", y="Percentage", color="Outcome",
                barmode="group", labels={"language": "Language"},
            )
            fig.update_yaxes(range=[0, 100])
            st.plotly_chart(fig, use_container_width=True)
            st.subheader("Quality dimensions · AI-evaluator scores (1–3)")
            st.dataframe(score_means, use_container_width=True)
            st.caption(
                "Completion and length-limit stops are separate, potentially overlapping "
                "outcomes. These descriptive charts do not establish causality."
            )
            st.subheader("Truncation-adjusted findings (Stage 3G H3)")
            adjusted_file = st.file_uploader(
                "Optional: upload NARL60_stage3G_H3_adjusted_truncation_results.csv",
                type="csv", key="narl60_adjusted",
            )
            if adjusted_file is not None:
                try:
                    if adjusted_file.size > 5_000_000:
                        raise ValueError("Adjusted results file must be smaller than 5 MB")
                    adjusted = pd.read_csv(adjusted_file)
                    required = {
                        "outcome", "coefficient_truncation", "ci95_low",
                        "ci95_high", "holm_p_value", "holm_reject",
                    }
                    if adjusted.empty or not required.issubset(adjusted.columns):
                        raise ValueError("The uploaded file is missing required Stage 3G H3 columns")
                    for field in ("coefficient_truncation", "ci95_low", "ci95_high", "holm_p_value"):
                        adjusted[field] = pd.to_numeric(adjusted[field], errors="raise")
                    if adjusted[list(required - {"outcome", "holm_reject"})].isna().any().any():
                        raise ValueError("Missing regression estimates")
                    significance = adjusted["holm_reject"].astype(str).str.lower()
                    if not significance.isin(["true", "false"]).all():
                        raise ValueError("Invalid Holm correction significance flags")
                    adjusted["Holm significant"] = significance.eq("true")
                except (ValueError, pd.errors.ParserError, UnicodeError) as exc:
                    st.error(f"Cannot read truncation results: {exc}")
                else:
                    shown = adjusted[[
                        "outcome", "coefficient_truncation", "ci95_low",
                        "ci95_high", "holm_p_value", "Holm significant",
                    ]].rename(columns={
                        "outcome": "Evaluation dimension",
                        "coefficient_truncation": "Truncation coefficient",
                        "ci95_low": "95% CI lower",
                        "ci95_high": "95% CI upper",
                        "holm_p_value": "Holm-adjusted p",
                    })
                    st.dataframe(shown, use_container_width=True, hide_index=True)
                    st.caption(
                        "Uploaded historical regression results; not recomputed here. "
                        "A negative coefficient indicates association with lower evaluator "
                        "scores under the original model specification, not causation."
                    )
                    st.download_button(
                        "Download adjusted-results table",
                        shown.to_csv(index=False).encode("utf-8-sig"),
                        file_name="narl60_truncation_adjusted_summary.csv",
                        mime="text/csv",
                    )
            else:
                st.caption(
                    "Upload the Stage 3G H3 CSV to view existing truncation-adjusted "
                    "coefficients, confidence intervals and Holm-corrected significance."
                )

            st.download_button(
                "Download language summary CSV",
                summary.to_csv(index=False).encode("utf-8-sig"),
                file_name="narl60_language_summary.csv",
                mime="text/csv",
            )
    else:
        st.info("Upload the two matching NARL-60 CSV files to view real results.")


# ---------------------------------------------------------
# About
# ---------------------------------------------------------

elif page == "About NARL":

    st.header("About NARL")

    st.write(
        """
        N-ATLAS Reliability Lab (NARL) is an open-source developer
        infrastructure project for evaluating the reliability of
        Nigeria's N-ATLAS multilingual AI model.

        NARL is designed to help developers and researchers conduct
        structured tests, run multilingual benchmarks, identify
        potential failure cases, and document model behaviour before
        deployment.
        """
    )

    st.subheader("Project Lead")

    st.write(
        "Olohimai Juliet Michael — "
        "African University of Science and Technology (AUST), Abuja."
    )

    st.subheader("Project Status")

    st.warning("In active development — N-ATLAS integration pending.")
