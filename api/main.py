from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers.auth import authenticator
from fastapi import APIRouter, Depends
from routers import accounts, messages

# from consumer import converse, start_connection, Hugo_cool

router = APIRouter()


@router.post("/api/things")
async def create_thing(
    # looks for a bearer token in the AUTH header or
    # looks for a cookie in the "fastapi_token"
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    pass


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authenticator.router)
app.include_router(accounts.router)
app.include_router(messages.router)
# start_connection()


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }
