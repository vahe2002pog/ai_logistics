from dataclasses import dataclass

@dataclass
class Parcel:
    tracking_number: str
    name: str
    weight: float
    client_fio: str
    sender_name: str
    origin: str
    destination: str
    status: str

    def to_text(self) -> str:
        """
        Текстовое представление для RAG
        """
        return (
            f"Номер отслеживания: {self.tracking_number}. "
            f"Наименование: {self.name}. "
            f"Вес: {self.weight} кг. "
            f"Клиент: {self.client_fio}. "
            f"Отправитель: {self.sender_name}. "
            f"Пункт отправления: {self.origin}. "
            f"Пункт назначения: {self.destination}. "
            f"Статус: {self.status}."
        )
