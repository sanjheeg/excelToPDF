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
    pdf.cell(w=50, h=8, txt=filename.title(), border=0)

    with open(filepath, "r") as file:
        data = file.readlines()
    pdf.ln(10)
    pdf.set_font(family="Times", size=11)

    count = 8
    for line in data:
        pdf.cell(w=170, h=12, txt=line, border=0)
        pdf.ln(12)
    # pdf.output(f"txt_pdf/{filename}.pdf")

# produces one pdf with multiple pages
pdf.output("animals.pdf")