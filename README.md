# Offline LLM-Based Cybersecurity Compliance Engine

## Project Overview

Organizations often struggle to determine whether their internal cybersecurity policies align with established security frameworks such as the NIST Cybersecurity Framework (CSF) 2.0. Manual policy reviews are time-consuming, inconsistent, and difficult to scale across multiple documents.

This project aims to develop a fully offline, AI-powered Cybersecurity Compliance Engine that automatically evaluates organizational policy documents against selected NIST CSF 2.0 controls. The system leverages Retrieval-Augmented Generation (RAG), ChromaDB, local embedding models, and locally hosted Large Language Models (LLMs) to perform evidence-based compliance assessments while ensuring complete data privacy.

---

# Problem Statement

Organizations maintain multiple cybersecurity policies covering areas such as access control, risk management, data protection, incident response, and disaster recovery. Determining whether these policies satisfy cybersecurity standards is often a manual and resource-intensive process.

The objective of this project is to automate cybersecurity policy assessment by:

- Parsing policy documents
- Retrieving relevant evidence
- Mapping evidence to NIST CSF 2.0 controls
- Determining compliance status
- Generating recommendations for improvement

All processing is performed locally without reliance on cloud-based APIs.

---

# Objectives

The primary objectives of the project are:

- Build a fully offline compliance assessment engine
- Analyze cybersecurity policy documents
- Evaluate policies against selected NIST CSF 2.0 controls
- Retrieve supporting evidence from documents
- Classify controls as:
  - Compliant
  - Partially Compliant
  - Non-Compliant
  - Not Enough Evidence
- Generate compliance reports and recommendations

---

# NIST CSF 2.0 Usage

This project uses the NIST Cybersecurity Framework (CSF) 2.0 as the baseline cybersecurity standard.

The framework organizes cybersecurity activities into six core functions:

1. Govern
2. Identify
3. Protect
4. Detect
5. Respond
6. Recover

For the Minimum Viable Product (MVP), a selected subset of approximately 20 important NIST CSF 2.0 controls is used for assessment.

---

# Key Features

- 100% Offline Execution
- Local LLM Integration using Ollama
- Local Embedding Generation
- ChromaDB Vector Storage
- Evidence-Based Compliance Assessment
- NIST CSF 2.0 Mapping
- Compliance Scoring
- Gap Identification
- Recommendation Generation

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.10+ |
| LLM Runtime | Ollama |
| Language Models | TinyLlama / Phi-3 |
| Vector Database | ChromaDB |
| Embedding Model | all-MiniLM-L6-v2 |
| PDF Parsing | PyMuPDF |
| Retrieval Framework | LangChain |
| UI Prototype | Streamlit |

---

# Minimum Viable Product (MVP)

The MVP includes:

### Document Processing

- Upload cybersecurity policy documents
- Extract document text
- Parse PDF documents

### Retrieval Pipeline

- Create text chunks
- Generate embeddings
- Store embeddings in ChromaDB
- Retrieve relevant policy evidence

### Assessment Engine

- Map evidence to NIST controls
- Evaluate compliance status
- Generate assessment results

### Reporting

- Display compliance findings
- Show supporting evidence
- Generate recommendations

---
## Supported Input Formats

For the MVP, the compliance engine accepts the following document formats:

* PDF (.pdf)
* Microsoft Word Documents (.docx)
* Text Files (.txt)

The system is designed to process machine-readable documents where text can be directly extracted.

### Out of Scope for MVP

The following formats are not supported in the current version:

* Scanned PDFs containing only images
* JPEG, PNG, TIFF, or other image files
* Handwritten documents
* Screenshots of policies

These document types require Optical Character Recognition (OCR) techniques to extract text before compliance assessment can be performed.

# Out of Scope (Current Version)

The following features are not included in the MVP:

- Cloud Deployment
- User Authentication
- Multi-User Support
- Real-Time Monitoring
- SIEM Integration
- Continuous Compliance Tracking
- Regulatory Framework Mapping beyond NIST CSF 2.0
- Automated Remediation

---

# Project Structure

