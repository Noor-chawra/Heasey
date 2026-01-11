from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import random
from Database.models import Customer, Manufacturer
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ---------------- CUSTOMER ----------------
def customer_signup(data, db: Session):
    if db.query(Customer).filter(Customer.email == data.email).first():
        raise HTTPException(status_code=400, detail="Customer already exists")

    user = Customer(
        name=data.name,
        email=data.email,
        password=pwd_context.hash(data.password)
    )
    db.add(user)
    db.commit()
    return {"message": "Customer account created"}


def customer_login(data, db: Session):
    user = db.query(Customer).filter(Customer.email == data.email).first()
    if not user or not pwd_context.verify(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Customer login successful"}


# ---------------- MANUFACTURER ----------------
def manufacturer_signup(data, db: Session):
    if db.query(Manufacturer).filter(Manufacturer.email == data.email).first():
        raise HTTPException(status_code=400, detail="Manufacturer already exists")

    manu = Manufacturer(
        company_name=data.company_name,
        email=data.email,
        password=pwd_context.hash(data.password)
    )
    db.add(manu)
    db.commit()
    return {"message": "Manufacturer account created"}


def manufacturer_login(data, db: Session):
    manu = db.query(Manufacturer).filter(Manufacturer.email == data.email).first()
    if not manu or not pwd_context.verify(data.password, manu.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Manufacturer login successful"}


# ---------------- OTP & PASSWORD ----------------
def send_otp(data, db: Session):
    user = db.query(Customer).filter(Customer.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.otp = random.randint(100000, 999999)
    db.commit()
    return {"message": "OTP sent successfully"}


def reset_password(data, db: Session):
    user = db.query(Customer).filter(Customer.email == data.email).first()
    if not user or user.otp != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user.password = pwd_context.hash(data.new_password)
    user.otp = None
    db.commit()
    return {"message": "Password reset successful"}


def change_password(data, db: Session):
    user = db.query(Customer).filter(Customer.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(data.old_password, user.password):
        raise HTTPException(status_code=401, detail="Old password incorrect")

    user.password = pwd_context.hash(data.new_password)
    db.commit()
    return {"message": "Password changed successfully"}
