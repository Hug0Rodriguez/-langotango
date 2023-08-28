from pydantic import BaseModel


class SessionOut(BaseModel):
    jti: str
    account_id: str


class AccountIn(BaseModel):
    username: str
    password: str
    full_name: str


class Account(AccountIn):
    pass


class AccountOut(BaseModel):
    id: str
    username: str
    full_name: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str
