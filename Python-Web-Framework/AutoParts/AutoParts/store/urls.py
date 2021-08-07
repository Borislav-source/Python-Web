from django.urls import path

from AutoParts.store.views import cart, checkout, updateItem

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update item'),
]