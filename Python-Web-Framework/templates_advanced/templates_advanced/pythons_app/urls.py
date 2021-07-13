from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
