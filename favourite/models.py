from django.db import models
from django.conf import settings 
from meal.models import Meal

class Favourite(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete = models.CASCADE,
                                 related_name = 'fav_user')
    name = models.ForeignKey(Meal, on_delete = models.CASCADE,
                             related_name = 'fav_name')
    favourite = models.ForeignKey(Meal, on_delete = models.CASCADE,
                                  related_name = 'fav_bool')
    
    def __str__(self):
        return "Favourites"
