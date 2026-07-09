# AI Automation Toolkit

A production-ready FastAPI-based automation toolkit providing RESTful API endpoints.

## Project Structure

    app/
    ├── __init__.py
    ├── main.py          # FastAPI app entry point
    ├── api/
    │   ├── __init__.py
    │   └── routes.py    # API route definitions
    ├── core/
    │   ├── __init__.py
    │   └── config.py    # Settings & configuration
    └── services/
        └── __init__.py
    main.py              # Thin wrapper for running the app
    requirements.txt
    Dockerfile
    docker-compose.yml
    .env.example

## Quick Start

1. Install dependencies:

       pip install -r requirements.txt

2. Run the server:

       python main.py

3. Open http://localhost:8000 in your browser.

## API Endpoints

- GET /              — returns a welcome message
- GET /health        — health check
- POST /api/chat     — echo chat endpoint

       Request:   { "message": "hello" }
       Response:  { "reply": "hello" }

## Docker

       docker-compose up --build
