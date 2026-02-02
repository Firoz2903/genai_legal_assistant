def explain_clause(clause_text):
    prompt = f"""
    Explain the following legal clause in simple business language.
    Identify risks and who benefits.

    Clause:
    {clause_text}
    """
    return prompt  # send to GPT-4 / Claude
