import json


class VerificationAgent:

    def __init__(self, llm):
        self.llm = llm

    def verify(self, question, answer, retrieved_docs):

        context = "\n\n".join(
            [doc.page_content for doc in retrieved_docs]
        )

        prompt = f"""
You are an evidence verification expert.

Question:
{question}

Retrieved Evidence:
{context}

Generated Answer:
{answer}

Return ONLY valid JSON.

Format:

{{
    "verified": true,
    "confidence": 0.95,
    "report": "...",
    "unsupported_claims": []
}}

Rules:
- confidence must be between 0 and 1.
- report must briefly explain the decision.
- unsupported_claims must always be a list.
- Output ONLY JSON.
"""

        response = self.llm.generate(prompt)

        try:
            result = json.loads(response)
            return result

        except Exception:

            return {
                "verified": False,
                "confidence": 0.0,
                "report": response,
                "unsupported_claims": [
                    "Could not parse verification output."
                ]
            }