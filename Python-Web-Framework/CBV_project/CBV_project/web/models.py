from django.db import models


class SourceModel(models.Model):
    name = models.CharField(
        max_length=50,
    )
    link = models.URLField(
        max_length=200
    )

    def __str__(self):
        return self.name


class ArticleModel(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    imageUrl = models.URLField(
        max_length=200,
    )
    source = models.ForeignKey(
        SourceModel,
        on_delete=models.CASCADE,
    )
