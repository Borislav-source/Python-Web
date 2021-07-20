from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect


def landing_page(request):
    return render(request, 'landing_page.html')
