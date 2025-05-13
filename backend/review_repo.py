from typing import Protocol
from pydantic import BaseModel

class KoalaFeedback(BaseModel):
    feedback: str
    review: str

class KoalaResponse(BaseModel):
    feedback: list[KoalaFeedback]

class ReviewRepo(Protocol):

    def review(self, code: str) -> KoalaResponse:
        ...


class OpenAIKoalaRepo(ReviewRepo):

    def __init__(self) -> None:
        super().__init__()

    def review(self, code: str) -> KoalaResponse:
        return KoalaResponse(
            feedback=[
                KoalaFeedback(feedback="HEEI<3", review="Here is your review, from the koala")
            ]
        )
