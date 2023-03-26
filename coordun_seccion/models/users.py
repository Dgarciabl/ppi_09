from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from .model_base import CoordBaseModel


class Profile(CoordBaseModel):
    """Profile model.
    A profile holds a user's public data like biography, picture,
    and statistics.
    """
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    semester = models.TextField(blank=True,null=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True, 
        null=True
        )
    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return username."""
        return str(self.user)
