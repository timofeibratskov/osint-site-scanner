from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import SessionLocal
from src.schemas.site_schema import SiteCreate, SiteResponse
from src.services.site_service import *

router = APIRouter(prefix="/sites", tags=["Sites"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SiteResponse)
def create(site: SiteCreate, db: Session = Depends(get_db)):
    return create_site(db, site.url)


@router.get("/", response_model=list[SiteResponse])
def find_all(db: Session = Depends(get_db)):
    return get_all_sites(db)


@router.get("/{site_id}", response_model=SiteResponse)
def find_by_id(site_id: int, db: Session = Depends(get_db)):
    site = get_site_by_id(db, site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site


@router.delete("/{site_id}")
def delete(site_id: int, db: Session = Depends(get_db)):
    site = delete_site(db, site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return {"message": "deleted"}