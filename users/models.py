from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)

from django.db.models.signals import post_save



class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pass_entry = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    is_blocked = models.BooleanField(default=False)
    is_employee =  models.BooleanField(default=True)
    is_admin =  models.BooleanField(default=False)