from django.db import models
from petstagram.pets.models import Pet


# class User(models.Model):
#     username = models.CharField(max_length=30, default='', unique=True)
#     age = models.IntegerField(default=0)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField()