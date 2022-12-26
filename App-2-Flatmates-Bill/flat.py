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

