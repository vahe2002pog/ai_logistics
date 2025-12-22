Инструкция по запуску
1. Создание виртуального окружения
```cmd
python -m venv venv
```
2. Активация виртуального окружения

Windows:
```cmd
venv\Scripts\activate
```

3. Установка зависимостей
```cmd
pip install -r requirements
```

4. Настройка API-ключа OpenRouter

Получить API-ключ:
https://openrouter.ai/keys

Указать ключ в файле config.py.

5. Генерация csv с данными
```cmd
.\venv\Scripts\python.exe ./utils/generate_csv.py
```

6. Запуск приложения
```cmd
.\venv\Scripts\python.exe main.py
```