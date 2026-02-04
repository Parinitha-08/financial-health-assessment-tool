# backend/i18n/translator.py

def translate_metrics(metrics: dict, language: str = "en"):
    if language == "hi":
        return {
            "कुल राजस्व": metrics["Total Revenue"],
            "कुल खर्च": metrics["Total Expense"],
            "लाभ": metrics["Profit"],
            "लाभ प्रतिशत": metrics["Profit Margin"],
            "कैश फ्लो": metrics["Cash Flow"],
            "वित्तीय स्वास्थ्य स्कोर": metrics["Financial Health Score"],
            "जोखिम स्तर": metrics["Risk Level"],
        }

    if language == "kn":
        return {
            "ಒಟ್ಟು ಆದಾಯ": metrics["Total Revenue"],
            "ಒಟ್ಟು ವೆಚ್ಚ": metrics["Total Expense"],
            "ಲಾಭ": metrics["Profit"],
            "ಲಾಭ ಶೇಕಡಾ": metrics["Profit Margin"],
            "ನಗದು ಹರಿವು": metrics["Cash Flow"],
            "ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಅಂಕ": metrics["Financial Health Score"],
            "ಅಪಾಯ ಮಟ್ಟ": metrics["Risk Level"],
        }

    return metrics
