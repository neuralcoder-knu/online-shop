from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from accounts.managers import OnlineShopUserManager


def has_perm(perm, obj=None):
    return True


def has_module_perms(app_label):
    return True


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = OnlineShopUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
