from pydantic import BaseModel, EmailStr

class ManufacturerCreateSchema(BaseModel):
    company_name: str
    email: EmailStr
    password: str

class ManufacturerUpdateSchema(BaseModel):
    company_name: str | None = None
    email: EmailStr | None = None

