from pydantic import BaseModel
from typing import List
from datetime import datetime


class UserMessage(BaseModel):
    text: str
    created_at: datetime


class Preferences(BaseModel):
    language: str
    difficulty: str


class ApiMessage(BaseModel):
    text: str
    created_at: datetime


# class UserAudio(BaseModel):
#   audio : bytes
