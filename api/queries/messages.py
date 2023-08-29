from pymongo.errors import DuplicateKeyError
from models.messages import MessageIn, MessageOut
from models.conversations
from queries.conversations import ConversationQueries
from datetime import datetime

# from models.messages import
from .client import Queries


class MessageQueries(Queries):
    DB_NAME = "mongo_data"
    COLLECTION = "messages"

    def create(
                self,
                UserMessageIn: MessageIn,

    ) -> MessageOut:
        props["username"]
        props["datetime"]
        props["token"]
        props["content"]
        props["role"]

    def create(self, UserMessageIn: MessageIn) -> MessageOut:
        # check if conversation associated with existing token exists

            props = UserMessageIn.dict()
            self.collection.insert_one(props)
            props["id"] = str(props["_id"])
            # props["username"] = str(props["username"])
            # props["timestamp"] = str(props[datetime.now()])
            # props["token"] = str(props[UserMessageIn.token])
            MessageOut["role"]

        # conversation already exists
        if self.messages.find({"username": UserMessageIn["username"]}):
            # set conversation to the existing conversation based on the token
            conversation = self.conversations.find_one(
                {"token": UserMessageIn.token}
            )
            # if convo exists, add messages

            # when convo is pulled up, add token to convo tokens list
            # else, convo doesn't exist, create convo

            # MessageOut is what we send to chatbot
        return MessageOut



"""
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
