from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import manufacturer_controller
from Schemas.manufacturer_schema import (
    ManufacturerCreateSchema,
    ManufacturerUpdateSchema
)

router = APIRouter()

# Create manufacturer
@router.post("/manufacturer")
def create_manufacturer(data: ManufacturerCreateSchema, db: Session = Depends(get_db)):
    return manufacturer_controller.create_manufacturer(data, db)

# Get manufacturer profile
@router.get("/manufacturer/{manufacturer_id}")
def get_manufacturer(manufacturer_id: int, db: Session = Depends(get_db)):
    return manufacturer_controller.get_manufacturer(manufacturer_id, db)

# Update manufacturer profile
@router.put("/manufacturer/{manufacturer_id}")
def update_manufacturer(
    manufacturer_id: int,
    data: ManufacturerUpdateSchema,
    db: Session = Depends(get_db)
):
    return manufacturer_controller.update_manufacturer(manufacturer_id, data, db)

# Delete manufacturer
@router.delete("/manufacturer/{manufacturer_id}")
def delete_manufacturer(manufacturer_id: int, db: Session = Depends(get_db)):
    return manufacturer_controller.delete_manufacturer(manufacturer_id, db)

# Get products by manufacturer (RELATION API)
@router.get("/manufacturer/{manufacturer_id}/products")
def get_products_by_manufacturer(manufacturer_id: int, db: Session = Depends(get_db)):
    return manufacturer_controller.get_products_by_manufacturer(manufacturer_id, db)
