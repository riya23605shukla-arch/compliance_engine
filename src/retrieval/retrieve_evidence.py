import json

from sentence_transformers import SentenceTransformer

from src.retrieval.chroma_manager import get_collection


# ==========================================================
# Load Embedding Model
# ==========================================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

collection = get_collection()


# ==========================================================
# Retrieve Evidence for One Control
# ==========================================================

def retrieve_control_evidence(control_id, top_k=8):
    """
    Retrieves the Top-K most relevant chunks
    for a single NIST CSF control.
    """

    with open(
        "frameworks/nist_csf_2_mvp.json",
        "r",
        encoding="utf-8"
    ) as file:

        controls = json.load(file)

    selected_control = None

    for control in controls:

        if control["control_id"] == control_id:

            selected_control = control

            break

    if selected_control is None:

        print(f"\nControl {control_id} not found.\n")

        return []

    # ==========================================================
    # Build Retrieval Query
    # ==========================================================

    query = (
        selected_control["subcategory"]
        + " "
        + " ".join(selected_control["expected_evidence"])
        + " "
        + " ".join(selected_control["keywords"])
        + " "
        + " ".join(selected_control["assessment_questions"])
    )

    print("\n" + "=" * 80)
    print("CONTROL :", control_id)
    print("=" * 80)

    print("\nRetrieval Query:\n")
    print(query)

    # ==========================================================
    # Encode Query
    # ==========================================================

    query_embedding = model.encode(
        query
    ).tolist()

    # ==========================================================
    # Retrieve from ChromaDB
    # ==========================================================

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=top_k

    )

    retrieved_chunks = []

    print("\n")
    print("=" * 80)
    print("TOP RETRIEVED CHUNKS")
    print("=" * 80)

    for i in range(len(results["ids"][0])):

        distance = results["distances"][0][i]

        # Ignore poor matches
        if distance > 1.35:
            continue

        metadata = results["metadatas"][0][i]

        document = results["documents"][0][i]

        print("\nRank :", i + 1)

        print(
            "Distance :",
            round(distance, 3)
        )

        print(
            "File :",
            metadata["file_name"]
        )

        print(
            "Page :",
            metadata["page_number"]
        )

        print("\nChunk Preview:\n")

        print(
            document[:350]
        )

        print("-" * 80)

        retrieved_chunks.append({

            "chunk_id": results["ids"][0][i],

            "text": document,

            "metadata": metadata,

            "distance": distance

        })

    print(
        f"\nTotal Retrieved Chunks : {len(retrieved_chunks)}"
    )

    return retrieved_chunks