# AI-Code-Review-Workshop
Code review workshop for Brilliant



# ⚔️ Quests 

- Create UI design for frontend 
- Implement frontend web app where user can input code, and receive code review.
- Explore the [OpenAI](https://pypi.org/project/openai/) Python package and learn how it works
- Implement the `/review` API endpoint in `main.py´. Take input code from user, and return a code review.


You can use the code under `testdata` folder for testing if you want, or bring your own code. 

Experiment with tweaking the `/review` endpoint. Find out what you can configure to improve the review. Think about adding more context (language, project type), be explicit about what you want to review (readability, performance, security), etc.


# Start frontend

1. In a terminal, navigate to the "frontend" folder. 
2. Run `npm install` 
3. Run `npm run dev`

The frontend is now running on http://localhost:5173


# start backend
1. In a terminal, navigate to the "backend" folder. 
2. Run `pip install -r requirements.txt` (Optional - create a virtual environemnt before installing dependencies)
3. Run `uvicorn main:app --reload --host 0.0.0.0 --port 8000` 

The APi is now running on http://localhost:8000

Documentation is available at: http://localhost:8000/docs