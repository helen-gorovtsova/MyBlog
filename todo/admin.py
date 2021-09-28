from django.contrib import admin

from todo.models import Category, TodoList

admin.site.register(Category)
admin.site.register(TodoList)
