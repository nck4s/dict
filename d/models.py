from django.db import models

class Dictionary(models.Model):
    word = models.CharField(max_length=200, unique=True)
    meaning = models.TextField()

    class Meta:
        verbose_name_plural = "Dictionaries"

    def __str__(self):
        return self.word