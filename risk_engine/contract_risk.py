def contract_risk(clause_scores):
    if clause_scores.count("HIGH") >= 3:
        return "HIGH"
    elif clause_scores.count("MEDIUM") >= 3:
        return "MEDIUM"
    else:
        return "LOW"
