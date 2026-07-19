import faiss
import numpy as np
import pickle
from pathlib import Path


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)


    def add_embeddings(self, embeddings):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)


    def search(self, query_embedding, k=3):

        query_embedding = (
            np.array(query_embedding)
            .astype("float32")
            .reshape(1, -1)
        )

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        return distances, indices


    # -------------------------
    # Save FAISS Index
    # -------------------------

    def save(self, path, chunks):

        path = Path(path)

        path.mkdir(
            parents=True,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            str(path / "index.faiss")
        )

        with open(path / "chunks.pkl", "wb") as f:
            pickle.dump(chunks, f)


    # -------------------------
    # Load FAISS Index
    # -------------------------

    @classmethod
    def load(cls, path):

        path = Path(path)

        index = faiss.read_index(
            str(path / "index.faiss")
        )

        with open(path / "chunks.pkl", "rb") as f:
            chunks = pickle.load(f)

        store = cls(
            index.d
        )

        store.index = index

        return store, chunks