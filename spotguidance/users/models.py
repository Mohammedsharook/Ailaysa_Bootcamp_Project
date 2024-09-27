from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    