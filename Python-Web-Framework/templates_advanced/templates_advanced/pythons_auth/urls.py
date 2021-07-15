from django.urls import path

from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='login'),
    path('sign-out/', views.sign_out, name='logout'),
    path('sign-up/', views.sign_up, name='register'),
]
