import ollama

prompt = """
Return ONLY JSON.

{
  "status":"Compliant",
  "reasoning":"test"
}
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
        "num_predict": 100
    }
)

print(response["message"]["content"])