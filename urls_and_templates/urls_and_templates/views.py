from django.shortcuts import render, redirect
from models import NewApp


def index(req):
    return render(req, 'index.html')

def apps(req):
    pass


def create_app(req):
    NewApp(
        name=input(),
        price=input(),
        release_date=input()
    ).save()
    return redirect('')
