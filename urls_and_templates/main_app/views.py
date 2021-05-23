from django.shortcuts import render


#Create views here
def index(req):
    return render(req, 'main_app/index.html')