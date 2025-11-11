# src/check_geminkey.py
from google import genai
import os
from dotenv import load_dotenv

load_dotenv("config/.env")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create a Gemini client
client = genai.Client(api_key=api_key)

print("\n Connected to Gemini API successfully!\n")

# List available models
print("🧠 Models available for this key:\n")
for model in client.models.list():
    print(" -", model.name)
