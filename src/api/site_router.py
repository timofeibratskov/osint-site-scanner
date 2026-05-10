from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from src.services.scan_service import scan_site
from src.db.database import SessionLocal
from src.schemas.site_schema import SiteCreate, SiteResponse, SiteDetailsResponse
from src.db.models import Site

site_router = APIRouter(prefix="/sites", tags=["Sites"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@site_router.post("/", response_model=SiteResponse)
def create(site: SiteCreate, db: Session = Depends(get_db)):
    exists_site = db.query(Site).filter(Site.domain == site.domain).first()

    if exists_site:
        raise HTTPException(
            status_code=400,
            detail="already exists!"
        )

    new_site = Site(domain=site.domain)
    db.add(new_site)
    db.commit()
    db.refresh(new_site)

    return new_site


@site_router.get("/", response_model=list[SiteResponse])
def find_all(db: Session = Depends(get_db)):
    return db.query(Site).all()


@site_router.get("/{site_id}", response_model=SiteDetailsResponse)
def find_by_id(site_id: int, db: Session = Depends(get_db)):
    site = (db.query(Site).filter(Site.id == site_id).first())
    if not site:
        raise HTTPException(status_code=404, detail="not found!")
    return site


@site_router.delete("/{site_id}")
def delete(site_id: int, db: Session = Depends(get_db)):
    site = db.query(Site).filter(Site.id == site_id).first()
    if site:
        db.delete(site)
        db.commit()
    if not site:
        raise HTTPException(status_code=404, detail="not found!")
    return {"message": "deleted"}


@site_router.post("/{site_id}/scan")
async def start_scan(site_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(scan_site, site_id)
    return {"message": "Сканирование запущено", "status": "processing"}
