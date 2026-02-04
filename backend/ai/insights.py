# backend/ai/insights.py

def generate_ai_insights(metrics: dict, language: str = "en"):
    profit_margin = metrics["Profit Margin"]
    risk = metrics["Risk Level"]

    insight_en = (
        "The business shows strong financial health with healthy profits and positive cash flow. "
        "Credit risk is low. To improve further, focus on reducing operational expenses and "
        "speeding up customer payments to strengthen working capital."
    )

    insight_hi = (
        "व्यवसाय की वित्तीय स्थिति मजबूत है। लाभ अच्छा है और नकदी प्रवाह सकारात्मक है। "
        "ऋण जोखिम कम है। लागत कम करने और ग्राहकों से भुगतान जल्दी प्राप्त करने पर ध्यान दें।"
    )

    insight_kn = (
        "ವ್ಯವಹಾರದ ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಉತ್ತಮವಾಗಿದೆ. ಲಾಭ ಮತ್ತು ನಗದು ಹರಿವು ಉತ್ತಮವಾಗಿದೆ. "
        "ವೆಚ್ಚಗಳನ್ನು ಕಡಿಮೆ ಮಾಡುವುದು ಮತ್ತು ಗ್ರಾಹಕರ ಪಾವತಿಗಳನ್ನು ವೇಗಗೊಳಿಸುವುದು ಉತ್ತಮ."
    )

    if language == "hi":
        return insight_hi
    if language == "kn":
        return insight_kn

    return insight_en
