from fastapi import HTTPException
from sqlalchemy.orm import Session
from Database.models import Product

# 1️⃣ Create product (Manufacturer)
def create_product(data, db: Session):
    product = Product(
        name=data.name,
        price=data.price,
        description=data.description,
        manufacturer_id=data.manufacturer_id,
        brand_id=data.brand_id,
        category_id=data.category_id
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"message": "Product created successfully"}

# 2️⃣ Update product
def update_product(product_id: int, data, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if data.name is not None:
        product.name = data.name
    if data.price is not None:
        product.price = data.price
    if data.description is not None:
        product.description = data.description

    db.commit()
    return {"message": "Product updated"}

# 3️⃣ Delete product
def delete_product(product_id: int, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}

# 4️⃣ Get product by ID
def get_product_by_id(product_id: int, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# 5️⃣ Get products by Manufacturer (RELATION)
def get_products_by_manufacturer(manufacturer_id: int, db: Session):
    return db.query(Product).filter(Product.manufacturer_id == manufacturer_id).all()

# 6️⃣ Get products by Brand (RELATION)
def get_products_by_brand(brand_id: int, db: Session):
    return db.query(Product).filter(Product.brand_id == brand_id).all()

# 7️⃣ Get products by Category (RELATION)
def get_products_by_category(category_id: int, db: Session):
    return db.query(Product).filter(Product.category_id == category_id).all()

# 8️⃣ Search products
def search_products(query: str, db: Session):
    return db.query(Product).filter(Product.name.contains(query)).all()

# 9️⃣ Sort products by price
def sort_by_price(db: Session):
    return db.query(Product).order_by(Product.price).all()
