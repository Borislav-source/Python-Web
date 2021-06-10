from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, default='', unique=True)
    age = models.IntegerField(default=0)
