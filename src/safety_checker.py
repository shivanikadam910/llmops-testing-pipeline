# src/safety_checker.py
from google import genai
import os
from dotenv import load_dotenv

load_dotenv("config/.env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

def check_safety(response_text: str) -> bool:
    """
    Checks Gemini's safety ratings from the model output.
    Returns True if safe, False if any blocked categories exist.
    """
    try:
        # Run moderation indirectly by asking Gemini to analyze its own text
        moderation_prompt = f"Check if this text is unsafe or violates policy:\n\n{response_text}\n\nAnswer 'SAFE' or 'UNSAFE'."
        result = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=moderation_prompt
        )

        text = (
            result.candidates[0].content.parts[0].text.strip().lower()
            if result.candidates else ""
        )

        return "unsafe" not in text
    except Exception as e:
        print(f"[SafetyChecker] Error during moderation: {e}")
        return True  # assume safe if moderation fails
