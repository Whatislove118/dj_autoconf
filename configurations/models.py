from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


User = get_user_model()

def generate_config_upload_url(instance, filename):
    print(instance)
    print(filename)
    return 'media'

class ConfigurationManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def get_configuration_by_user_id(self, user_id):
        return self.get_queryset().get(user_id=user_id)

class Configuration(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    path_to_file = models.FileField(blank=False, null=False, upload_to=generate_config_upload_url, default=settings.DEFAULT_CONFIG)
    profile = models.OneToOneField('Profile', blank=True, null=True, on_delete=models.CASCADE)

    objects = ConfigurationManager()

    class Meta:
        db_table = 'configuration'

class Profile(models.Model):
    name = models.TextField(null=False)

