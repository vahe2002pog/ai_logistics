import csv
from rag.vector_store import VectorStore
from rag.schema import Parcel


class DataAgent:
    """
    Агент данных.
    Отвечает за:
    - загрузку данных о посылках
    - хранение структурированных данных
    - формирование векторного представления (RAG)
    """

    def __init__(self):
        self.vector_store = VectorStore()
        self.parcels: list[Parcel] = []

    def add_parcel(self, parcel: Parcel):
        self.parcels.append(parcel)
        self.vector_store.add(parcel.to_text())

    def load_from_csv(self, file_path: str):
        """
        Загрузка данных о посылках из CSV-файла
        """
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                parcel = Parcel(
                    tracking_number=row["tracking_number"],
                    name=row["name"],
                    weight=float(row["weight"]),
                    client_fio=row["client_fio"],
                    sender_name=row["sender_name"],
                    origin=row["origin"],
                    destination=row["destination"],
                    status=row["status"]
                )
                self.add_parcel(parcel)

    def find_parcels(self, query: str):
        """
        Семантический поиск по данным о посылках
        """
        return self.vector_store.search(query)
