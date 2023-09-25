from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from database import Base

class Product(Base):
    __tablename__ = 'products'
    productID = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255))
    price = Column(Float)

class ProductBase(BaseModel):
    name: str
    description: str
    price: float