from fastapi import FastAPI
from src.api.site_router import site_router

app = FastAPI()

app.include_router(site_router)
