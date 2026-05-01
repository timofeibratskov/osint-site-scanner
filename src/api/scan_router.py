from fastapi import APIRouter
from src.schemas.site_schema import ScanRequest, ScanResponse
from src.services.scan_service import scan_site

scan_router = APIRouter(prefix="/scan", tags=["Scan"])


@scan_router.post("/", response_model=ScanResponse)
async def scan(request: ScanRequest):
    return await scan_site(request.url)
