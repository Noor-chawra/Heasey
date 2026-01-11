from pydantic import BaseModel

class PersonalDetailsSchema(BaseModel):
    customer_id: int
    personal_details: str

class IDProofSchema(BaseModel):
    customer_id: int
    id_proof: str

class BankDetailsSchema(BaseModel):
    customer_id: int
    bank_details: str
