from django.db import models
from django.contrib.auth.models import AbstractUser

from .model_base import CoordBaseModel

class User(CoordBaseModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(max_length=17, blank=True, validators=[phone_regex])

    USERNAME_FIELD = 'email' #Nuestro nuevo usernamae es el email

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have evething verifed'
    )

    def __str__(self):
        """Return username."""
        return self.username
    
    def get_short_name(self):
        """Return username."""
        return self.username

class Profile(CoordBaseModel):
    """Profile model.
    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True, 
        null=True
        )
    biography = models.TextField(max_length=500, blank=True)
    # Statistics
    reputation = models.FloatField(
        default=5.0,
        help_text='User reputation based on the rides taken and offered'
    )

    def __str__(self):
        """Return username."""
        return str(self.user)
