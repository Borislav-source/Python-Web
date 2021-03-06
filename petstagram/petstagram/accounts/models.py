from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

from petstagram.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = PetstagramUserManager()

    USERNAME_FIELD = 'email'


class UserProfile(models.Model):
    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    profile_picture = models.ImageField(
        upload_to='images/profiles',
        blank=True
    )


from petstagram.accounts import signals