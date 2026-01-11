from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Customer

# 1️⃣ Create customer profile
def create_customer(data, db: Session):
    if db.query(Customer).filter(Customer.email == data.email).first():
        raise HTTPException(status_code=400, detail="Customer already exists")

    customer = Customer(
        name=data.name,
        email=data.email,
        password=data.password
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return {"message": "Customer profile created"}

# 2️⃣ Get customer profile
def get_customer(customer_id: int, db: Session):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# 3️⃣ Update customer profile
def update_customer(customer_id: int, data, db: Session):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    if data.name:
        customer.name = data.name
    if data.email:
        customer.email = data.email

    db.commit()
    return {"message": "Customer profile updated"}

# 4️⃣ Delete customer
def delete_customer(customer_id: int, db: Session):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted"}
