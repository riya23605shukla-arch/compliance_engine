import streamlit as st
import pandas as pd
import plotly.express as px
import os
import json

from utils import save_uploaded_files
from pipeline import run_pipeline

# ======================================================
# CYBERSECURITY BANNER
# ======================================================

st.image(
    "assets/banner.png",
    width="stretch"
)

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Offline Cybersecurity Compliance Engine",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Offline LLM-Based Cybersecurity Compliance Engine")

st.markdown(
"""
This demo performs an automated cybersecurity compliance assessment
using uploaded policy documents and the NIST CSF 2.0 framework.
"""
)

st.markdown("---")

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("Assessment Settings")

framework = st.sidebar.selectbox(
    "Select Framework",
    [
        "NIST CSF 2.0"
    ]
)

uploaded_files = st.sidebar.file_uploader(
    "Upload Policy Documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

run = st.sidebar.button(
    "🚀 Run Compliance Assessment"
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Demo Workflow

1. Upload Policy Documents

2. Run Assessment

3. View Compliance Dashboard

4. Inspect Individual Controls

5. Download Reports
"""
)

# -------------------------------------------------------
# MAIN PIPELINE
# -------------------------------------------------------

if run:

    if len(uploaded_files) == 0:

        st.error("Please upload at least one policy document.")

        st.stop()

    with st.spinner("Saving uploaded documents..."):

        saved_files = save_uploaded_files(
            uploaded_files
        )

    st.success("Documents Uploaded Successfully")

    st.subheader("Uploaded Documents")

    for file in saved_files:

        st.write("📄", file)

    st.markdown("---")

    progress = st.progress(0)

    progress.progress(10)

    status = st.empty()

    status.info("Starting Compliance Assessment Pipeline...")

    progress.progress(20)

    status.info("Parsing Uploaded Documents...")

    progress.progress(40)

    status.info("Generating Embeddings...")

    progress.progress(60)

    status.info("Retrieving Evidence from ChromaDB...")

    progress.progress(80)

    status.info("Running Compliance Assessment...")

    with st.spinner("Running Assessment Engine..."):

        results = run_pipeline()

    progress.progress(100)

    status.success("Assessment Completed Successfully")

    st.balloons()

    st.markdown("---")

    # -------------------------------------------------------
    # DASHBOARD CALCULATIONS
    # -------------------------------------------------------

    total_controls = len(results)

    compliant = len(
        [
            r for r in results
            if r["status"] == "Compliant"
        ]
    )

    partial = len(
        [
            r for r in results
            if r["status"] == "Partially Compliant"
        ]
    )

    non = len(
        [
            r for r in results
            if r["status"] == "Non-Compliant"
        ]
    )

    not_enough = len(
        [
            r for r in results
            if r["status"] == "Not Enough Evidence"
        ]
    )

    overall_score = round(
        (
            sum(
                r["confidence"]
                for r in results
            )
            /
            total_controls
        ) * 100,
        2
    )

    st.header("📊 Compliance Summary Dashboard")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Overall Score",
        f"{overall_score}%"
    )

    c2.metric(
        "Compliant",
        compliant
    )

    c3.metric(
        "Partially",
        partial
    )

    c4.metric(
        "Non-Compliant",
        non
    )

    c5.metric(
        "Total Controls",
        total_controls
    )

    st.markdown("---")
        # =====================================================
    # PIE CHART
    # =====================================================

    st.subheader("📈 Compliance Distribution")

    pie_df = pd.DataFrame(
        {
            "Status": [
                "Compliant",
                "Partially Compliant",
                "Non-Compliant",
                "Not Enough Evidence"
            ],
            "Count": [
                compliant,
                partial,
                non,
                not_enough
            ]
        }
    )

    fig = px.pie(
        pie_df,
        names="Status",
        values="Count",
        hole=0.45,
        title="Compliance Status Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.markdown("---")

    # =====================================================
    # BAR CHART
    # =====================================================

    st.subheader("📊 Confidence Score by Control")

    confidence_df = pd.DataFrame(results)

    fig2 = px.bar(
        confidence_df,
        x="control_id",
        y="confidence",
        color="status",
        text="confidence",
        title="Confidence Score Across Controls"
    )

    fig2.update_layout(
        xaxis_title="Control ID",
        yaxis_title="Confidence Score"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

    st.markdown("---")

    # =====================================================
    # SUMMARY TABLE
    # =====================================================

    st.subheader("📋 Control Summary")

    table = pd.DataFrame(results)

    table = table[
        [
            "control_id",
            "status",
            "confidence"
        ]
    ]

    st.dataframe(
        table,
        width="stretch",
        hide_index=True
    )

    st.markdown("---")

    # =====================================================
    # QUICK STATISTICS
    # =====================================================

    st.subheader("📌 Assessment Statistics")

    left, right = st.columns(2)

    with left:

        st.success(
            f"✔ Compliant Controls : {compliant}"
        )

        st.warning(
            f"🟠 Partially Compliant Controls : {partial}"
        )

    with right:

        st.error(
            f"❌ Non-Compliant Controls : {non}"
        )

        st.info(
            f"📄 Total Controls Assessed : {total_controls}"
        )

    st.markdown("---")

    # =====================================================
    # DETAILED RESULTS HEADER
    # =====================================================

    st.header("🔍 Detailed Control Assessment")

    st.info(
        "Expand any control below to inspect "
        "its compliance assessment, evidence, "
        "reasoning and recommendations."
    )
        # =====================================================
    # DETAILED CONTROL RESULTS
    # =====================================================

    for result in results:

        # -------- Status Icon --------

        if result["status"] == "Compliant":

            status_icon = "🟢"

        elif result["status"] == "Partially Compliant":

            status_icon = "🟠"

        elif result["status"] == "Non-Compliant":

            status_icon = "🔴"

        else:

            status_icon = "⚪"

        with st.expander(
            f"{status_icon}  {result['control_id']}   |   {result['status']}"
        ):

            col1, col2 = st.columns(2)

            # ===========================================
            # LEFT COLUMN
            # ===========================================

            with col1:

                st.markdown("### 📌 Assessment")

                st.write(
                    "**Control ID:**",
                    result["control_id"]
                )

                st.write(
                    "**Status:**",
                    result["status"]
                )

                st.write(
                    "**Confidence Score:**",
                    f"{round(result['confidence']*100,2)} %"
                )

                st.progress(
                    float(result["confidence"])
                )

                st.markdown("---")

                st.markdown("### 🧠 LLM Reasoning")

                st.info(
                    result["reasoning"]
                )

            # ===========================================
            # RIGHT COLUMN
            # ===========================================

            with col2:

                st.markdown("### 📄 Evidence Viewer")

                found = result.get(
                    "found_evidence",
                    []
                )

                if len(found) == 0:

                    st.warning(
                        "No evidence matched for this control."
                    )

                else:

                    for index, evidence in enumerate(found):
                        with st.expander(f"Retrieved Evidence {index+1}"):

                               st.write(evidence)
                        
                            
                        

                        

                        
            
            # ===========================================
            # Missing Evidence
            # ===========================================

            st.markdown("## ❌ Missing Evidence")

            missing = result.get(
                "missing_evidence",
                []
            )

            if len(missing) == 0:

                st.success(
                    "No missing evidence."
                )

            else:

                for item in missing:

                    st.write(
                        "•",
                        item
                    )

            # ===========================================
            # Recommendations
            # ===========================================

            st.markdown("## 💡 Recommendations")

            rec = result.get(
                "recommendations",
                []
            )

            if len(rec) == 0:

                st.success(
                    "No recommendations required."
                )

            else:

                for item in rec:

                    st.write(
                        "✔",
                        item
                    )

            st.markdown("---")
                # =====================================================
    # DOWNLOAD REPORTS
    # =====================================================

    st.markdown("---")
    st.header("📥 Download Assessment Reports")

    json_file = "data/assessments/framework_assessment.json"
    csv_file = "data/reports/framework_report.csv"

    col1, col2 = st.columns(2)

    # ---------------- JSON ----------------

    if os.path.exists(json_file):

        with open(json_file, "rb") as file:

            col1.download_button(
                label="⬇ Download JSON Report",
                data=file,
                file_name="assessment_report.json",
                mime="application/json"
            )

    # ---------------- CSV ----------------

    if os.path.exists(csv_file):

        with open(csv_file, "rb") as file:

            col2.download_button(
                label="⬇ Download CSV Report",
                data=file,
                file_name="assessment_report.csv",
                mime="text/csv"
            )

    # =====================================================
    # HTML REPORT
    # =====================================================

    st.markdown("---")

    st.header("🌐 HTML Report")

    html = f"""
    <html>

    <head>

    <title>Compliance Report</title>

    <style>

    body{{font-family:Arial;padding:40px;}}

    table{{border-collapse:collapse;width:100%;}}

    th,td{{border:1px solid #ddd;padding:10px;}}

    th{{background:#efefef;}}

    </style>

    </head>

    <body>

    <h1>Offline Cybersecurity Compliance Assessment</h1>

    <h2>NIST CSF 2.0</h2>

    <hr>

    <h3>Assessment Summary</h3>

    <ul>

    <li>Overall Score : {overall_score}%</li>

    <li>Total Controls : {total_controls}</li>

    <li>Compliant : {compliant}</li>

    <li>Partially Compliant : {partial}</li>

    <li>Non-Compliant : {non}</li>

    </ul>

    <hr>

    <table>

    <tr>

    <th>Control</th>

    <th>Status</th>

    <th>Confidence</th>

    </tr>

    """

    for result in results:

        html += f"""

        <tr>

        <td>{result['control_id']}</td>

        <td>{result['status']}</td>

        <td>{round(result['confidence']*100,2)}%</td>

        </tr>

        """

    html += """

    </table>

    </body>

    </html>

    """

    st.download_button(

        "⬇ Download HTML Report",

        html,

        file_name="assessment_report.html",

        mime="text/html"

    )

    # =====================================================
    # PROJECT INFORMATION
    # =====================================================

    st.markdown("---")

    st.header("ℹ️ Project Information")

    info1, info2 = st.columns(2)

    with info1:

        st.info(
            """
**Framework**

NIST Cybersecurity Framework 2.0

**Assessment Engine**

Offline LLM-Based Compliance Assessment

**Vector Database**

ChromaDB

**Embedding Model**

all-MiniLM-L6-v2
"""
        )

    with info2:

        st.success(
            """
**Features**

✔ Policy Parsing

✔ Document Chunking

✔ Embedding Generation

✔ Chroma Retrieval

✔ Compliance Assessment

✔ Recommendations

✔ Traceability

✔ Report Generation
"""
        )

    st.markdown("---")

    st.caption(
        "Offline LLM-Based Cybersecurity Compliance Engine | Internship Project | 2026"
    )