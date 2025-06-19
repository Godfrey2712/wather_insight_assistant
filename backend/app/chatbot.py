import os
from openai import AzureOpenAI
from app.utils import load_weather_data, to_context_string
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI Client
client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
)

def ask_weather_question(question: str) -> str:
    df = load_weather_data()
    context = to_context_string(df)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for analyzing weather data."},
            {"role": "user", "content": f"Data:\n{context}\n\nQuestion:\n{question}"}
        ]
    )

    return response.choices[0].message.content