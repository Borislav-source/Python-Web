from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from Django_101.models import Person


def index(req):
    context = {
        'name': 'Bobkata',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


@csrf_exempt
def update(request):
    # print('Inside update function')
    if request.method == 'POST':
        # print("Inside post block")
        fname_data = request.POST['fname']
        lname_data = request.POST['lname']
        email_data = request.POST['email']
        password_data = request.POST['password']
        age_data = request.POST['age']
        x = Person(fname=fname_data,
                   lname=lname_data,
                   email=email_data,
                   password=password_data,
                   age=age_data,
                   )
        x.save()
    return redirect('/')


def delete_event(request, pk):
    event = Person.objects.get(pk=pk)
    event.delete()
    return redirect('/')


def sign_in(request):
    return render(request, 'signin.html')
