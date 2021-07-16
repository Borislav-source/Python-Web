from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Profile(models.Model):

    first_name = models.CharField(
        max_length=15,
        blank=True,
    )
    last_name = models.CharField(
        max_length=15,
        blank=True
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    is_done = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
