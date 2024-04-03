from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Procfile(AbstractUser):
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)