from fastapi import Depends, APIRouter, Request
from .auth import authenticator
from pydantic import BaseModel
from models.messages import (
    UserMessage,
)
from queries.messages import MessageQueries
from models.accounts import AccountOut
import os
import openai
from datetime import datetime


openai.api_key = os.environ["OPENAI_API_KEY"]

router = APIRouter()


class ChatbotResponse(BaseModel):
    content: str


# POST
@router.post("/api/messages", response_model=ChatbotResponse)
async def user_message_in(
    message: UserMessage,
    request: Request,
    repo: MessageQueries = Depends(),
    account: AccountOut = Depends(authenticator.try_get_current_account_data),
) -> ChatbotResponse:
    message = message.dict()
    token = request.cookies["fastapi_token"]
    message["username"] = account["username"]
    message["role"] = "user"
    message["time_stamp"] = datetime.now()
    new_message = repo.create(UserMessageIn=message, token=token)
    message_history = repo.get_all_in_convo(new_message["conversation_id"])
    # # ensure output of message_history is a list of dictionaries
    # # CHAP GPT CHATBOT EXAMPLE REQUEST
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # messages must be a list dictionaries in the form
        # {"role": "user/system", {"content": "string"}}
        messages=message_history,
    )

    # # # query to write completion to the DB collection
    response = completion.choices[0].message
    response["username"] = account["username"]
    response["role"] = "assistant"
    response["time_stamp"] = datetime.now()
    repo.create(UserMessageIn=response, token=token)


    # # return chat message
    return {"content": response["content"]}
    # return {"text": "SUCCESS"}
