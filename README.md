# 🤖 Gemini LLMOps Testing Automation Pipeline

### 🧠 AI-as-a-Judge | Model Quality Regression Testing

---

#### 📌 Overview

This project demonstrates how to **automate LLM testing and evaluation** using **Google Gemini models**

It’s designed as a **mini LLMOps pipeline** that continuously tests an LLM (like Gemini) against defined prompts, expected responses, and safety policies.

## 🚀 Key Features

| Feature | Description |
|----------|-------------|
| **Gemini-only stack** | Works entirely with your `GEMINI_API_KEY`. |
| **AI-as-a-Judge** | Uses Gemini itself to evaluate output quality (Relevance, Correctness, Faithfulness). |
| **Safety Validation** | Gemini-based content moderation check for unsafe or policy-violating outputs. |
| **Automated Reporting** | Generates timestamped result files (CSV / HTML) with scores and pass/fail status. |

---

⚙️ Installation & Setup
1. Clone the repository
cd llmops-testing-pipeline

2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate  # (Windows)

3. Install dependencies
pip install -r requirements.txt

4. Configure your Gemini API key
Create a .env file under config/:
GEMINI_API_KEY=your_api_key_here
