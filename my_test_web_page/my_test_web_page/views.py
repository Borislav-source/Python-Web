from django.shortcuts import render


def index(request):
    return render(request, 'root_page/index.html')