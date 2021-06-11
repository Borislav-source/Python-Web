from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Django_101.models import Person
from .forms import PersonForm
from django.contrib import messages


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
        form = PersonForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! You have sign up successfully!')
            return redirect('/')
        else:
            fname_data = request.POST['fname']
            lname_data = request.POST['lname']
            email_data = request.POST['email']
            password_data = request.POST['password']
            age_data = request.POST['age']

            messages.success(request, 'You made a mistake in filling your form! Please try again!')
            return render(request, 'signin.html',
                          {
                              'fname': fname_data,
                              'lname': lname_data,
                              'email': email_data,
                              'age': age_data,
                              'password': password_data,
                           }
                          )


def delete_event(request, pk):
    event = Person.objects.get(pk=pk)
    event.delete()
    return redirect('/')


def sign_in(request):
    return render(request, 'signin.html')


def landing_page(request):
    return render(request, 'landing_page.html')
