from django.db import models

class Dictionary(models.Model):
    word = models.CharField(max_length=200, unique=True)
    meaning = models.TextField()
