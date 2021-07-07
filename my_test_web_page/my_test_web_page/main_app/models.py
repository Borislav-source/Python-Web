from django.db import models


class Profile(models.Model):
    name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    profile_picture = models.ImageField(upload_to='images')
