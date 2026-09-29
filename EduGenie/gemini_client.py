"""Shared helper for calling Google Gemini."""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
_client = None


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return the text reply."""
    global _client
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")
    if _client is None:
        _client = genai.Client(api_key=key)
    resp = _client.models.generate_content(model=MODEL, contents=prompt)
    if not resp.text:
        raise RuntimeError("Gemini returned an empty or blocked response.")
    return resp.text.strip()
