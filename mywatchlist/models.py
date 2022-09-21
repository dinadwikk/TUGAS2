from django.db import models

class ContentMyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
# Create your models here.
