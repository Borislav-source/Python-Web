from django.db import models


class NewApp(models.Model):
    name = models.CharField
    price = models.IntegerField
    release_date = models.DateTimeField
