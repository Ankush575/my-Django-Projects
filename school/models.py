from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(null=False, max_length=100)
    rollNumber = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(null=False)
    address = models.TextField(null=False)
    DOB = models.DateField(null=False)
    gender = models.CharField(null=False, max_length=10)
    admissionDate = models.DateField(null=False)

    def __str__(self):
        return f"{self.name},{self.rollNumber}"
