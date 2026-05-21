# device-stats-api

Сервис для сбора и анализа данных с устройств.

## Стек

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Celery + Redis
- Docker + docker-compose

## Запуск

1. Клонировать репозиторий
2. Создать `.env` файл по примеру ниже
3. Запустить: `docker-compose up --build`
4. Применить миграции: `docker-compose exec app poetry run alembic upgrade head`

API доступно на `http://localhost:8000/docs`

## .env пример

DB_USER=postgres
DB_NAME=device_stats
DB_HOST=db
DB_PASS=postgres
DB_PORT=5432
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0

## Эндпоинты

- POST /devices — создать устройство
- POST /devices/{id}/measurements — добавить показание
- GET /devices/{id}/stats — статистика за всё время
- GET /devices/{id}/stats?from_dt=...&to_dt=... — статистика за период
- POST /users — создать пользователя
- GET /users/{id}/stats — статистика по всем устройствам пользователя

## Нагрузочное тестирование

Инструмент: Locust, 10 пользователей

| Эндпоинт | Запросов | Ошибок | Среднее (ms) |
|---|---|---|---|
| POST /devices | 40 | 0 | 12.83 |
| POST /devices/1/measurements | 124 | 0 | 13.17 |
| GET /devices/1/stats | 90 | 0 | 20.9 |
