from pydantic import BaseModel
from typing import List
from datetime import datetime


# dictated by user
class UserMessage(BaseModel):
    content: str


# goes into database
class MessageIn(BaseModel):
    username: str
    time_stamp: datetime
    content: str
    role: str


# comes out of db, goes to chatbot
class MessageOut(BaseModel):
    role: str
    content: str


# stretch goal
class Preferences(BaseModel):
    language: str
    difficulty: str


# class AudioIn(BaseModel):
#     audio: bytes

#     def decoded_audio(self):
#         pass


# class AudioOut(BaseModel):
#     audio: bytes
