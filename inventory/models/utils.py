'''Utility Classes'''
from pydantic import BaseModel


class Message(BaseModel):
    '''Message adapter class used in responses'''
    message: str
