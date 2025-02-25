from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    rollNumber = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField()
    address = models.TextField(max_length=200)
    age = models.IntegerField()
    addmissionDate = models.DateField(max_length=100)
    gender = models.CharField(max_length=10)
    classIncharge = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name},{self.rollNumber}"
