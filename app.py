#Below is the python program for adding text in a pdf file

#Please read README file to know how to use


import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from os.path import basename


def generate_pdf(text):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.setPageSize((794, 1123))                # PDF page size
    can.setFillColorRGB(223, 163, 9)            # Color of text
    can.setFont('Helvetica', 25)                # Font-style
    can.drawString(180, 475, text)              # x,y position of text
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("path/to/pdf.pdf", "rb"))              
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    outputStream = open("path/to/save/pdf/with/rename.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


generate_pdf("Raj Kishore Patra")





# ©rajkishorepatra- 📧rpatrasm@gmail.com