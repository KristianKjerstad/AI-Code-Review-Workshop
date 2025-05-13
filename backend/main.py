from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from typing import List
import os
import pathlib
import subprocess
from gitignore_parser import parse_gitignore
import openai

app = FastAPI()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to project files
PROJECT_BASE_PATH = os.getenv("PROJECT_BASE_PATH", "../../dingo-code")

# Domain description to help AI understand context
domain_description = """
This software project is a web-based platform that enables developers to collaborate on code reviews using AI assistance. The AI provides comments and suggestions on git diffs, evaluating changes in context of the project and intended outcomes.
"""

# --- File Scanner ---

def get_all_project_files(base_path: str) -> List[str]:
    gitignore_path = os.path.join(base_path, '.gitignore')
    is_ignored = parse_gitignore(gitignore_path) if os.path.exists(gitignore_path) else lambda path: False

    file_paths = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".py"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path)
            if not is_ignored(rel_path):
                file_paths.append(full_path)
    return file_paths

# --- Git Pull ---

def update_repository(base_path: str):
    try:
        result = subprocess.run(["git", "pull"], cwd=base_path, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Git pull failed: {str(e)}")

# --- AI Prompt Construction ---

def construct_prompt(diff: str, intent: str) -> str:
    # update_repository(PROJECT_BASE_PATH)

    files_content = ""
    for filepath in get_all_project_files(PROJECT_BASE_PATH):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                rel_path = os.path.relpath(filepath, PROJECT_BASE_PATH)
                files_content += f"\n\n--- FILE: {rel_path} ---\n{content}\n"
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading file {filepath}: {str(e)}")

    prompt = f"""
You are an expert software engineer helping review code changes. Here is the project description:

{domain_description}

The developer intends to: "{intent}"

Below is the full git diff of the proposed change:

{diff}

And here are all the existing files in the project, separated clearly by filename:

{files_content}

Please perform a code review, focusing on correctness, performance, readability, adherence to best practices, and alignment with the stated intent. Respond with specific, actionable feedback.
You are very strict, and will nitpick if you can not find anything to give feedback on.
You are not afraid to make the developer cry! Show no mercy!
Use Markdown and emojis to make the output pretty.
Be very fancy with styling, using headers and break into sections for easier reading, and use plenty of emojis.
"""
    return prompt

# --- AI Request Handler ---

def get_code_review(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior software engineer doing code reviews."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI request failed: {str(e)}")

# --- FastAPI Endpoint ---

@app.post("/code-review")
def code_review(
    diff: str = Form(...),
    intent: str = Form(...)
):
    prompt = construct_prompt(diff, intent)
    feedback = get_code_review(prompt)
    return {"review": feedback}
