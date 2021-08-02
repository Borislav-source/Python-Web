from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, FormView, ListView

from CBV_project.web.models import SourceModel, ArticleModel


class NewsView(ListView):
    template_name = 'resources/pages/home.html'
    model = ArticleModel


class SourcesView(ListView):
    template_name = 'resources/pages/sources.html'
    model = SourceModel


class CreateSource(CreateView):
    model = SourceModel
    template_name = 'resources/pages/create-source.html'
    fields = '__all__'
    success_url = reverse_lazy('home page')


class CreateArticle(CreateView):
    model = ArticleModel
    template_name = 'resources/pages/create-article.html'
    fields = '__all__'
    success_url = reverse_lazy('create article')


class DetailsArticle(DetailView):
    model = SourceModel
    template_name = 'resources/pages/source-details.html'
