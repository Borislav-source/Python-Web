from django.urls import path
from todo.views import todo, fill, update_todo, is_done, delete_todo

urlpatterns = [
    path('', todo, name='list of todos'),
    path('fill/', fill, name="new todo"),
    path('updatetodo/', update_todo, name="update todo"),
    path('isdone/<int:pk>', is_done, name='todo is done'),
    path('deletetodo/<int:pk>', delete_todo, name="delete todo")
]