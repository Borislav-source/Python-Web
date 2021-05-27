from django.http import HttpResponse
from django.shortcuts import render, redirect

from Django_101.models import Person


def create_person(req):
    Person(name='Pesho', age=2).save()
    return redirect('/')


def index(req):
    context = {
        'name': 'Bobkata',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)

