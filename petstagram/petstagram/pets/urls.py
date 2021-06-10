from django.urls import path
from pets.views import pet_all, pet_detail, like

urlpatterns = [
    path('', pet_all, name='all pets list'),
    path('details/<int:pk>', pet_detail, name="pet details"),
    path('like/<int:pk>', like, name='new like')
]