# Tests for chatbot
def test_ask():
    from app.chatbot import ask_weather_question
    response = ask_weather_question("What was the temperature trend?")
    assert isinstance(response, str) and len(response) > 0