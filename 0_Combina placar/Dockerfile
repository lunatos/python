FROM python:3.12.4-slim

WORKDIR /app

COPY src /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME World

CMD ["python", "script.py"]