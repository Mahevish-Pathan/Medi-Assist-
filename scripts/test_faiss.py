import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(
    0,
    project_root
)

from app.backend.rag.loader import (
    DocumentLoader
)

from app.backend.rag.chunker import (
    DocumentChunker
)

from app.backend.rag.embeddings import (
    EmbeddingModel
)

from app.backend.rag.vectordb import (
    VectorDatabase
)

loader = DocumentLoader()

documents = loader.load_document(
    "data/raw_data/HOSPITAL_OPERATIONS.pdf"
)

chunker = DocumentChunker()

chunks = (
    chunker.split_documents(
        documents
    )
)

texts = [
    chunk.page_content
    for chunk in chunks
]

embedding_model = (
    EmbeddingModel()
)

embeddings = (
    embedding_model
    .encode_documents(texts)
)

vector_db = (
    VectorDatabase()
)

vector_db.create_index(
    embeddings,
    chunks
)

print(
    "FAISS Index Created Successfully"
)