from django.http import HttpResponseRedirect
from django.shortcuts import render

from todo.forms import ToDoForm
from todo.models import TodoList


def todo_list(request):
    tasks = TodoList.objects.all().order_by('-created')
    return render(request, 'todo/todo_list.html', context={'tasks': tasks})

def create_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.cleaned_data['status'] = 'В процессе'
            form.save()
            return HttpResponseRedirect('/todo')
    else:
        form = ToDoForm()
        print(form.errors)
    return render(request, 'todo/create_todo.html', context={'form': form})