from django.db import models

class CoordBaseModel(models.Model):
    """Models abstract base class, used in all models in the project."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        