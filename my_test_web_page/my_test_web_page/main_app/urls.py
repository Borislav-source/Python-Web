from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from my_test_web_page.main_app import views


urlpatterns = [
    path('', views.index, name='root page')
]