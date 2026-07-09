from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "AI Automation Toolkit"}


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/api/chat")
async def chat(body: dict):
    message = body.get("message", "")
    return {"reply": message}
