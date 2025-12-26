from typing import List
from utils.openrouter_client import client
from config import LLM_MODEL


class SearchAgent:
    """
    Агент-поисковик для RAG.
    - Вычленяет ключевые слова/фразы из запроса с помощью LLM
    - Выполняет семантический поиск в `DataAgent`/`VectorStore`
    """

    def __init__(self, data_agent):
        self.data_agent = data_agent

    def _extract_keywords(self, user_query: str) -> list[str]:
        prompt = f"""
        Выдели 3-6 ключевых слов или коротких фраз, которые лучше всего подходят
        для семантического поиска по базе данных посылок. Отвечай одним строковым
        списком через запятую, без пояснений.

        Вопрос пользователя:
        {user_query}
        """

        resp = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )

        text = resp.choices[0].message.content.strip()
        # Ожидаем строку с ключевыми словами через запятую, переводим в список
        parts = [p.strip() for p in text.split(",") if p.strip()]
        return parts

    def search(self, user_query: str) -> tuple[list[str], List[str]]:
        """Возвращает кортеж (keywords, релевантные текстовые фрагменты).

        keywords: список строк
        results: список текстовых фрагментов
        """
        keywords = self._extract_keywords(user_query)
        query = ", ".join(keywords) if keywords else user_query

        results = self.data_agent.find_parcels(query)
        return keywords, results
