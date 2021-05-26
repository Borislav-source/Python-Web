from django.db import models


class NewApp(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)
    release_date = models.DateTimeField
