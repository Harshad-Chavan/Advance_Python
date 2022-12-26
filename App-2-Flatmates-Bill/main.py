import os.path
import webbrowser

from fpdf import FPDF


class Flatmate:
    """
    Create a flatmate who lives in the flat and pays the share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        amount = bill.amount * weight
        return amount


class Bill:
    """
    Bill contains the total bill amount that needs to be paid
    it has an amount and the period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


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


bill = Bill(120, "March 2022")
Harshad = Flatmate("Harshad", 20)
Nivi = Flatmate("Nivi", 25)

print(Harshad.pays(bill, Nivi))
print(Nivi.pays(bill, Harshad))

pdf = PdfReport(filename="my report")
pdf.generate(Harshad, Nivi, bill)
