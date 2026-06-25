# src/assessment/llm_assessor.py

import ollama


def assess_with_phi3(prompt):

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
            "num_predict": 300
        }
    )

    return response["message"]["content"]