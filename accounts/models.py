from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    first_name = None
    last_name = None

    user_num = models.AutoField(primary_key=True)
    username = models.CharField(
        unique=True,
        max_length=50
    )
    nickname = models.CharField(
        max_length=100
    )
    birthdate = models.DateField(
        blank=True, null=True
    )

    updated_at = models.DateTimeField(auto_now=True)