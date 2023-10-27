from django.db import models
from django.conf import settings 
from table.models import Table

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
    table = models.ForeignKey(Table, on_delete=models.CASCADE,
                              related_name='booking_table')
    persons = models.ForeignKey(Table, on_delete=models.CASCADE,
                                related_name='booking_persons')
    date = models.DateField()
    time = models.TimeField()
    date_created = models.DateTimeField()

    def __str__(self):
        return self.number + ", " + self.last_name
