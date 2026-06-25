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


loader = DocumentLoader()

documents = loader.load_document(
    "data/raw_data/Hospital_Operations.pdf"
)

print("=" * 50)

print("TOTAL PAGES")

print(len(documents))

print("=" * 50)

print(documents[0].page_content[:1000])