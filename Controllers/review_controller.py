from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Review

# 1️⃣ Create review (Customer → Product)
def create_review(data, db: Session):
    review = Review(
        customer_id=data.customer_id,
        product_id=data.product_id,
        rating=data.rating,
        comment=data.comment
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return {"message": "Review added successfully"}

# 2️⃣ Get reviews by product (RELATION)
def get_reviews_by_product(product_id: int, db: Session):
    return db.query(Review).filter(
        Review.product_id == product_id
    ).all()

# 3️⃣ Get reviews by customer (RELATION)
def get_reviews_by_customer(customer_id: int, db: Session):
    return db.query(Review).filter(
        Review.customer_id == customer_id
    ).all()
