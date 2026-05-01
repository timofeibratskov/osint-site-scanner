from sqlalchemy.orm import Session
from src.db.models import Site

def create_site(db: Session, url: str):
    site = Site(url=url)
    db.add(site)
    db.commit()
    db.refresh(site)
    return site


def get_all_sites(db: Session):
    return db.query(Site).all()


def get_site_by_id(db: Session, site_id: int):
    return db.query(Site).filter(Site.id == site_id).first()


def delete_site(db: Session, site_id: int):
    site = db.query(Site).filter(Site.id == site_id).first()
    if site:
        db.delete(site)
        db.commit()
    return site