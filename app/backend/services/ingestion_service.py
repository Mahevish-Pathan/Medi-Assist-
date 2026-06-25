from app.backend.rag.loader import DocumentLoader
from app.backend.rag.chunker import DocumentChunker
from app.backend.rag.embeddings import EmbeddingModel
from app.backend.rag.vectordb import VectorDatabase


class IngestionService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = DocumentChunker()

        self.embedding_model = EmbeddingModel()

        self.vector_db = VectorDatabase()

    def ingest_document(
        self,
        file_path
    ):

        documents = self.loader.load_document(
            file_path
        )

        chunks = self.chunker.split_documents(
            documents
        )

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        embeddings = (
            self.embedding_model
            .encode_documents(texts)
        )

        self.vector_db.create_index(
            embeddings,
            chunks
        )

        return len(chunks)