# backend/analysis/metrics.py

def calculate_metrics(df):
    total_revenue = int(df["revenue"].sum())
    total_expense = int(df["expense"].sum())
    cash_flow = int(df["cash_in"].sum() - df["cash_out"].sum())
    profit = total_revenue - total_expense
    profit_margin = round(profit / total_revenue, 2) if total_revenue else 0

    health_score = 100
    risk_level = "Low"

    if profit_margin < 0.2:
        health_score = 60
        risk_level = "Medium"
    if profit_margin < 0.1:
        health_score = 40
        risk_level = "High"

    return {
        "Total Revenue": total_revenue,
        "Total Expense": total_expense,
        "Profit": profit,
        "Profit Margin": profit_margin,
        "Cash Flow": cash_flow,
        "Financial Health Score": health_score,
        "Risk Level": risk_level
    }
