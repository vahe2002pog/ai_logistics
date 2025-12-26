import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Optional


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

    def search(self, query: str, k: Optional[int] = None):
        if self.index is None or len(self.texts) == 0:
            return []

        # Если пользователь не задаёт k или указывает неположительное число,
        # возвращаем все доступные документы
        if k is None or k <= 0:
            k = len(self.texts)

        # Не запрашиваем больше соседей, чем в индексе
        k = min(k, len(self.texts))

        query_embedding = self._embed(query)
        distances, indices = self.index.search(
            np.array([query_embedding]),
            k
        )

        # Фильтруем возможные -1 или некорректные индексы
        result_texts = []
        for idx in indices[0]:
            if idx is None:
                continue
            if idx >= 0 and idx < len(self.texts):
                result_texts.append(self.texts[idx])

        return result_texts
