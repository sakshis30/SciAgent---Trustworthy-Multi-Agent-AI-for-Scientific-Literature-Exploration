from parser import PDFParser
from chunker import DocumentChunker
from embedder import Embedder
from vector_store import VectorStore
from llm import OllamaLLM
from prompt_builder import PromptBuilder

def main():

    parser = PDFParser("data/papers/attention_is_all_you_need.pdf")
    documents = parser.load()
    #print(f"Loaded {len(documents)} pages.\n")
    #print(documents[0].page_content[:1000])

    chunker = DocumentChunker()
    chunks = chunker.split(documents)
    #print(f"Number of chunks: {len(chunks)}\n")
    #print("\nFirst chunk:\n")
    #print(chunks[0].page_content)
    
    embedder = Embedder()
    embeddings = embedder.encode(chunks)
    #print(f"Generated embeddings for {len(embeddings)} chunks.")
    #print(embeddings.shape)

    vector_db = VectorStore(dimension=embeddings.shape[1])
    vector_db.add_embeddings(embeddings)
    #print("Vector store created and embeddings added.")

    question = input("Ask a question: ")

    query_embedding = embedder.model.encode([question], convert_to_numpy=True)

    distances, indices = vector_db.search(query_embedding, k=3)
    
    retrieved_docs = [chunks[idx] for idx in indices[0]]

    prompt = PromptBuilder.build(question, retrieved_docs)

    llm = OllamaLLM()
    answer = llm.generate(prompt)

    print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()