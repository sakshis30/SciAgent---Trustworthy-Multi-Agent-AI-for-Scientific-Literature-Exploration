from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader


class PDFParser:
    """Loads one or more PDF papers."""

    def __init__(self, papers_folder):
        self.papers_folder = Path(papers_folder)


    def load(self):

        if not self.papers_folder.exists():
            raise FileNotFoundError(
                f"Paper folder not found: {self.papers_folder}"
            )


        documents = []

        pdf_files = list(
            self.papers_folder.glob("*.pdf")
        )


        if len(pdf_files) == 0:
            raise ValueError(
                "No PDF files found."
            )


        for pdf in pdf_files:

            loader = PyMuPDFLoader(
                str(pdf)
            )

            docs = loader.load()


            for doc in docs:

                doc.metadata["paper"] = pdf.name

                # Convert zero-indexed page to human page number
                doc.metadata["page"] = (
                    doc.metadata.get("page", 0) + 1
                )


            documents.extend(docs)


        print(
            f"Loaded {len(pdf_files)} papers "
            f"with {len(documents)} pages."
        )


        return documents