# src/assessment/compliance_prompt.py

def build_compliance_prompt(
    control_id,
    control_description,
    expected_evidence,
    retrieved_chunks
):
    """
    Build compliance assessment prompt for Phi3.
    """

    evidence_text = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a cybersecurity compliance assessor.

Control ID:
{control_id}

Control Description:
{control_description}

Expected Evidence:
{expected_evidence}

Retrieved Evidence:
{evidence_text}

Rules:

1. Use ONLY the retrieved evidence.
2. Do NOT assume missing evidence exists.
3. Do NOT invent evidence.
4. Select EXACTLY ONE status from:

- Compliant
- Partially Compliant
- Non-Compliant
- Not Enough Evidence

5. Return ONLY valid JSON.
6. Do not include markdown.
7. Do not include explanations outside JSON.

For each expected evidence item:

1. If evidence exists in the retrieved text,
   add it to found_evidence.

2. If evidence is missing,
   add it to missing_evidence.

3. Determine status using:

   - Compliant
   - Partially Compliant
   - Non-Compliant
   - Not Enough Evidence

4. Generate recommendations only for missing evidence.

Return ONLY valid JSON.

{{
    "status": "",

    "reasoning": "",

    "found_evidence": [],

    "missing_evidence": [],

    "recommendations": []
}}
"""

    return prompt