from fastapi import (
    Depends,
    # HTTPException,
    # status,
    # Response,
    APIRouter,
    # Request,
    BackgroundTasks,
)
from pydantic import BaseModel
from models.messages import (
    UserMessage,
)
from consumer import start_connection, Hugo_cool
from token_auth import get_current_user
import pika
import json
import time

# print("")
# start_connection()

# Hugo_cool()


def produce_message(data):
    parameters = pika.ConnectionParameters(host="rabbitmq")
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="messages")
    channel.basic_publish(exchange="", routing_key="messages", body=f"{data}")
    connection.close()


# basic command version
# Speech to Text API
router = APIRouter()


class TestResponse(BaseModel):
    message: str


class ReceivedMessage(BaseModel):
    text: str


def bard_test(**kwargs):
    with open("file.txt", "w") as new_file:
        new_file.write("test")


# POST
@router.post("/api/messages", response_model=ReceivedMessage)
async def user_message_in(
    message: UserMessage,
    background_tasks: BackgroundTasks
    # account: dict = Depends(get_current_user),
):
    background_tasks.add_task(bard_test, kwargs=message)
    # get text from request
    print(message, "print on line 60")
    # print("hello sir")
    # produce_message(message)
    # Send message to consumer.py

    return message


"""
import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
"""
