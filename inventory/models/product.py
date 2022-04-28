'''Models and Resources'''
from pydantic import BaseModel
from redis_om import HashModel


class Product(HashModel):
    '''Atual Product model'''
    name: str
    price: float
    quantity: int


class NewProduct(BaseModel):
    '''Adaptation model for Product used in responses'''
    name: str
    price: float
    quantity: int
