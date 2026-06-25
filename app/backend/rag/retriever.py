class Retriever:

    def __init__(
        self,
        vector_db,
        embedding_model
    ):

        self.vector_db = vector_db
        self.embedding_model = embedding_model

    def retrieve(
        self,
        query,
        k=5
    ):

        query_embedding = (
            self.embedding_model
            .encode_query(query)
        )

        results = (
            self.vector_db.search(
                query_embedding,
                k
            )
        )

        return results