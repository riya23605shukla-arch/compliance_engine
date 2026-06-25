import json

from src.assessment.control_assessor import (
    assess_control
)

control_id = "PR.AA-05"

control_description = (
    "Access permissions are managed."
)

expected_evidence = [
    "password policy",
    "access review"
]

retrieved_chunks = [
    {
        "text":
        "Users must follow password requirements. Authentication controls are enforced."
    }
]

result = assess_control(
    control_id,
    control_description,
    expected_evidence,
    retrieved_chunks
)

print(result)