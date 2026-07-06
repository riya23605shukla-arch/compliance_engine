from src.assessment.framework_assessor import assess_framework
from src.assessment.save_assessment import save_assessments
from src.assessment.report_generator import generate_report
from src.assessment.traceability_logger import save_traceability_log

from src.retrieval.chroma_manager import get_collection

# ==========================================
# LOAD CHUNKS FROM CHROMADB
# ==========================================

collection = get_collection()

data = collection.get()

retrieved_chunks = []

documents = data.get("documents", [])
metadatas = data.get("metadatas", [])

for i, doc in enumerate(documents):

    metadata = {}

    if i < len(metadatas):
        metadata = metadatas[i]

    retrieved_chunks.append(
        {
            "text": doc,
            "metadata": metadata
        }
    )

print(f"\nRetrieved {len(retrieved_chunks)} chunks from ChromaDB\n")

# ==========================================
# RUN ASSESSMENT
# ==========================================

results = assess_framework(
    retrieved_chunks
)

save_assessments(results)

generate_report(results)

save_traceability_log(results)

# ==========================================
# PRINT RESULTS
# ==========================================

for item in results:

    print(
        item["control_id"],
        item["status"],
        item["confidence"]
    )