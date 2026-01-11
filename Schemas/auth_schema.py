from pydantic import BaseModel, EmailStr

# ---------- CUSTOMER ----------
class CustomerSignupSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class CustomerLoginSchema(BaseModel):
    email: EmailStr
    password: str


# ---------- MANUFACTURER ----------
class ManufacturerSignupSchema(BaseModel):
    company_name: str
    email: EmailStr
    password: str

class ManufacturerLoginSchema(BaseModel):
    email: EmailStr
    password: str


# ---------- PASSWORD / OTP ----------
class SendOTPSchema(BaseModel):
    email: EmailStr

class ResetPasswordSchema(BaseModel):
    email: EmailStr
    otp: int
    new_password: str

class ChangePasswordSchema(BaseModel):
    email: EmailStr
    old_password: str
    new_password: str
