from django.db import models
from ModelForms.validators import title_validator


class Book(models.Model):
    title = models.CharField(
        max_length=20,
        validators=(
            title_validator,
        ),
    )
    pages = models.IntegerField(
        default=0,
    )
    description = models.CharField(
        max_length=100,
        default='',
    )
    author = models.CharField(
        max_length=20,
    )
