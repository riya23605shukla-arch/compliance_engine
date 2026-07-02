import json

from sentence_transformers import SentenceTransformer

from src.retrieval.chroma_manager import get_collection


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

collection = get_collection()


def retrieve_control_evidence(control_id, top_k=5):
    """
    Returns retrieved evidence for one control.
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

        return []

    query = " ".join(

        selected_control["subcategory"]

        + " "

        + " ".join(selected_control["expected_evidence"])

        + " "

        + " ".join(selected_control["keywords"])

        + " "

        + " ".join(selected_control["assessment_questions"])

    )

    query_embedding = model.encode(query).tolist()

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=top_k

    )

    retrieved_chunks = []

    for i in range(len(results["ids"][0])):

        retrieved_chunks.append({

            "chunk_id": results["ids"][0][i],

            "text": results["documents"][0][i],

            "metadata": results["metadatas"][0][i],

            "distance": results["distances"][0][i]

        })

    return retrieved_chunks