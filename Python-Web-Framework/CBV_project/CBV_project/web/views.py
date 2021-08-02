from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView


class NewsView(TemplateView):
    template_name = 'resources/pages/home.html'


class CreateSource(CreateView):
    template_name = 'resources/pages/create-source.html'
