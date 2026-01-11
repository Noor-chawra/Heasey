from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Brand, Product

# ======================== Create Brand ========================
def create_brand(data, db: Session):
    brand = db.query(Brand).filter(Brand.name == data.name).first()
    if brand:
        raise HTTPException(status_code=400, detail="Brand already exists")

    new_brand = Brand(name=data.name)
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return {"message": "Brand created successfully"}

# ======================== Get All Brands ========================
def get_all_brands(db: Session):
    return db.query(Brand).all()

# ======================== Get Products by Brand (RELATION) ========================
def get_products_by_brand(brand_id: int, db: Session):
    products = db.query(Product).filter(Product.brand_id == brand_id).all()
    return products
