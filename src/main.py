from parser import PDFParser

def main():

    parser = PDFParser("data/papers/attention_is_all_you_need.pdf")

    documents = parser.load()

    print(f"Loaded {len(documents)} pages.\n")
    print(documents[0].page_content[:1000])

if __name__ == "__main__":
    main()
