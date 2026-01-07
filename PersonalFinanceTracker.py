from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# ===== נתונים פיננסיים (כרגע סטטיים) =====
finance_data = {
    "Month_Total_Balance": "11/2025",
    "income": 26000,
    "credit_total": 19000,
    "loans_total": 1150,
    "mortgage_total": 4000,
    "bank_account_balance": 1850,
    "Professional_Development_Fund": 150000,
    "Pension_Fund": 1200000
}

# ===== עמוד ראשי – UI עם צבעים =====
@app.route("/")
def home():
    totals = {
        "total_debt": finance_data["credit_total"]
                      + finance_data["loans_total"]
                      + finance_data["mortgage_total"],
        "net_monthly": finance_data["income"]
                       - (finance_data["loans_total"]
                          + finance_data["mortgage_total"])
    }

    return render_template(
        "index.html",
        finance_data=finance_data,
        totals=totals,
        updated_at=datetime.now().strftime("%d/%m/%Y %H:%M")
    )

# ===== API (לא חובה, אבל שימושי) =====
@app.route("/api/finance")
def api_finance():
    return jsonify(finance_data)

# ===== הרצה =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

