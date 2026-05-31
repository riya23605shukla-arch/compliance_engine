import streamlit as st
import ollama
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
st.set_page_config(
    page_title="AI Cybersecurity Policy Analyzer",
    page_icon="🔐",
    layout="wide"
)
st.set_page_config(
    page_title="AI Cybersecurity Policy Analyzer",
    page_icon="🔐",
    layout="wide"
)


st.markdown("""
<style>

/* ===== MAIN APP ===== */

.stApp {
    background:
        radial-gradient(circle at top left, #0f172a, #020617),
        radial-gradient(circle at bottom right, #111827, #000000);

    color: white;
    overflow-x: hidden;
}

/* ===== REMOVE STREAMLIT DEFAULTS ===== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.85);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(0,255,255,0.2);
}

/* ===== HERO SECTION ===== */

.hero {
    padding: 35px;
    border-radius: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(0,255,255,0.08),
            rgba(255,255,255,0.03)
        );

    backdrop-filter: blur(25px);

    border:
        1px solid rgba(0,255,255,0.2);

    box-shadow:
        0 0 40px rgba(0,255,255,0.08);

    text-align: center;

    margin-bottom: 25px;
}

/* ===== TITLE ===== */

.cyber-title {

    font-size: 64px;

    font-weight: 800;

    color: #00ffff;

    text-shadow:
        0 0 10px #00ffff,
        0 0 20px #00ffff,
        0 0 40px #00ffff;

    animation: glow 2s infinite alternate;
}

/* ===== SUBTITLE ===== */

.cyber-subtitle {

    color: #94a3b8;

    font-size: 20px;

    margin-top: 10px;
}

/* ===== GLOW ANIMATION ===== */

@keyframes glow {

    from {
        text-shadow:
            0 0 10px #00ffff,
            0 0 20px #00ffff;
    }

    to {
        text-shadow:
            0 0 20px #00ffff,
            0 0 40px #00ffff,
            0 0 60px #00ffff;
    }
}

/* ===== METRIC CARDS ===== */

div[data-testid="metric-container"] {

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid rgba(0,255,255,0.15);

    padding: 20px;

    border-radius: 20px;

    backdrop-filter: blur(25px);

    box-shadow:
        0 0 25px rgba(0,255,255,0.08);

    transition: 0.3s ease;
}

div[data-testid="metric-container"]:hover {

    transform: translateY(-8px);

    box-shadow:
        0 0 35px rgba(0,255,255,0.25);
}

/* ===== BUTTONS ===== */

.stButton > button {

    width: 100%;

    background:
        linear-gradient(
            90deg,
            #00ffff,
            #0ea5e9
        );

    color: black;

    font-weight: bold;

    border: none;

    border-radius: 14px;

    padding: 14px;

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0 0 25px #00ffff;
}

/* ===== FILE UPLOADER ===== */

[data-testid="stFileUploader"] {

    border:
        2px dashed rgba(0,255,255,0.4);

    border-radius: 20px;

    background:
        rgba(255,255,255,0.03);

    padding: 25px;
}

/* ===== EXPANDER ===== */

.streamlit-expanderHeader {

    background:
        rgba(255,255,255,0.04);

    border-radius: 12px;
}

/* ===== ALERTS ===== */

.stAlert {

    border-radius: 16px;
}

/* ===== PROGRESS BAR ===== */

.stProgress > div > div > div > div {

    background:
        linear-gradient(
            90deg,
            #00ffff,
            #0ea5e9
        );
}

/* ===== TABS ===== */

button[data-baseweb="tab"] {

    background:
        rgba(255,255,255,0.04);

    border-radius: 12px;

    color: white;

    margin-right: 10px;

    padding: 10px 20px;

    transition: 0.3s ease;
}

button[data-baseweb="tab"]:hover {

    background:
        rgba(0,255,255,0.15);
}

/* ===== CODE BLOCK ===== */

pre {

    border-radius: 20px !important;

    border:
        1px solid rgba(0,255,255,0.15);

    background:
        rgba(0,0,0,0.5) !important;
}

/* ===== SCROLLBAR ===== */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-thumb {

    background: #00ffff;

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("🔐 Cybersecurity Dashboard")

st.sidebar.info(
    """
    Offline AI-Powered Cybersecurity
    Policy Gap Analysis System

    Features:
    - Policy Upload
    - Gap Detection
    - Compliance Scoring
    - AI Recommendations
    """
)
nist_mapping = {

    "Risk Management": "Identify",

    "Vendor Risk Management": "Identify",

    "Access Control": "Protect",

    "Data Security": "Protect",

    "Monitoring": "Detect",

    "Incident Response": "Respond",

    "Recovery Plan": "Recover"
}
# Required cybersecurity sections
required_sections = {
    "Risk Management": [
        "risk",
        "risk assessment",
        "risk management"
    ],

    "Vendor Risk Management": [
        "vendor",
        "third party",
        "supplier"
    ],

    "Access Control": [
        "access control",
        "authentication",
        "authorization"
    ],

    "Data Security": [
        "data security",
        "encryption",
        "data protection"
    ],

    "Monitoring": [
        "monitoring",
        "logging",
        "network monitoring"
    ],

    "Incident Response": [
        "incident response",
        "security incident",
        "response plan"
    ],

    "Recovery Plan": [
        "backup",
        "recovery",
        "disaster recovery"
    ]
}

# App Title
st.markdown(
    "<h1 style='text-align: center; color: cyan;'>"
    "🔐 AI Cybersecurity Policy Gap Analyzer"
    "</h1>",
    unsafe_allow_html=True
)

# Upload File
uploaded_files = st.file_uploader(
    "Upload Policy Files",
    accept_multiple_files=True
)

# Analyze File

if uploaded_files:

    for uploaded_file in uploaded_files:

        policy = uploaded_file.read().decode("utf-8")

        st.header(f"📄 {uploaded_file.name}")

        # Policy Content

        with st.expander("📄 View Uploaded Policy"):

            st.write(policy)

        st.divider()

        # Gap Detection

        missing_sections = []

        for section, keywords in required_sections.items():

            found = False

            for keyword in keywords:

                if keyword.lower() in policy.lower():

                    found = True
                    break

            if not found:

                missing_sections.append(section)

        # Compliance Score

        total = len(required_sections)

        missing = len(missing_sections)

        score = ((total - missing) / total) * 100

        st.subheader("Compliance Score")

        st.progress(int(score))

        st.metric(
            label="Compliance Percentage",
            value=f"{score:.2f}%"
        )

        # Risk Level

        if missing >= 5:

            risk = "HIGH RISK"

        elif missing >= 3:

            risk = "MEDIUM RISK"

        else:

            risk = "LOW RISK"

        st.subheader("Cybersecurity Risk Level")

        if risk == "HIGH RISK":

            st.error(risk)

        elif risk == "MEDIUM RISK":

            st.warning(risk)

        else:

            st.success(risk)

        # Compliance Level

        if score >= 80:

            level = "HIGH COMPLIANCE"

        elif score >= 50:

            level = "MEDIUM COMPLIANCE"

        else:

            level = "LOW COMPLIANCE"

        # Compliance Level Colors

        if level == "HIGH COMPLIANCE":

            st.success(f"Compliance Level: {level}")

        elif level == "MEDIUM COMPLIANCE":

            st.warning(f"Compliance Level: {level}")

        else:

            st.error(f"Compliance Level: {level}")

        # Analytics Cards

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Sections",
            total
        )

        col2.metric(
            "Covered",
            total - missing
        )

        col3.metric(
            "Missing",
            missing
        )

        # Pie Chart

        labels = ['Covered', 'Missing']

        sizes = [
            total - missing,
            missing
        ]

        fig, ax = plt.subplots()

        ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%'
        )

        st.subheader("Compliance Visualization")

        st.pyplot(fig)

        # NIST Framework Mapping

        st.subheader("NIST Framework Mapping")

        for section in missing_sections:

            function = nist_mapping.get(section, "Unknown")

            st.warning(
                f"{section} → NIST Function: {function}"
            )

        # Missing Sections

        st.subheader("Missing Sections")

        for section in missing_sections:

            st.error(f"❌ {section}")



        # AI Gap Analysis

        from langchain_community.embeddings import HuggingFaceEmbeddings
        from langchain_community.vectorstores import Chroma

        # Load ChromaDB

        embedding_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        vector_db = Chroma(
            persist_directory="chroma_db",
            embedding_function=embedding_model
        )

        # Retrieve relevant NIST context

        results = vector_db.similarity_search(policy, k=1)

        nist_context = ""

        for result in results:

            nist_context += result.page_content + "\n\n"

        st.subheader("AI Gap Analysis")

        prompt = f"""
You are a cybersecurity compliance auditor.

Analyze the policy using the NIST cybersecurity framework context.

Identify:
- compliance gaps
- weak areas
- missing controls

Provide:
- recommendations
- short implementation roadmap

POLICY:
{policy}

NIST CONTEXT:
{nist_context[:1000]}
"""

        with st.spinner("Generating AI Gap Analysis..."):

            response = ollama.chat(
                model='tinyllama',
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )

        st.success(response['message']['content'])

        # Generate PDF Report

        if st.button(
            f"📥 Download Compliance Report - {uploaded_file.name}"
        ):

            pdf_path = "compliance_report.pdf"

            c = canvas.Canvas(pdf_path)

            c.setFont("Helvetica-Bold", 16)

            c.drawString(
                100,
                800,
                "Cybersecurity Compliance Report"
            )

            c.setFont("Helvetica", 12)

            c.drawString(
                50,
                760,
                f"Compliance Score: {score:.2f}%"
            )

            y = 720

            c.drawString(
                50,
                y,
                "Missing Sections:"
            )

            y -= 20

            for section in missing_sections:

                c.drawString(
                    70,
                    y,
                    f"- {section}"
                )

                y -= 20

            y -= 20

            c.drawString(
                50,
                y,
                "AI Recommendations:"
            )

            y -= 20

            recommendations = response['message']['content']

            for line in recommendations.split('\n'):

                c.drawString(
                    70,
                    y,
                    line[:90]
                )

                y -= 20

                if y < 50:

                    c.showPage()

                    y = 800

            c.save()

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="⬇ Download PDF",
                    data=file,
                    file_name="compliance_report.pdf",
                    mime="application/pdf"
                )

        st.divider()

st.caption(
    "Developed using Streamlit + Ollama + TinyLlama"
)