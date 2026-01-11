from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import kyc_controller
from Schemas.kyc_schema import (
    PersonalDetailsSchema,
    IDProofSchema,
    BankDetailsSchema
)

router = APIRouter()

@router.post("/kyc/personal-details")
def upload_personal_details(data: PersonalDetailsSchema, db: Session = Depends(get_db)):
    return kyc_controller.upload_personal_details(data, db)

@router.post("/kyc/id-proof")
def upload_id_proof(data: IDProofSchema, db: Session = Depends(get_db)):
    return kyc_controller.upload_id_proof(data, db)

@router.post("/kyc/bank-details")
def upload_bank_details(data: BankDetailsSchema, db: Session = Depends(get_db)):
    return kyc_controller.upload_bank_details(data, db)
