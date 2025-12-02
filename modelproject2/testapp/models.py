from django.db import models
#from faker import faker
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    #phonenumber = models.CharField(30) for django-seed module
    address = models.TextField()
