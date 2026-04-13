def score_policy(policy_id=1):
    from langchain_groq import ChatGroq
    from .utils import get_context

    context = get_context("coverage exclusions conditions", policy_id)

    llm = ChatGroq(
        api_key="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",  # or env
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
Evaluate insurance policy.

Return STRICT JSON:

{{
  "score": 0-100,
  "summary": "",
  "pros": [],
  "cons": []
}}

Context:
{context}
"""

    return llm.invoke(prompt).content