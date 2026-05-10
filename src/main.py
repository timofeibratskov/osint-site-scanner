from fastapi import FastAPI
from src.api.site_router import site_router
from src.api.scan_router import scan_router

app = FastAPI()

app.include_router(site_router)
app.include_router(scan_router)
