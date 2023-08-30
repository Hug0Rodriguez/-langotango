from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime


class ConversationIn(BaseModel):
    time_stamp: datetime
    username: str
    tokens: List[str]


class ConversationOut(ConversationIn):
    _id: ObjectId


class Accounts(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str


# class Input(BaseModel):
#     audiofile: Optional[bytes]
#     text: Optional[str]


# class Translation(BaseModel):
#     translated_text: str


# class Languages(BaseModel):
