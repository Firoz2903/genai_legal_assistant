import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "PARTIES": [],
        "DATES": [],
        "MONEY": [],
        "LAW": [],
        "GPE": []
    }

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON"]:
            entities["PARTIES"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["DATES"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["MONEY"].append(ent.text)
        elif ent.label_ in ["GPE"]:
            entities["GPE"].append(ent.text)

    return entities
