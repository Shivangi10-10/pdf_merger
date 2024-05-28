import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        with open(file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            merger.append(pdf_reader)

with open("combinedPDFs.pdf", 'wb') as output_file:
    merger.write(output_file)
