def detect_hidden_clauses(policy_id=1):
    from langchain_groq import ChatGroq
    from .utils import get_context

    context = get_context(
        "hidden clauses exclusions limitations fine print",
        policy_id
    )

    if not context:
        return '{"hidden_clauses":[],"risk_summary":"","severity":"Low"}'

    llm = ChatGroq(
        api_key="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",
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
Find risky clauses.

Return STRICT JSON:

{{
  "hidden_clauses": [],
  "risk_summary": "",
  "severity": "Low/Medium/High"
}}

Context:
{context}
"""

    return llm.invoke(prompt).content