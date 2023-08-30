from bson.objectid import ObjectId
from models.messages import MessageIn, MessageOut
from .conversations import ConversationQueries
from fastapi import Depends
from typing import List

# from pymongo.errors import DuplicateKeyError
# from datetime import datetime
# from models.messages import
from .client import Queries


class MessageQueries(Queries):
    DB_NAME = "mongo_data"
    COLLECTION = "messages"

    def create(
        self,
        UserMessageIn: MessageIn,
        convo_queries: ConversationQueries = Depends(),
    ) -> MessageOut:
        props = self.collection.insert_one({UserMessageIn.content})
        # link message with conversation id
        conversation = convo_queries.get_one_by_token(UserMessageIn.token)
        props["conversation_id"] = ObjectId(conversation["_id"])
        self.collection.insert_one(props)

    def get_all(
        UserMessageIn: MessageIn,
        convo_queries: ConversationQueries = Depends(),
    ) -> List[MessageOut]:
        # for loop for creating list of all messages
        # associated with a conversation's id
        # for messages inside db
        # if message has id of conversation querie
        # append message to List[MessageOut]
        pass


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
