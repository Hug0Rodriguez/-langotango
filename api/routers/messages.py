from fastapi import (
    Depends,
    # HTTPException,
    # status,
    # Response,
    APIRouter,
    # Request,
    # BackgroundTasks,
    # WebSocket,
    # WebSocketDisconnect,
)
from pydantic import BaseModel
from models.messages import (
    UserMessage,
)
import os

# from bardapi import Bard
# from google.cloud import texttospeech
import base64
import requests
import openai

# from token_auth import get_current_user
import json

# import time


openai.api_key = os.environ["OPENAI_API_KEY"]

router = APIRouter()


class TestResponse(BaseModel):
    message: str

    # token = os.environ["TOKEN"]
    # # token of the day: aAjFqKGwYEp32myZHuDxafvHU6wOMKc5prWPlvqu8ydT9V4ITLpNMBkoQaVJ3r2dfyalKw.
    # bard = Bard(token=token)
    # chatbot_response = bard.get_answer(text)["content"]


class ReceivedMessage(BaseModel):
    text: str




def bard_test(**kwargs):
    pass


async def text_to_chatbot(text):
    with open("file.txt", "a") as new_file:
        new_file.write(text + "FROM TEXT_TO_CHAT")
    # return chatbot_response
    pass


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
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,  # Specifying en-US will conflict with our current non-English test-cases.
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


connected_socket = None


# ADD WEBSOCKETS HERE
# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     global connected_socket
#     await websocket.accept()
#     connected_socket = websocket
#     while True:
#         chatbot_response = await websocket.receive_text()
#         # audio_base64 = google_text_to_speech(chatbot_response)
#         with open("file.txt", "a") as new_file:
#             new_file.write(chatbot_response + "FROM websocket")
#         await websocket.send_text(chatbot_response)
#         return {"message": "The message was sent"}


# @router.post("/api/return-text")
# def sending_text(message: str):
#     # global connected_socket
#     # message_in = json.loads(message)
#     # if connected_socket:
#     #     with open("file.txt", "a") as new_file:
#     #         new_file.write("SOCKET OPEN")
#     #     await connected_socket.send_text(message_in)
#     #     return {"message": message_in}
#     # else:
#     #     with open("file.txt", "a") as new_file:
#     #         new_file.write("NO SOCKET")
#     # with open("file.txt", "a") as new_file:
#     #     new_file.write(message + "FROM sending_text")
#     return {}


# async def message_processor(message: dict):
#     # use bard api call to generate response
#     # might be os.environ.get()
#     text = message.text
#     chatbot_response = text_to_chatbot(text)
#     # audio = google_text_to_speech(chatbot_response)

#     # 6 sends audio back to client
#     await requests.post("http://localhost:8000/api/return-text", text)


# POST
@router.post("/api/messages", response_model=ReceivedMessage)
async def user_message_in(
    message: UserMessage,
    # background_tasks: BackgroundTasks
    # repo: ConversationQueries = Depends()
    # account: dict = Depends(get_current_user),
):
    message_in = # Query to create new message and add it into conversation collection
    message_history = # query to pull previous related messages from DB
    # ensure output of message_history is a list of dictionaries
    # CHAP GPT CHATBOT EXAMPLE REQUEST
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
         # messages must be a list dictionaries in the form
         # {"role": "user/system", {"message": "string"}}
        messages=message_history
    )

    # query to write completion to the DB collection
    print(completion.choices[0].message)

    # return chat message
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
