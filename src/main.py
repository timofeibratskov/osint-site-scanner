from fastapi import FastAPI
from src.api.site_router import router
from src.db.database import engine
from src.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)