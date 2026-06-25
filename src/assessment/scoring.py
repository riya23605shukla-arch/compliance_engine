# src/assessment/scoring.py

def calculate_confidence(
    found_requirements,
    total_requirements
):
    """
    Deterministic confidence score.

    Example:
    8 found / 10 expected
    = 0.8
    """

    if total_requirements == 0:
        return 0.0

    return round(
        found_requirements / total_requirements,
        2
    )