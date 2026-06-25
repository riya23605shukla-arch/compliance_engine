import ollama


def generate_reasoning(
    control_id,
    found_evidence,
    missing_evidence,
    status
):

    prompt = f"""
Control: {control_id}

Status: {status}

Found Evidence:
{found_evidence}

Missing Evidence:
{missing_evidence}

Provide:

1. Short compliance reasoning

2. Recommendations

Return JSON only:

{{
    "reasoning":"",
    "recommendations":[]
}}
"""

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0,
            "num_predict": 150
        }
    )

    return response["message"]["content"]