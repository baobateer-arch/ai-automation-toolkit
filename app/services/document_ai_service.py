import json
import re
from app.services.ai_service import AIService


class DocumentAIService:

    @staticmethod
    async def analyze(text: str) -> dict:
        prompt = f"""You are a professional document analyst. Analyze the following document and return a JSON object with exactly these four fields:

- "summary": a concise Chinese summary of the document (1-3 sentences)
- "key_points": an array of 3-5 key points in Chinese
- "risks": an array of potential risks or issues identified in the document, in Chinese (can be empty)
- "suggestions": an array of actionable suggestions based on the document content, in Chinese (can be empty)

Only output the JSON object, no other text.

Document:
{text[:8000]}
"""
        reply = await AIService.chat(prompt)

        # Try to parse the JSON from the reply
        try:
            # First, try direct JSON parse
            return json.loads(reply)
        except json.JSONDecodeError:
            pass

        # Try to extract a JSON block from markdown fences
        match = re.search(r'```(?:json)?\s*\n?(.*?)\n?```', reply, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                pass

        # Try to find a JSON-like object with curly braces
        brace_match = re.search(r'\{.*\}', reply, re.DOTALL)
        if brace_match:
            try:
                return json.loads(brace_match.group(0))
            except json.JSONDecodeError:
                pass

        # Fallback: return the raw reply wrapped in a generic structure
        return {
            "summary": reply,
            "key_points": [],
            "risks": [],
            "suggestions": [],
        }
