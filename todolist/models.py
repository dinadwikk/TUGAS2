from operator import mod
from django.db import models
from django.conf import settings

# Create your models here.
class TodolistTemplate(models.Model):
    id = models.AutoField (primary_key= True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank= True, null= True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    #isfinished = models.BooleanField(default= True)