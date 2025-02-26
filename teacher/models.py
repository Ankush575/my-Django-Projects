from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(null=False, max_length=20)
    department = models.CharField(null=False, max_length=20)

    def __str__(self):
        return f"{self.name}, {self.department}"
