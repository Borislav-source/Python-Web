"""Django_101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Django_101.views import index, delete_event, update, sign_in, landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing page'),
    path('registred-people/', index, name='registered people'),
    path('update/', update),
    path('delete_event/<int:pk>', delete_event),
    path('todo/', include('todo.urls')),
    path('signin/', sign_in, name='sign in'),
    path('forms/', include('Forms_exercise.urls')),
]
