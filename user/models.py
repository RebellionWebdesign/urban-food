from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from cloudinary.models import CloudinaryField

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """
    The User class is a custom class written for the project.
    """
    image = CloudinaryField("image", null=True, blank=True, default="placeholder")
    username = models.CharField(max_length=150, unique=True, null=True,
                                blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.last_name