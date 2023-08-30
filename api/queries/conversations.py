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
    # W16D3
    def create(self, conversation: ConversationIn) -> ConversationOut:
        # check if conversation associated with existing token exists
        check_conversation = self.get_one_by_token(conversation["tokens"][0])
            # if convo exists, add messages
        if check_conversation:
            return check_conversation
            # when convo is pulled up, add token to convo tokens list
        # else, convo doesn't exist, create convo
        else:
            # insert conversation into conversations collection
            self.collection.insert_one(conversation)
            conversation_out = self.get_one_by_token(conversation["tokens"][0])
            return conversation_out

    def get_one_by_token(
        self,
        token: str,
    ) -> ConversationOut | None:
        # logic to spit out ConversationOut | None
        # look within list, "tokens", to see if any value=token is in there
        conversation_out = self.collection.find_one({"tokens": { '$elemMatch': { "$eq": token } } })
        return conversation_out

    #W16D3
    def get_one_by_id(
            self,
            id: str,
    ) -> ConversationOut:
        # grab existing conversation by specified id
        conversation_out = self.collection.find_one({"_id": ObjectId(id)})
        return conversation_out

    def update_one_tokens(self, id: str, token: str) -> ConversationOut:
        conversation = self.get_one_by_id(id)
        tokens = conversation.tokens
        tokens.insert(0, token)
        updated_conversation = self.collection.update_one(
            {"_id": ObjectId(id)}, {"$set": {"tokens": tokens}}
        )
        return updated_conversation

    # Used for displaying Conversation History
    def get_all(self) -> List[ConversationOut]:
        conversations = self.collection.find()
        return conversations

    def delete_by_id(self, id: str) -> True:
        self.collection.delete({"_id": ObjectId(id)})
        return True
