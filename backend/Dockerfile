FROM python:3.11-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die requirements.txt zuerst, um den Cache zu nutzen
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code
COPY . .

# Der Befehl, um die App zu starten (kann in Compose überschrieben werden)
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]