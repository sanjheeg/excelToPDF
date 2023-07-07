import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# .glob creates a list of all the filepaths of all files that end with .xlsx
filepaths = glob.glob("invoices/*.xlsx")

# creates the pdf, its title, and stores output in directory
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # Path(filepath) --> PosixPath("invoices/10001-2023.1.18.xlsx")
    # Path(filepath).stem = "10001-2023.1.18"
    filename = Path(filepath).stem
    inv_num = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{inv_num}")
    pdf.output(f"PDFs/{filename}.pdf")
