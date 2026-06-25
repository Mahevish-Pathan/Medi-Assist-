from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

import os


class DocumentLoader:

    def load_document(self, file_path):

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)

        elif file_path.endswith(".txt"):
            loader = TextLoader(file_path)

        elif file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)

        else:
            raise ValueError(
                "Unsupported file format"
            )

        documents = loader.load()

        return documents