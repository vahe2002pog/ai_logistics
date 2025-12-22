import csv
import random

# Файлы для генерации
cities = ["Москва", "Тюмень", "Ханты-Мансийск", "Сургут", "Екатеринбург", "Нижневартовск"]
names = ["Электроника", "Документы", "Одежда", "Книги", "Игрушки", "Продукты", "Мебель", "Инструменты"]
statuses = ["в пути", "доставлено", "задержка"]
clients = ["Иванов И.И.", "Петров П.П.", "Сидорова А.А.", "Кузнецова Е.В.", "Смирнов А.А.", "Михайлов М.М."]
senders = ["ООО ТехноМир", "АО Партнёр", "ИП Мода", "ООО Библио", "ИП Игрушки", "ООО ДомТовары"]

# Имя CSV-файла
csv_file = "parcels.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Заголовок
    writer.writerow(["tracking_number","name","weight","client_fio","sender_name","origin","destination","status"])
    
    # Генерация 50 записей
    for i in range(1, 51):
        tracking_number = f"YG{100000 + i}"
        name = random.choice(names)
        weight = round(random.uniform(0.3, 5.0), 2)
        client_fio = random.choice(clients)
        sender_name = random.choice(senders)
        origin, destination = random.sample(cities, 2)
        status = random.choice(statuses)
        
        writer.writerow([tracking_number, name, weight, client_fio, sender_name, origin, destination, status])

print(f"CSV-файл '{csv_file}' с 50 записями успешно создан.")
