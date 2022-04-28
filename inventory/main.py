'''Main entry point for Inventry app'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routers.product import router as productRouter

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=['*'],
                   allow_headers=['*'])


app.include_router(productRouter)


@ app.get('/', response_class=RedirectResponse, status_code=302)
def hello():
    '''Redirects root requests to Swagger doc'''
    return RedirectResponse('/docs')
