from django.urls import path

from CBV_project.web.views import NewsView, CreateSource

urlpatterns = [
    path('', NewsView.as_view(), name='home page'),
    path('create-source/', CreateSource.as_view(), name='create source'),

]
