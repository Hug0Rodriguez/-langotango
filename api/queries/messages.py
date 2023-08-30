from bson.objectid import ObjectId
from models.messages import MessageIn, MessageOut, MessageOutWithConvoId
from .conversations import ConversationQueries
from fastapi import Depends
from typing import List
# from pymongo.errors import DuplicateKeyError
# from datetime import datetime
from .client import Queries
from models.validator import PydanticObjectId


class MessageQueries(Queries):
    DB_NAME = "mongo-data"
    COLLECTION = "messages"

    def create(
        self,
        UserMessageIn: MessageIn,
        token: str,
    ) -> MessageOutWithConvoId:
        # create "ConversationIn" object to pass into ConversationQueries.create()
        conversation_in = {}
        conversation_in["time_stamp"] = UserMessageIn["time_stamp"]
        conversation_in["username"] = UserMessageIn["username"]
        conversation_in["tokens"] = [token]
        # find/create conversation based on token
        convo_queries = ConversationQueries()
        conversation = convo_queries.create(conversation=conversation_in)
        # Assigning the new message's associated id to the id of the conversation
        # UserMessageIn = UserMessageIn.dict()
        UserMessageIn["conversation_id"] = conversation["_id"]
        # add UserMessageIn to messages collection
        new_message = self.collection.insert_one(UserMessageIn)
        # prep output with role and content to feed to chatgpt
        # select the message in the db by it's ObjectId
        message_out = self.get_one_by_id(new_message.inserted_id)

        return message_out

    def get_one_by_id(self, id: str) -> MessageOutWithConvoId:
        message = self.collection.find_one({"_id": ObjectId(id)})
        message_out = {}
        message_out["role"] = message["role"]
        message_out["content"] = message["content"]
        message_out["conversation_id"] = message["conversation_id"]
        return message_out

    def get_all_in_convo(
            self,
        conversation_id: PydanticObjectId,
    ) -> List[MessageOut]:
        #### Matching_messages = []
        # for loop for creating list of all messages
        messages = self.collection.find(
            {
            "conversation_id": {"$eq": conversation_id}
            },
            {
            "_id": 0,
            "time_stamp": 0,
            "conversation_id": 0,
            "username": 0,
        }
        )
            #### for message in COLLECTION.find():
        # associated with a conversation's id
             ###### if message.conversation_id == UserMessageIn.conversation_id:
        # associated with a conversation's id
            # if message["conversation_id"] == conversation_id:
            #     matching_messages.append(message)
            #### output_message = MessageOut
        # for messages inside db
        # if message has id of conversation querie
        # append message to List[MessageOut]
            ####### matching_messages.append(output_message)
        return [message for message in messages]


"""
MessageIn/MessageOut Models:
class MessageIn(BaseModel):
    username: str
    timestamp: datetime
    token: str
    content: list
    role: str

class MessageOut(BaseModel):
    role: str
    content: str

Example Queries:
class BookQueries(Queries):
    DB_NAME = "library"
    COLLECTION = "inventory"

    def create(self, book: BookIn) -> BookOut:
        # converts BookIn to dict to store
        props = book.dict()
        # insert s props into collection
        self.collection.insert_one(props)
        # converts id to _id because mongo likes it that way
        props["id"] = str(props["_id"])
        # returns Bookout object with empty loand and howevermany keyword props
        return BookOut(loans=[], **props)

    def get_all(self) -> List[BookOut]:
        result = self.collection.aggregate(
            [
                {
                    "$lookup": {
                        "from": "loans",
                        "localField": "_id",
                        "foreignField": "book_id",
                        "as": "loans",
                    }
                },
                {"$sort": {"title": 1}},
            ]
        )
        bookPropsList = list(result)
        for bookProps in bookPropsList:
            bookProps["id"] = str(bookProps["_id"])
            bookProps["loans"] = [
                str(props["account_id"]) for props in bookProps["loans"]
            ]
        return [BookOut(**book) for book in bookPropsList]


class LoanQueries(Queries):
    DB_NAME = "library"
    COLLECTION = "loans"

    def create(self, loan: LoanIn) -> Loan:
        props = loan.dict()
        # ObjectId grabs id of existing account_id?
        props["account_id"] = ObjectId(props["account_id"])
        props["book_id"] = ObjectId(props["book_id"])
        self.collection.insert_one(props)
        # assigns id to each loan
        props["id"] = str(props["_id"])

        props["account_id"] = str(props["account_id"])
        props["book_id"] = str(props["book_id"])
        return Loan(**props)

    def delete(self, book_id: str, account_id: str):
        self.collection.delete_one(
            {
                "account_id": ObjectId(account_id),
                "book_id": ObjectId(book_id),
            }
        )

"""
