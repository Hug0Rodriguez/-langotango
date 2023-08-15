from pymongo.errors import DuplicateKeyError
from models.accounts import (
    # Account,
    AccountIn,
    AccountOutWithPassword,
)
from .client import Queries


# wants AccountIN, AccountOut, AccoutnRepo, DuplicateErrorAccount
class DuplicateAccountError(ValueError):
    pass


class AccountQueries(Queries):
    DB_NAME = "mongo-data"
    COLLECTION = "accounts"

    # function to get an account
    def get(self, username: str) -> AccountOutWithPassword:
        props = self.collection.find_one({"username": username})
        if not props:
            return None
        props["id"] = str(props["_id"])
        print("🕰️props in GET is: ", props)
        return AccountOutWithPassword(**props)

    # function to create an account
    def create(
        self, info: AccountIn, hashed_password: str, roles=["patron"]
    ) -> AccountOutWithPassword:
        props = info.dict()
        props["hashed_password"] = hashed_password
        props["roles"] = roles

        try:
            self.collection.insert_one(props)
        except DuplicateKeyError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])
        return AccountOutWithPassword(**props)
