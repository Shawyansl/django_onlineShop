from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    objects = CustomUserManager()