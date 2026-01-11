from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers import product_controller
from Schemas.product_schema import ProductCreateSchema, ProductUpdateSchema

router = APIRouter()

@router.post("/product")
def create_product(data: ProductCreateSchema, db: Session = Depends(get_db)):
    return product_controller.create_product(data, db)

@router.put("/product/{product_id}")
def update_product(product_id: int, data: ProductUpdateSchema, db: Session = Depends(get_db)):
    return product_controller.update_product(product_id, data, db)

@router.delete("/product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_controller.delete_product(product_id, db)

@router.get("/product/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_controller.get_product_by_id(product_id, db)

@router.get("/product/manufacturer/{manufacturer_id}")
def products_by_manufacturer(manufacturer_id: int, db: Session = Depends(get_db)):
    return product_controller.get_products_by_manufacturer(manufacturer_id, db)

@router.get("/product/brand/{brand_id}")
def products_by_brand(brand_id: int, db: Session = Depends(get_db)):
    return product_controller.get_products_by_brand(brand_id, db)

@router.get("/product/category/{category_id}")
def products_by_category(category_id: int, db: Session = Depends(get_db)):
    return product_controller.get_products_by_category(category_id, db)

@router.get("/product/search/{query}")
def search_products(query: str, db: Session = Depends(get_db)):
    return product_controller.search_products(query, db)

@router.get("/product/sort/price")
def sort_by_price(db: Session = Depends(get_db)):
    return product_controller.sort_by_price(db)
