# backend/main.py

print("=== Backend starting ===")

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from backend.analysis.metrics import calculate_metrics
from backend.i18n.translator import translate_metrics
from backend.ai.insights import generate_ai_insights
from backend.report import generate_pdf_report
from fastapi.responses import FileResponse


app = FastAPI(title="SME Financial Health API")

# CORS (for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "Backend running"}


@app.post("/analyze")
async def analyze_file(
    company_name: str = Form(...),
    language: str = Form("en"),
    file: UploadFile = File(...)
):
    try:
        print("=== /analyze called ===")
        print("Company:", company_name)
        print("File:", file.filename)

        if not file.filename.endswith(".csv"):
            return {"error": "Only CSV files are supported"}

        df = pd.read_csv(file.file)

        metrics = calculate_metrics(df)
        translated_metrics = translate_metrics(metrics, language)
        ai_insights = generate_ai_insights(metrics, language)

        return {
            "company_name": company_name,
            "filename": file.filename,
            "language": language,
            "metrics": translated_metrics,
            "raw_metrics": metrics,
            "ai_insights": ai_insights
        }

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}

@app.post("/report")
async def generate_report(
    company_name: str = Form(...),
    language: str = Form("en"),
    file: UploadFile = File(...)
):
    df = pd.read_csv(file.file)

    metrics = calculate_metrics(df)
    translated_metrics = translate_metrics(metrics, language)
    ai_insights = generate_ai_insights(metrics, language)

    pdf_file = generate_pdf_report(
        company_name=company_name,
        metrics=translated_metrics,
        ai_insights=ai_insights,
        language=language
    )

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename=pdf_file
    )
