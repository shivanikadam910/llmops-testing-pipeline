import pandas as pd
import os
from datetime import datetime

def generate_report(results, report_name):
    """
    Generate both CSV and HTML reports for LLM evaluations.
    """
    os.makedirs("reports", exist_ok=True)
    df = pd.DataFrame(results)

    csv_path = f"reports/{report_name}.csv"
    html_path = f"reports/{report_name}.html"

    # Save CSV
    df.to_csv(csv_path, index=False)

    # Create HTML report
    passed = df['result'].value_counts().get('PASS', 0)
    failed = df['result'].value_counts().get('FAIL', 0)
    safe = df['safe'].value_counts().get('YES', 0)
    unsafe = df['safe'].value_counts().get('NO', 0)

    summary_html = f"""
    <h2>🧠 Gemini LLM Test Report</h2>
    <p><b>Passed:</b> {passed} | <b>Failed:</b> {failed}</p>
    <p><b>Safe:</b> {safe} | <b>Unsafe:</b> {unsafe}</p>
    <hr>
    {df.to_html(index=False)}
    """

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(summary_html)

    print(f"Reports generated:\n - {csv_path}\n - {html_path}")
