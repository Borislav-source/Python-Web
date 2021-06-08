from django.shortcuts import render, redirect
from todo.forms import TodoForm
from todo.models import Todo


def todo(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo.html', context=context)


def fill(request):
    context = {
        'todos': Todo.objects.all(),
        'todo_form': TodoForm()
    }
    return render(request, 'new_todo.html', context)


def update_todo(request):
    if request.method == 'POST':
        # form = TodoForm(request.POST or None)
        # if form.is_valid():
        #     form.save()
        title = request.POST['title']
        description = request.POST['description']
        instance = Todo(title=title, description=description)
        instance.save()
        return redirect('/todo/')

