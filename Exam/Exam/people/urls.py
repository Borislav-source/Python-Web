from django.urls import path

from Exam.people.views import profile_info, create_profile, delete_profile

urlpatterns = [
    path('', profile_info, name='profile info'),
    path('create-profile/', create_profile, name='profile create'),
    path('delete-profile/', delete_profile, name='profile delete'),
]