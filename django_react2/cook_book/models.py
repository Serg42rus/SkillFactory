from django.db import models

class Cook_Book (models.Model):
    name = models.CharField(max_length=100, default="name")
    category = models.CharField(max_length=100, default="anycategory")
    text = models.TextField(default="reciept")

    def __str__(self):
        return f'{self.name}'


class Category (models.Model):
    title= models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.title}'