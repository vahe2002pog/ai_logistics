import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:
    """
    Векторное хранилище для RAG
    (локальные эмбеддинги)
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.texts = []
        self.index = None

    def _embed(self, text: str) -> np.ndarray:
        embedding = self.model.encode(text)
        return embedding.astype("float32")

    def add(self, text: str):
        embedding = self._embed(text)

        if self.index is None:
            self.index = faiss.IndexFlatL2(len(embedding))

        self.texts.append(text)
        self.index.add(np.array([embedding]))

    def search(self, query: str, k: int = 3):
        if self.index is None:
            return []

        query_embedding = self._embed(query)
        _, indices = self.index.search(
            np.array([query_embedding]), k
        )

        return [self.texts[i] for i in indices[0]]
