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


class TestResponse(BaseModel):
    message: str


# POST
@router.post("/api/messages")
def user_message_in():
    # get text and token from request
    print()

    # Send message and token to consumer.py

    return


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
