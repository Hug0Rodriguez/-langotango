from pymongo.errors import DuplicateKeyError
from models.accounts import (
    AccountIn,
    AccountOutWithPassword,
)
from typing import Dict
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
        return AccountOutWithPassword(**props)

    # function to create an account
    def create(
        self,
        info: AccountIn,
        hashed_password: str,
    ) -> AccountOutWithPassword:
        props = info.dict()
        props["hashed_password"] = hashed_password
        del props["password"]

        try:
            self.collection.insert_one(props)
        except DuplicateKeyError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])
        return AccountOutWithPassword(**props)

    # Take a username to find the bard token stored in the user document
    def get_bard_token(
        self,
        username: str,
    ) -> Dict:
        props = self.collection.find_one({"username": username})
        return props.bard_token
