from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=300)
    status = models.BooleanField(default=False) 