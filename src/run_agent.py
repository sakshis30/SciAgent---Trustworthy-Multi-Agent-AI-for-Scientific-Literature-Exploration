from pathlib import Path
from parser import PDFParser
from chunker import DocumentChunker
from embedder import Embedder
from vector_store import VectorStore
from llm import OllamaLLM
from core.sci_agent import SciAgent

from config import (
    PAPERS_FOLDER,
    VECTOR_STORE_PATH,
)

def initialize_agent():

    parser = PDFParser(PAPERS_FOLDER)

    documents = parser.load()
    print("\n First page")
    print(documents[0].page_content[:1000])

    chunker = DocumentChunker()

    chunks = chunker.split(documents)

    embedder = Embedder()

    index_file = Path(VECTOR_STORE_PATH) / "index.faiss"

    if index_file.exists():

        print("Loading existing FAISS index...")

        vector_db, chunks = VectorStore.load(
            VECTOR_STORE_PATH
        )

    else:

        print("Creating FAISS index...")

        embeddings = embedder.encode(chunks)

        vector_db = VectorStore(
            dimension=embeddings.shape[1]
        )

        vector_db.add_embeddings(embeddings)

        vector_db.save(
            VECTOR_STORE_PATH,
            chunks
        )

        print("FAISS index saved.")

    llm = OllamaLLM()

    return SciAgent(
        vector_db,
        embedder,
        chunks,
        llm
    )