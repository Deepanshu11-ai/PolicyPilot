def simulate_scenario(scenario, policy_id=1):
    from langchain_groq import ChatGroq
    from .utils import get_context

    context = get_context(scenario, policy_id)

    llm = ChatGroq(
        api_key="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",  # or env
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
Analyze scenario.

Return ONLY JSON:

{{
  "decision": "Covered/Not Covered",
  "reason": "",
  "risk_level": "Low/Medium/High"
}}

Context:
{context}

Scenario:
{scenario}
"""

    return llm.invoke(prompt).content