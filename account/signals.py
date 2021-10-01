from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from configurations.models import Configuration

User = get_user_model()

@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='create_user_profile_uid')
def create_default_configuration(sender, instance, created, **kwargs):
    print(1)
    Configuration.objects.create(user=instance)
