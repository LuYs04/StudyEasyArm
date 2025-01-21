FROM python:3.11.11-slim

WORKDIR /app  # Set a specific working directory

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

HEALTHCHECK --interval=30m --timeout=5s --retries=3 CMD ["python", "main.py"]

CMD ["python", "main.py"]
