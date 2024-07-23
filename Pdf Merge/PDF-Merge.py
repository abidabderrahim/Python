"""
this program can merge pdf from current directory .
"""

import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("My.pdf")
