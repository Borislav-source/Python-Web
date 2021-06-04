from django.db import models


class Person(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30, null=True)
    age = models.IntegerField()
    password = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname
