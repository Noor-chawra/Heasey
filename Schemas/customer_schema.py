from pydantic import BaseModel, EmailStr

class CustomerCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class CustomerUpdateSchema(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
