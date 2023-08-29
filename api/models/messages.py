from pydantic import BaseModel
from datetime import datetime


class UserMessage(BaseModel):
    text: str
<<<<<<< HEAD
    created_at: datetime
    username: str
    conversation_id = int
=======
    # created_at: datetime
    # username: str
    # conversation_id: int

>>>>>>> 1d3d056637faebb2fb699f7c0b23e8447ba4f047


class Preferences(BaseModel):
    language: str
    difficulty: str
<<<<<<< HEAD
=======


class ApiMessage(BaseModel):
    text: str
    # created_at: datetime

class MessageIn(BaseModel):
    username: str
    timestamp: datetime
    token: str
    content: list
    role: str

class MessageOut(BaseModel):
    role: str
    content: str



# class AudioIn(BaseModel):
#     audio: bytes

#     def decoded_audio(self):
#         pass


# class AudioOut(BaseModel):
#     audio: bytes
>>>>>>> 1d3d056637faebb2fb699f7c0b23e8447ba4f047
