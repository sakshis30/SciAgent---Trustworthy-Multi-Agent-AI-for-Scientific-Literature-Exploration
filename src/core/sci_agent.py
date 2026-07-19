from agents.retrieval_agent import RetrievalAgent
from agents.reasoning_agent import ReasoningAgent
from agents.verification_agent import VerificationAgent


class SciAgent:

    def __init__(self, vector_db, embedder, chunks, llm):

        self.retriever = RetrievalAgent(
            vector_db,
            embedder,
            chunks
        )

        self.reasoner = ReasoningAgent(llm)

        self.verifier = VerificationAgent(llm)

    def answer(self, question):

        # Retrieve relevant chunks
        docs = self.retriever.retrieve(question)

        # Generate answer
        draft = self.reasoner.answer(question, docs)

        # Verify answer
        verification = self.verifier.verify(
            question,
            draft,
            docs
        )

        # Build citations
        citations = []

        for doc in docs:

            citations.append(
                {
                    "paper": doc.metadata.get("paper", "Unknown"),
                    "page": doc.metadata.get("page", 0),
                    "distance": doc.metadata.get("distance", 0)
                }
            )

        return {
            "draft": draft,
            "verification": verification,
            "citations": citations,
            "documents": docs
        }