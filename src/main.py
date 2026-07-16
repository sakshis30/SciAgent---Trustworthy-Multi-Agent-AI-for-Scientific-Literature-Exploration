from parser import PDFParser
from chunker import DocumentChunker
from embedder import Embedder

def main():

    parser = PDFParser("data/papers/attention_is_all_you_need.pdf")
    documents = parser.load()
    print(f"Loaded {len(documents)} pages.\n")
    #print(documents[0].page_content[:1000])

    chunker = DocumentChunker()
    chunks = chunker.split(documents)
    print(f"Number of chunks: {len(chunks)}\n")
    #print("\nFirst chunk:\n")
    #print(chunks[0].page_content)
    
    embedder = Embedder()
    embeddings = embedder.encode(chunks)
    #print(f"Generated embeddings for {len(embeddings)} chunks.")
    print(embeddings.shape)

if __name__ == "__main__":
    main()
