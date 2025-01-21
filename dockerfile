FROM python:3.12-slim

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirments.txt

COPY . .

HEALTHCHECK --interval=30m --timeout=5s --retries=3 CMD  ["python", "main.py"]

CMD  ["python", "main.py"]
