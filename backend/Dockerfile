FROM python:3.11-slim
COPY test.py .
RUN pip install fastapi uvicorn
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]