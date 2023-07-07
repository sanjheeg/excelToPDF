import pandas as pd
import glob

# .glob creates a list of all the filepaths of all files that end with .xlsx
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
