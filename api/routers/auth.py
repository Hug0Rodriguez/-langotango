import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from models.accounts import AccountOut, Account, AccountOutWithPassword
from queries.accounts import AccountQueries


class Auth(Authenticator):
    async def get_account_data(
        self, username: str, accounts: AccountQueries
    ) -> Account:
        return accounts.get(username)

    def get_account_getter(
        self, accounts: AccountQueries = Depends()
    ) -> AccountQueries:
        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword) -> str:
        return account.hashed_password

    def get_account_data_for_cookie(self, account: Account) -> AccountOut:
        return account.username, AccountOut(**account.dict())


authenticator = Auth(os.environ["SIGNING_KEY"])
