from django.urls import path
from pets.views import pet_all, pet_detail, like, create, edit, delete

urlpatterns = [
    path('', pet_all, name='all pets list'),
    path('details/<int:pk>', pet_detail, name="pet details"),
    path('like/<int:pk>', like, name='new like'),
    path('create/', create, name='create a new pet'),
    path('edit/<int:pk>', edit, name='edit pet info'),
    path('delete/<int:pk>', delete, name='delete a pet'),
]