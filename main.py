from fastapi import FastAPI

# Создаём экземпляр приложения
app = FastAPI(title="OSINT Diplom API", description="Простой API для диплома")

# Простой GET-запрос
@app.get("/")
def root():
    return {"message": "Hello World!"}

# Ещё один тестовый эндпоинт
@app.get("/ping")
def ping():
    return {"status": "ok", "message": "pong"}

# POST-запрос с телом
@app.post("/echo")
def echo(data: dict):
    return {"received": data}