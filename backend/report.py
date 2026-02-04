# backend/report.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_pdf_report(company_name, metrics, ai_insights, language):
    filename = f"{company_name.replace(' ', '_')}_Financial_Report.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "Financial Health Assessment Report")
    y -= 30

    # Meta
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Company: {company_name}")
    y -= 15
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%d %b %Y %H:%M')}")
    y -= 30

    # Metrics
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Financial Metrics")
    y -= 20

    c.setFont("Helvetica", 11)
    for key, value in metrics.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 15

    y -= 20

    # AI Insights
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AI Insights & Recommendations")
    y -= 20

    c.setFont("Helvetica", 11)
    text = c.beginText(60, y)
    for line in ai_insights.split(". "):
        text.textLine(line.strip())
    c.drawText(text)

    c.showPage()
    c.save()

    return filename
