from django.urls import path
from petstagram.common import views

urlpatterns = [
    path('', views.landing_page, name='home page'),
    path('login', views.log_in, name='login'),
    path('loguot', views.log_out, name='logout'),
]