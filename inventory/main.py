import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from redis_om.model.model import NotFoundError

from dotenv import load_dotenv
load_dotenv()


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=['*'],
                   allow_headers=['*'])


redis = get_redis_connection(
    host=os.environ['REDIS_HOST'],
    port=os.environ['REDIS_PORT'],
    password=os.environ['REDIS_PSW'],
    decode_responses=True)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta():
        database = redis


@ app.get('/')
def hello():
    return {"message": "hello"}


def format(pk: str):
    try:
        product = Product.get(pk)
        return {
            'id': product.pk,
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity
        }
    except NotFoundError:
        return {"message": "Product not found"}


@ app.get('/products')
def getAllProducts():
    return [format(pk) for pk in Product.all_pks()]


@ app.get('/products/{pk}')
def getSingleProduct(pk: str):
    return format(pk)


@ app.post('/products')
def createProduct(product: Product):
    product.save()
    return format(product.pk)


@ app.delete('/products/{pk}')
def deleteProduct(pk: str):
    return Product.delete(pk)
