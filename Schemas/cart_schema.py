from pydantic import BaseModel

class AddToCartSchema(BaseModel):
    customer_id: int
    product_id: int
    quantity: int = 1
