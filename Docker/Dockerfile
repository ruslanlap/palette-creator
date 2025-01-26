FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libcairo2 libcairo2-dev libpango-1.0-0 \
    libpangocairo-1.0-0 gcc pkg-config python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /app/output /app/custom && \
    chmod 777 /app/output /app/custom

CMD ["sh", "-c", "python main.py && cp -r /app/output/* /app/custom/"]