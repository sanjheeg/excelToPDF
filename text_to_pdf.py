import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("TXTs/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename)

    with open(filepath, "r") as file:
        data = file.read()
    pdf.ln(10)
    pdf.set_font(family="Times", size=11)
    pdf.cell(w=50, h=8, txt=data)
    pdf.output(f"txt_pdf/{filename}.pdf")

