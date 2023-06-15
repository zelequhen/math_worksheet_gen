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

    pdf.accept_page_break
    col = 0
    col_width = pdf.epw / 3
    for prob in problems:
        if pdf.get_y() + 0.75 >= pdf.eph:
            pdf.set_y(1.15)
            if col > 2:
                pdf.add_page()
                col = 0
            else:
                col += 1
        for i, line in enumerate(str(prob).split("\n")):
            pdf.set_x(-(3 - col) * col_width)
            if i != 0 and i == len(str(prob).split("\n")) - 1:
                pdf.set_font(None, "U")
            else:
                pdf.set_font(None, "")
            pdf.cell(col_width, 0.25, f"{line}", ln=1)
        pdf.cell(col_width, 0.5, "", ln=1)

    if path is not None:
        try:
            pdf.output(path)
        except OSError as err:
            raise OSError(f"Could not save to {path}", err)
