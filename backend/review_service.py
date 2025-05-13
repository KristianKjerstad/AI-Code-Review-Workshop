from review_repo import KoalaResponse, KoalaRepo
import review_repo

class ReviewService:
    review_repo: KoalaRepo

    def __init__(self, review_repo: KoalaRepo):
        self.review_repo = review_repo

    def review(self, code: str) -> KoalaResponse:
        return self.review_repo.review(code)
