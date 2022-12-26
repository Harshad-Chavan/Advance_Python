from report import PdfReport
from flat import Bill, Flatmate

bill_amount = int(input("hey user ! Enter your total bill amount:"))
period = input("Enter period:")
bill = Bill(bill_amount, period)


flatmate_1 = input("Enter name of first flatmate:")
days_in_house = int(input(f"hey {flatmate_1} ! Enter number of days:"))
flatmate_1_obj = Flatmate(flatmate_1, days_in_house)

flatmate_2 = input("Enter name of second flatmate:")
days_in_house = int(input(f"hey {flatmate_2} ! Enter number of days:"))
flatmate_2_obj = Flatmate(flatmate_2, days_in_house)

pdf = PdfReport(filename="my report")
pdf.generate(flatmate_1_obj, flatmate_2_obj, bill)
