import plotly.graph_objects as go

# Calculate the total savings by the time of retirement
def calculate_total_savings(current_savings, annual_income, savings_rate, current_age, retirement_age, annual_return, inflation_rate, income_growth_rate):
    years_to_retirement = retirement_age - current_age
    total_savings = current_savings
    unadjusted_savings_data = [current_savings] # Savings without inflation
    inflation_adjusted_savings_data = [current_savings] # Savings adjusted for inflation

    for year in range(years_to_retirement):
        # Add yearly savings based on a percentage of income
        yearly_savings = annual_income * (savings_rate / 100)
        total_savings += yearly_savings

        # Apply annual return
        total_savings *= (1 + annual_return / 100)

        # Save unadjusted savings data
        unadjusted_savings_data.append(total_savings)

        # Adjust the savings for inflation a
        inflation_factor = (1 + inflation_rate / 100) ** (year + 1)
        inflation_adjusted_savings_data.append(total_savings / inflation_factor)

        # Increase the income for the next year based on income growth
        annual_income *= (1 + income_growth_rate / 100)

    return round(total_savings, 2), unadjusted_savings_data, inflation_adjusted_savings_data

# Default chart you see when you load the website
def generate_default_chart():
    # Placeholder data
    current_age = 25
    retirement_age = 65
    years_to_retirement = retirement_age - current_age
    current_savings = 10000
    annual_income = 60000
    savings_rate = 15
    annual_return = 7
    inflation_rate = 3
    income_growth_rate = 2

    # Calculate unadjusted and inflation-adjusted savings
    total_savings, unadjusted_savings_data, inflation_adjusted_savings_data = calculate_total_savings(
        current_savings=current_savings,
        annual_income=annual_income,
        savings_rate=savings_rate,
        current_age=current_age,
        retirement_age=retirement_age,
        annual_return=annual_return,
        inflation_rate=inflation_rate,
        income_growth_rate=income_growth_rate,
    )

    # Generate the default chart
    chart_path = generate_interactive_chart(unadjusted_savings_data, inflation_adjusted_savings_data, current_age, retirement_age)
    return chart_path

# The chart that will be generated via user's inputs
def generate_interactive_chart(unadjusted_savings_data, inflation_adjusted_savings_data, current_age, retirement_age):
    years = list(range(current_age, retirement_age + 1))  # List of ages from start to retirement

    # Create a Plotly chart
    fig = go.Figure()

    # For unadjusted savings
    fig.add_trace(go.Scatter(
        x=years,
        y=unadjusted_savings_data,
        mode='lines+markers',
        name='Unadjusted Savings'
    ))

    # For inflation-adjusted savings
    fig.add_trace(go.Scatter(
        x=years,
        y=inflation_adjusted_savings_data,
        mode='lines+markers',
        name='Inflation-Adjusted Savings',
        line=dict(dash='dash')
    ))

    # Chart layout
    fig.update_layout(
        title="Savings Growth Over Time (Unadjusted vs. Inflation-Adjusted)",
        xaxis_title="Age",
        yaxis_title="Savings ($)",
        template="plotly_white",
        legend=dict(title="Savings Type")
    )

    # Save the chart as an HTML file
    chart_path = "app/static/savings_chart.html"
    fig.write_html(chart_path)

    return chart_path
