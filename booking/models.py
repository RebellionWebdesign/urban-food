from django.db import models
from django.conf import settings 

class Booking(models.Model):
    number = models.IntegerField()
    first_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='booking_fname')
    last_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='booking_lname')
    email = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='booking_email')
    date = models.DateField()
    time = models.TimeField()
    date_created = models.DateTimeField()

    def __str__(self):
        return "TEST"
#self.number + " | " + 