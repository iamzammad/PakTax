from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_tax(annual_income):
    if annual_income <= 600000:
        return 0
    elif annual_income <= 1200000:
        return (annual_income - 600000) * 0.05
    elif annual_income <= 2200000:
        return 30000 + (annual_income - 1200000) * 0.15
    elif annual_income <= 3200000:
        return 180000 + (annual_income - 2200000) * 0.25
    elif annual_income <= 4100000:
        return 430000 + (annual_income - 3200000) * 0.30
    else:
        return 700000 + (annual_income - 4100000) * 0.35

@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        salary_input = request.form.get("monthly_salary")
        monthly_salary = float(salary_input)

        if monthly_salary < 0:
            return render_template("form.html", result={"error": "Salary cannot be negative"})

        annual_salary = monthly_salary * 12
        annual_tax = calculate_tax(annual_salary)
        monthly_tax = annual_tax / 12
        net_income = monthly_salary - monthly_tax

        result = {
            "gross": round(monthly_salary, 2),
            "tax": round(monthly_tax, 2),
            "net": round(net_income, 2)
        }

        return render_template("form.html", result=result)

    except (ValueError, TypeError):
        return render_template("form.html", result={"error": "Please enter a valid number"})

if __name__ == "__main__":
    app.run(debug=True)