```text
compliance-engine/
│
├── data/
│   ├── raw_docs/
│   │   ├── policy_1.pdf
│   │   ├── policy_2.pdf
│   │   ├── policy_3.pdf
│   │   ├── policy_4.pdf
│   │   ├── policy_5.pdf
│   │   └── document_inventory.csv
│   │
│   ├── parsed_docs/
│   │
│   ├── chunks/
│   │
│   ├── chroma_db/
│   │
│   └── outputs/
│       └── sample_expected_output.json
│
├── frameworks/
│   ├── nist_csf_2_mvp.json
│   ├── assessment_status_rules.md
│   └── evidence_requirements.md
│
├── src/
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── retrieval/
│   ├── llm/
│   ├── scoring/
│   └── reporting/
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── run_assessment.py
```
## Architecture Diagram
{"type":"excalidraw/clipboard","workspaceId":"1VVTXJqv5UqJ5tTIAwst","elements":[{"0":525,"1":340,"renderVersion":"20260702","strokeColor":"#d7d9dc","fillStyle":"solid","backgroundColor":"transparent","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"strokeSharpness":"sharp","version":121,"isDeleted":false,"id":"l_LV56mp-DMiOrSYKu5k","code":"","x":65,"y":5,"diagramType":"freeform-diagram","forceAiMode":false,"isBeingGenerated":false,"lastEditMode":"ai","scale":1,"type":"diagram","width":1250,"height":1120,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1155004104,"zIndex":0,"title":"Offline LLM Cybersecurity Compliance Assessment System","modifiedAt":1782977806977,"isSyntaxMissing":false},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"3b2bd14fe683a90a958ae6611036f286","x":400,"y":20,"diagramEntityId":"title","isContainer":false,"freeform":{"tag":"Textbox","text":"# Offline LLM-Based Cybersecurity Compliance Engine","fontSize":"large","hAlign":"center"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":676.25,"height":35,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1522694328,"version":1,"zIndex":1},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"d63b2601c6ab5a84f477c14770659679","x":80,"y":420,"diagramEntityId":"user","isContainer":false,"freeform":{"tag":"Icon","icon":"user","size":"md","texts":[{"text":"User"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":50,"height":50,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":55086792,"version":1,"zIndex":2},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"6642dc236e05333f8c01cbb28c56d566","x":220,"y":320,"diagramEntityId":"ui","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Streamlit UI","icon":"monitor"},"bgColor":"#EAF4FB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":260,"height":260,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":509780408,"version":1,"zIndex":3},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6642dc236e05333f8c01cbb28c56d566","figureId":null,"id":"01d0646e69a58e0e80b67603695ede98","x":240,"y":370,"diagramEntityId":"ui_upload","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Upload Policy Documents","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1742435784,"version":1,"zIndex":4},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6642dc236e05333f8c01cbb28c56d566","figureId":null,"id":"2d4278bdce325b1e0d3c98dfccd58442","x":240,"y":402,"diagramEntityId":"ui_framework","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Select Framework (NIST CSF 2.0)","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":773171896,"version":1,"zIndex":5},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6642dc236e05333f8c01cbb28c56d566","figureId":null,"id":"200f44489159aa12d631db34ea66b78b","x":240,"y":434,"diagramEntityId":"ui_run","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Run Compliance Assessment","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":662273224,"version":1,"zIndex":6},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6642dc236e05333f8c01cbb28c56d566","figureId":null,"id":"83ababbcfffa41a283ffa9c937291d13","x":240,"y":466,"diagramEntityId":"ui_dash","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Dashboard","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1149211576,"version":1,"zIndex":7},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6642dc236e05333f8c01cbb28c56d566","figureId":null,"id":"603d9ee00761ba42148878744b762afe","x":240,"y":498,"diagramEntityId":"ui_evidence","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Evidence Viewer","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1941873608,"version":1,"zIndex":8},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6642dc236e05333f8c01cbb28c56d566","figureId":null,"id":"c9a88c57497d25203c114e35740248e1","x":240,"y":530,"diagramEntityId":"ui_report","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Report Download","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":667180216,"version":1,"zIndex":9},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"3b6b1ea240ca18fe973b79f1ec546e9c","x":540,"y":340,"diagramEntityId":"ingest","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Document Ingestion","icon":"file"},"bgColor":"#FFF3E6"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":192,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1791421128,"version":2,"zIndex":12},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"3b6b1ea240ca18fe973b79f1ec546e9c","figureId":null,"id":"2e4eea2fa85e002c40706f53d3c2b043","x":560,"y":390,"diagramEntityId":"pdf","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"PDF Parser","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":965215672,"version":1,"zIndex":13},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"3b6b1ea240ca18fe973b79f1ec546e9c","figureId":null,"id":"0430d770a4c1eaa21aca966c735b702d","x":560,"y":422,"diagramEntityId":"docx","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"DOCX Parser","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":120476104,"version":1,"zIndex":14},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"3b6b1ea240ca18fe973b79f1ec546e9c","figureId":null,"id":"e23bd13abc83aa3c50c03241034c85bc","x":560,"y":454,"diagramEntityId":"txt","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"TXT Parser","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":116297400,"version":1,"zIndex":15},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"3b6b1ea240ca18fe973b79f1ec546e9c","figureId":null,"id":"a4887940df732343d8676376578a1d95","x":560,"y":486,"diagramEntityId":"cleaner","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Text Cleaner","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":269539528,"version":1,"zIndex":16},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"6b44e3bd73dea037d0105824b14dc543","x":820,"y":380,"diagramEntityId":"chunk","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Chunk Generator","icon":"grid"},"bgColor":"#FFF3E6"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":96,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1486616504,"version":2,"zIndex":18},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6b44e3bd73dea037d0105824b14dc543","figureId":null,"id":"987add3e1758d4a5e52af5b82a2ac3ff","x":840,"y":430,"diagramEntityId":"metachunks","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Generate Metadata Chunks","fontSize":11}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":160,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":151683016,"version":1,"zIndex":19},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"983a52ca8d7abccf250bb72532a1250d","x":1080,"y":360,"diagramEntityId":"embed","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Embedding Engine","icon":"cpu"},"bgColor":"#FFF3E6"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":128,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1119109304,"version":2,"zIndex":21},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"983a52ca8d7abccf250bb72532a1250d","figureId":null,"id":"561396f8af47ba52cb3197d5b31be17f","x":1100,"y":410,"diagramEntityId":"st","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"SentenceTransformer","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":574047944,"version":1,"zIndex":22},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"983a52ca8d7abccf250bb72532a1250d","figureId":null,"id":"546e5f589f0247d28d65939786de9bb1","x":1100,"y":442,"diagramEntityId":"minilm","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"all-MiniLM-L6-v2","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":886794680,"version":1,"zIndex":23},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"7213b8015d1d4bd66e6e11365e003749","x":1080,"y":580,"diagramEntityId":"vdb","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Vector Database","icon":"database"},"bgColor":"#EAF4FB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":110,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":674442696,"version":1,"zIndex":25},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"7213b8015d1d4bd66e6e11365e003749","figureId":null,"id":"bfd51c3183c3e2aed3ed06ab1ab1d68a","x":1100,"y":630,"diagramEntityId":"chroma","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"ChromaDB","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":171274936,"version":1,"zIndex":26},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"42b67fb6003e56ea7d565d13b342cdf8","x":820,"y":580,"diagramEntityId":"retrieval","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Retrieval Engine","icon":"search"},"bgColor":"#EAF4FB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":170,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1947874504,"version":1,"zIndex":28},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"42b67fb6003e56ea7d565d13b342cdf8","figureId":null,"id":"3e5ca3c1e884be14fb6c6880ed2fad4a","x":840,"y":630,"diagramEntityId":"qgen","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Query Generator","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":426138552,"version":1,"zIndex":29},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"42b67fb6003e56ea7d565d13b342cdf8","figureId":null,"id":"e2df314f1ef0438cd1d6e5820b0e8267","x":840,"y":662,"diagramEntityId":"sim","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Similarity Search","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1535663048,"version":1,"zIndex":30},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"42b67fb6003e56ea7d565d13b342cdf8","figureId":null,"id":"c57c2aaaa5dc9bc9d457911117c137ec","x":840,"y":694,"diagramEntityId":"topk","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Top-K Evidence","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1150428344,"version":1,"zIndex":31},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"803992dfd6820af309556d4ad3ed9ba7","x":540,"y":610,"diagramEntityId":"nist","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"NIST Framework","icon":"book"},"bgColor":"#F0EAFB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":110,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":546939592,"version":1,"zIndex":33},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"803992dfd6820af309556d4ad3ed9ba7","figureId":null,"id":"6ca2a6519469240d406650a096780bdc","x":560,"y":660,"diagramEntityId":"nistc","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"NIST CSF 2.0 Controls","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":157076920,"version":1,"zIndex":34},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"7cf6ea5e0151f8d0c46be145ab8d599f","x":540,"y":780,"diagramEntityId":"llm","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Offline LLM","icon":"brain"},"bgColor":"#F0EAFB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":110,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1642727880,"version":1,"zIndex":36},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"7cf6ea5e0151f8d0c46be145ab8d599f","figureId":null,"id":"176eaa972e15e48dcd3e946b22e137b0","x":560,"y":830,"diagramEntityId":"phi3","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Phi-3 Mini (Ollama)","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":283793080,"version":1,"zIndex":37},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"308af8e68192ace5ac3203a8c13fcbdd","x":820,"y":790,"diagramEntityId":"assess","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Assessment Engine","icon":"shield"},"bgColor":"#EAF4FB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":240,"height":260,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":177574088,"version":1,"zIndex":39},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"308af8e68192ace5ac3203a8c13fcbdd","figureId":null,"id":"96d57672013c339b317a0023d4e8d044","x":840,"y":840,"diagramEntityId":"fa","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Framework Assessor","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1071562680,"version":1,"zIndex":40},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"308af8e68192ace5ac3203a8c13fcbdd","figureId":null,"id":"5d60c705f6cc5a6e06fdac42077eafad","x":840,"y":872,"diagramEntityId":"ca","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Control Assessor","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1110980552,"version":1,"zIndex":41},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"308af8e68192ace5ac3203a8c13fcbdd","figureId":null,"id":"617f7dfb68e7a06973716bfaa111ef3f","x":840,"y":904,"diagramEntityId":"score","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Compliance Scoring","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1180567736,"version":1,"zIndex":42},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"308af8e68192ace5ac3203a8c13fcbdd","figureId":null,"id":"80c523eab50f1a17d4ce09b7f51c1217","x":840,"y":936,"diagramEntityId":"reason","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Reasoning Generator","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1559101128,"version":1,"zIndex":43},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"308af8e68192ace5ac3203a8c13fcbdd","figureId":null,"id":"21c82301dc280b639c282eb888d787d9","x":840,"y":968,"diagramEntityId":"rec","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Recommendation Generator","fontSize":11}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":806105528,"version":1,"zIndex":44},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"308af8e68192ace5ac3203a8c13fcbdd","figureId":null,"id":"ed09bc52e9e5bd92c488cbfaace60f24","x":840,"y":1000,"diagramEntityId":"trace","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"Traceability Logger","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":200,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1263723976,"version":1,"zIndex":45},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"f80dff83e5a138e7bd7216eb3d75de65","x":540,"y":950,"diagramEntityId":"reportg","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Report Generator","icon":"file-text"},"bgColor":"#FFF3E6"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":160,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1947024056,"version":2,"zIndex":47},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"f80dff83e5a138e7bd7216eb3d75de65","figureId":null,"id":"2f6fea00bcdb42b8639dc5d71cd5eb9b","x":560,"y":1000,"diagramEntityId":"jsonr","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"JSON Report","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":176352456,"version":1,"zIndex":48},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"f80dff83e5a138e7bd7216eb3d75de65","figureId":null,"id":"bd31f714370736d4578df7c5b00db833","x":560,"y":1032,"diagramEntityId":"csvr","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"CSV Report","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":84222904,"version":1,"zIndex":49},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"f80dff83e5a138e7bd7216eb3d75de65","figureId":null,"id":"46835b9f850a27295866a1f76b6efc6f","x":560,"y":1064,"diagramEntityId":"htmlr","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"HTML Report","fontSize":12}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":180,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":337253320,"version":1,"zIndex":50},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","figureId":null,"id":"6d663952b8850450fd9a65d55c0f5128","x":220,"y":720,"diagramEntityId":"storage","isContainer":true,"sizingMode":"manual","freeform":{"tag":"Group","title":{"text":"Data Storage","icon":"folder"},"bgColor":"#F0EAFB"},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":260,"height":288,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1628957880,"version":2,"zIndex":53},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"11121d79da533a3322323b4f87fb37d2","x":240,"y":770,"diagramEntityId":"raw","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/raw_docs","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1312053960,"version":1,"zIndex":54},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"5ff7c16595902b746049237f2cdd0360","x":240,"y":802,"diagramEntityId":"parsed","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/parsed_docs","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":568956344,"version":1,"zIndex":55},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"be759d7d8399ae2f6248fcdcf4ced0c4","x":240,"y":834,"diagramEntityId":"chunks","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/chunks","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":2070790600,"version":1,"zIndex":56},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"23716001afabece9d7f6203667e5ce22","x":240,"y":866,"diagramEntityId":"chromadb","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/chroma_db","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":211689144,"version":1,"zIndex":57},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"7f8b38d84077ff45c1c432c4ac882a11","x":240,"y":898,"diagramEntityId":"assessments","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/assessments","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":719472840,"version":1,"zIndex":58},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"7d05b728ab850f0b942b3cf318e00de0","x":240,"y":930,"diagramEntityId":"reports","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/reports","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":567904184,"version":1,"zIndex":59},{"strokeColor":"#1c1c1c","backgroundColor":"transparent","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","strokeSharpness":"round","opacity":100,"roughness":1,"shouldApplyRoughness":true,"isDeleted":false,"diagramId":"l_LV56mp-DMiOrSYKu5k","containerId":"6d663952b8850450fd9a65d55c0f5128","figureId":null,"id":"fd302789b590e4f1768269c735c260cc","x":240,"y":962,"diagramEntityId":"logs","isContainer":false,"freeform":{"tag":"Shape","texts":[{"text":"data/logs","fontSize":12,"typeface":"mono"}]},"compound":{"type":"parent","containerType":"freeform"},"type":"freeform","width":220,"height":26,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":674099144,"version":1,"zIndex":60},{"id":"f1da3f9a6cd8698278dc6fdedd25aefa","type":"arrow","x":130,"y":445,"points":[[0,0],[39,0],[39,11],[90,11]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r1","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","down","right"]},"freeform":{"tag":"Relationship","from":"user","fromPort":"right","to":"ui","toPort":"left"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"d63b2601c6ab5a84f477c14770659679","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"6642dc236e05333f8c01cbb28c56d566","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":90,"height":11,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":384918968,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":10,"modifiedAt":1782977806857},{"id":"9855ad43c10b42921938372d875e1563","type":"arrow","x":480,"y":450,"points":[[0,0],[30,0],[30,-14],[60,-14]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r2","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","up","right"]},"freeform":{"tag":"Relationship","from":"ui","fromPort":"right","to":"ingest","toPort":"left"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"6642dc236e05333f8c01cbb28c56d566","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"3b6b1ea240ca18fe973b79f1ec546e9c","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":60,"height":14,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":394981832,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":17,"modifiedAt":1782977806858},{"id":"98c32f051e772d5d74c6ae934a7fb93a","type":"arrow","x":650,"y":532,"points":[[0,0],[0,2],[-140,2],[-140,112],[-306,112],[-306,188]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r3","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["down","left","down","left","down"]},"freeform":{"tag":"Relationship","from":"ingest","fromPort":"bottom","to":"storage","toPort":"top"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"3b6b1ea240ca18fe973b79f1ec546e9c","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"down"}},"endBinding":{"elementId":"6d663952b8850450fd9a65d55c0f5128","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"up"}},"width":306,"height":188,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":808185528,"version":7,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":61,"modifiedAt":1782977806860},{"id":"f31fdc5c19f42372b3fa0e9fdfd1603d","type":"arrow","x":760,"y":436,"points":[[0,0],[30,0],[30,-8],[60,-8]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r4","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","up","right"]},"freeform":{"tag":"Relationship","from":"ingest","fromPort":"right","to":"chunk","toPort":"left"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"3b6b1ea240ca18fe973b79f1ec546e9c","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"6b44e3bd73dea037d0105824b14dc543","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":60,"height":8,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":735672520,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":20,"modifiedAt":1782977806941},{"id":"9a791c310055c0b5e4e3781c9789e96f","type":"arrow","x":920,"y":476,"points":[[0,0],[0,52],[-130,52],[-130,274],[-398,274],[-398,229],[-564,229],[-564,244]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r5","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["down","left","down","left","up","left","down"]},"freeform":{"tag":"Relationship","from":"chunk","fromPort":"bottom","to":"storage","toPort":"top"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"6b44e3bd73dea037d0105824b14dc543","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"down"}},"endBinding":{"elementId":"6d663952b8850450fd9a65d55c0f5128","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"up"}},"width":564,"height":274,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":858609592,"version":6,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":62,"modifiedAt":1782977806941},{"id":"af0ecc1b19f7ff0b986c79c1488cc72a","type":"arrow","x":1020,"y":428,"points":[[0,0],[58,0],[58,-4],[60,-4]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r6","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","up","right"]},"freeform":{"tag":"Relationship","from":"chunk","fromPort":"right","to":"embed","toPort":"left"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"6b44e3bd73dea037d0105824b14dc543","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"983a52ca8d7abccf250bb72532a1250d","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":60,"height":4,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1656692680,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":24,"modifiedAt":1782977806943},{"id":"8e21f47353f18e168d65813b1845bcdc","type":"arrow","x":1190,"y":488,"points":[[0,0],[0,92]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r7","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["down"]},"freeform":{"tag":"Relationship","from":"embed","fromPort":"bottom","to":"vdb","toPort":"top"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"983a52ca8d7abccf250bb72532a1250d","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"down"}},"endBinding":{"elementId":"7213b8015d1d4bd66e6e11365e003749","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"up"}},"width":0,"height":92,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":68788408,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":27,"modifiedAt":1782977806943},{"id":"2672f71b93076aadab6ecfbc4c4a7345","type":"arrow","x":1080,"y":635,"points":[[0,0],[-2,0],[-2,30],[-40,30]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r8","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["left","down","left"]},"freeform":{"tag":"Relationship","from":"vdb","fromPort":"left","to":"retrieval","toPort":"right"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"7213b8015d1d4bd66e6e11365e003749","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"endBinding":{"elementId":"42b67fb6003e56ea7d565d13b342cdf8","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"width":40,"height":30,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":475522760,"version":4,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":32,"modifiedAt":1782977806944},{"id":"3f90f4603c58145b63819b5568145cb7","type":"arrow","x":760,"y":665,"points":[[0,0],[60,0]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r9","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right"]},"freeform":{"tag":"Relationship","from":"nist","fromPort":"right","to":"retrieval","toPort":"left"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"803992dfd6820af309556d4ad3ed9ba7","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"42b67fb6003e56ea7d565d13b342cdf8","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":60,"height":0,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1653918136,"version":4,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":35,"modifiedAt":1782977806945},{"id":"b51323bf56ed47ced463bb86e3ab15aa","type":"arrow","x":930,"y":750,"points":[[0,0],[0,20],[-140,20],[-140,79],[-170,79]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r10","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["down","left","down","left"]},"freeform":{"tag":"Relationship","from":"retrieval","fromPort":"bottom","to":"llm","toPort":"right"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"42b67fb6003e56ea7d565d13b342cdf8","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"down"}},"endBinding":{"elementId":"7cf6ea5e0151f8d0c46be145ab8d599f","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"width":170,"height":79,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1430244808,"version":4,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":38,"modifiedAt":1782977806945},{"id":"066c012102fa7aef796c552daeeb23da","type":"arrow","x":760,"y":841,"points":[[0,0],[30,0],[30,73],[60,73]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r11","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["right","down","right"]},"freeform":{"tag":"Relationship","from":"llm","fromPort":"right","to":"assess","toPort":"left"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"7cf6ea5e0151f8d0c46be145ab8d599f","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"endBinding":{"elementId":"308af8e68192ace5ac3203a8c13fcbdd","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"width":60,"height":73,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":2042811064,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":46,"modifiedAt":1782977806945},{"id":"4c6004e5f339c4e1f9aa1d6a939fe97a","type":"arrow","x":820,"y":926,"points":[[0,0],[-30,0],[-30,104],[-60,104]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r12","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["left","down","left"]},"freeform":{"tag":"Relationship","from":"assess","fromPort":"left","to":"reportg","toPort":"right"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"308af8e68192ace5ac3203a8c13fcbdd","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"endBinding":{"elementId":"f80dff83e5a138e7bd7216eb3d75de65","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"width":60,"height":104,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":378721480,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":51,"modifiedAt":1782977806946},{"id":"5d12b71d2f235f08f29c2927baad6b55","type":"arrow","x":540,"y":1030,"points":[[0,0],[-42,0],[-42,-166],[-60,-166]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r13","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["left","up","left"]},"freeform":{"tag":"Relationship","from":"reportg","fromPort":"left","to":"storage","toPort":"right"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"f80dff83e5a138e7bd7216eb3d75de65","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"endBinding":{"elementId":"6d663952b8850450fd9a65d55c0f5128","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"right"}},"width":60,"height":166,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1883749304,"version":6,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":63,"modifiedAt":1782977806947},{"id":"c5996b4d80e25efaa02263bc74fc25ba","type":"arrow","x":650,"y":950,"points":[[0,0],[0,-30],[-140,-30],[-140,-294],[-300,-294],[-300,-370]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r14","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["up","left","up","left","up"]},"freeform":{"tag":"Relationship","from":"reportg","fromPort":"top","to":"ui","toPort":"bottom"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"f80dff83e5a138e7bd7216eb3d75de65","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"up"}},"endBinding":{"elementId":"6642dc236e05333f8c01cbb28c56d566","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"down"}},"width":300,"height":370,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":1710029768,"version":5,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":52,"modifiedAt":1782977806947},{"id":"1e3d9c3324977345a8d9070611c460eb","type":"arrow","x":220,"y":444,"points":[[0,0],[-39,0],[-39,-206],[-115,-206],[-115,-24]],"diagramId":"l_LV56mp-DMiOrSYKu5k","diagramEntityId":"r15","backgroundColor":"transparent","fillStyle":"solid","strokeSharpness":"elbow","roughness":0,"opacity":100,"arrowHeadSize":12,"cardinalElbowData":{"isEnabled":true,"preferredSegmentDirections":["left","up","left","down"]},"freeform":{"tag":"Relationship","from":"ui","fromPort":"left","to":"user","toPort":"top"},"strokeColor":"#1c1c1c","strokeWidth":0.75,"strokeStyle":"solid","startArrowhead":null,"endArrowhead":"triangle","lastCommittedPoint":null,"startBinding":{"elementId":"6642dc236e05333f8c01cbb28c56d566","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"left"}},"endBinding":{"elementId":"d63b2601c6ab5a84f477c14770659679","bindingType":"portOrCenter","portLocationOptions":{"portLocation":"varying.CardinalDirection","preferredDirection":"up"}},"width":115,"height":206,"angle":0,"groupIds":[],"lockedGroupId":null,"seed":2017952952,"version":4,"isDeleted":false,"compound":{"type":"parent","containerType":"freeform-relationship"},"zIndex":11,"modifiedAt":1782977806947}],"diagramMetadata":{"settings":{},"diagramType":"freeform-diagram","diagramId":"l_LV56mp-DMiOrSYKu5k","entitySettings":{}}}
---

## Document Ingestion Pipeline

The ingestion pipeline converts cybersecurity policy documents into structured, machine-readable data for future compliance assessment against NIST CSF 2.0.

### Supported Formats

* PDF (.pdf)
* DOCX (.docx)
* TXT (.txt)

### Not Supported

* Images (.png, .jpg, .jpeg)
* Scanned/Image-based PDFs (OCR support planned in future versions)

### Workflow

Policy Document
→ Parsing
→ Text Cleaning
→ Chunk Generation
→ JSON Output
→ Embedding Ready Data

### Implemented Components

* PDF Parser
* DOCX Parser
* TXT Parser
* Text Cleaning Module
* Chunk Generation Module
* Processing Summary Report

### Output Locations

* Parsed Documents: `data/parsed_docs/`
* Generated Chunks: `data/chunks/`
* Processing Statistics: `data/outputs/processing_summary.json`

### Next Phase

The generated chunks will be used for embedding creation, ChromaDB storage, semantic retrieval, and NIST CSF 2.0 compliance assessment.


# Folder Description

| Folder/File | Purpose |
|------------|----------|
| data/raw_docs | Original policy documents |
| data/parsed_docs | Extracted text from documents |
| data/chunks | Generated text chunks |
| data/chroma_db | ChromaDB vector database |
| data/outputs | Assessment outputs and reports |
| frameworks | NIST controls and assessment definitions |
| src/ingestion | Document parsing logic |
| src/chunking | Text chunking logic |
| src/embeddings | Embedding generation logic |
| src/retrieval | Semantic retrieval logic |
| src/llm | LLM assessment logic |
| src/scoring | Compliance scoring engine |
| src/reporting | Report generation logic |
| notebooks | Prototypes and experimentation |
| run_assessment.py | Main execution script |

---

# Expected Workflow

## Step 1: Document Ingestion

Policy documents are uploaded and stored in the raw document repository.

## Step 2: Parsing

Documents are parsed and converted into clean text.

## Step 3: Chunking

Text is divided into smaller overlapping chunks.

## Step 4: Embedding Generation

Each chunk is converted into vector embeddings using a local embedding model.

## Step 5: Vector Storage

Embeddings are stored inside ChromaDB.

## Step 6: Evidence Retrieval

Relevant policy evidence is retrieved for each NIST control.

## Step 7: Compliance Assessment

The LLM evaluates retrieved evidence against control requirements.

## Step 8: Scoring

Controls are assigned compliance statuses.

## Step 9: Reporting

A final compliance assessment report is generated.

---

### Retrieval-Augmented Generation (RAG)

This project follows a Retrieval-Augmented Generation (RAG) approach for cybersecurity compliance assessment.

Workflow:

Policy Documents
        ↓
Document Parsing
        ↓
Text Cleaning
        ↓
Chunk Generation
        ↓
Embeddings (all-MiniLM-L6-v2)
        ↓
ChromaDB Vector Storage
        ↓
NIST CSF Control Query Generation
        ↓
Top-K Evidence Retrieval
        ↓
Compliance Assessment

Instead of sending entire policy documents to an LLM, the system first retrieves the most relevant evidence chunks from organizational policy documents. This improves accuracy, traceability, and explainability of compliance assessments.

Current Scope:
- PDF, DOCX, and TXT policy documents are supported.
- Text-based documents only.
- Scanned PDFs and image-based documents are not supported because OCR is outside the current project scope.

Future Work:
- OCR support for scanned documents.
- Hybrid retrieval (keyword + vector search).
- LLM-based evidence summarization.
- Automated compliance scoring.

# Assessment Status Categories

The assessment engine classifies controls into four categories:

### Compliant

Sufficient evidence exists demonstrating that the control is implemented.

### Partially Compliant

Some evidence exists, but implementation is incomplete or weak.

### Non-Compliant

No meaningful evidence exists showing implementation of the control.

### Not Enough Evidence

Available documents do not provide enough information to make a determination.

---
## Compliance Assessment Flow

1. Load NIST CSF 2.0 controls
2. Retrieve evidence from policy documents
3. Assess compliance status
      Compliant
      Partially Compliant
      Non-Compliant
Not Enough Evidence
4. Calculate deterministic confidence score
5. Generate recommendations for missing evidence.
6. Save assessment results
7. Generate framework report
8. Create traceability logs


## Output Artifacts
framework_assessment.json
framework_report.csv
traceability_log.json

# Expected Output

The final compliance engine should generate:

- Overall compliance score
- Control-by-control assessment
- Supporting evidence references
- Document source information
- Confidence scores
- Missing evidence identification
- Compliance recommendations

---

# Future Enhancements

Future versions may include:

- Advanced control scoring
- Multi-framework support
- Automated remediation suggestions
- Interactive dashboards
- Cloud deployment options
- Continuous compliance monitoring
-Future versions of the system may incorporate OCR-based processing using tools such as:

* Tesseract OCR
* EasyOCR
* PaddleOCR

This will allow the engine to assess scanned documents and image-based policies in addition to text-based documents.

---

### Retrieval Evaluation

The retrieval pipeline is evaluated using:

- Hit Rate@5
- Precision@5
- Recall@5
- Mean Reciprocal Rank (MRR)

These metrics help measure how effectively the system retrieves relevant evidence for NIST CSF 2.0 controls from the policy document corpus.

# Conclusion

The Offline LLM-Based Cybersecurity Compliance Engine demonstrates how Retrieval-Augmented Generation (RAG), local vector databases, and locally hosted language models can be used to automate cybersecurity policy compliance assessments while maintaining complete data privacy and offline operability. The project provides a scalable foundation for evidence-driven compliance evaluation aligned with the NIST Cybersecurity Framework 2.0.
