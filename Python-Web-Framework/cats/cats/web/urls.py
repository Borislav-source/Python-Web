from django.urls import path

from cats.web.views import index, list_of_cats, IndexView, ShowCats

urlpatterns = [
    path('', IndexView.as_view(), name='landing page'),
    path('cat-list/', ShowCats.as_view(), name='cats list'),
]