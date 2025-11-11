import csv
from datetime import datetime
import os
from llm_model import ask_model
from model_evaluator import evaluate_with_model
from safety_checker import check_safety
from report_generator import generate_report

def run_llm_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '..', 'data', 'test_prompts.csv')  # adjust if folder is different
    """
    Run the full Gemini-based LLM test pipeline.
    """
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        test_cases = list(reader)

    results = []

    for test in test_cases:
        prompt = test["prompt"]
        expected = test["expected_output"]

        print(f"Testing prompt ID {test['id']}...")

        actual = ask_model(prompt)
        eval_result = evaluate_with_model(prompt, expected, actual)
        safe = check_safety(actual)

        relevance = eval_result["AnswerRelevance"]
        correctness = eval_result["AnswerCorrectness"]
        passed = relevance >= 0.7 and correctness >= 0.7

        results.append({
            "id": test["id"],
            "prompt": prompt,
            "expected": expected,
            "actual": actual,
            "safe": "YES" if safe else "NO",
            "relevance": relevance,
            "correctness": correctness,
            "result": "PASS" if passed else "FAIL"
        })

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    generate_report(results, f"gemini_results_{timestamp}")

if __name__ == "__main__":
    run_llm_tests()
