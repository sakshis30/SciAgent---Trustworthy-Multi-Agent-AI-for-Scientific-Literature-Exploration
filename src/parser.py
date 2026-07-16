from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

class PDFParser:
    "Responsible for loading documents"

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)
    
    def load(self):
        "Loads the PDF and returns Langchain documents"

        loader = PyMuPDFLoader(str(self.pdf_path))
        documents = loader.load()

        return documents
        

