def suggest_alternative(clause_text):
    prompt = f"""
    Suggest a more SME-friendly alternative clause.
    Keep it legally safe and balanced.

    Clause:
    {clause_text}
    """
    return prompt
