from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram.accounts.models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_user(signal, instance, created, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
        )
        profile.save()
