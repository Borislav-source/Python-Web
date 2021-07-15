from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from pythons_auth.forms import SignForm


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'GET':
        context = {
            'form': form,
        }
        return render(request, 'sign-up.html', context)
    user = UserCreationForm(request.POST)
    user.save()
    return redirect('index')


def sign_in(request):
    if request.method == 'GET':
        context = {
            'form': SignForm()
        }
        return render(request, 'sign-in.html', context)
    form = SignForm(request.POST)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user:
            login(request, user)
    return redirect('index')

    # user = authenticate(username='bogdan', password='yolo1234')
    # # user = authenticate(username='bobo', password='12345qwe')
    # if user:
    #     login(request, user)
    # return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')
