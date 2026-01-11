from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import review_controller
from Schemas.review_schema import ReviewCreateSchema

router = APIRouter()

# Create review
@router.post("/review")
def create_review(data: ReviewCreateSchema, db: Session = Depends(get_db)):
    return review_controller.create_review(data, db)

# Get reviews by product
@router.get("/review/product/{product_id}")
def reviews_by_product(product_id: int, db: Session = Depends(get_db)):
    return review_controller.get_reviews_by_product(product_id, db)

# Get reviews by customer
@router.get("/review/customer/{customer_id}")
def reviews_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return review_controller.get_reviews_by_customer(customer_id, db)
