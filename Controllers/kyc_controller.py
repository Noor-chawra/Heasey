from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import KYC

# Create or get KYC row
def _get_or_create_kyc(customer_id: int, db: Session):
    kyc = db.query(KYC).filter(KYC.customer_id == customer_id).first()
    if not kyc:
        kyc = KYC(customer_id=customer_id)
        db.add(kyc)
        db.commit()
        db.refresh(kyc)
    return kyc


# 1️⃣ Upload personal details
def upload_personal_details(data, db: Session):
    kyc = _get_or_create_kyc(data.customer_id, db)
    kyc.personal_details = data.personal_details
    db.commit()
    return {"message": "Personal details uploaded"}


# 2️⃣ Upload ID proof
def upload_id_proof(data, db: Session):
    kyc = _get_or_create_kyc(data.customer_id, db)
    kyc.id_proof = data.id_proof
    db.commit()
    return {"message": "ID proof uploaded"}


# 3️⃣ Upload bank details
def upload_bank_details(data, db: Session):
    kyc = _get_or_create_kyc(data.customer_id, db)
    kyc.bank_details = data.bank_details
    kyc.status = "submitted"
    db.commit()
    return {"message": "Bank details uploaded"}
