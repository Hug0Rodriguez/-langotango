from fastapi import (
    Depends,
    # HTTPException,
    # status,
    Response,
    APIRouter,
    Request,
)
from pydantic import BaseModel
from models.messages import (
    UserMessage,
)
from queries.accounts import AccountQueries
import pika
import json

# from requests import session

router = APIRouter()


class TestResponse(BaseModel):
    message: str


def produce_message(data):
    parameters = pika.ConnectionParameters(host="rabbitmq")
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="user_messages")
    channel.basic_publish(
        exchange="", routing_key="user_messages", body=f"{data}"
    )
    connection.close()

    # in the sending fxn


# POST
@router.post("/api/messages", response_model=TestResponse)
def user_message_in(
    info: UserMessage,
    request: Request,
    response: Response,
    repo: AccountQueries = Depends(),
):
    # find way to extract username or bearer token from request
    bard_token = repo.get_bard_token(username)
    message_fields = {"text": info.text, "bard_token": bard_token}

    message = json.dumps(message_fields)
    produce_message(message, "user_messages")

    return TestResponse(message="Success")
