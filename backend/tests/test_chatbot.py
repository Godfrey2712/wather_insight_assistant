import pytest
from app.chatbot import ask_weather_question

def test_ask_weather_question_returns_string():
    question = "What was the temperature trend?"
    response = ask_weather_question(question)

    assert isinstance(response, str), "Response is not a string"
    assert len(response.strip()) > 0, "Response is empty"
    assert "temperature" in response.lower() or "trend" in response.lower(), "Response does not mention temperature/trend"
