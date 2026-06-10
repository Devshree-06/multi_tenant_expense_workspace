from python:3.13-slim

WORKDIR /app

COPY requirements.txt .

run pip install --no-cache-dir -r requirements.txt

copy . .

expose 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
