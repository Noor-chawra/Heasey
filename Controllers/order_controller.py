from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Order, OrderItem

# 1️⃣ Place order
def place_order(data, db: Session):
    order = Order(customer_id=data.customer_id)
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in data.items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(order_item)

    db.commit()
    return {"message": "Order placed successfully", "order_id": order.id}

# 2️⃣ Order history (customer → orders)
def order_history(customer_id: int, db: Session):
    return db.query(Order).filter(Order.customer_id == customer_id).all()

# 3️⃣ Get all orders (admin / manufacturer use)
def get_all_orders(db: Session):
    return db.query(Order).all()

# 4️⃣ Cancel order
def cancel_order(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()
    return {"message": "Order cancelled"}
