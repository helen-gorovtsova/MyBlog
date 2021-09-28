from django.urls import path

from todo import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add_todo/', views.create_todo, name='create_todo'),
]
