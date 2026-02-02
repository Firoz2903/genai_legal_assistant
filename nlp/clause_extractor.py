import re

def extract_clauses(text):
    clauses = re.split(r'\n\d+\.|\n[A-Z][A-Za-z ]+:', text)
    return [c.strip() for c in clauses if len(c.strip()) > 30]
