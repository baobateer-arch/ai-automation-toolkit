from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.services.ai_service import AIService

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to Contract Risk AI"}


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/api/chat", response_model=ChatResponse)
async def chat(body: ChatRequest):
    reply = await AIService.chat(body.message)
    return ChatResponse(reply=reply)
