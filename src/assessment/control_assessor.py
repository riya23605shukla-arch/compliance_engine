from sentence_transformers import SentenceTransformer, util
from src.assessment.scoring import calculate_confidence

# ============================================================
# Load Embedding Model
# ============================================================

model = SentenceTransformer("all-MiniLM-L6-v2")

# ============================================================
# Constants
# ============================================================

COMPLIANT = "Compliant"
PARTIALLY_COMPLIANT = "Partially Compliant"
NON_COMPLIANT = "Non-Compliant"
NOT_ENOUGH_EVIDENCE = "Not Enough Evidence"

FULL_MATCH_THRESHOLD = 0.75
PARTIAL_MATCH_THRESHOLD = 0.55


def assess_control(
    control_id,
    control_description,
    expected_evidence,
    retrieved_chunks
):

    print("\n" + "=" * 80)
    print("Assessing Control :", control_id)
    print("=" * 80)

    if len(retrieved_chunks) == 0:

        return {

            "status": NOT_ENOUGH_EVIDENCE,

            "confidence": 0,

            "reasoning": "No retrieved chunks available.",

            "found_evidence": [],

            "missing_evidence": expected_evidence,

            "matched_chunks": [],

            "recommendations": [
                f"Provide evidence for: {e}"
                for e in expected_evidence
            ]

        }

    # ======================================================
    # Prepare Chunks
    # ======================================================

    chunk_texts = [

        chunk["text"]

        for chunk in retrieved_chunks

    ]

    chunk_embeddings = model.encode(

        chunk_texts,

        convert_to_tensor=True

    )

    found_evidence = []

    missing_evidence = []

    matched_chunks = []

    similarity_scores = []
    # ======================================================
    # Semantic Matching
    # ======================================================

    for evidence in expected_evidence:

        evidence_embedding = model.encode(
            evidence,
            convert_to_tensor=True
        )

        scores = util.cos_sim(
            evidence_embedding,
            chunk_embeddings
        )[0]

        best_index = scores.argmax().item()

        best_score = float(
            scores[best_index]
        )

        best_chunk = chunk_texts[
            best_index
        ]

        similarity_scores.append(
            best_score
        )

        print("\n" + "-" * 60)
        print("Expected Evidence :")
        print(evidence)

        print("\nBest Similarity :")
        print(round(best_score, 3))

        print("\nMatched Chunk :")
        print(best_chunk[:300])

        print("-" * 60)

        if best_score >= FULL_MATCH_THRESHOLD:

            found_evidence.append(
                evidence
            )

            matched_chunks.append({

                "expected_evidence": evidence,

                "similarity": round(
                    best_score,
                    3
                ),

                "matched_text": best_chunk

            })

        elif best_score >= PARTIAL_MATCH_THRESHOLD:

            found_evidence.append(
                evidence + " (Semantic Match)"
            )

            matched_chunks.append({

                "expected_evidence": evidence,

                "similarity": round(
                    best_score,
                    3
                ),

                "matched_text": best_chunk

            })

        else:

            missing_evidence.append(
                evidence
            )
     # ======================================================
    # Confidence Calculation (Semantic Based)
    # ======================================================

    total = len(expected_evidence)

    found = len(found_evidence)

    if similarity_scores:

        average_similarity = sum(similarity_scores) / len(similarity_scores)

        confidence = round(average_similarity, 2)

    else:

        confidence = 0

    if confidence >= 0.80:

        status = COMPLIANT

    elif confidence >= 0.60:

        status = PARTIALLY_COMPLIANT

    elif len(retrieved_chunks) == 0:

        status = NOT_ENOUGH_EVIDENCE

    else:

        status = NON_COMPLIANT

    # ======================================================
    # Recommendations
    # ======================================================

    recommendations = []

    for item in missing_evidence:

        recommendations.append(
            f"Provide evidence for: {item}"
        )

    # ======================================================
    # Reasoning
    # ======================================================

    reasoning = (
        f"{found} of {total} expected evidence items matched. "
        f"Average semantic similarity = {confidence}."
    )

    print("\nSummary")

    print("Found Evidence :", found)

    print("Missing Evidence :", len(missing_evidence))

    print("Confidence :", confidence)

    print("Status :", status)

    # ======================================================
    # Return
    # ======================================================

    return {

        "status": status,

        "confidence": confidence,

        "reasoning": reasoning,

        "found_evidence": found_evidence,

        "missing_evidence": missing_evidence,

        "matched_chunks": matched_chunks,

        "recommendations": recommendations

    }