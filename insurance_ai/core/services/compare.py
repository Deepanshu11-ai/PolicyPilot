def compare_policies(p1, p2):
    from langchain_groq import ChatGroq
    from .utils import get_context

    context1 = get_context("coverage exclusions conditions", p1)
    context2 = get_context("coverage exclusions conditions", p2)

    llm = ChatGroq(
        api_key="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",
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
Compare two insurance policies.

Return STRICT JSON ONLY:

{{
  "better_policy": "Policy 1 or Policy 2",
  "verdict": "short explanation",
  "differences": [
    "key difference 1",
    "key difference 2"
  ]
}}

Policy 1:
{context1}

Policy 2:
{context2}
"""

    return llm.invoke(prompt).content