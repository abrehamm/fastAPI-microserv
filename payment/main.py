import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


from dotenv import load_dotenv
load_dotenv()


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=['*'],
                   allow_headers=['*'])

DBUser = os.environ['DB_USER_NAME']
DBPsw = os.environ['DB_USER_PSW']
DBHost = os.environ['DB_HOST']
DBName = os.environ['DB_NAME']
client = MongoClient(
    f"mongodb+srv://{DBUser}:{DBPsw}@{DBHost}/{DBName}?retryWrites=true&w=majority")
db = client['fastAPI-microserv']
payment = db.payment


@app.get('/')
def hello():
    print(payment.find_one())
    return {"message": "Hello"}
