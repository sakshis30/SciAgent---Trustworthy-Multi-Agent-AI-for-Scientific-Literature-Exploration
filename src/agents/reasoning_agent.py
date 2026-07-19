from prompt_builder import PromptBuilder

class ReasoningAgent:

    def __init__(self, llm):
        self.llm = llm

    def answer(self, question, retrieved_docs):

        print("\n" + "="*80)
        print("RETRIEVED CHUNKS")
        print("="*80)

        for i, doc in enumerate(retrieved_docs):
            print(f"\nChunk {i+1}")
            print(f"Paper : {doc.metadata.get('paper')}")
            print(f"Page  : {doc.metadata.get('page')}")
            print("-"*60)
            print(doc.page_content[:600])

        prompt = PromptBuilder.build(question, retrieved_docs)

        print("\n" + "="*80)
        print("PROMPT SENT TO OLLAMA")
        print("="*80)
        print(prompt[:3000])

        answer = self.llm.generate(prompt)

        print("\n" + "="*80)
        print("LLM ANSWER")
        print("="*80)
        print(answer)

        return answer