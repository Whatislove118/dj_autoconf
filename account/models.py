from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
import django.contrib.auth.password_validation as validators

# Create your models here.

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        self._validate_credentials(username, email, password)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        self._validate_credentials(email, password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def _validate_credentials(self, username, email, password):
        if username is None:
            raise TypeError('User must have a username')
        if email is None:
            raise TypeError('User must have a email address')
        if password is None:
            raise TypeError('User must have a password')
        validators.validate_password(password)


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'

