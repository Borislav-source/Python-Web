from django.urls import path

from Forms_exercise.views import index

urlpatterns = [
    path('', index, name='print user info'),
]
