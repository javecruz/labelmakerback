from django.db import models
from django.contrib.auth.models import AbstractUser


class OwnUser(AbstractUser):
    pass


class Label(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False)
    front_text = models.CharField(max_length=50, null=False, blank=False)
    back_text = models.CharField(max_length=50, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.front_text + " --- " + self.back_text

