# AI Automation Toolkit

A production-ready FastAPI-based automation toolkit providing RESTful API endpoints.

## Project Structure

    app/
    ├── __init__.py
    ├── main.py              # FastAPI app entry point
    ├── schemas.py           # Pydantic request/response models
    ├── api/
    │   ├── __init__.py
    │   └── routes.py        # API route definitions
    ├── core/
    │   ├── __init__.py
    │   └── config.py        # Settings & configuration
    └── services/
        ├── __init__.py
        └── ai_service.py    # AI Service layer (DeepSeek-ready)
    main.py                  # Thin wrapper for running the app
    requirements.txt
    Dockerfile
    docker-compose.yml
    .env.example

## Quick Start

1. Install dependencies:

       pip install -r requirements.txt

2. (Optional) Configure AI Service:

   Copy .env.example to .env and set your DeepSeek API key:

       DEEPSEEK_API_KEY=sk-your-key-here

   Without a real key, the chat endpoint returns a mock reply.

3. Run the server:

       python main.py

4. Open http://localhost:8000 in your browser.

## API Endpoints

- GET /              — returns a welcome message
- GET /health        — health check
- POST /api/chat     — AI chat (mock mode if no API key)

       Request:   { "message": "hello" }
       Response:  { "reply": "AI Service is ready: hello" }

## AI Service

The `AIService` layer in `app/services/ai_service.py` is designed
to bridge the chat endpoint with the DeepSeek API.

- When `DEEPSEEK_API_KEY` is not set or equals `your_api_key_here`,
  the service returns a mock response: `"AI Service is ready: {message}"`.
- Set the environment variable to a real key to enable the actual API call.

## Docker

       docker-compose up --build
