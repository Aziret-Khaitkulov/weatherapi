import time
from fastapi.testclient import TestClient
from app.main import app


# Создаем тестовый клиент на основе FastAPI-приложения
client = TestClient(app)


def test_weather():
    response = client.get("/weather/London")
    assert response.status_code == 200
    assert "temperature" in response.json()
