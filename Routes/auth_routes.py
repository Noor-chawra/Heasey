from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import auth_controller
from Schemas.auth_schema import (
    CustomerSignup,
    CustomerLogin,
    ManufacturerSignup,
    ManufacturerLogin
)

router = APIRouter()

@router.post("/customer/signup")
def customer_signup(data: CustomerSignup, db: Session = Depends(get_db)):
    return auth_controller.customer_signup(data, db)

@router.post("/customer/login")
def customer_login(data: CustomerLogin, db: Session = Depends(get_db)):
    return auth_controller.customer_login(data, db)

@router.post("/manufacturer/signup")
def manufacturer_signup(data: ManufacturerSignup, db: Session = Depends(get_db)):
    return auth_controller.manufacturer_signup(data, db)

@router.post("/manufacturer/login")
def manufacturer_login(data: ManufacturerLogin, db: Session = Depends(get_db)):
    return auth_controller.manufacturer_login(data, db)

@router.post("/send-otp")
def send_otp(email: str, db: Session = Depends(get_db)):
    return auth_controller.send_otp(email, db)

@router.post("/reset-password")
def reset_password(email: str, otp: int, new_password: str, db: Session = Depends(get_db)):
    return auth_controller.reset_password(email, otp, new_password, db)
