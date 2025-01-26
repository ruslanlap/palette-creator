# Dockerfile
FROM python:3.9-slim

# Встановлення системних залежностей
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Створення робочої директорії
WORKDIR /app

# Копіювання необхідних файлів
COPY requirements.txt .
COPY main.py .
COPY color_palette.py .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск скрипта
ENTRYPOINT ["python", "main.py"]