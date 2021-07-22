from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from cats.web.models import Cat


def index(request):
    context = {

    }
    return render(request, 'index.html', context)


def list_of_cats(request):
    context = {
        'cats': Cat.objects.all(),
    }

    return render(request, 'list-of-cats.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    extra_context = {
        'title': 'Hello World!'
    }

    # def get_context_data(self, **kwargs):
    #     return {
    #       'title': 'Hello from CBV',
    #     }


class ShowCats(ListView):
    model = Cat
    template_name = 'list-of-cats.html'
    context_object_name = 'cats'
