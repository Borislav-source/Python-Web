from django.shortcuts import render, redirect

from Expenses_tracker.core.calculations import calculate_budget
from Expenses_tracker.expenses.forms import ExpenseForm
from Expenses_tracker.expenses.models import Expense
from Expenses_tracker.profiles.forms import ProfileForm
from Expenses_tracker.profiles.models import Profile


def home_page(request):
    profile = Profile.objects.first()
    if profile:
        context = {
            'budget': profile.budget,
            'expenses': Expense.objects.all(),
            'sum': calculate_budget()
        }
        return render(request, 'home-with-profile.html', context)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home-with-profile.html')
    return render(request, 'home-no-profile.html')


def create_expense(request):
    if request.method == 'GET':
        return render(request, 'expense-create.html')
    else:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        else:
            context = {
                'form': form
            }
            return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense
        }
        return render(request, 'expense-edit.html', context)
    expense = ExpenseForm(request.POST, instance=expense)
    if expense.is_valid():
        expense.save()
        return redirect('home page')
    context = {
        'expense': expense
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense
        }
        return render(request, 'expense-delete.html', context)
    expense.delete()
    return redirect('home page')
