from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from pydantic import BaseModel
from models.messages import (
    UserMessage,
)

# basic command version
# Speech to Text API
router = APIRouter()

# # function, similar to hashed_pw, that gets the text out of request
# print("💻💻💻info looks like this: ", info)
# # not sure about below code
# audio = info.decoded_audio(info)
# print("🎤audio looks like this: ", audio)

# # Is request the mp3 file?
# # what is response
# model = whisper.load_model("base")
# print("💿💿💿 POST Model Loaded")
# result = model.transcribe(audio)
# print("🗣️🗣️🗣️Result after transcription is: ", result)


class TestResponse(BaseModel):
    message: str


# POST
@router.post("/api/messages", response_model=TestResponse)
def user_message_in(
    info: UserMessage,
    request: Request,
    response: Response,
):
    # get text and token from request

    # Send message and token to consumer.py

    return TestResponse(message="Success")


# import whisper
# Truncated Whisper code
# @router.get("/api/messages")
# def whisper_test():
#     model = whisper.load_model("base")
#     print("💿💿💿Model Loaded")
#     # .mp3, .wav, and .aif work (not sure about efficiency)
#     # .mp4 does not work
#     result = model.transcribe("./Efecto.wav")
#     print("🗣️🗣️🗣️Result after transcription is: ", result)
#     print(result["text"])
# Version with language detecetion and logmel shaving
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
