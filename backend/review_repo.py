from typing import Protocol
from pydantic import BaseModel

class KoalaFeedback(BaseModel):
    msg: str
    code_suggestion: str

class KoalaResponse(BaseModel):
    feedback: list[KoalaFeedback]

class KoalaRepo(Protocol):

    def review(self, code: str) -> KoalaResponse:
        ...


class OpenAIKoalaRepo(KoalaRepo):

    def __init__(self) -> None:
        super().__init__()

    def review(self, code: str) -> KoalaResponse:
        return KoalaResponse(
            feedback=[
                KoalaFeedback(msg="HEEI<3", code_suggestion="Here is your review, from the koala")
            ]
        )

class MockKoalaRepo(KoalaRepo):

    def review(self, code: str) -> KoalaResponse:
        return KoalaResponse(
            feedback=[
                KoalaFeedback(msg="HEEI FROM MOCK REPO<3", code_suggestion="Here is your review, from the koala")
            ]
        )
