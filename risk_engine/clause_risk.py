def clause_risk_score(text):
    text = text.lower()

    if "indemnify" in text or "penalty" in text:
        return "HIGH"
    if "termination without notice" in text:
        return "HIGH"
    if "auto-renew" in text or "lock-in" in text:
        return "MEDIUM"
    return "LOW"

def compare_with_template(clause_text, template_text):
    clause_words = set(clause_text.lower().split())
    template_words = set(template_text.lower().split())

    similarity = len(clause_words & template_words) / max(len(template_words), 1)
    return similarity
