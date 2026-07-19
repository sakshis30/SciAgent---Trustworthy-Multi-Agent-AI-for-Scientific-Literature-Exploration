class CitationAgent:

    def build_citations(self, retrieved_docs):

        citations = []

        seen = set()

        for doc in retrieved_docs:

            paper = doc.metadata.get("paper", "Unknown")

            page = doc.metadata.get("page", "Unknown")

            key = (paper, page)

            if key not in seen:

                citations.append({
                    "paper": paper,
                    "page": page
                })

                seen.add(key)

        return citations