import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Create a pdf file which contains data about the flatmate and the bill report
    """

    def __init__(self, filename):
        self.filename = filename + ".pdf"

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pays = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add house image
        pdf.image(name="house.png", w=20, h=20)

        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt="Period: ", border=0, align="L")
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align="L", ln=1)

        # insert name and amount to be paid by the flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=0, align="L")
        pdf.cell(w=150, h=40, txt=flatmate1_pays, border=0, align="L", ln=1)

        pdf.cell(w=150, h=40, txt=flatmate2.name, border=0, align="L")
        pdf.cell(w=150, h=40, txt=flatmate2_pays, border=0, align="L", ln=1)

        pdf.output(name=self.filename)
        webbrowser.open("file://" + os.path.realpath(self.filename))

