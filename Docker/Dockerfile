# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files
COPY requirements.txt .
COPY main.py .
COPY color_palette.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the script with arguments
ENTRYPOINT ["python", "main.py"]