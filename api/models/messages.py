from pydantic import BaseModel
from datetime import datetime

# from typing import List


class UserMessage(BaseModel):
    text: str
    created_at: datetime


class Preferences(BaseModel):
    language: str
    difficulty: str


class ApiMessage(BaseModel):
    text: str
    created_at: datetime


# class AudioIn(BaseModel):
#     audio: bytes

#     def decoded_audio(self):
#         pass


# class AudioOut(BaseModel):
#     audio: bytes
