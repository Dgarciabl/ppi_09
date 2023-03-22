from django.db import models
from django.contrib.auth.models import User
from .model_base import CoordBaseModel


class Degree(CoordBaseModel):
    """Degree model."""
    # Call the students profesion, with user_set 
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True, 
        null=True
        )
    
    def __str__(self):
        """Return name."""
        return self.name
    

class Students(CoordBaseModel):
    """This is the students model, this is the join with the user and the degree"""
    
    STUDENT = 'student'
    GRADUATED = 'graduated'
    PROFESOR = 'profesor'
    choice_user = (
        (STUDENT, "S"),
        (GRADUATED, "G"),
        (PROFESOR, "P"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    situation = models.CharField(
        choices=choice_user,
        max_length=9,
        default=STUDENT,
    )
    
    def __str__(self):
        return f"Student {self.user.username} - {self.degree.name}"
    