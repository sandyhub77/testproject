from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    salary = models.IntegerField()


