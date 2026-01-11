from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Manufacturer, Product

# 1️⃣ Create manufacturer profile
def create_manufacturer(data, db: Session):
    if db.query(Manufacturer).filter(Manufacturer.email == data.email).first():
        raise HTTPException(status_code=400, detail="Manufacturer already exists")

    manu = Manufacturer(
        company_name=data.company_name,
        email=data.email,
        password=data.password
    )
    db.add(manu)
    db.commit()
    db.refresh(manu)
    return {"message": "Manufacturer profile created"}

# 2️⃣ Get manufacturer profile
def get_manufacturer(manufacturer_id: int, db: Session):
    manu = db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if not manu:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return manu

# 3️⃣ Update manufacturer profile
def update_manufacturer(manufacturer_id: int, data, db: Session):
    manu = db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if not manu:
        raise HTTPException(status_code=404, detail="Manufacturer not found")

    if data.company_name:
        manu.company_name = data.company_name
    if data.email:
        manu.email = data.email

    db.commit()
    return {"message": "Manufacturer profile updated"}

# 4️⃣ Delete manufacturer
def delete_manufacturer(manufacturer_id: int, db: Session):
    manu = db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if not manu:
        raise HTTPException(status_code=404, detail="Manufacturer not found")

    db.delete(manu)
    db.commit()
    return {"message": "Manufacturer deleted"}

# 5️⃣ Get products by manufacturer (RELATION)
def get_products_by_manufacturer(manufacturer_id: int, db: Session):
    return db.query(Product).filter(
        Product.manufacturer_id == manufacturer_id
    ).all()
