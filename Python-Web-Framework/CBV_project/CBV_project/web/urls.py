from django.urls import path

from CBV_project.web.views import NewsView, CreateSource, CreateArticle, SourcesView, DetailsArticle

urlpatterns = [
    path('', NewsView.as_view(), name='home page'),
    path('create-source/', CreateSource.as_view(), name='create source'),
    path('create-article/', CreateArticle.as_view(), name='create article'),
    path('sources/', SourcesView.as_view(), name='sources list'),
    path('source-details/<int:pk>', DetailsArticle.as_view(), name='article details'),
]
