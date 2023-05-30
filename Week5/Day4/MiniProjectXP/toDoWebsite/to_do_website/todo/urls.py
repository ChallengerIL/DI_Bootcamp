from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('all-todos/', views.display_todos, name='display_todos'),
    path('todo-done/<int:pk>', views.todo_done, name='todo_done'),
]
