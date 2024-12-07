from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = "user"
    ADMIN = "admin"
    ROLE_CHOICES = (
        (USER, "user"),
        (ADMIN, "admin"),
    )
    role = models.CharField(
        choices=ROLE_CHOICES, default="user", null=True, blank=True
    )
# Create your models here.
