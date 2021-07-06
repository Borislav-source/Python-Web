from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python
from django_cleanup.signals import cleanup_pre_delete


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
        return render(req, 'create.html', {'form': form})


def delete(req, pk):
    python = Python.objects.get(pk=pk)
    python.delete()
    return redirect('index')
