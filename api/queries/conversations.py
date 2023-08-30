from bson.objectid import ObjectId
from models.conversations import ConversationIn, ConversationOut
from typing import List

# from pymongo.errors import DuplicateKeyError

# from models.messages import
from .client import Queries


class ConversationQueries(Queries):
    DB_NAME = "mongo-data"
    COLLECTION = "conversations"

    # TOKEN scenario
    def create(self, conversation: ConversationIn) -> ConversationOut:
        # check if conversation associated with existing token exists

        # if convo exists, add messages

        # when convo is pulled up, add token to convo tokens list
        # else, convo doesn't exist, create convo

        # MessageOut is what we send to chatbot
        return ConversationOut

    def get_one_by_token(
        self,
    ) -> ConversationOut | None:
        pass

    def get_one_by_id(self) -> ConversationOut:
        pass

    def get_all(self) -> List[ConversationOut]:
        conversations = self.collection.find()
        return conversations

    def update_one_tokens(self, id: str, token: str) -> ConversationOut:
        conversation = self.collection.find_one({"_id": ObjectId(id)})
        tokens = conversation.tokens
        tokens.append(token)
        updated_conversation = self.collection.update_one(
            {"_id": ObjectId(id)}, {"$set": {"tokens": tokens}}
        )
        return updated_conversation

    def delete_by_id(self, id: str) -> True:
        self.collection.delete({"_id": ObjectId(id)})
        return True
