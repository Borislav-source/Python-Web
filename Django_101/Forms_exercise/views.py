from django.shortcuts import render, redirect

from Forms_exercise.forms import UserFormModel, TodoForm
from Forms_exercise.models import TodoModel


def index(request):
    if request.method == 'POST':
        form = UserFormModel(request.POST)
        if form.is_valid():
            fields = ['name', 'age', 'Email', 'Password', 'Text']
            print('VALIDATION SUCCESS')
            [print(f'{field.upper()}: {form.cleaned_data[field]}') for field in fields]
            return redirect('/forms/')
        else:
            print(form.errors)
    else:
        context = {
            'form': UserFormModel()
        }
        return render(request, 'todo_app/create.html', context)


def todo_forms_exercise(request):
        context = {
            'todos': TodoModel.objects.all(),
        }
        return render(request, 'todo_app/index.html', context)


def create_new_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            todo = TodoModel(title=title, description=description)
            todo.save()
        return redirect('create new todo')

    else:
        context = {
            'form': TodoForm()
        }
        return render(request, 'todo_app/create.html', context)
