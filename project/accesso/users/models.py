from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    photo_image = models.ImageField(upload_to='photos/', blank=True, null=True, max_length=255)
