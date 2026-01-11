from fastapi import FastAPI
from Database.database import Base, engine
from Routes.auth_routes import router as auth_router
from Routes.customer_routes import router as customer_router
from Routes.manufacturer_routes import router as manufacturer_router
from Routes.brand_routes import router as brand_router
from Routes.category_routes import router as category_router
from Routes.product_routes import router as product_router
from Routes.cart_routes import router as cart_router
from Routes.order_routes import router as order_router
from Routes.kyc_routes import router as kyc_router
from Routes.review_routes import router as review_router

Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(manufacturer_router)
app.include_router(brand_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(kyc_router)
app.include_router(review_router)


