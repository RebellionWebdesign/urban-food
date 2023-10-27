from django.db import models
from django.conf import settings 
from table.models import Table
from booking.models import Booking

class StaffArea(models.Model):
    booking_number = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                       related_name = 'staff_bnumber')
    first_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name = 'staff_fname')
    last_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete = models.CASCADE,
                                  related_name = 'staff_lname')
    email = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete = models.CASCADE,
                              related_name = 'staff_email')
    table = models.ForeignKey(Table, on_delete = models.CASCADE,
                              related_name = 'staff_table')
    persons = models.ForeignKey(Table, on_delete=models.CASCADE,
                                related_name='staff_persons')
    booking_date = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                     related_name = 'staff_bdate')
    booking_time = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                     related_name = 'staff_btime' )

    def __str__(self):
        return self.booking_number + " - " + self.last_name
