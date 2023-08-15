from .client import Queries
from models.accounts import Account, SessionOut
from bson.objectid import ObjectId
from typing import Optional

# So SessionQueries is for WebSockets integration???


class SessionQueries(Queries):
    # Below should be mongo-data or something
    DB_NAME = "mongo-data"
    # collection can be named anything i think
    COLLECTION = "sessions"

    def get(self, jti: str):
        return self.collection.find_one({"jti": jti})

    def create(self, jti: str, account: Account) -> Optional[Account]:
        print("🎉Session Querie is created")
        result = self.collection.insert_one(
            {
                "jti": jti,
                "account_id": ObjectId(account.id),
            }
        )
        print("🎉🎉Session Querie Result is created and is: ", result)
        if result and result.inserted_id:
            return SessionOut(jti=jti, account_id=account.id)
        return None

    def delete(self, jti: str):
        self.collection.delete_many({"jti": jti})

    def validate(self, jti: str):
        return self.collection.count_documents({"jti": jti}) > 0

    def delete_sessions(self, account_id: str):
        self.collection.delete_many({"account_id": ObjectId(account_id)})
