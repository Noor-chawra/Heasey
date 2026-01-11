from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
    name: str
    price: float
    description: str
    manufacturer_id: int
    brand_id: int
    category_id: int

class ProductUpdateSchema(BaseModel):
    name: str | None = None
    price: float | None = None
    description: str | None = None
