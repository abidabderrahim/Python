"""
pip install tk ghostscript camelot-py
pip install opencv-python
"""

import camelot

pdf_name = str(input("Enter Pdf Name : "))
page = str(input("Enter Page Number : "))
table = int(input("Enter Tbale Number : "))
tables = camelot.read_pdf(pdf_name, pages=page)
tables.export('data.csv', f='csv', compress=True)
tables[table].to_csv('data.csv')
