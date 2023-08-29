from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class Conversation(BaseModel):
    messages: str
    time: datetime
    languages: List[str]


class ConversationIn(BaseModel):
    pass


class ConversationOut(BaseModel):
    pass


# class Input(BaseModel):
#     audiofile: Optional[bytes]
#     text: Optional[str]


# class Translation(BaseModel):
#     translated_text: str


# class Languages(BaseModel):
