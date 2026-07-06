import json

from src.assessment.control_assessor import (
    assess_control
)

from src.assessment.scoring import (
    calculate_confidence
)


def load_controls():

    with open(
        "frameworks/nist_csf_2_mvp.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def assess_framework(
    retrieved_chunks
):

    controls = load_controls()

    results = []

    for control in controls:

        assessment = assess_control(

            control["control_id"],

            control["subcategory"],

            control["expected_evidence"],

            retrieved_chunks
        )

        expected_count = len(
            control["expected_evidence"]
        )

        found_count = len(

            assessment.get(
                "found_evidence",
                []
            )
        )

        confidence = assessment["confidence"]

           

        results.append({

            "control_id":
                control["control_id"],

            "status":
                assessment["status"],

            "confidence":
                confidence,

            "reasoning":
                assessment["reasoning"],

            "found_evidence":
                assessment.get(
                    "found_evidence",
                    []
                ),

            "missing_evidence":
                assessment.get(
                    "missing_evidence",
                    []
                ),

            "recommendations":
                assessment.get(
                    "recommendations",
                    []
                ),
            "matched_chunks":
                 assessment.get(
                    "matched_chunks",
                     []
        )
        })

    return results