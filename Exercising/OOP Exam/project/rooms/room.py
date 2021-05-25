from appliances.appliance import Appliance


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if not value:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    def calculate_expenses(self, *args):
        expenses = 0
        for lst in args:
            for ele in lst:
                if isinstance(ele, Appliance):
                    expenses += ele.get_monthly_expenses() * self.members_count
                else:
                    expenses += ele.get_monthly_expenses()

        self.__expenses = expenses
        return expenses
