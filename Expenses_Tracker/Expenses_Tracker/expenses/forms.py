from django import forms

from Expenses_tracker.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
