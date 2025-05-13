from review_repo import KoalaResponse, ReviewRepo
import review_repo

class ReviewService:
    review_repo: ReviewRepo

    def __init__(self, review_repo: ReviewRepo):
        self.review_repo = review_repo

    def review(self, code: str) -> KoalaResponse:
        return self.review_repo.review(code)
