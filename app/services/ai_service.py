import httpx
from app.core.config import settings


class AIService:

    @staticmethod
    async def chat(message: str) -> str:
        if not settings.deepseek_api_key or settings.deepseek_api_key == "your_api_key_here":
            return f"AI Service is ready: {message}"

        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    "https://api.deepseek.com/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.deepseek_api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": "deepseek-chat",
                        "messages": [
                            {
                                "role": "user",
                                "content": message,
                            }
                        ],
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                return data["choices"][0]["message"]["content"]
        except httpx.HTTPStatusError as e:
            return f"AI 服务暂时不可用（HTTP {e.response.status_code}），请稍后再试。"
        except httpx.RequestError:
            return "AI 服务连接失败，请检查网络或 API 配置。"
        except (KeyError, IndexError, ValueError):
            return "AI 服务返回了异常数据，请稍后再试。"
