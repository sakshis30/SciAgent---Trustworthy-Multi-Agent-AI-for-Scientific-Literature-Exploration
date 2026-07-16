from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        print("Loading embedding model...")

        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        print("Embedding model loaded.")

    def encode(self, chunks):
        texts = [chunk.page_content for chunk in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True,convert_to_numpy=True)
        return embeddings