from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taskTitle = models.CharField(max_length=200, null=False)
    taskDescription = models.TextField(max_length=500, null=False)
    taskStartDate = models.DateField()
    taskDueDate = models.DateField()
    taskStatus = models.CharField(max_length=30,
                                  choices=[('in progress', 'in progress'), ('yet to start', 'yet to start'), ('completed', 'completed')], default='yet to start')

    def __str__(self):
        return f"{self.taskTitle}, {self.taskStatus}"
