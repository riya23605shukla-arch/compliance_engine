# src/assessment/recommendation_generator.py

def generate_recommendations(
    missing_evidence
):
    """
    Generate recommendations
    from missing evidence.
    """

    recommendations = []

    for item in missing_evidence:

        recommendations.append(
            f"Implement and document {item}."
        )

    return recommendations