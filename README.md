````markdown
# Weather API

Weather API — это приложение на основе FastAPI, которое предоставляет прогноз погоды для указанного города. Приложение использует шаблоны HTML для отображения данных на фронтенде.

## Функционал

- Получение прогноза погоды по названию города.
- Отображение данных о температуре и описании погоды.
- Обработка ошибок, если город не найден.
- Сохранение города в кэше на 10 минут.

## Технологии

- **Python 3.11** — основной язык программирования.
- **FastAPI** — для создания API.
- **Requests** — для выполнения HTTP-запросов.
- **Cachetools** — для кэширования данных.
- **Pytest** — для написания тестов.
- **Docker** — для контейнеризации приложения.

1. Клонирование репозитория

Склонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/Aziret-Khaitkulov/weatherapi.git
cd weatherapi
```
````

## Установка зависимостей

```bash
python -m venv venv
venv\Scripts\activate  # Для Windows
source venv/bin/activate  # Для Linux/Mac
pip install -r requirements.txt
```

3. Запустите приложение с помощью Uvicorn:

```bash
   uvicorn app.main:app --reload
```

## Использование Docker

Если вы хотите запустить приложение в контейнере Docker:

Постройте Docker-образ:

```bash
docker build -t weatherapi .
```

Запустите контейнер:

```bash
docker run -d -p 8000:8000 weatherapi
```

приложение будет доступно по адресу `http://localhost:8000`.

## Структура проекта

````markdown
weatherapi/
├── app/
│ ├── main.py # Основной файл приложения
│ ├── weather.py # Логика получения данных о погоде
│ ├── models.py # Модели данных
├── templates/
│ ├── index.html # HTML-шаблон для отображения данных
├── tests/
│ ├── test_weather.py # Тесты для проверки функциональности API
├── .gitignore # Файлы и папки, игнорируемые Git
├── Dockerfile # Конфигурация для контейнеризации приложения
├── requirements.txt # Список зависимостей Python

# Тестирование

## Как запустить тесты.

```bash
pytest
```
````
