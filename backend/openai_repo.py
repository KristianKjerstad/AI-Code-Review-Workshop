from openai import OpenAI
from review_repo import KoalaRepo, KoalaResponse, KoalaFeedback


class OpenAIKoalaRepo(KoalaRepo):
    def __init__(self, api_key: str) -> None:
        # Initialize OpenAI client with API key from environment
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
        self.client = OpenAI(api_key=self.api_key)

    def review(self, code: str) -> KoalaResponse:
        # Call OpenAI API to review the code
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful code reviewer. Review the provided code and provide constructive feedback and suggestions for improvement."},
                    {"role": "user", "content": f"Please review this code:\n\n```\n{code}\n```"}
                ],
                temperature=0.7,
            )
            
            # Extract and format the response
            review_text = response.choices[0].message.content.strip()
            
            # Split into paragraphs for separate feedback items
            paragraphs = review_text.split("\n\n")
            feedback_items = []
            
            for paragraph in paragraphs:
                if paragraph.strip():  # Skip empty paragraphs
                    feedback_items.append(
                        KoalaFeedback(
                            msg=paragraph,
                            code_suggestion=""  # You can enhance this to extract code suggestions
                        )
                    )
            
            # If no feedback was extracted, provide a default response
            if not feedback_items:
                feedback_items = [KoalaFeedback(
                    msg="The code looks good! No issues found.",
                    code_suggestion=""
                )]
                
            return KoalaResponse(feedback=feedback_items)
            
        except Exception as e:
            # Handle errors gracefully
            return KoalaResponse(
                feedback=[
                    KoalaFeedback(
                        msg=f"Error during code review: {str(e)}",
                        code_suggestion="Please try again later."
                    )
                ]
            ) 