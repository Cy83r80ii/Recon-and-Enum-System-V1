from fpdf import FPDF


def generate_report(findings, target):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="ARES-X Security Report", ln=True)

    pdf.cell(200, 10, txt=f"Target: {target}", ln=True)

    pdf.cell(200, 10, txt=f"Findings: {len(findings)}", ln=True)

    pdf.ln(10)

    for f in findings:

        pdf.set_font("Arial", size=10)

        pdf.multi_cell(
            0,
            8,
            txt=f"{f.get('type')} | {f.get('url','')} | Severity: {f.get('severity','info')}"
        )

        pdf.ln(2)

    pdf.output("scan_report.pdf")
