``` Временное ТЗ (будет рефакториться)
Главное: FastAPI + PostgreSQL + SQLAlchemy 2.0 (async) + JWT авторизация

## Обязательные фичи:
- Регистрация пользователя (email + пароль)
- Логин → выдача JWT токена
- Все роуты только для авторизованных (dependency с JWT)
- CRUD для задач:
    - Создать задачу (title, description, deadline: дата, status: todo/in_progress/done)
    - Список своих задач с пагинацией (limit/offset или page)
    - Обновить задачу
    - Удалить задачу
- Фильтры в списке: по статусу, по дедлайну (просроченные, сегодня и т.д.)

## Техническое must-have:
- Python 3.12 + uv
- FastAPI + uvicorn
- SQLAlchemy 2.0 async + asyncpg
- Alembic для миграций
- Pydantic для валидации
- PyJWT + passlib для хэша паролей
- Loguru для логов
- Docker + docker-compose (api + postgres + возможо frontend)
- .env для конфигов (DATABASE_URL, SECRET_KEY и т.д.)
- Типы везде (Type Hints)
- Минимум 5–10 тестов (pytest + async)

## Структура кода (примерно):
app/
├── main.py          # app = FastAPI(), include routers
├── dependencies.py  # get_current_user, get_db
├── models.py        # User и Task
├── schemas.py       # Pydantic модели
├── crud.py          # функции create/read/update/delete
├── routers/
│   ├── auth.py
│   └── tasks.py
└── utils/           # хэш пароля и т.д.

## Как запустить (должно работать из коробки):
- `docker-compose up -d`
- `alembic upgrade head`
- `uvicorn app.main:app --reload`
Открываешь /docs — всё работает, регистрация, токен, задачи.

## Таски
- [ ] Первый день разработки
    - [ ] Создать базовую структуру routes для FastAPI
    - [ ] Создать ручку /health
    - [ ] Написать рабочий Dockerfile с кэширование
    - [ ] Простой класс для работы с БД (add, get, edit, delete)
    - [ ] ОПЦИОНАЛЬНО: Сделать функцию edit в классе СУБД частичной (чтобы данные можно было обновлять любыми частями, главное передать id записи и id юзера)
    - [ ] Начать разрабатывать класс валидации юзеров (генерация ключа, отправка email, валидацию пароля, проверка токена и тд)
    - [ ] Создать модели данных SqlAlchemy (/users: /auth, /create, /edit, /delete, /get; /tasks: /get, /edit, /add, /delete)
```