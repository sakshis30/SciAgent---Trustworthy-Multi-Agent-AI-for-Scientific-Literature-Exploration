class RetrievalAgent:

    def __init__(self, vector_db, embedder, chunks):

        self.vector_db = vector_db
        self.embedder = embedder
        self.chunks = chunks

    def retrieve(self, question, k=3):

        query_embedding = self.embedder.model.encode(
            [question],
            convert_to_numpy=True
        )

        distances, indices = self.vector_db.search(
            query_embedding,
            k=k
        )

        retrieved_docs = []

        for idx, distance in zip(indices[0], distances[0]):

            doc = self.chunks[idx]

            doc.metadata["distance"] = float(distance)

            retrieved_docs.append(doc)

        return retrieved_docs