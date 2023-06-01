import datetime
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    context = {
        'page_title': "To-Dos | Homepage",
    }
    return render(request, 'todo/index.html', context)


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("display_todos")
    else:
        form = TodoForm()

    return render(request, "todo/add_todo.html", {"form": form})


def display_todos(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'todo/all_todos.html', context)


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        if 'done' in request.POST:
            todo.has_been_done = True
            todo.date_completion = datetime.datetime.now()
            todo.save()
        elif 'undone' in request.POST:
            todo.has_been_done = False
            todo.date_completion = None
            todo.save()

    return redirect('display_todos')
