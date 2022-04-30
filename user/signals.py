from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User, UserProfile


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
