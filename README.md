# OSINT Scanner & Domain Analyzer

Автоматизированная система для сбора данных о доменах и анализа безопасности.

## 🛠 Требования

Для работы проекта вам понадобятся:
* **Python 3.10+**
* **Docker & Docker Compose** (только для базы данных)
* **Pip** (менеджер пакетов Python)

## 📦 Подготовка окружения

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/timofeibratskov/osint-site-scanner.git](https://github.com/timofeibratskov/osint-site-scanner.git)
   cd osint-scanner
   ```
2. **Создайте и активируйте виртуальное окружение: **
  ```bash
  python -m venv .venv
  # Windows:
  .venv\Scripts\activate
  # Linux/Mac:
  source .venv/bin/activate
```
3. **Установите зависимости: **
  ```bash
  pip install -r requirements.txt
```
## 🚀 Запуск приложения
Проект запускается в три этапа. Не нарушайте последовательность.

**Этап 1: База данных (Docker)**
1. Запустите контейнер с базой данных PostgreSQL:

```bash
docker-compose up -d
```
База будет доступна на порту 5432 (или твоем порту).

2. Инициализация таблиц:
Так как проект использует "чистый" SQL для структуры, необходимо создать таблицы вручную. Для этого:

Подключитесь к вашей БД (через DBeaver, pgAdmin или терминал).

Скопируйте содержимое файла DBscripts.sql (лежит в корне проекта).

Выполните (Run) этот SQL-запрос в консоли вашей базы данных.

Это создаст таблицы sites и scans, а также настроит связи между ними.

**Этап 2: Backend API (Терминал №1)**
Откройте первый терминал, активируйте venv и запустите сервер:

```bash
 uvicorn src.main:app --reload
```
API будет доступно по адресу: http://127.0.0.1:8000

Этап 3: Интерфейс Flet (Терминал №2)
Откройте второй терминал, активируйте venv и запустите GUI:

```bash
python -m src.ui.main
```
