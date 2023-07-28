from django.db import models

class Cook_Book (models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="anycategory")
    text = models.TextField(default="recept")
