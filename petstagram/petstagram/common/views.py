from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect


def landing_page(request):
    return render(request, 'landing_page.html')


def log_in(request):
    user = authenticate(username='stilqna', password='yolo1234')
    if user.is_authenticated:
        login(request, user)
    return redirect('home page')


def log_out(request):
    logout(request)
    return redirect('home page')
