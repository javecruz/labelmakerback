from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Label(models.Model):
    author = models.ForeignKey('api.CustomUser', related_name='labels', on_delete=models.CASCADE)
    front_text = models.CharField(max_length=50, null=False, blank=False)
    back_text = models.CharField(max_length=50, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.front_text + " --- " + self.back_text
