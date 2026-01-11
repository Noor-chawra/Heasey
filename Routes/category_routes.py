from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import category_controller
from Schemas.category_schema import CategoryCreateSchema

router = APIRouter()

# Create category
@router.post("/category")
def create_category(data: CategoryCreateSchema, db: Session = Depends(get_db)):
    return category_controller.create_category(data, db)

# Get all categories
@router.get("/category")
def get_all_categories(db: Session = Depends(get_db)):
    return category_controller.get_all_categories(db)

# Get products by category (RELATION API)
@router.get("/category/{category_id}/products")
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    return category_controller.get_products_by_category(category_id, db)
