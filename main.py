# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel

from agent import ai_agent

app = FastAPI(title="Mini AI Agent API")


class AskRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {"status": "running"}


@app.post("/ask")
def ask_question(request: AskRequest):
    response = ai_agent(request.question)

    return {
        "question": request.question,
        "answer": response
    }