# AI Automation Toolkit (V3)

A production-ready FastAPI-based automation toolkit providing RESTful API endpoints.
Integrated with DeepSeek API for real AI chat responses.

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
        └── ai_service.py    # AI Service layer (DeepSeek V3)
    main.py                  # Thin wrapper for running the app
    requirements.txt
    Dockerfile
    docker-compose.yml
    .env.example

## Quick Start

1. Install dependencies:

       pip install -r requirements.txt

2. (Optional) Configure AI Service (DeepSeek):

   Copy `.env.example` to `.env` and set your DeepSeek API key:

       DEEPSEEK_API_KEY=sk-your-key-here

   Get a key at [https://platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys).

   Without a real key, the chat endpoint returns a mock reply.

3. Run the server:

       python main.py

4. Open http://localhost:8000 in your browser.

## API Endpoints

- GET /              — returns a welcome message
- GET /health        — health check
- POST /api/chat     — AI chat (real DeepSeek reply when API key is set, mock otherwise)

       Request:   { "message": "hello" }
       Response:  { "reply": "Hello! How can I help you today?" }


- POST /api/upload   — upload a PDF file and extract its text

       Request:  multipart/form-data with a "file" field (PDF)
       Response: { "filename": "...", "text_length": N, "preview": "first 500 chars" }

## AI Service

The `AIService` layer in `app/services/ai_service.py` bridges the chat
endpoint with the DeepSeek API using `httpx.AsyncClient`.

- **Mock mode**: When `DEEPSEEK_API_KEY` is not set or equals
  `your_api_key_here`, returns `"AI Service is ready: {message}"`.
- **Real mode**: When a valid key is configured, sends the user message
  to `https://api.deepseek.com/chat/completions` (`deepseek-chat` model)
  and returns the AI-generated reply.
- **Error handling**: If the API call fails (network error, invalid key,
  server error, or unexpected response format), a friendly Chinese error
  message is returned rather than crashing.

No changes to the POST `/api/chat` interface — the request/response
schemas (`ChatRequest` / `ChatResponse`) remain identical.

### DeepSeek Configuration Steps

1. Obtain a DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/).
2. Create a `.env` file in the project root:

       DEEPSEEK_API_KEY=sk-your-actual-key

3. Restart the server. The chat endpoint will now use the real model.

**Note**: The API key is read from environment or `.env` file via
`pydantic-settings`. No hardcoded keys are used.

## PDF Upload API

Upload a PDF file and extract its text content using PyMuPDF (fitz).

- **Endpoint**: `POST /api/upload`
- **Request**: `multipart/form-data` with a `file` field
- **File size limit**: controlled by FastAPI defaults (`UploadFile`)
- **Flow**: uploaded file is saved to `uploads/`, then `PDFService.extract_text()`
  reads all pages using PyMuPDF and returns a preview.

### Example

    curl -X POST http://localhost:8000/api/upload \\
      -F "file=@document.pdf"

### Response

    {
      "filename": "document.pdf",
      "text_length": 3421,
      "preview": "First 500 characters of extracted text..."
    }

**Note**: Only `.pdf` files are accepted. A random UUID filename is used
on the server to avoid collisions.

## Docker

       docker-compose up --build
