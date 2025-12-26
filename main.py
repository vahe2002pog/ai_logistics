from agents.data_agent import DataAgent
from agents.analysis_agent import AnalysisAgent
from agents.search_agent import SearchAgent
from agents.answer_agent import AnswerAgent

def main():
    data_agent = DataAgent()
    # загружаем данные о посылках
    try:
        data_agent.load_from_csv("parcels.csv")
    except FileNotFoundError:
        print("Файл parcels.csv не найден — убедитесь, что он в рабочей директории.")

    analysis_agent = AnalysisAgent()
    search_agent = SearchAgent(data_agent)
    answer_agent = AnswerAgent()


    # Семантический поиск всех данных (можно использовать весь контекст)
    context = [p.to_text() for p in data_agent.parcels]

    print("\n=== Чат с аналитическим агентом ===")
    print("Введите вопрос по посылкам (или 'выход' для завершения)")

    while True:
        user_input = input("\nВаш вопрос: ").strip()
        if user_input.lower() in ["выход", "exit", "quit"]:
            print("Завершение работы чата...")
            break

        # Первый шаг: поиск релевантного контекста
        keywords, hits = search_agent.search(user_input)

        if not hits:
            print("\nНичего релевантного не найдено в базе.")
            continue

        # Второй шаг: генерация ответа на основе найденного контекста
        structured = answer_agent.answer(hits, user_input, keywords=keywords)

        # Единый вывод в консоль в стандартизованной форме
        print("\n**Ответ**")
        print(f"{structured.get('answer')}\n")
        # print(f"- **Keywords:** {', '.join(structured.get('keywords', []))}")
        # print(f"- **Used context fragments:** {structured.get('used_context_count')}")
        # print("- **Relevant Parcels:**")
        # for p in structured.get('relevant_parcels', []):
        #     print(f"  - {p.get('tracking_number')}: {p.get('snippet')}")


if __name__ == "__main__":
    main()
