class Flatmate:
    """
    Create a flatmate who lives in the flat and pays the share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


class Bill:
    """
    Bill contains the total bill amount that needs to be paid
    it has an amount and the period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def pays(self, bill):
        pass
        
class PdfReport:
    """
    Create a pdf file which contains data about the flatmate and the bill report
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass