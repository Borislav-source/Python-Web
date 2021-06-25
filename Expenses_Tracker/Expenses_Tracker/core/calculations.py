from Expenses_tracker.expenses.models import Expense
from Expenses_tracker.profiles.models import Profile


def calculate_budget():
    budget = Profile.objects.first().budget
    exp = Expense.objects.all()
    expenses = sum(e.price for e in exp)
    result = budget - expenses
    return result