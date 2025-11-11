# src/llm_model.py
from google import genai
import os
from dotenv import load_dotenv

load_dotenv("config/.env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

def ask_model(prompt: str) -> str:
    """Send a prompt to Gemini 2.5 Flash and return clean output."""
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        # Extract text safely
        if response and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "[No response from model]"
    except Exception as e:
        return f"[Gemini Error: {e}]"
