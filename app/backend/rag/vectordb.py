import faiss
import pickle
import numpy as np
import os


class VectorDatabase:

    def __init__(self):

        self.index = None

        self.documents = []

        self.index_path = (
            "data/vector_store/faiss_index.bin"
        )

        self.docs_path = (
            "data/vector_store/documents.pkl"
        )

    def create_index(
        self,
        embeddings,
        documents
    ):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings.astype(
                np.float32
            )
        )

        self.documents = documents

        os.makedirs(
            "data/vector_store",
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(
            self.docs_path,
            "wb"
        ) as f:

            pickle.dump(
                documents,
                f
            )

    def load_index(self):

        self.index = faiss.read_index(
            self.index_path
        )

        with open(
            self.docs_path,
            "rb"
        ) as f:

            self.documents = pickle.load(
                f
            )

    def search(
        self,
        query_embedding,
        k=5
    ):

        distances, indices = (
            self.index.search(
                np.array(
                    [query_embedding]
                ).astype(
                    np.float32
                ),
                k
            )
        )

        results = []

        for idx, score in zip(
            indices[0],
            distances[0]
        ):

            results.append(
                (
                    self.documents[idx],
                    score
                )
            )

        return results