from turtle import mode
from django.db import models

# Create your models here.
class Employee_Details(models.Model):
    emp_name=models.CharField(max_length=255)
    emp_email=models.CharField(max_length=255)
    emp_phone=models.CharField(max_length=255)
    emp_designation=models.CharField(max_length=255)
    emp_salary=models.IntegerField()
