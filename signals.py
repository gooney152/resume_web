from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile
#wire signal to apps.py
#when users is created it sends a signal to this py file and function is called
@receiver(post_save, sender=User)
class create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
