from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentChunker:
    "Splits documents into overlapping chunks."

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
        )

    def split(self, documents):
        return self.splitter.split_documents(documents)