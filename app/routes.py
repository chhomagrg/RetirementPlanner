from flask import request, render_template
from app.utils import calculate_total_savings, generate_interactive_chart
from app import app
@app.route("/", methods=["GET", "POST"])
def index():
    total_savings = None
    inflation_adjusted_savings = None
    chart_url = None

    if request.method == "POST":
        # Collect user inputs
        current_savings = float(request.form["current_savings"])
        annual_income = float(request.form["annual_income"])
        savings_rate = float(request.form["savings_rate"])
        current_age = int(request.form["current_age"])
        retirement_age = int(request.form["retirement_age"])
        annual_return = float(request.form["annual_return"])
        inflation_rate = float(request.form["inflation_rate"])
        income_growth_rate = float(request.form["income_growth_rate"])

        # Perform calculations
        total_savings, unadjusted_savings_data, inflation_adjusted_savings_data = calculate_total_savings(
            current_savings=current_savings,
            annual_income=annual_income,
            savings_rate=savings_rate,
            current_age=current_age,
            retirement_age=retirement_age,
            annual_return=annual_return,
            inflation_rate=inflation_rate,
            income_growth_rate=income_growth_rate
        )

        # Format inflation-adjusted savings and total savings
        inflation_adjusted_savings = f"{inflation_adjusted_savings_data[-1]:,.2f}"
        total_savings = f"{total_savings:,.2f}"

        # Generate the chart
        chart_url = generate_interactive_chart(unadjusted_savings_data, inflation_adjusted_savings_data, current_age, retirement_age)

    return render_template("index.html", total_savings=total_savings, inflation_adjusted_savings=inflation_adjusted_savings, chart_url=chart_url)











