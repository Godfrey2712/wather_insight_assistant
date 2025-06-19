# 🌤️ Weather Insight Assistant

> A full-stack, Azure-powered weather analysis chatbot system\
> Built with Microsoft Fabric, Azure OpenAI, React, Docker, and CI/CD

---

## 🔠 What This Project Does

- Ingests weather data from [Meteostat API](https://dev.meteostat.net/api/) via Microsoft Fabric from Rapid API
- Curates it into structured CSV for querying
- Lets users interact via a GPT-4o chatbot
- Deploys frontend + backend to Azure with CI/CD pipelines

---

## 🔧 Technologies Used

| Area | Stack |
| ---- | ----- |
| Data |       |

| **Microsoft Fabric** (Lakehouse, Notebooks) |                                                     |
| ------------------------------------------- | --------------------------------------------------- |
| AI Model                                    | **Azure OpenAI** (GPT-4o via RAG)                   |
| Frontend                                    | **React + TypeScript**                              |
| Backend                                     | **FastAPI + Docker**                                |
| DevOps                                      | **GitHub Actions CI/CD**                            |
| Hosting                                     | **Azure Container Apps**, **Azure Static Web Apps** |

---

## 📁 Architecture Overview

```text
[ Meteostat API ] ---> [ Fabric Ingestion & Notebook ] ---> [ Curated CSV (Lakehouse) ]
                                                              ↓
                                                        [ FastAPI + Azure OpenAI ]
                                                              ↓
                                                      [ React Chat Interface (SPA) ]
```

---

## ✅ Features

### 📡 Data Ingestion & Storage

- Ingests hourly weather data using Microsoft Fabric notebooks
- Saves curated data to both Lakehouse table & CSV

### 💬 Chatbot with Azure OpenAI

- Conversational UI with GPT-4o
- Answers natural language queries about trends, anomalies, etc.

### 🖥️ Frontend (React + TypeScript)

- Chat UI built with Vite + TypeScript
- Calls backend API for responses

### 🚀 CI/CD + Deployment

- Backend: Deployed via Docker to Azure Container Apps
- Frontend: Auto-deployed to Azure Static Web Apps
- GitHub Actions automate tests & deployments

---

## 🌐 Live Demos

| Component       | URL                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------ |
| 🔙 Backend API  | [Swagger Docs](https://weather-api.victorioussea-d774307a.westeurope.azurecontainerapps.io/docs) |
| 🕒 Frontend     | [Live Chat App](https://blue-desert-0f166e803.2.azurestaticapps.net/)                            |
| 🐳 Docker Image | [Docker Hub](https://hub.docker.com/r/godfrey27/weather-api)                                     |

---

## 🥞 Sample Questions to Try

- “What was the temperature trend over the past 3 days?”
- “Did wind speed spike this week?”
- “Summarise the weather conditions in the last 24 hours.”
- “Compare humidity between June 10 and June 12.”

---

## ⚙️ Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/weather_insight_assistant
cd weather_insight_assistant
```

### 2. Backend (FastAPI)

```bash
cd backend
docker build -t weather-api .
docker run -p 8000:8000 --env-file ../.env weather-api
```

### 3. Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

### 4. Tests

```bash
PYTHONPATH=backend pytest backend/tests
```

---

## 🤖 CI/CD Setup

### Backend: `.github/workflows/ci-cd.yml`

- Builds image
- Runs tests
- Pushes to Docker Hub
- Deploys to Azure Container App

### Frontend: `.github/workflows/azure-static-web-apps-*.yml`

- Builds with Vite
- Deploys to Azure Static Web Apps

---

## ☁️ Deploy Backend to Azure (Manually)

```bash
# 1. Create infra
az group create --name weather-rg --location westeurope
az containerapp env create --name weather-env --resource-group weather-rg --location westeurope

# 2. Build and push
docker build -t godfrey27/weather-api:latest .
docker push godfrey27/weather-api:latest

# 3. Deploy
az containerapp create \
  --name weather-api \
  --resource-group weather-rg \
  --environment weather-env \
  --image godfrey27/weather-api:latest \
  --target-port 8000 \
  --ingress external \
  --env-vars \
    AZURE_OPENAI_KEY=<your-api-key> \
    AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.cognitiveservices.azure.com/
```

---

## 🔐 Environment Variables Required

Set these in `.env` and/or GitHub Secrets:

```env
AZURE_OPENAI_KEY=<your-api-key>
AZURE_OPENAI_ENDPOINT=https://<your-endpoint>
X-Rapidapi-Key=<your-rapidapi-key>
```

---

## 📋 References

- [Azure OpenAI Docs](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Meteostat API](https://dev.meteostat.net/api/)
- [Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Vite](https://vitejs.dev/)
