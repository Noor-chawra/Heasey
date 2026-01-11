from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import CartItem

# ------------------------- Add product to cart -----------------------
def add_to_cart(data, db: Session):
    item = db.query(CartItem).filter(
        CartItem.customer_id == data.customer_id,
        CartItem.product_id == data.product_id
    ).first()

    if item:
        item.quantity += data.quantity
    else:
        item = CartItem(
            customer_id=data.customer_id,
            product_id=data.product_id,
            quantity=data.quantity
        )
        db.add(item)

    db.commit()
    return {"message": "Product added to cart"}

# ---------------------- Get cart items (RELATION)------------------------------------------
def get_cart_items(customer_id: int, db: Session):
    return db.query(CartItem).filter(
        CartItem.customer_id == customer_id
    ).all()

# ------------------ Remove / cancel cart item---------------------------------------
def remove_from_cart(cart_item_id: int, db: Session):
    item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item removed from cart"}
