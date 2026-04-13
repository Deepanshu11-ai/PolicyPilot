from langchain_groq import ChatGroq
import json


def extract_features(scenario):
    llm = ChatGroq(
        api_key="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",
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
Extract structured features from this insurance claim scenario.

Scenario:
{scenario}

Return ONLY JSON:

{{
  "claim_type": 1 for accident, 2 for cosmetic, 3 for illness,
  "waiting_period": 0 or 1,
  "covered": 0 or 1
}}

Rules:
- accident/injury → claim_type = 1
- cosmetic/plastic → claim_type = 2
- illness/disease → claim_type = 3
- pre-existing → waiting_period = 1
- if scenario likely covered → covered = 1 else 0
"""

    response = llm.invoke(prompt).content

    try:
        cleaned = response.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned)
    except:
        return {
            "claim_type": 3,
            "waiting_period": 0,
            "covered": 0
        }