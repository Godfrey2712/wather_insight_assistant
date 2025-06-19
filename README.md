Weather Source API:
[Meteostat JSON API](https://dev.meteostat.net/api/)

## Overview

This project provides a weather-based data pipeline and chatbot interface to analyze weather trends and their potential impact on energy demand. The system integrates data ingestion, transformation, and a conversational AI interface for querying weather insights.

## Features

### Data Pipeline
- **Ingestion**: Fetches hourly weather data from the Meteostat API for a specified location (e.g., Toronto).
- **Transformation**: Converts raw weather data into a curated schema using PySpark for downstream analysis.
- **Storage**: Saves curated data in a Lakehouse table and as CSV files for easy access.

### Chatbot
- **Conversational Interface**: Allows users to ask weather-related questions and receive insights.
- **Powered by Azure OpenAI**: Uses GPT-based models to generate responses based on weather data.
- **Contextual Analysis**: Converts weather data into a readable format for the AI model.

### Frontend
- **Interactive UI**: A React-based interface for users to input questions and view chatbot responses.

### Infrastructure
- **Azure Integration**: Utilizes Azure OpenAI and Bicep templates for cloud infrastructure deployment.
- **CI/CD**: Automated testing and deployment using GitHub Actions.

## System Architecture

1. **Data Ingestion**:
    - File: `data-pipeline/weather_ingest.py`
    - Fetches weather data using the Meteostat API and saves it locally.

2. **Data Transformation**:
    - File: `data-pipeline/transform_to_curated.py`
    - Transforms raw weather data into a curated schema using PySpark.

3. **Backend**:
    - File: `backend/app/chatbot.py`
    - Handles chatbot logic and integrates with Azure OpenAI for generating responses.
    - File: `backend/app/utils.py`
    - Provides utility functions for loading and formatting weather data.

4. **Frontend**:
    - File: `frontend/src/components/Chat.tsx`
    - Implements the chat interface for user interaction.

5. **Testing**:
    - File: `backend/tests/test_chatbot.py`
    - Includes unit tests for chatbot functionality.

6. **Deployment**:
    - File: `.github/workflows/ci-cd.yml`
    - Automates testing and deployment processes.

## Environment Variables

The following environment variables are required:
- `AZURE_OPENAI_KEY`: API key for Azure OpenAI.
- `AZURE_OPENAI_ENDPOINT`: Endpoint for Azure OpenAI.
- `X-Rapidapi-Key`: API key for Meteostat.

## Sample Queries for Chatbot

### 🌡️ Temperature-based Demand Patterns
- “What was the temperature trend over the past 3 days?”
- “How did the temperature drop affect demand on June 15?”
- “Was there a sudden spike in temperature yesterday that might correlate with increased usage?”

### 💨 Wind/Humidity Influence
- “Was the wind speed unusually high during any period this week?”
- “Compare humidity between June 10 and June 12 — was it a factor in energy demand?”
- “Does high humidity correspond with high energy usage?”

### 📈 Trend Analysis & Alerts
- “List any weather anomalies in the last 48 hours that may have caused demand spikes.”
- “Which hours today had both low temperature and high wind speed?”
- “What weather conditions typically lead to demand spikes in the evening?”

### 🔄 General Diagnostic & Summary
- “Summarise the weather conditions over the last 24 hours.”
- “What weather pattern do we see this week that could affect power usage?”
- “How does today’s weather compare to the same time last week?”

## How to Run

1. **Backend**:
    - Install dependencies: `pip install -r backend/requirements.txt`
    - Run the server: `uvicorn backend/app/main:app --host 0.0.0.0 --port 8000`

2. **Frontend**:
    - Navigate to the `frontend` directory.
    - Install dependencies: `npm install`
    - Start the development server: `npm start`

3. **Data Pipeline**:
    - Run ingestion: `python data-pipeline/weather_ingest.py`
    - Run transformation: `python data-pipeline/transform_to_curated.py`

4. **Testing**:
    - Run tests: `pytest backend/tests --cov=app`

## Deployment

- Use the provided Bicep templates in the `infra` directory for Azure resource provisioning.
- CI/CD pipeline is configured in `.github/workflows/ci-cd.yml`.

## Notes

- Ensure the `.env` file is correctly configured with the required API keys.
- The chatbot relies on the curated weather data stored in `data/curated_data.csv`.

## References

- [Meteostat API Documentation](https://dev.meteostat.net/api/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
