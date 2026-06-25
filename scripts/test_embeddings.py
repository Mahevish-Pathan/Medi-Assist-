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

model = EmbeddingModel()

vector = model.encode_query(
    "What is hospital admission process?"
)

print(len(vector))