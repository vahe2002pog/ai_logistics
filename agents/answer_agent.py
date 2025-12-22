from typing import List
import re
from utils.openrouter_client import client
from config import LLM_MODEL


class AnswerAgent:
    """
    Агент-ответчик: формирует запрос в LLM и отвечает на основе переданного контекста.
    Возвращает структурированный ответ в едином формате (dict).
    """

    def __init__(self):
        pass

    @staticmethod
    def _extract_tracking(text: str) -> str:
        m = re.search(r"Номер отслеживания:\s*([^\.\s,]+)", text)
        return m.group(1) if m else ""

    def answer(self, context: List[str], user_question: str, keywords: List[str] | None = None) -> dict:
        # Собираем контекст в единый блок текста
        context_text = "\n---\n".join(context)

        prompt = f"""
        Ты — ассистент, который отвечает на вопросы, используя только предоставленный контекст.
        Не добавляй никакой информации, которой нет в контексте. Если в контексте нет ответа,
        честно скажи, что данных недостаточно.

        КОНТЕКСТ:
        {context_text}

        ВОПРОС:
        {user_question}

        ОТВЕТ (коротко и по делу):
        """

        resp = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        answer_text = resp.choices[0].message.content.strip()

        # Собираем релевантные номера отслеживания и короткие сниппеты из контекста
        relevant = []
        for txt in context:
            tn = self._extract_tracking(txt)
            snippet = txt if len(txt) <= 300 else txt[:297] + "..."
            relevant.append({"tracking_number": tn, "snippet": snippet})

        return {
            "answer": answer_text,
            "keywords": keywords or [],
            "relevant_parcels": relevant,
            "used_context_count": len(context),
        }
