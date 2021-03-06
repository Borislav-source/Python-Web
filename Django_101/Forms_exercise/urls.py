from django.urls import path

from Forms_exercise.views import index, todo_forms_exercise, create_new_todo, update_todo, delete_todo

urlpatterns = [
    path('', index, name='print user info'),
    path('todos/', todo_forms_exercise, name='forms todo ex'),
    path('create-new-todo/', create_new_todo, name='create new todo'),
    path('todos/update/<int:pk>', update_todo, name='update todo forms ex'),
    path('todos/delete/<int:pk>', delete_todo, name='delete todo forms ex')
]
