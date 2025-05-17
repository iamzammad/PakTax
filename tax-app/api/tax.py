from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("form.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        monthly_salary = float(request.form['monthly_salary'])
        annual_salary = monthly_salary * 12

        # Tax logic
        tax = 0
        if annual_salary <= 600000:
            tax = 0
        elif annual_salary <= 1200000:
            tax = (annual_salary - 600000) * 0.025
        elif annual_salary <= 2400000:
            tax = 15000 + (annual_salary - 1200000) * 0.125
        elif annual_salary <= 3600000:
            tax = 165000 + (annual_salary - 2400000) * 0.2
        elif annual_salary <= 6000000:
            tax = 405000 + (annual_salary - 3600000) * 0.25
        elif annual_salary <= 12000000:
            tax = 1005000 + (annual_salary - 6000000) * 0.325
        else:
            tax = 2955000 + (annual_salary - 12000000) * 0.35

        monthly_tax = tax / 12
        net_monthly_income = monthly_salary - monthly_tax

        result = {
            "gross": round(monthly_salary, 2),
            "tax": round(monthly_tax, 2),
            "net": round(net_monthly_income, 2)
        }
    except Exception:
        result = { "error": "Please enter a valid numeric salary." }

    return render_template("form.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)