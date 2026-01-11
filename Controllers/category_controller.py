from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Category, Product

# ------------- Create Category-----------------------------------
def create_category(data, db: Session):
    existing = db.query(Category).filter(Category.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")

    category = Category(name=data.name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return {"message": "Category created successfully"}

# --------------- Get All Categories----------------------------
def get_all_categories(db: Session):
    return db.query(Category).all()

# ------------------------------------Get Products by Category (RELATION)-----------------------------------------
def get_products_by_category(category_id: int, db: Session):
    products = db.query(Product).filter(Product.category_id == category_id).all()
    return products
