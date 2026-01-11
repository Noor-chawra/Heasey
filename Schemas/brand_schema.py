from pydantic import BaseModel

class BrandCreateSchema(BaseModel):
    name: str

class BrandResponseSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
