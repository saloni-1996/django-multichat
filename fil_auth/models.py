from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default = False)
    is_ecoord = models.BooleanField(default = False)
    is_presenter = models.BooleanField(default = True)
    about = models.CharField(max_length=1000)
