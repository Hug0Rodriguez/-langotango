from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class Conversation(BaseModel):
    messages: str
    time: datetime
    languages: List[str]


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
