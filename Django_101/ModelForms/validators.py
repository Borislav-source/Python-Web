from django.core.exceptions import ValidationError


def title_validator(value):
    if len(value) > 20:
        raise ValidationError('Title must be less than 21 symbols')