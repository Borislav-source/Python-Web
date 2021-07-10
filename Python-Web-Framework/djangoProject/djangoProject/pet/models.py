from django.db import models


class Pet(models.Model):
    TYPE_CAT_CHOICE = 'cat'
    TYPE_DOG_CHOICE = 'dog'
    TYPE_PARROT_CHOICE = 'parrot'
    pet_choices = (
        (TYPE_CAT_CHOICE, 'Cat'),
        (TYPE_DOG_CHOICE, 'Dog'),
        (TYPE_PARROT_CHOICE, 'Parrot'),
    )

    type = models.CharField(
        max_length=13,
        choices=pet_choices
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/pets')


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
