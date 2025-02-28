from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
# function to fectch all tasks


def getAllTasks(request):
    tasks = Task.objects.all()
    return render(request, 'alltask.html', {'tasks': tasks})

# function to get task by id


def getTaskById(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'singletask.html', {'task': task})

# function to create a task


def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasklist')

    else:
        form = TaskForm()
    return render(request, 'createtask.html', {'form': form})

# function to update a task


def updateTask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

    else:
        form = TaskForm(instance=task)
    return render(request, 'updatetask.html', {'form': form})

# function to delete a task


def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('tasklist')

    else:
        return render(request, 'deletetask.html', {'task': task})
