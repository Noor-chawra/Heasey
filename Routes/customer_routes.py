from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import customer_controller
from Schemas.customer_schema import CustomerCreateSchema, CustomerUpdateSchema

router = APIRouter()

# Create customer
@router.post("/customer")
def create_customer(data: CustomerCreateSchema, db: Session = Depends(get_db)):
    return customer_controller.create_customer(data, db)

# Get customer profile
@router.get("/customer/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return customer_controller.get_customer(customer_id, db)

# Update customer profile
@router.put("/customer/{customer_id}")
def update_customer(customer_id: int, data: CustomerUpdateSchema, db: Session = Depends(get_db)):
    return customer_controller.update_customer(customer_id, data, db)

# Delete customer
@router.delete("/customer/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return customer_controller.delete_customer(customer_id, db)
