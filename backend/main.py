# FILE: /backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

from review_repo import KoalaResponse, MockKoalaRepo, OpenAIKoalaRepo
from review_service import ReviewService

load_dotenv()  # Load environment variables from .env

app = FastAPI()

# Enable CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")


class ReviewRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    raw_code: str
    review: str




@app.post("/review")
async def review_code(request: ReviewRequest) -> KoalaResponse:
    svc = ReviewService(review_repo=MockKoalaRepo())

    return svc.review(request.code)
