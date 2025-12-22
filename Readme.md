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

4. Создание config.py и настройка API-ключа OpenRouter

Создайте config.py со следующим содержанием:
```python
OPENROUTER_API_KEY = "API_KEY"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

LLM_MODEL = "openai/gpt-4o-mini"
```
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
