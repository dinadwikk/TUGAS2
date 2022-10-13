from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodolistTemplate(models.Model):
    id = models.AutoField (primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
