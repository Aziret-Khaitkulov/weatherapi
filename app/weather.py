import requests

from app.config import API_KEY, BASE_URL
from app.cache import cache


def get_weather(city: str):
    """Получает данные о погоде по названию города"""

    # Проверяем, есть ли данные в кэше
    if city in cache:
        return cache[city]

    # Формируем параметры запроса
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    # Делаем GET-запрос к OpenWeatherMap
    responce = requests.get(BASE_URL, params=params)

    # Если город не найден, API вернет статус 404
    if responce.status_code != 200:
        return None

    # Преобразуем JSON-ответ в словарь
    data = responce.json()

    # Формируем результат в удобном формате
    result = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }

    # Сохраняем результат в кэше
    cache[city] = result
    return result  # Возвращаем данные
