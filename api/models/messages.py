from pydantic import BaseModel
from datetime import datetime


class UserMessage(BaseModel):
    text: str
    created_at: datetime
    username: str
    conversation_id = int


class Preferences(BaseModel):
    language: str
    difficulty: str
