from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
