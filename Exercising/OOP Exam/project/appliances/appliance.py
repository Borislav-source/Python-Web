class Appliance:
    Month = 30

    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expenses(self):
        return self.cost * self.Month