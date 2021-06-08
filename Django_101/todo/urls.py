from django.urls import path
from todo.views import todo, fill, update_todo

urlpatterns = [
    path('', todo),
    path('fill/', fill, name="new todo"),
    path('updatetodo/', update_todo, name="update todo"),
]