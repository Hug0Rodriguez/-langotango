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


# contents authenticator.py
# import os
# from fastapi import Depends
# from jwtdown_fastapi.authentication import Authenticator
# from queries.accounts import AccountQueries
# from models.accounts import Account, AccountOut, AccountOutWithPassword


# class MyAuthenticator(Authenticator):
#     async def get_account_data(
#         self,
#         username: str,
#         accounts: AccountQueries,
#     ):
#         # Use your repo to get the account based on the
#         # username (which could be an email)
#         return accounts.get(username)

#     def get_account_getter(
#         self,
#         accounts: AccountQueries = Depends(),
#     ):
#         # Return the accounts. That's it.
#         return accounts

#     def get_hashed_password(self, account: AccountOutWithPassword):
#         # Return the encrypted password value from your
#         # account object
#         print("🪩", type(account))
#         return account.hashed_password

#     def get_account_data_for_cookie(self, account: AccountOut):
#         # Return the username and the data for the cookie.
#         # You must return TWO values from this method.
#         return account.username, AccountOut(**account.dict())


# # Signing key shoudl be 20-40 chars

# authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
