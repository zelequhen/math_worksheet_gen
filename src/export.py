import fpdf
from typing import List, Optional

import problem

def generate_pdf(problems: List[problem.Problem], path: Optional[str] = None) -> None:
    pdf = fpdf.FPDF(orientation="P", format="Letter", unit="in")
    pdf.set_font("Helvetica", "", 18)
    pdf.add_page()
    pdf.set_margin(0.5)
    pdf.cell(pdf.epw, 0.25, "Math Worksheet", ln=2, align="C", center=True)
    pdf.ln(0.375)

    for prob in problems:
        pdf.cell(pdf.epw, 0.5, f"{prob} = ____", ln=1)

    if path is not None:
        try:
            pdf.output(path)
        except OSError as err:
            raise OSError(f"Could not save to {path}", err)
    