from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import ask_weather_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Query):
    return {"response": ask_weather_question(q.question)}