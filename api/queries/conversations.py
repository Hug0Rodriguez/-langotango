from pymongo.errors import DuplicateKeyError
from models.messages import MessageIn, MessageOut
from models.conversations
from datetime import datetime


class ConversationQueries(Queries):
    DB_NAME = "mongo_data"
    COLLECTION = "conversations"

    # TOKEN scenario

    def get(self, token) -> ConferenceOut | None:
          pass
