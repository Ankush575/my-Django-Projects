# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Task
# from .forms import TaskForm

# # Create your views here.

# # function for home page


# def home(request):
#     homescreen = Task.objects.all()
#     return render(request, 'home.html', {'homescreen': homescreen})

# # function to fectch all tasks


# def getAllTasks(request):
#     tasks = Task.objects.all()
#     return render(request, 'alltask.html', {'tasks': tasks})

# # function to get task by id


# def getTaskById(request, id):
#     task = get_object_or_404(Task, id=id)
#     return render(request, 'singletask.html', {'task': task})

# # function to create a task


# def createTask(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('tasklist')

#     else:
#         form = TaskForm()
#     return render(request, 'createtask.html', {'form': form})

# # function to update a task


# def updateTask(request, id):
#     task = get_object_or_404(Task, id=id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()

#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'updatetask.html', {'form': form})

# # function to delete a task


# def deleteTask(request, id):
#     task = get_object_or_404(Task, id=id)
#     if request.method == "POST":
#         task.delete()
#         return redirect('tasklist')

#     else:
#         return render(request, 'deletetask.html', {'task': task})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Home page function


def home(request):
    return render(request, 'home.html')

# Function to fetch all tasks (Only for logged-in users)


@login_required
def getAllTasks(request):
    tasks = Task.objects.filter(user=request.user)  # Show only user's tasks
    return render(request, 'alltask.html', {'tasks': tasks})

# Function to get task by ID (Only for logged-in users)


@login_required
def getTaskById(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)  # Restrict access
    return render(request, 'singletask.html', {'task': task})

# Function to create a task (Only for logged-in users)


@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the logged-in user
            task.save()
            return redirect('tasklist')
    else:
        form = TaskForm()
    return render(request, 'createtask.html', {'form': form})

# Function to update a task (Only for logged-in users)


@login_required
def updateTask(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)  # Restrict access
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form = TaskForm(instance=task)
    return render(request, 'updatetask.html', {'form': form})

# Function to delete a task (Only for logged-in users)


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)  # Restrict access
    if request.method == "POST":
        task.delete()
        return redirect('tasklist')
    else:
        return render(request, 'deletetask.html', {'task': task})
