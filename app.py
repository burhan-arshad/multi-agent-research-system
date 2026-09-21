import streamlit as st
from pipeline import run_search_pipeline


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ResearchAI",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ================= APP ================= */

    .stApp {
        background: #070a11;
        color: #e5e7eb;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 5rem;
    }


    /* ================= SIDEBAR ================= */

    section[data-testid="stSidebar"] {
        background: #090c13;
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    .sidebar-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 5px;
    }

    .sidebar-text {
        color: #64748b;
        font-size: 0.82rem;
        line-height: 1.6;
    }

    .sidebar-heading {
        color: #94a3b8;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 28px;
        margin-bottom: 10px;
    }


    /* ================= HERO ================= */

    .hero {
        text-align: center;
        padding: 35px 0 20px 0;
    }

    .hero-badge {
        color: #a5b4fc;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    .hero-title {
        color: #f8fafc;
        font-size: 3.4rem;
        line-height: 1.05;
        font-weight: 800;
        letter-spacing: -0.05em;
        margin-bottom: 18px;
    }

    .hero-accent {
        color: #818cf8;
    }

    .hero-description {
        max-width: 720px;
        margin: auto;
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.7;
    }


    /* ================= SEARCH ================= */

    .search-container {
        background: #0b1019;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 16px;
        padding: 22px;
        margin-top: 35px;
    }

    .search-label {
        color: #e2e8f0;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 8px;
    }

    div[data-testid="stTextInput"] input {
        background: #080c14 !important;
        color: #f8fafc !important;
        border: 1px solid #263044 !important;
        border-radius: 10px !important;
        height: 50px !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 1px #6366f1 !important;
    }

    div.stButton > button {
        height: 50px;
        border-radius: 10px;
        background: #4f46e5;
        border: none;
        color: white;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #4338ca;
    }


    /* ================= SECTION ================= */

    .section-heading {
        color: #f8fafc;
        font-size: 1.2rem;
        font-weight: 750;
        margin-top: 42px;
        margin-bottom: 16px;
    }


    /* ================= CARDS ================= */

    .card {
        background: #0b1019;
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 20px;
        height: 100%;
    }

    .card-title {
        color: #f1f5f9;
        font-weight: 700;
        font-size: 0.92rem;
        margin-bottom: 7px;
    }

    .card-text {
        color: #64748b;
        font-size: 0.8rem;
        line-height: 1.6;
    }

    .step-number {
        color: #818cf8;
        font-size: 0.8rem;
        font-weight: 800;
        margin-bottom: 10px;
    }


    /* ================= RESULT ================= */

    .result-heading {
        color: #f8fafc;
        font-size: 1.55rem;
        font-weight: 750;
        margin-top: 45px;
        margin-bottom: 5px;
    }

    .result-subtitle {
        color: #64748b;
        font-size: 0.8rem;
        margin-bottom: 18px;
    }


    /* ================= REPORT ================= */

    .report {
        background: #0b1019;
        border: 1px solid rgba(99,102,241,0.18);
        border-radius: 16px;
        padding: 28px;
    }


    /* ================= FOOTER ================= */

    .footer {
        text-align: center;
        color: #475569;
        font-size: 0.72rem;
        margin-top: 70px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.05);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">ResearchAI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-text">
            A multi-agent research workspace for discovering,
            reading and analyzing current information.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-heading">Workflow</div>',
        unsafe_allow_html=True,
    )

    st.write("01  News Discovery")
    st.write("02  Article Extraction")
    st.write("03  Report Generation")
    st.write("04  AI Critique")

    st.markdown(
        '<div class="sidebar-heading">Technology</div>',
        unsafe_allow_html=True,
    )

    st.write("Groq")
    st.write("LangChain")
    st.write("Tavily")
    st.write("BeautifulSoup")
    st.write("Streamlit")

    st.markdown(
        '<div class="sidebar-heading">About</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-text">
            ResearchAI uses multiple specialized AI components.
            Sources are discovered, article content is processed,
            a report is generated and a separate critic reviews it.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="hero">',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-badge">MULTI-AGENT RESEARCH SYSTEM</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-title">
        Research smarter.<br>
        <span class="hero-accent">Understand deeper.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-description">
        Ask a research question and let a coordinated AI pipeline
        discover recent information, extract article content,
        write a structured report and critically review the result.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# =========================================================
# SEARCH
# =========================================================

st.markdown(
    '<div class="search-container">',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="search-label">Research topic</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns([5, 1])

with col1:

    topic = st.text_input(
        "Research topic",
        placeholder="Example: What is the current petrol subsidy situation in Pakistan?",
        label_visibility="collapsed",
    )

with col2:

    search = st.button(
        "Start Research",
        use_container_width=True,
    )

st.caption(
    "Research involving current information may take some time "
    "because the system uses external APIs and multiple AI stages."
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# =========================================================
# WORKFLOW
# =========================================================

st.markdown(
    '<div class="section-heading">How ResearchAI works</div>',
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="step-number">01</div>
            <div class="card-title">Discover</div>
            <div class="card-text">
                Finds recent sources related to your question.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="step-number">02</div>
            <div class="card-title">Extract</div>
            <div class="card-text">
                Processes relevant article pages and extracts content.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="step-number">03</div>
            <div class="card-title">Write</div>
            <div class="card-text">
                Turns the collected research into a structured report.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        """
        <div class="card">
            <div class="step-number">04</div>
            <div class="card-title">Critique</div>
            <div class="card-text">
                Reviews the report and identifies weaknesses or gaps.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# WHAT YOU GET
# =========================================================

st.markdown(
    '<div class="section-heading">What you get</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        """
        <div class="card">
            <div class="card-title">
                Recent Information
            </div>
            <div class="card-text">
                Tavily searches the web for recent information
                relevant to your research question.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:

    st.markdown(
        """
        <div class="card">
            <div class="card-title">
                Source Processing
            </div>
            <div class="card-text">
                Relevant pages are processed so the system can
                work with article content instead of search
                snippets alone.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:

    st.markdown(
        """
        <div class="card">
            <div class="card-title">
                Independent Review
            </div>
            <div class="card-text">
                A separate critic examines the generated report
                for weaknesses and missing information.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# RESEARCH
# =========================================================

if search:

    if not topic.strip():

        st.warning("Please enter a research topic first.")

    else:

        st.markdown(
            '<div class="result-heading">Research in progress</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="result-subtitle">
                This may take a little while. The pipeline is
                contacting external services and processing
                several AI stages.
            </div>
            """,
            unsafe_allow_html=True,
        )

        progress = st.progress(5)

        status = st.empty()

        status.info(
            "Researching: discovering sources, processing articles, "
            "writing the report and running the critique..."
        )

        try:

            progress.progress(15)

            result = run_search_pipeline(topic)

            progress.progress(100)

            status.success("Research completed.")

            # =============================================
            # REPORT
            # =============================================

            st.markdown(
                '<div class="result-heading">Research Report</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <div class="result-subtitle">
                    Generated from the collected research material.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="report">',
                unsafe_allow_html=True,
            )

            st.markdown(result["written_report"])

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

            # =============================================
            # CRITIQUE
            # =============================================

            st.markdown(
                '<div class="result-heading">AI Critique</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <div class="result-subtitle">
                    Independent review of the generated report.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.info(result["critique"])

            # =============================================
            # EVIDENCE
            # =============================================

            st.markdown(
                '<div class="result-heading">Research Evidence</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <div class="result-subtitle">
                    Information collected during the research process.
                </div>
                """,
                unsafe_allow_html=True,
            )

            with st.expander("Discovered sources"):

                st.markdown(
                    result["news_result"]
                )

            with st.expander("Extracted article content"):

                st.markdown(
                    result["scraped_content"]
                )

            # =============================================
            # DOWNLOAD
            # =============================================

            report_text = f"""
ResearchAI Report

Research Topic
--------------
{topic}

Research Report
---------------
{result["written_report"]}

AI Critique
-----------
{result["critique"]}
"""

            st.download_button(
                "Download Research Report",
                data=report_text,
                file_name="researchai_report.txt",
                mime="text/plain",
            )

        except Exception as e:

            progress.empty()

            status.error(
                f"Research pipeline failed: {e}"
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        ResearchAI · Multi-agent research system
    </div>
    """,
    unsafe_allow_html=True,
)