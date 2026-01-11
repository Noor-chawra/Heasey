from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import order_controller
from Schemas.order_schema import OrderCreateSchema

router = APIRouter()

# Place order
@router.post("/order")
def place_order(data: OrderCreateSchema, db: Session = Depends(get_db)):
    return order_controller.place_order(data, db)

# Order history
@router.get("/order/customer/{customer_id}")
def order_history(customer_id: int, db: Session = Depends(get_db)):
    return order_controller.order_history(customer_id, db)

# Get all orders
@router.get("/order")
def get_all_orders(db: Session = Depends(get_db)):
    return order_controller.get_all_orders(db)

# Cancel order
@router.delete("/order/{order_id}")
def cancel_order(order_id: int, db: Session = Depends(get_db)):
    return order_controller.cancel_order(order_id, db)
