def classify_clause(text):
    text = text.lower()

    if "shall" in text:
        return "OBLIGATION"
    elif "may" in text:
        return "RIGHT"
    elif "shall not" in text or "not allowed" in text:
        return "PROHIBITION"
    else:
        return "NEUTRAL"
