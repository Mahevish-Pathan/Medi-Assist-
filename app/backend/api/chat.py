from app.backend.mcp_router import handle_mcp_query
from fastapi import APIRouter
from pydantic import BaseModel

from app.backend.rag.embeddings import EmbeddingModel
from app.backend.rag.vectordb import VectorDatabase
from app.backend.rag.retriever import Retriever
from app.backend.services.chat_service import ChatService

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: ChatRequest):
        # Check MCP first

    mcp_result = handle_mcp_query(
        request.query
    )

    if mcp_result:

        return {
            "question": request.query,
            "answer": str(mcp_result),
            "sources": []
        }
    embedding_model = EmbeddingModel()

    # Load vector database
    vector_db = VectorDatabase()
    vector_db.load_index()

    # Create retriever
    retriever = Retriever(
        vector_db=vector_db,
        embedding_model=embedding_model
    )

    # Retrieve relevant chunks
    results = retriever.retrieve(
        request.query
    )

    # Build context
    context = ""

    for doc, score in results:
        context += doc.page_content + "\n\n"

    # Collect sources
    sources = []

    for doc, score in results:

        file_name = doc.metadata.get(
            "source",
            "Unknown"
        )

        page_number = doc.metadata.get(
            "page",
            "N/A"
        )

        sources.append(
            {
                "file": file_name,
                "page": page_number
            }
        )

    # Generate answer
    chat_service = ChatService()

    answer = chat_service.generate_answer(
        request.query,
        context
    )

    # Send response
    response = {
        "question": request.query,
        "answer": answer,
        "sources": sources
    }

    return response