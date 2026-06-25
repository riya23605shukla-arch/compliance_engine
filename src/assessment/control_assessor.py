# src/assessment/control_assessor.py

from src.assessment.scoring import (
    calculate_confidence
)


COMPLIANT = "Compliant"

PARTIALLY_COMPLIANT = "Partially Compliant"

NON_COMPLIANT = "Non-Compliant"

NOT_ENOUGH_EVIDENCE = "Not Enough Evidence"


def assess_control(
    control_id,
    control_description,
    expected_evidence,
    retrieved_chunks
):

    print("\n-----------------------------------")
    print("Assessing Control:", control_id)
    print("-----------------------------------")

    combined_text = " ".join(

        chunk["text"]

        for chunk in retrieved_chunks

    ).lower()

    found_evidence = []

    missing_evidence = []

    for evidence in expected_evidence:

        if evidence.lower() in combined_text:

            found_evidence.append(
                evidence
            )

        else:

            missing_evidence.append(
                evidence
            )

    confidence = calculate_confidence(

        len(found_evidence),

        len(expected_evidence)
    )

    if len(found_evidence) == len(expected_evidence):

        status = COMPLIANT

    elif len(found_evidence) > 0:

        status = PARTIALLY_COMPLIANT

    elif len(retrieved_chunks) == 0:

        status = NOT_ENOUGH_EVIDENCE

    else:

        status = NON_COMPLIANT

    recommendations = []

    for item in missing_evidence:

        recommendations.append(

            f"Provide evidence for: {item}"

        )

    reasoning = (

        f"{len(found_evidence)} of "

        f"{len(expected_evidence)} "

        f"expected evidence items "

        f"were found."
    )

    return {

        "status":
            status,

        "reasoning":
            reasoning,

        "found_evidence":
            found_evidence,

        "missing_evidence":
            missing_evidence,

        "recommendations":
            recommendations
    }