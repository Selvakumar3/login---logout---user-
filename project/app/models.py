from turtle import width
from django.db import models

class Details(models.Model):
    username = models.CharField(max_length=30)
   # password= models.CharField(max_length=30, widget=models.Passwordinput)
