from django.urls import path

from ModelForms.views import index, create, edit

urlpatterns = [
       path('', index, name='all books'),
       path('create/', create, name='create'),
       path('edit/<int:pk>', edit, name='edit'),
]
