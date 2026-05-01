from pydantic import BaseModel

class SiteCreate(BaseModel):
    url: str

class SiteResponse(BaseModel):
    id: int
    url: str

    class Config:
        from_attributes = True