from app.core.config import settings


class AIService:

    @staticmethod
    async def chat(message: str) -> str:
        if not settings.deepseek_api_key or settings.deepseek_api_key == "your_api_key_here":
            return f"AI Service is ready: {message}"

        # TODO: call DeepSeek API when key is configured
        # async with httpx.AsyncClient() as client:
        #     resp = await client.post(...)
        return f"AI Service is ready: {message}"
