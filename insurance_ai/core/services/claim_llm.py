from langchain_groq import ChatGroq


def generate_explanation(scenario, probability, decision, factors):
    llm = ChatGroq(
        api_key="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",
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
You are an insurance expert.

Explain claim approval clearly.

Scenario: {scenario}
Approval Probability: {probability}%
Decision: {decision}

Factors:
{factors}

Explain in simple language:
"""

    return llm.invoke(prompt).content