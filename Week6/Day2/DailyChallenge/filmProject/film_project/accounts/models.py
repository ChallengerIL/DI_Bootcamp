from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(region='IL')
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'email']

    def __str__(self):
        return f"{self.username}"
