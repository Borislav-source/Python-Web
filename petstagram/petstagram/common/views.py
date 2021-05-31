from django.shortcuts import render

from petstagram.common.models import User


def landing_page(request):
    context = {
        'boby': 19,
        'people': User.objects.all(),
    }
    return render(request, 'landing_page.html', context)
