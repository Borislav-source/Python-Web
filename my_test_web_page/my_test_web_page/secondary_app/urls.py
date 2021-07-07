from django.urls import path
from my_test_web_page.secondary_app import views


urlpatterns = [
    path('', views.index)
]