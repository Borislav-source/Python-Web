from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def update(request):
    # print('Inside update function')
    if request.method=='POST':
        # print("Inside post block")
        name_data=request.POST['name']
        age_data=request.POST['age']
        x=Person(name=name_data,
        age=age_data)
        x.save()
    return redirect('/')