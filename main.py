from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
from models import Product, ProductBase, Base
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)]

# Add a product
@app.post('/add-product', status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductBase, db: db_dep):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    return {"message": "Product added"}

# List a product
@app.get('/products', status_code=status.HTTP_200_OK)
async def list_all_product(db: db_dep):
    product = db.query(Product).all()
    if product is None:
        raise HTTPException(status_code=404, detail="Empty Data")
    return product

# Read a product by ID
@app.get('/products/{product_id}', status_code=status.HTTP_200_OK)
async def read_product(product_id: int, db: db_dep):
    product = db.query(Product).filter(Product.productID == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
    
# Update a product by ID
@app.put("/update-product/{product_id}", status_code=status.HTTP_200_OK)
def update_product(product_id: int, product: ProductBase, db: db_dep):
    db_product = db.query(Product).filter(Product.productID == product_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        raise HTTPException(status_code=404, detail="Product not found")
        
# Delete a product by ID
@app.delete("/delete-product/{product_id}")
def delete_product(product_id: int, db: db_dep):
    success = db.query(Product).filter(Product.productID ==product_id).first()
    if success:
        db.delete(success)
        db.commit()
        return {"message": "Product deleted"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")  
