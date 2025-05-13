# FILE: /backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from pydantic import BaseModel

from review_repo import KoalaResponse
from openai_repo import OpenAIKoalaRepo
from review_service import ReviewService

# Load environment variables from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

# Enable CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    raw_code: str
    review: str

@app.post("/review")
async def review_code(request: ReviewRequest) -> KoalaResponse:
    svc = ReviewService(review_repo=OpenAIKoalaRepo(openai_api_key))
    return svc.review(request.code)
