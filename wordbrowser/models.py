from django.db import models

# Create your models here.


class Word(models.Model):
    name = models.CharField(max_length=150)
    article = models.CharField(max_length=3)
    part_of_speech = models.CharField(max_length=50)
    meaning = models.CharField(max_length=100)
    extra = models.CharField(max_length=100)