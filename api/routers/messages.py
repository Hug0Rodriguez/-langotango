from fastapi import (
    Depends,
    # HTTPException,
    # status,
    # Response,
    APIRouter,
    # Request,
    BackgroundTasks,
    WebSocket,
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
import os
from bardapi import Bard
from google.cloud import texttospeech
import base64

# start_connection()


def produce_message(data):
    parameters = pika.ConnectionParameters(host="rabbitmq")
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="messages")
    channel.basic_publish(exchange="", routing_key="messages", body=f"{data}")
    connection.close()


router = APIRouter()


class TestResponse(BaseModel):
    message: str


class ReceivedMessage(BaseModel):
    text: str


def bard_test(**kwargs):
    with open("file.txt", "w") as new_file:
        new_file.write("test")


def text_to_chatbot(**kwargs):
    # use bard api call to generate response
    # might be os.environ.get()
    token = os.environ("token_variable_name")
    # token of the day: aAjFqKGwYEp32myZHuDxafvHU6wOMKc5prWPlvqu8ydT9V4ITLpNMBkoQaVJ3r2dfyalKw.
    bard = Bard(token=token)
    chatbot_response = bard.get_answer("hola me llamo beau")["content"]
    return chatbot_response # This goes nowehere

# ADD WEBSOCKETS HERE
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        chatbot_response = await websocket.receive_text() # Where is this receiving text from?
        audio_base64 = google_text_to_speech(chatbot_response)
        await websocket.send_text(audio_base64)

def google_text_to_speech(chatbot_response):
    # pass in response to google text to speech
    # use api documentation to convert tocorrect audiofile type
    # # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # # Set the text input to be synthesized
    # maybe have a chatbot_response = Depends() so that it waits for text_to_chatbot() to resolve before ecexuting
    synthesis_input = texttospeech.SynthesisInput(text=chatbot_response)

    # # Build the voice request, select the language code ("en-US") and the ssml
    # # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL # Specifying en-US will conflict with our current non-English test-cases.
    )

    # # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # # Perform the text-to-speech request on the text input with the selected
    # # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    # convert response to base 64 which can be read by frontend HTML
    audio_base64 = base64.b64encode(response.audio_content).decode("utf-8")
    return audio_base64

    # # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
        # OUTPUT.mp3 is the audiofile we want our frontend to play


# POST
@router.post("/api/messages", response_model=ReceivedMessage)
async def user_message_in(
    message: UserMessage,
    background_tasks: BackgroundTasks
    # account: dict = Depends(get_current_user),
):
    # background_tasks.add_task(bard_test, kwargs=message)
    # # get text from request
    # print(message, "print on line 60")

    # 3. calls bard.get_answer
    background_tasks.add_task(text_to_chatbot, kwargs=something)

    # 4.5 Takes text from chatbot response
    # I don't know what to put here??

    # 5 calls bard text to speech
    background_tasks.add_task(google_text_to_speech, kwargs=something)

    # 6 sends audio back to client
    # Use Websockets

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
