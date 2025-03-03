from django.urls import path
from .import views

urlpatterns = [
    path('tasks', views.getAllTasks, name='tasklist'),
    path('<int:id>/', views.getTaskById, name='taskdetail'),
    path("createtask/", views.createTask, name='create'),
    path('modify/<int:id>', views.updateTask, name='updatemytask'),
    path('deletetask/<int:id>', views.deleteTask, name='delete'),
    path('', views.home, name='home')
]
