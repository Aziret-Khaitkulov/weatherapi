from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.weather import get_weather

# Создаем приложение FastAPI
app = FastAPI(title="Weather API",
              description="API для получения прогноза погоды")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/weather", response_class=HTMLResponse)
def weather(request: Request, city: str):
    """Эндпоинт для получения погоды по городу"""
    data = get_weather(city)
    if not data:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Город не найден"})
    return templates.TemplateResponse("index.html", {"request": request, "weather": data})
