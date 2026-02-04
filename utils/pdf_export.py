from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

def generate_pdf(text):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    for line in text.split("\n"):
        elements.append(Paragraph(line, styles["Normal"]))
        elements.append(Spacer(1, 8))

    doc.build(elements)

    buffer.seek(0)
    return buffer


def build_summary(analysis):
    lines = []
    lines.append("Contract Risk Summary\n")
    lines.append(f"Overall Risk: {analysis['overall_risk']}\n")

    lines.append("Key Issues:\n")

    if analysis["high_risk_clauses"]:
        for clause in analysis["high_risk_clauses"]:
            lines.append(f"- HIGH RISK: {clause[:80]}...\n")

    if analysis["medium_risk_clauses"]:
        for clause in analysis["medium_risk_clauses"]:
            lines.append(f"- MEDIUM RISK: {clause[:80]}...\n")

    lines.append("\nExtracted Entities:\n")
    for k, v in analysis["entities"].items():
        if v:
            lines.append(f"{k}: {', '.join(set(v))}\n")

    return "".join(lines)
