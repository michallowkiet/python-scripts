import os

from PyPDF2 import PdfWriter

merger = PdfWriter()

for file in os.listdir("."):
    if file.endswith(".pdf"):
        merger.append(file)

merger.write("merged.pdf")

merger.close()

print("Done")
