from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import brand_controller
from Schemas.brand_schema import BrandCreateSchema

router = APIRouter()

# ======================== Create Brand ========================
@router.post("/brand")
def create_brand(data: BrandCreateSchema, db: Session = Depends(get_db)):
    return brand_controller.create_brand(data, db)

# ======================== Get All Brands ========================
@router.get("/brand")
def get_all_brands(db: Session = Depends(get_db)):
    return brand_controller.get_all_brands(db)

# ======================== Get Products by Brand ========================
@router.get("/brand/{brand_id}/products")
def get_products_by_brand(brand_id: int, db: Session = Depends(get_db)):
    return brand_controller.get_products_by_brand(brand_id, db)
