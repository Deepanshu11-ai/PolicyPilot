def get_coverage(policy_id=1):
    from langchain_groq import ChatGroq
    from .utils import get_context

    # 🔥 Separate queries
    covered_ctx = get_context(
        "what is covered benefits hospitalization coverage inclusions",
        policy_id
    )

    not_covered_ctx = get_context(
        "exclusions what is not covered limitations",
        policy_id
    )

    conditions_ctx = get_context(
        "waiting period conditions rules policy terms",
        policy_id
    )

    # combine all
    context = "\n\n".join(filter(None, [
        covered_ctx,
        not_covered_ctx,
        conditions_ctx
    ]))

    if not context:
        return '{"covered":[],"not_covered":[],"conditions":[]}'

    llm = ChatGroq(
        api_key="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",
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
Extract insurance details clearly.

VERY IMPORTANT:
- Identify covered items EVEN if small mentions
- Do NOT leave covered empty unless absolutely none

Return STRICT JSON:

{{
  "covered": [],
  "not_covered": [],
  "conditions": []
}}

Context:
{context}
"""

    return llm.invoke(prompt).content