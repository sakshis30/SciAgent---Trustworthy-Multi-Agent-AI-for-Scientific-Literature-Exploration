class PromptBuilder:

    @staticmethod
    def build(question, retrieved_docs):
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
        You are a SciAgent, an AI assistant for scientific literature.

        Answer ONLY using the provided context.

        If the answer is not contained in the context,
        say:

        "I cannot find sufficient evidence in the paper."

        Always be factual.
        Do not hallucinate.

        =========================================================
        CONTEXT
        =========================================================

        {context}

        =========================================================
        QUESTION
        =========================================================

        {question}

        =========================================================
        ANSWER
        =========================================================
        """
        return prompt