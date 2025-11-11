# src/model_evaluator.py
from google import genai
import os, json, re
from dotenv import load_dotenv

load_dotenv("config/.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=GEMINI_API_KEY)

def evaluate_with_model(prompt, expected, actual):
    """
    Uses Gemini 2.5 Flash to self-evaluate the answer.
    Returns relevance, correctness, and faithfulness scores (0–1).
    """
    eval_prompt = f"""
    You are an expert evaluator.
    Rate how well the AI's answer matches the expected output.

    Prompt: {prompt}
    Expected: {expected}
    Actual: {actual}

    Return valid JSON:
    {{
      "relevance": <float>,
      "correctness": <float>,
      "faithfulness": <float>
    }}
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=eval_prompt
        )

        # Extract text safely
        text = (
            response.candidates[0].content.parts[0].text.strip()
            if response.candidates else ""
        )

        json_match = re.search(r"\{.*\}", text, re.S)
        scores = json.loads(json_match.group()) if json_match else {}

        return {
            "AnswerRelevance": float(scores.get("relevance", 0)),
            "AnswerCorrectness": float(scores.get("correctness", 0)),
            "Faithfulness": float(scores.get("faithfulness", 0))
        }

    except Exception as e:
        print(f"Evaluation failed: {e}")
        return {"AnswerRelevance": 0, "AnswerCorrectness": 0, "Faithfulness": 0}
