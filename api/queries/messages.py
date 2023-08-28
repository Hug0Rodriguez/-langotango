from pymongo.errors import DuplicateKeyError
from models.messages import Conversation
from datetime import datetime

# from models.messages import
from .client import Queries

class ConversationQueries(Queries):
    DB_Name = "mongo_data"
    COLLECTION = "conversations"

    #TOKEN scenario
    def create(self, userMessageIn: shape_of_data) -> MessageOut

    # check if conversation associated with existing token exists
    if db.conversations.getalletc["token"]is False:
        #text of the message,
        # possible time stamps,
        # username,
        # a good sorting system for conversations
        # token associated
        # conversation_id for each covnersation
        props = userMessageIn.dict()
        props["id"] = str(props["_id"])
        props["username"] = str(props["username"])
        props["timestamp"] = str(props[datetime.now()])
        props["token"] = # can access token from the request header
        props["messages"] = # list of messages

    # conversation already exists
    elif db.conversations.find({ token: request.token }):
    # set conversation to the existing conversation based on the token
    conversations = db.conversations.find(conversations["token"])
    # if convo exists, add messages

    #when convo is pulled up, add token to convo tokens list
    # else, convo doesn't exist, create convo

    # MessageOut is what we send to chatbot
    return MessageOut

'''
Example Queries:
class BookQueries(Queries):
    DB_NAME = "library"
    COLLECTION = "inventory"

    def create(self, book: BookIn) -> BookOut:
        props = book.dict()
        self.collection.insert_one(props)
        props["id"] = str(props["_id"])
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

'''
