from src.assessment.compliance_prompt import build_compliance_prompt
from src.assessment.llm_assessor import assess_with_phi3

prompt = build_compliance_prompt(
    control_id="PR.AA-05",
    control_description="Access permissions are managed.",
    expected_evidence=[
        "password policy",
        "access review"
    ],
    retrieved_chunks=[
        "Users must follow password requirements.",
        "Authentication controls are enforced."
    ]
)

result = assess_with_phi3(prompt)

print(result)