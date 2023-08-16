from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .auth import authenticator
from jwtdown_fastapi.authentication import Token
from pydantic import BaseModel
from queries.accounts import (
    AccountQueries,
    DuplicateAccountError,
)
from queries.sessions import SessionQueries
from models.accounts import (
    AccountIn,
    # Account,
    AccountOut,
    AccountOutWithPassword,
)


# Below code is defining mddels and creating account function


class AccountForm(BaseModel):
    username: str
    password: str


# Below code is for including your browser's cookies in a fetch call.
class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()

not_authorized = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.post("/api/accounts", response_model=AccountToken | HttpError)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    # AccountQueries
    repo: AccountQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = repo.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.username, password=info.password)
    # login automatically via login def in imported authenticator
    # is the login def creating a session querie?
    token = await authenticator.login(response, request, form, repo)
    print("🫒token is: ", token)
    return AccountToken(account=account, **token.dict())


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    # Double check line below
    account: AccountOutWithPassword = Depends(
        authenticator.try_get_current_account_data
    ),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


# @router.delete("/api/sessions/{account_id}", response_model=bool)
# async def delete_session(
#     account_id: str,
#     account: dict = Depends(authenticator.get_current_account_data),
#     repo: SessionQueries = Depends(),
# ) -> bool:
#     if "patron" not in account["roles"]:
#         raise not_authorized
#     repo.delete_sessions(account_id)
#     return True


# test beau
# Below code is for getting the current account data
# Possibly don't need. From fastapi auth docs, not HR example
# @router.get("/api/things")
# async def get_things(
#     account_data: Optional[dict] = Depends(
#         authenticator.try_get_current_account_data
#     ),
# ):
#     if account_data:
#         return personalized_list
#     return general_list


@router.get("/conversations")
def get_conversations():
    return []


@router.post("/conversations")
def create_conversations():
    return []


@router.delete("/conversations")
def delete_conversations():
    return None
