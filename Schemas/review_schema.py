from pydantic import BaseModel

class ReviewCreateSchema(BaseModel):
    customer_id: int
    product_id: int
    rating: int
    comment: str
