from django.urls import path
from djangoProject.pet import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('pets/', views.pet_all, name='pet_all'),
    path('create/', views.create_pet, name='create pet'),
    path('details/<int:pk>', views.pet_details, name='details'),
    path('like/<int:pk>', views.like, name='new like'),
    path('edit/<int:pk>', views.edit_pet, name='edit pet info'),
    path('delete/<int:pk>', views.delete, name='delete pet'),
    path('comment/<int:pk>', views.comment, name='comment')
]