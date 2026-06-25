import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, project_root)

from app.backend.rag.embeddings import EmbeddingModel
from app.backend.rag.vectordb import VectorDatabase
from app.backend.rag.retriever import Retriever

embedding_model = EmbeddingModel()

vector_db = VectorDatabase()

vector_db.load_index()

retriever = Retriever(
    vector_db,
    embedding_model
)

query = input("Ask Question: ")

results = retriever.retrieve(
    query,
    k=5
)

for i, (doc, score) in enumerate(results):

    print("\n")
    print("=" * 70)

    print(f"Result {i+1}")

    print(f"Distance Score: {score}")

    print(doc.page_content[:500])