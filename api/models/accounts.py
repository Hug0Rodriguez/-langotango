from pydantic import BaseModel
from typing import List, Optional

# from .validator import PydanticObjectId


class SessionOut(BaseModel):
    jti: str
    account_id: str


class AccountIn(BaseModel):
    username: str
    password: str
    full_name: str
    bard_token: Optional["str"]


class Account(AccountIn):
    # id: PydanticObjectId
    pass


class AccountOut(BaseModel):
    id: str
    username: str
    full_name: str
    bard_token: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


# class LoanIn(BaseModel):
#     account_id: str
#     book_id: str


# class Loan(LoanIn):
#     id: PydanticObjectId


# class LoanOut(LoanIn):
#     id: str


# class BookIn(BaseModel):
#     author: str
#     title: str
#     quantity: int
#     synopsis: str
#     cover: str | None


# class Book(BookIn):
#     id: PydanticObjectId


# class BookOut(BookIn):
#     id: str
#     loans: List[str]


# class BookList(BaseModel):
#     books: List[BookOut]
