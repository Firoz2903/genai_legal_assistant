from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(summary_text, output_path="contract_summary.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    x = 40
    y = height - 40

    c.setFont("Helvetica", 10)

    for line in summary_text.split("\n"):
        if y < 40:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = height - 40
        c.drawString(x, y, line)
        y -= 14

    c.save()
    return output_path

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
