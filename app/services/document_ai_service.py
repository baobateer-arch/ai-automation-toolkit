import json
import re
from app.services.ai_service import AIService


class DocumentAIService:

    @staticmethod
    async def analyze(text: str) -> dict:
        prompt = f"""You are an experienced contract lawyer reviewing a business agreement.

Analyze the contract text below and return a JSON object with exactly these five fields:

- "risk_level": "Low", "Medium", or "High" — overall risk assessment
- "summary": a concise English summary of the contract (2-3 sentences)
- "high_risks": an array of high-risk clauses or issues found, in English (can be empty)
- "missing_clauses": an array of important clauses that appear to be missing, in English (can be empty)
- "suggestions": an array of actionable suggested improvements, in English (can be empty)

Only output the JSON object, no other text.

Contract text:
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
            "risk_level": "Unknown",
            "summary": reply,
            "high_risks": [],
            "missing_clauses": [],
            "suggestions": [],
        }
