from django.urls import path

from Forms_exercise.views import index, todo_forms_exercise, create_new_todo

urlpatterns = [
    path('', index, name='print user info'),
    path('todos/', todo_forms_exercise, name='forms todo ex'),
    path('create-new-todo/', create_new_todo, name='create new todo'),
]
