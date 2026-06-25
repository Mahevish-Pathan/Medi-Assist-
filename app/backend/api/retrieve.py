from fastapi import APIRouter
from pydantic import BaseModel

from app.backend.rag.embeddings import EmbeddingModel
from app.backend.rag.vectordb import VectorDatabase
from app.backend.rag.retriever import Retriever

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/retrieve")
def retrieve_chunks(
    request: QueryRequest
):

    embedding_model = EmbeddingModel()

    vector_db = VectorDatabase()

    vector_db.load_index()

    retriever = Retriever(
        vector_db,
        embedding_model
    )

    results = retriever.retrieve(
        request.query
    )

    response = []

    for doc, score in results:

        response.append(
            {
                "score": float(score),
                "content": doc.page_content[:1000]
            }
        )

    return response