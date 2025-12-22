import sys
from agents.data_agent import DataAgent

def populate(csv_file: str):
    """
    Загружает данные из CSV и наполняет RAG
    """
    data_agent = DataAgent()
    data_agent.load_from_csv(csv_file)
    print(f"Загружено {len(data_agent.parcels)} посылок из файла {csv_file}")
    return data_agent

def main():
    if len(sys.argv) < 2:
        print("Использование: python populate_csv.py <путь_к_csv>")
        sys.exit(1)

    csv_file = sys.argv[1]
    populate(csv_file)

if __name__ == "__main__":
    main()
