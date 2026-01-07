from flask import Flask, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)

# Keep your existing env-based path (works in Docker/K8s/Helm)
DATA_FILE = os.environ.get("DATA_PATH", os.path.join("json_data", "finance_data.json"))


def load_finance_data(path: str) -> dict:
    """Load finance data from JSON file. Returns {} if file missing/invalid."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": f"Data file not found: {path}"}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON in: {path}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def calc_demo_score(data: dict) -> int:
    """
    Simple (demo) score 0-100 for the UI meter.
    Not financial advice—just a visual indicator for the project.
    """
    # If there's an error, show a low score to highlight the issue
    if "error" in data:
        return 30

    income = float(data.get("income", 0) or 0)
    credit = float(data.get("credit_total", 0) or 0)
    loans = float(data.get("loans_total", 0) or 0)
    mortgage = float(data.get("mortgage_total", 0) or 0)

    debt = credit + loans + mortgage

    # Very simple heuristic: higher income and lower debt -> higher score
    if income <= 0 and debt > 0:
        return 25

    ratio = (income + 1) / (debt + 1)  # avoid divide by zero
    # Map ratio to score
    score = int(max(0, min(100, (ratio * 25) + 35)))
    return score


@app.route("/")
def home():
    data = load_finance_data(DATA_FILE)
    score = calc_demo_score(data)
    raw_json = json.dumps(data, indent=2, ensure_ascii=False)
    year = datetime.now().year

    return render_template(
        "index.html",
        data=data,
        score=score,
        raw_json=raw_json,
        year=year,
        data_file=DATA_FILE,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

