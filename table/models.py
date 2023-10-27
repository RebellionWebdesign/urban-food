from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    persons = models.IntegerField()
    max_persons = models.IntegerField()
    booked_out = models.BooleanField()

    def __str__(self):
        return "Table Number " + self.number
