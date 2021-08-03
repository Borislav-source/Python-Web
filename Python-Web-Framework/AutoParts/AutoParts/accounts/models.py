from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    profile_picture = models.ImageField(
        upload_to='profiles/images'
    )
    age = models.IntegerField()
    is_done = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
