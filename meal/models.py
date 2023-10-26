from django.db import models
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    image = CloudinaryField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.CharField(max_length=150)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
