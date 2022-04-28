'''Routes using Product resource'''
from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from redis_om.model.model import NotFoundError

from models.product import NewProduct, Product
from models.utils import Message

router = APIRouter(prefix='/products')


@ router.get('/', response_model=List[Product])
def get_all_products() -> List[Product]:
    '''Returns list of JSON rep of products'''
    return [Product.get(pk) for pk in Product.all_pks()]


@ router.get('/{pk}', response_model=Product, responses={404: {'model': Message}})
def get_single_product(pk: str) -> Product:
    '''Returns a single product or rises 404 when not found'''
    try:
        product = Product.get(pk)
    except NotFoundError:
        return JSONResponse(status_code=404, content={'message': 'Product not found'})
    return product


@ router.post('/', response_model=Product, status_code=201)
def create_product(product: NewProduct) -> Product:
    '''Creates and returns a new Product based on req body'''
    new_product = Product(**product.dict())
    new_product.save()
    return new_product


@ router.delete('/{pk}', response_model=Message)
def delete_product(pk: str) -> Message:
    '''Deletes a poduct or returns 404'''
    if not Product.delete(pk):
        return JSONResponse(status_code=404, content={'message': 'Product not found'})
    return Message(message='Product deleted')
