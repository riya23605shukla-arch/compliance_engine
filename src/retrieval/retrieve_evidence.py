import json
import chromadb

from sentence_transformers import SentenceTransformer


# Load  sentence transformer embedding model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Connect to ChromaDB

from src.retrieval.chroma_manager import get_collection

collection = get_collection()


# Select NIST Control

control_id = "PR.AA-01"


# Load controls

with open(
    "frameworks/nist_csf_2_mvp.json",
    "r",
    encoding="utf-8"
) as file:

    controls = json.load(file)


# Generate retrieval query

query = ""

for control in controls:

    if control["control_id"] == control_id:

        query = " ".join([
            control["subcategory"],
            " ".join(control["expected_evidence"]),
            " ".join(control["keywords"]),
            " ".join(control["assessment_questions"])
        ])

        break

print("\nGenerated Query:\n")
print(query)

# Convert query to embedding

query_embedding = model.encode(
    query
).tolist()


# Retrieve top 5 chunks
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)


# Display results

for i in range(
    len(results["ids"][0])
):

    print("\n====================")
    print("Result", i + 1)
    print("====================")

    print(
        "Chunk ID:",
        results["ids"][0][i]
    )

    print(
        "Similarity Score:",
        results["distances"][0][i]
    )

    print(
        "Metadata:",
        results["metadatas"][0][i]
    )

    print("\nEvidence:\n")

    print(
        results["documents"][0][i][:700]
    )