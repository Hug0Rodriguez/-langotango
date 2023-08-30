from pydantic import BaseModel
from typing import List
from datetime import datetime
from bson.objectid import ObjectId
from .validator import PydanticObjectId


# dictated by user
class UserMessage(BaseModel):
    content: str


# goes into database
class MessageIn(BaseModel):
    username: str
    time_stamp: datetime
    role: str
    content: str


# comes out of db, goes to chatbot
class MessageOut(BaseModel):
    role: str
    content: str


class MessageOutWithConvoId(MessageOut):
    convesersation_id: PydanticObjectId




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
