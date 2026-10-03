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
# Header
# ---------------------------------------------------------

st.title("🧪 N-ATLAS Reliability Lab (NARL)")

st.subheader(
    "Testing Nigeria's sovereign AI for reliable multilingual deployment."
)

st.info(
    "NARL is an open-source developer toolkit for testing, benchmarking, "
    "and evaluating N-ATLAS across multilingual and real-world contexts."
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.title("NARL")

page = st.sidebar.radio(
    "Navigation",
    [
        "Evaluation Playground",
        "Benchmark Lab",
        "Reliability Dashboard",
        "About NARL",
    ],
)

st.sidebar.divider()

st.sidebar.caption("National AI Innovation Challenge 2026")
st.sidebar.caption("Developer Infrastructure")


# ---------------------------------------------------------
# Evaluation Playground
# ---------------------------------------------------------

if page == "Evaluation Playground":

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

    st.header("Reliability Dashboard")

    st.write(
        "Evaluation results and reliability indicators will appear "
        "here after genuine N-ATLAS tests have been completed."
    )

    metric1, metric2, metric3 = st.columns(3)

    metric1.metric("Evaluations", "0")
    metric2.metric("Languages Tested", "0")
    metric3.metric("Flagged Cases", "0")

    st.info(
        "No evaluation results are displayed yet because the "
        "N-ATLAS integration has not been activated."
    )


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
