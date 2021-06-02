from django.shortcuts import render
from todo.models import Todo


def todo(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo.html', context=context)
