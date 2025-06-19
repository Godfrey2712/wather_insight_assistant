from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import ask_weather_question

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Query):
    return {"response": ask_weather_question(q.question)}