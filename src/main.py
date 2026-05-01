from fastapi import FastAPI
from src.api.site_router import site_router
from src.api.scan_router import scan_router

# from src.db.database import engine
# from src.db.models import Base
#
# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(site_router)
app.include_router(scan_router)
