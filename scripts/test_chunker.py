import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, project_root)

from app.backend.rag.loader import DocumentLoader
from app.backend.rag.chunker import (
    DocumentChunker
)

loader = DocumentLoader()

documents = loader.load_document(
    "data/raw_data/Standard_Operating_Procedure.pdf"
)

chunker = DocumentChunker()

chunks = chunker.split_documents(
    documents
)

print("=" * 50)

print("TOTAL CHUNKS")

print(len(chunks))

print("=" * 50)

print(chunks[0].page_content)