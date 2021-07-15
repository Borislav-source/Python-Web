from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .decorators import authorised_users_only
from .forms import PythonCreateForm
from .models import Python
from django_cleanup.signals import cleanup_pre_delete


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


@authorised_users_only(['User'])
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
