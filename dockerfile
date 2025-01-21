FROM python:3.12-slim

# Установим рабочую директорию
WORKDIR /app

# Скопируем файл зависимостей
COPY requirements.txt .

# Установим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем весь исходный код
COPY . .

# Удалим HEALTHCHECK, так как фоновые воркеры обычно не проверяют состояние через порты
# HEALTHCHECK --interval=30m --timeout=5s --retries=3 CMD ["python", "main.py"]

# Основная команда для запуска приложения
CMD ["python", "main.py"]
