from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from pydantic import BaseModel
import whisper

# from queries.messages import (
#     DuplicateAccountError,
# )
# from models.messages import (


# )
# basic command version
# Speech to Text API
router = APIRouter()


@router.get("/api/messages")
def whisper_test():
    model = whisper.load_model("tiny")
    print("💿💿💿Model Loaded")
    result = model.transcribe("./HR_test.mp3")
    print("🗣️🗣️🗣️Result after transcription is: ", result)
    print(result["text"])


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


@router.post("/api/messages")
def user_message_in(
    # info: ,
    request: Request,
    response: Response,
):
    pass
